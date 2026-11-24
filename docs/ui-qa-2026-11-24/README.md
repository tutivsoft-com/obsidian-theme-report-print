# Report Print desktop and PDF verification

Tested source version 3.6.2 in Obsidian 1.15.1 on Windows on 24 November 2026. The isolated vault contained synthetic notes and a chart. Report Print has no theme-specific settings panel. The test used Obsidian's built-in Appearance, note views, and Export to PDF controls.

Obsidian's desktop mobile emulation also applied the theme's 8 px editor padding.

## Fixed print contrast

The 3.6.1 Letter PDF rendered the tip callout title in bright cyan (`#00bfbc`) on a pale cyan background. Version 3.6.2 uses the theme's dark print text (`#182735`) for callout titles and retains the callout tint. The export regression check reads the title color from the saved PDF. The stylesheet test checks that the rule applies in print and leaves screen callout styles alone.

## Desktop screenshots

These captures show the rendered Obsidian window or settings window at its original resolution.

| Evidence | State checked |
| --- | --- |
| [01](01-dark-reading-report.jpg) | Dark Reading view with properties, report heading, inline highlight, links, note callout and short table. |
| [02](02-dark-reading-code-and-chart.jpg) | Dark Reading view after scrolling to the quote, inline code, equation, long code and chart. |
| [03](03-dark-live-preview-editor.jpg) | Dark Live Preview editor with focus, rendered callout, table and tasks. |
| [04](04-dark-source-editor.jpg) | Dark Source mode with Markdown and task markers visible. |
| [05](05-light-reading-report.jpg) | Light Reading view with the same report and scheme-specific colors. |
| [06](06-light-note-options.jpg) | Light note menu with the native Export to PDF command. |
| [07](07-light-register-table.jpg) | Light Reading view with the 42-row inventory table. |
| [08](08-export-a4-portrait.jpg) | A4 portrait export from dark mode with file title, default margins and 100% scale. |
| [09](09-export-letter-landscape.jpg) | Letter landscape export from light mode with file title off, minimal margins and 85% scale. |
| [10](10-light-appearance.jpg) | Appearance settings showing the selected scheme and Report Print theme. |

## PDF exports

The Obsidian export action generated six PDFs. The test harness supplied a path in the isolated test directory in place of the Windows save picker so that the same action could run repeatedly. The app rendered and saved each PDF through its built-in export pipeline.

| Paper | Orientation | File title | Margins | Scale |
| --- | --- | --- | --- | --- |
| [A4](report-a4-portrait.pdf) | Portrait | On | Default | 100% |
| [Letter](register-letter-landscape.pdf) | Landscape | Off | Minimal | 85% |
| A3 | Portrait | Off | None | 90% |
| A5 | Portrait | On | Minimal | 95% |
| Legal | Landscape | Off | Default | 10% |
| Tabloid | Portrait | On | None | 100% |

The A4 export contains the links, formatted text, callout, tasks, chart, equation and closing marker. The long code line wraps and retains its ending marker. Both pages of the Letter export show the table header, and all 42 records appear once, in order. The test checked each file's page size and orientation, title toggle, and the Export dialog's Cancel control. No printer was used.

## Reproduce

1. Copy the files from [fixtures](fixtures/) into a test vault. Install the root `manifest.json` and `theme.css` under the vault's `.obsidian/themes/Report Print` folder.
2. Activate Report Print in Appearance. Open Operations report in Reading view, then switch among Live Preview, Source mode, and the light and dark base schemes.
3. Export Operations report as A4 and Quarterly register as Letter using the settings above. Review the callout titles, code ending, chart, links, and table headers.
4. Run `python -B -m unittest discover -s tests` from the root of this repository.
