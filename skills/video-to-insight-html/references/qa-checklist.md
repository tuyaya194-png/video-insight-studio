# Pre-delivery QA Checklist

## Content consistency

- [ ] Record title, speaker, platform, date, URL, and subtitle or transcript source.
- [ ] Separate direct claims, speaker examples, and analyst inference.
- [ ] Include a thesis, logical chapter progression, practical relevance, possible actions, and applicability.
- [ ] Keep core claims and page order identical across both HTML versions.
- [ ] Do not add unsupported conclusions to the visual review version.
- [ ] Record the output language. In bilingual mode, keep pages aligned without shrinking text or crowding the canvas.
- [ ] Preserve the original source link and state that the output is an analysis aid, not a copy or replacement for the video.

## Deep-reading functionality

- [ ] The 3:4 canvas has no overflow, clipping, or abnormal scaling at 1080×1440.
- [ ] Every page is independently understandable with clear typography and hierarchy.
- [ ] Previous, next, play/pause, progress, and keyboard controls work.
- [ ] `?clean=1` hides controls and `?autoplay=1` starts playback.
- [ ] Timing matches narration or text length, and the last page ends or loops correctly.

## Visual review quality

- [ ] Each page contains one core claim and one primary visual relationship.
- [ ] The lower visual field uses one consistent raised baseline.
- [ ] Comparable icons use the same size, stroke, frame, and alignment.
- [ ] Labels have consistent spacing; no icon, line, or text overlaps another element.
- [ ] Arrow lengths, weights, heads, and endpoints are consistent and stop at node boundaries.
- [ ] Nodes render above connectors, so no line cuts a frame or circular background.
- [ ] Every loop fully closes and every node center sits on the same circumference, with no extra outer ring or radial stub.
- [ ] The loop passes behind opaque node backgrounds without cutting icons or frames.
- [ ] Color meaning remains consistent; no one-off fill or stray color is introduced.
- [ ] A viewer can identify flow, comparison, convergence, layers, loop, or divide within two seconds.

## Browser acceptance

- [ ] Inspect every page of both versions at 1080×1440 or an equivalent 3:4 viewport.
- [ ] Capture at least one stable-state screenshot per page type; capture every complex flow and loop.
- [ ] Inspect animation entry, transition, and stable state for temporary overlap.
- [ ] Test the largest heading, smallest text, longest label, and difficult wrapping cases.
- [ ] Keep every node inside its parent container and eliminate horizontal or vertical scrollbars.
- [ ] Confirm the console has no JavaScript error and external failures do not break core rendering.
- [ ] Visit both preview URLs instead of assuming the server command succeeded.
- [ ] Record actual ports and explain that localhost links stop when the server stops.

## Automated structural validation

```bash
python3 scripts/validate_project.py \
  --text-dir "/absolute/path/to/deep-reading" \
  --presentation-dir "/absolute/path/to/visual-review"
```

Automated validation is only a minimum gate. It never replaces browser-based visual inspection.
