# Contributing

Thanks for helping improve Video Insight Studio.

## Before opening an issue

- Confirm the problem exists in the latest `main` branch.
- State whether it affects source analysis, text HTML, presentation HTML, preview serving, or validation.
- For visual bugs, include the slide number, viewport size, screenshot, and expected relationship.
- Do not upload private videos, transcripts, personal data, or copyrighted source files without permission.

## Pull requests

1. Keep `SKILL.md` concise and place detailed rules in `references/`.
2. Preserve the single-file and offline behavior of both HTML templates.
3. Keep connectors behind opaque nodes; no line may cut an icon, card, or label.
4. Update the bundled template and the example when a visual-system fix changes both.
5. Run the local validation commands below.

```bash
python3 -m py_compile \
  skills/video-to-insight-html/scripts/create_project.py \
  skills/video-to-insight-html/scripts/serve_previews.py \
  skills/video-to-insight-html/scripts/validate_project.py

python3 skills/video-to-insight-html/scripts/validate_project.py \
  --text-dir skills/video-to-insight-html/assets/text-version \
  --presentation-dir skills/video-to-insight-html/assets/presentation-version

python3 scripts/check_release.py
```

## Scope

Good contributions improve source fidelity, repeatability, offline portability, accessibility, or visual clarity. Decorative complexity, keyword stuffing, and platform-specific lock-in are out of scope.
