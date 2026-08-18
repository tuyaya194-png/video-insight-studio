---
name: video-to-insight-html
description: "Turn captioned YouTube videos, subtitle files, transcripts, interviews, or local media into source-grounded viewpoint analysis, then generate two 3:4 single-file HTML experiences: a Chinese, English, or bilingual deep-reading version and a visual review version for fast understanding and recall. Use for video analysis, video summaries, transcript analysis, cross-language reading, and long-video review."
---

# Video Insight Studio

Turn source material into a complete chain: **source-grounded analysis → shared content master → deep-reading HTML → visual review HTML → browser QA**. Both HTML versions must use the same claims and page order, but serve different reading needs.

## Why this skill is different

- **Crosses language barriers:** the deep-reading version can be Chinese, English, or bilingual.
- **Provides two reading speeds:** scan the visual structure first, then open the full reasoning when needed.
- **Analyzes instead of collecting quotes:** separate speaker claims, examples, evidence, interpretation, and applicability.
- **Finds practical relevance:** explain implications for work, learning, time, income, risk, and everyday decisions without inventing benefits unsupported by the source.
- **Uses one shared content master:** prevent the two outputs from drifting apart.
- **Creates durable HTML:** single-file, local-first, searchable, and reopenable offline without PowerPoint or a temporary localhost link.
- **Preserves traceability:** keep the original URL and timestamps when available; never present analysis as a direct quotation.
- **Requires visual QA:** inspect typography, wrapping, arrows, icons, loops, and the 3:4 canvas before delivery.

## Verified inputs and support boundaries

| Input | Status | Conditions |
| --- | --- | --- |
| Public YouTube URL | Verified | The video must be accessible and have manual or automatic captions. Private, region-restricted, or caption-disabled videos are not guaranteed. |
| `.srt`, `.vtt`, or `.txt` subtitles or transcripts | Verified | The most stable platform-independent entry path. |
| Pasted interview, podcast, or video text | Verified | Can go directly into analysis. |
| Local video or audio | Conditional | The current environment must provide a working speech-to-text tool. Check before promising delivery. |
| X, Bilibili, Xiaohongshu, and other platform URLs | Best effort, not promised | Process only when the current environment can legally read the content. Otherwise request subtitles, a transcript, or a local file immediately. |

For every URL, run a read-only availability check before committing to delivery. Fail early with a clear fallback instead of making the user install or wait before learning the content is inaccessible.

## First-run onboarding and defaults

Treat the user's first successful result—not documentation coverage—as the onboarding goal. Do not require the user to read the repository or understand every output option before starting.

When the user invokes the skill without source material, ask for exactly one of these entry paths in a compact message:

1. A public YouTube URL with accessible captions.
2. An `.srt`, `.vtt`, or `.txt` subtitle or transcript file.
3. Pasted transcript, interview, podcast, or video text.

State the defaults in the same message: use the conversation language for the deep-reading version, focus on the core argument and practical relevance for ordinary people, and create both HTML versions. Mention that the user can request Chinese, English, bilingual output, or a different focus, but do not make those choices mandatory.

When the user already provides a usable source, do not block progress with a preference questionnaire. Run the availability check, apply the defaults, and begin. Ask a follow-up only when a missing choice would materially change the result or the source cannot be accessed.

After the availability check, give one short kickoff summary:

```text
Source: accessible / blocked
Language: conversation language unless requested otherwise
Focus: core argument + practical relevance for ordinary people
Outputs: deep-reading HTML + visual review HTML
```

If the source is blocked, stop early and say what will unblock the work: upload subtitles, paste a transcript, or provide a readable local file. Do not make the user troubleshoot platform restrictions.

After delivery, offer only the most useful next adjustments: change language, change analytical focus, shorten or expand the output, or regenerate one version. Do not end with a list of every supported option.

## Required references

Before analysis, read [references/analysis-method.md](references/analysis-method.md) completely.

Before building HTML, read [references/visual-system.md](references/visual-system.md) completely. Reuse the verified template and visual grammar instead of inventing a new icon system.

Before delivery, read and execute [references/qa-checklist.md](references/qa-checklist.md) completely. Code inspection is not a substitute for browser-based visual QA.

## Workflow

### 1. Acquire trustworthy source material

- For YouTube, verify the page and captions, then record the title, speaker, publication date, caption source, and original URL.
- For unverified platforms, state whether the content is accessible in the first progress update. If it is blocked, request subtitles, a transcript, or a local file immediately.
- For local media, extract captions or transcribe the audio when a working speech-to-text tool is available.
- Distinguish direct speaker claims, source examples, and analytical interpretation. Never infer the full argument from a title or description alone.
- Preserve copyright boundaries: generate analysis, paraphrase, and understanding aids. Do not redistribute the source video, thumbnail, paid material, or a full transcript by default. Remind the user to confirm rights before public or commercial use.

### 2. Produce viewpoint analysis

- Write one thesis, followed by 6–10 logically connected chapters.
- Each chapter must include: core claim, explanation, an ordinary-life example, applicability or common misunderstanding, and a possible action.
- Explicitly answer “Why does this matter in ordinary life?” Look for opportunity, cost, risk, capability shifts, and a testable next step.
- Label the speaker's own advice separately from application-level inference.
- Correct attention-grabbing but overbroad claims. Replace statements such as “knowledge is useless” or “everyone will be replaced” with precise, conditional formulations.
- Finish a standalone `viewpoint-analysis.md` before designing pages.

### 3. Build one shared content master

For every page, record:

- `claim`: the unchanged core sentence at the top of both versions.
- `body`: the full deep-reading explanation.
- `note`: additional context or review guidance.
- `diagram`: one visual relationship for the lower half.
- `nodes`: the small set of objects and short labels required by the diagram.

Both versions must use the same page order, claims, and examples. The visual version must not invent conclusions that do not exist in the source material.

### 4. Initialize a project

```bash
python3 scripts/create_project.py \
  --name "Topic name" \
  --source-url "https://example.com/video" \
  --language "en" \
  --output-root "/path/to/output"
```

`--language` accepts `zh-CN`, `en`, or `bilingual`. The script creates a dated project directory with the analysis, both HTML versions, and project metadata. It does not overwrite an existing project.

### 5. Create the deep-reading HTML

- Copy and rewrite `assets/text-version/index.html` without changing its verified playback, navigation, or canvas structure.
- Follow the requested output language. If none is specified, use the conversation language.
- In bilingual mode, keep semantic alignment across languages and split pages when necessary rather than shrinking text.
- Use 12–24 independently understandable scenes with explanations, examples, boundaries, and actions.
- Preserve `?clean=1&autoplay=1`, text-length-driven timing, progress, keyboard controls, and notes.
- Prefer typography, hierarchy, comparison, and restrained geometry over decorative icon accumulation.

### 6. Create the visual review HTML

- Copy and rewrite `assets/presentation-version/index.html` without changing the verified node, connector, icon, or canvas coordinate system.
- Keep only the shared core claim in the upper half. Use the lower half for one diagram, not a second paragraph.
- Use only the defined flow, comparison, convergence, layers, loop, and divide grammars.
- Prefer static Lucide line icons. Keep labels short enough to remain legible in the selected language.
- Preserve `?clean=1`, autoplay, notes, keyboard controls, and the five-stage progress rail.
- Do not add icons, colors, or connectors merely to make a page look fuller. A viewer should identify the relationship within two seconds.

### 7. Validate and inspect in a browser

Run structural validation:

```bash
python3 scripts/validate_project.py \
  --text-dir "/absolute/path/to/deep-reading" \
  --presentation-dir "/absolute/path/to/visual-review"
```

Start both previews:

```bash
python3 scripts/serve_previews.py \
  --text-dir "/absolute/path/to/deep-reading" \
  --presentation-dir "/absolute/path/to/visual-review"
```

The server prefers ports 8765 and 8766 and moves to the next available ports when needed. A localhost URL stops working when the preview server stops; the underlying HTML remains valid.

Inspect every page at a 1080×1440 or equivalent 3:4 viewport. Pay special attention to long labels, arrows, loops, node edges, layer order, and clipping. Reinspect every affected page after a fix.

## Delivery requirements

Deliver all of the following:

- `viewpoint-analysis.md`: source record, thesis, chapter analysis, boundaries, practical relevance, and possible actions.
- `deep-reading/index.html`: Chinese, English, or bilingual; independently readable and suitable for repeated reference.
- `visual-review/index.html`: one core claim plus one clear visual relationship per page.
- Two locally verified preview URLs.
- A short note covering page count, autoplay, keyboard controls, and known limitations.
- The original source URL and copyright boundary.

Link to the generated files with absolute local paths. Do not deliver localhost URLs as the only output because they expire when the preview server stops.
