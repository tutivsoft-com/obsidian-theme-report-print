# Report Print original design plan

This is the historical plan from 13 November 2026. See the [README](README.md) for the current theme and installation steps.

A professional Obsidian document theme with a planned print and PDF stylesheet.

**Status at the time: planning only.**

Plan date: 13 November 2026. The repository initially contained only this plan. The working name still needed a Community directory availability check.

Search keywords: Obsidian theme, PDF export, print, reports, document typography, tables.

## Who this is for

People who turn notes into reports, handouts and printable documents.

## User need and evidence

Users ask why their theme colours and formatting disappear during PDF export and want a more consistent document result.

- [Request to export a PDF with theme styling](https://www.reddit.com/r/ObsidianMD/comments/1i4f1g4/)

The request came from the preceding idea research. Other themes and snippets may address parts of this need.

## Planned appearance and features

- Use clean document typography, strong headings and restrained professional colours.
- Plan explicit print styling alongside screen styling.
- Keep tables readable with clear headers, borders and optional alternating row shading.
- Avoid splitting headings from following text and avoid splitting short callouts or table rows where the print engine allows.
- Keep code blocks, images, links and maths legible in exported pages.
- Provide a paper-friendly white export background; document which screen accents carry through.
- Document export-engine limits rather than promising identical screen and PDF output.

## Mode scope

Plan light and dark screen modes with a separate light print presentation.

## Future implementation and release plan

1. Confirm the final palette and layout against the requirements above.
2. Build the theme only after Rahul authorises implementation. Prefer supported Obsidian CSS variables and keep source readable.
3. Test representative notes, navigation, tabs, properties, menus, settings, search, Canvas and Bases where applicable. Include focus, selection, hover and error states.
4. Run the theme-specific checks below and record the actual Obsidian versions, devices and modes tested.
5. Prepare the root manifest, stylesheet, licence and real screenshots. Decide the first release version and minimum app version from actual testing.
6. Follow the current Obsidian submission guidance when a release is separately authorised. Commit source and screenshots, tag the intended revision, attach matching release assets and verify the published listing.

Keep assets offline, respect font and third-party licences, and avoid required plugins for the core appearance. Do not configure GitHub Actions or automatic deployment.

Official references for later implementation:

- [Build a theme](https://docs.obsidian.md/Themes/App%20themes/Build%20a%20theme)
- [Submit a theme](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme)
- [Developer policies](https://docs.obsidian.md/community-directory/developer-policies)

These references supported the original implementation and release plan.

## Acceptance checklist for later implementation

- [ ] Export representative notes to A4 and Letter PDF and inspect every page.
- [ ] Check page breaks, long tables, images, code and callouts.
- [ ] Verify supported export paths before making compatibility claims.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Scope of the original planning task

The original task covered repository creation and this plan. Theme source, screenshots and published releases followed in later work.
