# Dual-HTML Visual System

## 1. Shared canvas and technical constraints

- Use a 3:4 portrait canvas and validate at 1080×1440.
- Deliver a single `index.html` with inline CSS and JavaScript. Core rendering must not depend on external fonts, icon libraries, or scripts.
- Use a system font stack. Include appropriate CJK system fonts for Chinese output.
- Keep the verified paper gray, deep navy, functional blue, result green, and emphasis orange. Color communicates meaning and must not change arbitrarily between pages.
- Support the normal control mode and `?clean=1`; preserve the template's autoplay behavior.

## 2. Deep-reading version

- The page must be understandable without a presenter. Use 12–24 scenes.
- Support Chinese, English, and bilingual output. In bilingual mode, split pages to preserve legibility and white space instead of shrinking both languages into one crowded frame.
- Keep one main conclusion per page. Organize information with large type, short paragraphs, comparisons, steps, and restrained emphasis.
- Complete explanations are welcome, but a long article must be divided into paced scenes.
- Keep previous, next, play/pause, progress, keyboard controls, notes, and text-length-driven timing.
- Decoration must serve hierarchy. Remove icons and lines that do not express a real relationship.

## 3. Visual review version

### Page hierarchy

1. Upper half: one core claim, identical to the deep-reading version.
2. Lower half: one visual relationship, not another explanatory paragraph.
3. Footer: the template's phase rail, page number, or required controls.

Keep the lower visual field on one consistent, slightly raised baseline. Use the template's established transform instead of per-page patches.

### Node system

- Use the same frame size, corner radius, stroke weight, and icon viewport for all comparable nodes.
- Nodes on one row must be equal in size and aligned to the same centerline.
- Use static Lucide 24×24 line paths. Do not combine multiple icons into one complex symbol.
- Keep node backgrounds in the paper color; use strokes and icon color for semantic distinction.
- Keep labels short enough for the selected language and place them at a consistent distance below nodes.
- Draw connectors behind node backgrounds. Lines must never cut through icons, node frames, or labels.

### Semantic colors

- Deep navy: problem, business context, human judgment, or neutral start.
- Functional blue: AI, resources, tools, and computation.
- Result green: validation, completion, outcomes, and adoption.
- Emphasis orange: decisions, key choices, the user, or an important human action.
- Light gray: supporting relationships, the background grid, and secondary borders.

Use each color consistently across the full series.

## 4. Six visual grammars

### Flow

- Arrange 3–6 equal nodes on one horizontal line.
- Keep equal spacing and identical arrow length and weight.
- Start and end lines at node boundaries; arrowheads must not enter icons.

### Compare

- Give both sides the same dimensions, baseline, and structure.
- Express difference through color, labels, or a restrained result marker—not accidental visual imbalance.

### Converge

- Arrange sources in a clean column or arc and converge them into one target.
- Lines leave the center of each source frame, merge outside label safe zones, and form one final arrow into the target boundary.
- Do not let lines cover nodes, labels, or form messy crossings.

### Layers

- Use three vertical or concentric layers to express foundations, capability stacks, or leverage.
- Give each layer one icon and one short label. Do not add decorative connectors.

### Loop

- The ring must visibly close. Do not use a fixed dash pattern that creates an accidental gap.
- Place every node center on one circumference. Draw only the ring; do not add a second outer ring or radial connector stubs.
- Draw the ring first and nodes second. Opaque paper backgrounds must cover the ring so it appears to pass behind every node without cutting icons or frames.
- Use a directional gray solid line with a weight close to node borders. Use at most one direction cue between adjacent nodes.
- Keep the center label in clear white space.

### Divide

- Separate two states with one clear vertical or horizontal boundary.
- Keep equal visual weight on both sides. Show the behavior or outcome difference without complex scene illustration.

## 5. Prohibited patterns

- Do not add icons, colors, cards, or decorative lines merely to fill space.
- Do not repeat identical icons unless repetition clearly expresses quantity, groups, or comparison.
- Do not let lines cross icons, frames, text, or labels; do not hide arrowheads behind nodes.
- Do not mix arrow lengths, weights, heads, or endpoints without meaning.
- Do not create detailed composite icons or stack two icons.
- Do not put paragraphs in boxes and call them a visualization.
- Do not skip real browser screenshot inspection.
