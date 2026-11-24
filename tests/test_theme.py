import unittest
from pathlib import Path
from xml.etree import ElementTree

import cssselect2
import tinycss2


ROOT = Path(__file__).resolve().parents[1]


def build_matcher(rules, medium, matcher):
    for rule in rules:
        if rule.type == "error":
            raise ValueError(rule.message)
        if rule.type == "at-rule" and rule.lower_at_keyword == "media":
            if tinycss2.serialize(rule.prelude).strip() == medium:
                build_matcher(
                    tinycss2.parse_rule_list(rule.content, skip_comments=True, skip_whitespace=True),
                    medium,
                    matcher,
                )
        if rule.type == "qualified-rule":
            declarations = tinycss2.parse_declaration_list(
                rule.content, skip_comments=True, skip_whitespace=True
            )
            for declaration in declarations:
                if declaration.type != "declaration":
                    raise ValueError(f"Invalid declaration on line {declaration.source_line}")
            for selector in cssselect2.compile_selector_list(rule.prelude):
                matcher.add_selector(selector, declarations)


def declarations_by_element(css, theme_class, medium):
    matcher = cssselect2.Matcher()
    build_matcher(css, medium, matcher)
    root = cssselect2.ElementWrapper.from_html_root(ElementTree.fromstring(f"""
        <body id="page" class="{theme_class}">
          <article id="note" class="markdown-rendered">
            <h2 id="heading">Heading</h2>
            <div class="callout"><div id="callout-title" class="callout-title">Tip</div></div>
            <table><thead id="headers"><tr><th>Column</th></tr></thead>
              <tbody><tr id="row"><td>One</td></tr><tr><td>Two</td></tr></tbody>
            </table>
            <pre id="code">Long line of code</pre>
          </article>
        </body>
    """))
    resolved = {}
    for element in root.iter_subtree():
        values = {}
        if element.parent is not None:
            values.update({
                name: value for name, value in resolved[element.parent].items()
                if name.startswith("--")
            })
        matched = {}
        for specificity, order, pseudo, declarations in matcher.match(element):
            if pseudo is None:
                for declaration in declarations:
                    rank = (declaration.important, specificity, order)
                    previous = matched.get(declaration.name)
                    if previous is None or rank >= previous[0]:
                        matched[declaration.name] = (rank, tinycss2.serialize(declaration.value).strip())
        values.update({name: entry[1] for name, entry in matched.items()})
        resolved[element] = values
    return {
        element.id: values for element, values in resolved.items() if element.id is not None
    }


class ThemeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.css = tinycss2.parse_stylesheet(
            (ROOT / "theme.css").read_text(encoding="utf-8"),
            skip_comments=True,
            skip_whitespace=True,
        )

    def test_print_palette_overrides_screen_mode_on_the_page_and_in_the_note(self):
        for theme in ("theme-dark", "theme-light", ""):
            print_styles = declarations_by_element(self.css, theme, "print")
            for element in ("page", "note"):
                with self.subTest(theme=theme, element=element):
                    styles = print_styles[element]
                    self.assertEqual(styles["--background-primary"], "#fff")
                    self.assertEqual(styles["--text-normal"], "#182735")
                    self.assertEqual(styles["--link-color"], "#1c4b78")
                    self.assertEqual(styles["--link-external-color"], "#1c604b")
                    self.assertEqual(styles["--code-background"], "#eef2f5")
                    self.assertEqual(styles["--code-normal"], "#182735")

    def test_screen_palette_still_depends_on_the_selected_mode(self):
        light = declarations_by_element(self.css, "theme-light", "screen")
        dark = declarations_by_element(self.css, "theme-dark", "screen")
        self.assertEqual(light["note"]["--background-primary"], "#ffffff")
        self.assertEqual(dark["note"]["--background-primary"], "#18222e")
        self.assertEqual(dark["note"]["--link-color"], "#a5d0fa")
        self.assertEqual(dark["note"]["--code-normal"], "#eef4fa")

    def test_callout_titles_use_dark_text_only_in_print(self):
        for theme in ("theme-light", "theme-dark", ""):
            with self.subTest(theme=theme):
                print_styles = declarations_by_element(self.css, theme, "print")
                screen_styles = declarations_by_element(self.css, theme, "screen")
                self.assertEqual(print_styles["callout-title"]["color"], "var(--text-normal)")
                self.assertNotIn("color", screen_styles["callout-title"])

    def test_print_styles_keep_headings_with_text_and_wrap_code(self):
        styles = declarations_by_element(self.css, "theme-dark", "print")
        self.assertEqual(styles["heading"]["break-after"], "avoid")
        self.assertEqual(styles["headers"]["display"], "table-header-group")
        self.assertEqual(styles["row"]["break-inside"], "avoid")
        self.assertEqual(styles["code"]["white-space"], "pre-wrap")
        self.assertEqual(styles["code"]["overflow-wrap"], "anywhere")


if __name__ == "__main__":
    unittest.main()
