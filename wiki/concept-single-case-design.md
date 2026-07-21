---
title: Single-Case Designs & Progress Monitoring
type: concept
tags: [single-case-design, single-subject, aba, abab, reversal, multiple-baseline, progress-monitoring, measurement-based-care]
unit: 12
source_units: [12]
cluster: research-designs
---

# Single-Case Designs & Progress Monitoring

Group research answers "does this work **on average, across people**?" But a counselor sits with **one** person, and often wants to know something a group study can't tell them: "is this working for **this** client?" Single-case methods are built for exactly that question — and the surprising, useful fact is that you can run a **genuine experiment on a single participant**, with real internal validity, without a control group. This is also the design tradition (from applied behavior analysis and special education) closest to everyday clinical practice, which is why the course-map flags it as a discrimination target and why counselors report doing single-case and outcome evaluation more than any other kind [S15][S17].

## The core move: repeated measurement across phases

A single-case (single-subject) experimental design measures the outcome **repeatedly over time**, dividing the study into labeled **phases** — conventionally **A** for baseline and **B** for treatment [S15]:

- **Baseline (A)** — repeated measurement with **no treatment**, continued until the behavior is **stable** (the "steady state"). The baseline is the comparison the whole design rests on: it's what the client's trajectory looks like *without* the intervention.
- **Treatment (B)** — the intervention is introduced and measurement continues.

A bare **AB** design (baseline, then treatment) shows *change*, but can't rule out [[concept-validity-threats | history or maturation]] — maybe the client would have improved anyway. The experimental single-case designs add controls that defend the causal claim.

## The two workhorse designs

**Reversal (ABAB / withdrawal) design.** Introduce treatment (B), then **withdraw** it (return to A), then **reintroduce** it (B). If the behavior improves under treatment, drifts back toward baseline when it's removed, and improves *again* when it's reapplied, the treatment — not some coincidental outside event — is almost certainly the cause. That tracking-with-the-phases is the strongest single-case demonstration of causation [S15]. Its limits are obvious and important: you can't (and shouldn't) **withdraw** a treatment for a dangerous behavior, and some gains **don't reverse** (a skill, once learned, stays learned) — in both cases reversal is the wrong tool.

**Multiple-baseline design.** The ethical and practical fix. Instead of withdrawing treatment, **stagger its onset** across several baselines — across **behaviors** (same person, different targets), **settings** (same person, different contexts), or **people**. If each baseline changes **only when treatment reaches it** — and not before — the staggered pattern rules out history/maturation just as convincingly, **without ever removing an effective treatment** [S15]. This is the design of choice when reversal is unethical or impossible.

## How you read the data: visual inspection

Single-case data are judged primarily by **visual inspection** of the graph — not (mainly) by inferential statistics — along three features [S15]:

- **Level** — the average height of the outcome within a phase (did it jump?).
- **Trend** — the slope across observations (was it already climbing, or did treatment bend the line?).
- **Latency** — the **time between** the phase change and the change in behavior (a fast, tight response to each phase change is more convincing than a slow, ambiguous drift).

A convincing single-case result shows changes in level/trend that are **large, immediate, and repeated** at each phase change. (Statistical methods for single-case data exist and are growing, but remain supplementary to the visual analysis.)

## Single-case design vs. a case study — don't confuse them

A perennial mix-up (and a clean exam discrimination): a **case study** is **descriptive** — a rich narrative account of one person, with **no manipulation** and **no baseline logic**, so it cannot support a causal claim (it sits near the **bottom** of the evidence hierarchy, [[concept-evidence-based-practice]]). A **single-case experimental design** systematically **manipulates** the intervention against a **stable baseline** with repeated measurement, so it **can** support causal inference. Same "N = 1," opposite evidentiary weight. (Confusingly, both are sometimes called "case" work — read for the **baseline + manipulation**, which only the experimental design has.)

## The clinical cousin: progress monitoring / measurement-based care

Strip a single-case design down to its most usable core — repeated measurement of one client, plotted over time — and you have **progress monitoring**, the practice-level tool this whole thread has been building toward. In everyday care it's usually an **AB** design (no reversal, no staggering), which means it is **good enough to guide *this* client's care but not to *prove* the therapy caused the change** — and that's the correct trade for clinical work.

**Measurement-based care (MBC)** formalizes it: routinely administer a brief outcome measure (the PHQ-9 / GAD-7 from Unit 7's [[concept-screening-tools]]), plot the scores, and **use them to adjust treatment** — the "golden thread" of [[concept-treatment-planning]] made continuous. Its payoff is specific and evidence-backed: MBC and **feedback-informed treatment** improve outcomes especially by catching the client who is **not on track** — the quietly deteriorating person whom clinical intuition, left alone, tends to miss [S16]. And the question "is this 4-point drop real or just noise?" is answered by the **reliable change index** on [[concept-effect-size]]. This is measurement in service of the relationship, not a reduction of the person to a number — the unit's stance, made concrete.

## Connects to

- [[concept-experimental-vs-correlational]] — single-case designs are true experiments scaled to one participant; baseline logic replaces the control group.
- [[concept-validity-threats]] — reversal/multiple-baseline are ways to defend **internal** validity (rule out history/maturation) without a between-groups control.
- [[concept-effect-size]] — the reliable change index / clinical significance is how you read one client's outcome data.
- [[concept-evidence-based-practice]] — where single-case (and the case study it's confused with) sit on the evidence hierarchy; well-controlled single-case series can even support EST status.
- [[concept-screening-tools]] and [[concept-treatment-planning]] (Unit 7) — the instruments and the golden thread that progress monitoring runs on.

## Sources

[S15] Price et al., *Research Methods in Psychology* (single-subject chapter, fetched in full) + Kazdin, *Single-Case Research Designs* — reversal, multiple-baseline, visual inspection, case-study contrast. [S16] Fortney et al. (2017), *A Tipping Point for Measurement-Based Care*, Psychiatric Services. [S17] program-evaluation survey (counselors' frequent use of single-case/outcome evaluation). Full notes in [`../research/unit12-research-sources.md`](../research/unit12-research-sources.md).
