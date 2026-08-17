# Video Viewpoint Analysis Method

## 1. Source threshold

Before analysis, record the title, speaker, platform, publication date, original URL, and subtitle or transcript source. Preserve timestamps for important claims when available.

Also record the output language: `zh-CN`, `en`, or `bilingual`. If the user does not specify one, use the conversation language. For cross-language work, separate source meaning, translation, and analytical interpretation so polished translation is not mistaken for the speaker's exact wording.

Classify content into three categories:

1. **Direct claims:** judgments explicitly stated by the speaker.
2. **Evidence and examples:** cases, data, or analogies used by the speaker.
3. **Analytical interpretation:** synthesis, extension, or criticism added to help the user understand.

Mark the third category with language such as “This can be understood as,” “This implies,” or “A more precise formulation is.” Never infer a full argument from the title, thumbnail, or a secondary summary.

## 2. Copyright and usage boundaries

- Preserve the title, creator or speaker, platform, and original link so readers can return to the source context.
- Produce analysis, summary, paraphrase, and understanding aids. Do not include the full transcript, long continuous quotations, source media, thumbnails, or paid material by default.
- Do not describe the HTML outputs as a replacement for the original video or recommend public redistribution by default.
- If the user plans public or commercial use, remind them to confirm rights for media, quotations, and translations.

## 3. Argument hierarchy

Build one complete chain:

`thesis → mechanism → real-world expression → ordinary-life example → possible action → applicability`

- **Thesis:** what belief does the video want the viewer to reconsider?
- **Mechanism:** why would the change happen?
- **Real-world expression:** how does it appear in work, daily life, or organizations?
- **Ordinary-life example:** show a concrete task, not only an occupation name.
- **Possible action:** what can the reader try tomorrow, and how can they evaluate it?
- **Applicability:** under what conditions might the conclusion not hold?

Chapters must advance the reasoning rather than sit as parallel quotations. Use 6–10 chapters, each with one primary logical job.

## 4. Practical relevance

For every major claim, ask:

- What work habit, competitive advantage, or choice does this change?
- Does it affect income, time, risk, trust, or decision authority?
- What real task can a person test tomorrow?
- Which judgment, responsibility, and interpersonal steps must remain human-owned?

“Benefit” does not mean money alone. Check five dimensions and retain only those supported by the source:

1. **Opportunity:** a lower barrier or a new space for value.
2. **Efficiency:** less time, cost, or experimentation.
3. **Capability:** knowledge, judgment, or human skills that become more valuable.
4. **Risk:** standardized value that may decline and decisions that must not be outsourced.
5. **Action:** a low-cost, testable real-world experiment.

Separate the speaker's explicit advice from application-level inference. If a benefit cannot be reasonably derived from the source, say so instead of forcing one.

Avoid vague advice such as “keep learning” or “embrace change.” A useful action includes a verb, object, and evaluation standard. Example: choose a repeated weekly task, ask AI for a first draft, log every error, encode the human judgment criteria into the workflow, then compare time and quality.

## 5. Counterarguments and boundaries

Check these common overextensions:

- A trend does not establish a certain timeline.
- Automating standardized tasks does not mean an entire profession disappears.
- Lowering the cost of baseline output does not make domain knowledge irrelevant.
- Phrases such as “smarter” or “replaced” may be hooks; restore the narrower capability they actually describe.
- Individual outcomes also depend on institutions, resources, markets, teams, and responsibility boundaries.

For disputed claims, use a three-part treatment: when the original claim is valid, how it is easily misunderstood, and what a more precise formulation would be.

## 6. Shared content master

Append this structure to `viewpoint-analysis.md` and use it as the common source for both HTML versions:

```markdown
# Shared content master

Topic:
One-sentence thesis:
Output language: zh-CN / en / bilingual

## Page 1 | Chapter name
- Core claim:
- Full explanation:
- Ordinary-life example:
- Boundary / misunderstanding:
- Note / review cue:
- Diagram: flow / compare / converge / layers / loop / divide
- Nodes:
```

The core claim must match exactly across both HTML versions. `body` explains, `note` adds context, and `diagram` expresses one relationship; none should substitute for another. In bilingual mode, preserve semantic alignment without sacrificing accuracy to literal translation.
