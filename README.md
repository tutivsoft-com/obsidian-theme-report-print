# Report Print

An Obsidian theme for reading notes on screen and exporting reports, handouts and other documents to PDF.

Source version 3.6.2. The theme supports dark and light screen modes and requires Obsidian 1.15.1 or newer.

Print uses a white page with dark body and callout title text, blue internal links and green external links. The stylesheet asks the print engine to repeat table headers, keep headings with the following text and wrap long code lines. Pagination and background shading can vary with the export engine.

## Preview

![Dark mode](screenshot.png)

![Light mode](screenshot-light.png)

[Desktop and PDF verification](docs/ui-qa-2026-11-24/README.md)

## Install

Find **Report Print** under **Settings > Appearance > Themes** or follow these steps to install manually.

1. Download `manifest.json` and `theme.css` from the [latest published release](https://github.com/tutivsoft-com/obsidian-theme-report-print/releases/latest).
2. Put both files in `.obsidian/themes/Report Print/` in your vault.
3. Open **Settings > Appearance** and select **Report Print**. Choose a supported base colour scheme.

## Run the stylesheet tests

The tests use Python with `cssselect2` and `tinycss2`.

```text
python -m pip install cssselect2 tinycss2
python -B -m unittest discover -s tests
```

See the [original design plan](PLAN.md). [MIT license](LICENSE).
