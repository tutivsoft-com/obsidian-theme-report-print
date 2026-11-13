# Report Print

A professional Obsidian document theme with a planned print and PDF stylesheet.

**Status: planning only. No theme code has been written.**

Plan date: 13 November 2026. This repository currently contains this planning README only. The name is a descriptive working name; Community name availability must be checked before any future submission.

Search keywords: Obsidian theme, PDF export, print, reports, document typography, tables.

## Who this is for

People who turn notes into reports, handouts and printable documents.

## User need and evidence

Users ask why their theme colours and formatting disappear during PDF export and want a more consistent document result.

- [Request to export a PDF with theme styling](https://www.reddit.com/r/ObsidianMD/comments/1i4f1g4/)

The Reddit links come from the preceding idea research and represent qualitative demand, not a market-size estimate or proof that existing themes do not solve the problem. For Pure OLED Rainbow, the additional requirement comes directly from the owner. Other themes and snippets may already address parts of these needs.

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

These are future work items. No release, installation instructions, compatibility certification or Community listing is being claimed by this planning repository.

## Acceptance checklist for later implementation

- [ ] Export representative notes to A4 and Letter PDF and inspect every page.
- [ ] Check page breaks, long tables, images, code and callouts.
- [ ] Verify supported export paths before making compatibility claims.
- [ ] Confirm every claimed feature has been implemented and tested before replacing the planning-only status.
- [ ] Review screenshots for private information and verify all published documentation and asset paths.
- [ ] Verify the default branch, release revision and uploaded assets before calling any future release complete.

## Current boundary

Only repository creation and this Markdown plan are authorised in this task. Do not add theme CSS, manifests, screenshots, release tags or submissions as part of this planning work. Future work stays on this repository's verified primary branch.
