# PEDAGOGY.md — Learning-Science Conventions (shared across ALL books in the series)

> Evidence-based pedagogy baked into every book, grounded in RCTs. Apply to all NEW chapters; retrofit the
> highest-value items (front-matter warning, teaching solutions) into existing ones. Portable to static HTML→PDF;
> the adaptive/interactive parts of Google's product are out of scope (companion-app only). Sources are real and
> cited; verify URLs at print.

## The evidence (why we do this)
- **Google "Learn Your Way" RCT** (Google Research, Sep 2025; arXiv:2509.13348): multiple synchronized
  representations + embedded active-retrieval questions + personalization vs a standard PDF reader. **Delayed
  retention (3–5 days): 78% vs 67%, +11 points (p=0.03)**; immediate +~9%. The durable win is attributed to
  active retrieval + dual coding, not the UI.
- **Harvard active learning** (Deslauriers et al., *PNAS* 2019): active learning **+0.46 SD on the actual test**
  yet students **rate their own learning −0.56 SD** — the *feeling-of-learning gap*. A ~20-min up-front framing
  intervention closes it. (Mazur Peer Instruction; Hake 1998 ≈2× normalized gain.)
- Canonical: retrieval practice / testing effect (Roediger & Karpicke 2006; ~56% vs 42% at 1 week); practice
  testing + distributed practice = highest-utility, rereading/highlighting lowest (Dunlosky et al. 2013);
  interleaving ~doubles delayed scores (Taylor & Rohrer 2010); worked-example effect + guidance fading (Sweller);
  self-explanation causes large gains (Chi 1989/1994, 82% vs 46%); elaborative interrogation (Willoughby & Wood
  1994); dual coding / multiple representations (Paivio; Ainsworth); desirable difficulties (Bjork); pretesting/
  curiosity gap; formative feedback (Hattie & Timperley 2007).

## THE central principle for a self-study book — the feeling-of-learning gap
A lone reader with a PDF will abandon effortful methods (retrieval, faded examples, interleaving) for re-reading
that *feels* productive but teaches little — no instructor holds the line. So every book must:
1. **Warn up front and at point of use.** Front-matter section **"How to use this book (and why the good parts
   feel harder)"** — state plainly (citing PNAS 2019) that retrieval/faded/mixed work feels slower and less
   pleasant than re-reading, and *that discomfort is the learning*; re-reading feels great and teaches little.
   Repeat a one-line version at point of use.
2. **Make effortful mechanics low-friction** (seconds, not minutes) so they actually get done.
3. **Build self-calibration** so the reader sees the method worked *on them* (belief → data).

## Concrete conventions (apply to all new chapters)

**Chapter opener — a `recall` block.** Right after `p.chapter-nav`, an `aside.recall` ("Before you read on"):
2–4 questions, **≥1 drawn from 2–3 chapters back** (spacing), answers WITHHELD (resolve in-text or in solutions).
For a brand-new topic, ask the reader to *predict/guess* (pretesting/curiosity gap).

**In-chapter checkpoints.** Every 1–2 sections, a 1-line `aside.recall` "Quick check" — one question answered from
memory; answer one page-turn away (below a rule / next page in the PDF), never on the same line.

**Worked → faded → independent ladder.** For each major skill: (1) fully worked *with the reasoning for each
step*; (2) **faded** — same solution with the last step(s) blanked for the reader to complete (backward fading),
scaffold given; (3) independent. Use exercise KIND **`faded`**; solutions for faded rungs show the filled step
*plus why that step and not another*.

**Interleaving at the practice layer.** Topics are taught blocked (correct for first exposure); interleave in
*exercises*: include **`mixed`** items requiring the reader to first *decide which method applies* (don't name the
method in the prompt), including methods from earlier chapters. A part-boundary **"mixed bag"** set shuffles types.

**Self-explanation / elaborative interrogation.** Make the `communicate` ("Say it like an X") box **prompt-then-
reveal** (reader articulates first, then the model answer). Inside worked examples, add bracketed **"Why this
step?"** questions on load-bearing (not trivial) steps, answered before the text explains.

**Multiple representations — "same idea three ways."** For each central concept, present it in three complementary
codes: (a) prose/definition, (b) a diagram (inline SVG, informative-only), (c) a **worked trace / concrete
example** (a step-by-step state table: input→state→output). Optional `aside.threeways` to make it a habit. One
tight, disposable analogy per hard concept, immediately followed by the precise mechanism.

**Metacognition.** Phrase the `takeaway` "Key ideas" as a **"Can you… *without looking*?" checklist**. On quizzes,
ask **confidence (low/med/high) before revealing** the answer; flag that overconfidence on a missed item is the
highest-value signal.

**End-of-chapter retrieval + end-of-part cumulative quiz.** Keep the transfer-oriented exercises, but ADD a short
"Retrieval" block (3–5 closed questions on the chapter's core, answers in solutions) distinct from the exercises.
At each **part boundary**, an 8–12 question cumulative quiz sampling all chapters in the part (cumulative retrieval
+ spacing), answers in back matter.

**Teaching solutions (strengthen the existing standard).** Every solution states (a) the **why + method-
selection** ("we reached for X because the problem has property Y"), (b) a named **"tempting wrong answer / why
it's tempting"** where a classic trap exists, (c) a **feed-forward** pointer for hard items ("if you missed this,
revisit §N.k").

**Cognitive load.** The many-short-chapters (chunking) approach is well-supported — keep it. One new hard idea per
chunk; consistent, *small* box vocabulary (offload "what kind of thing is this" to stable layout); 2–5 informative
diagrams, never decoration. **Expertise-reversal caveat:** keep `warm`/`faded` rungs clearly labeled and skippable
so advanced readers jump to `core`/`stretch`.

## Style additions required
- New aside classes: **`recall`** (opener/quick-check), optionally **`threeways`**. Add CSS.
- New exercise KINDs: **`faded`**, **`mixed`** (added to warm/core/complexity/stretch/lab). Add CSS chips.

## NOT portable to a static PDF (companion-app / web edition only — do not promise)
On-demand personalization/regeneration; adaptive branching; audio lessons/narrated slides; interactive mind maps/
timelines; automatic answer-checking with tailored feedback. A static book offers *fixed* alternate framings, a
*fixed* concept-map SVG, and reader-graded pre-written feedback.
