---
title: "Reliability, Validity & Screening Statistics"
type: concept
tags: [reliability, validity, psychometrics, sensitivity, specificity, standardization, assessment]
unit: 7
source_units: [7, 12]
cluster: reliability-vs-validity
---

# Reliability, Validity & Screening Statistics

Every number this unit produces — a PHQ-9 score, an IQ, a personality profile — is only as good as the instrument behind it, and there are exactly two questions to ask of any instrument: **is it consistent (reliability)?** and **does it measure what we think it measures, for the use we're putting it to (validity)?** Get the relationship between those two backwards and you'll either trust a number you shouldn't or discard one you should. This page is the psychometric floor under [[concept-screening-tools]], and it's where [[unit04-multicultural | culture-fair assessment]] and [[concept-validity-threats | Unit 12's research methods]] meet clinical practice.

## Reliability — is it consistent?

Reliability is the **stability and consistency of scores** [S5]. Four kinds, by *what could vary*:

- **Test–retest reliability** — same test, same person, two time points. Does the score hold when the trait hasn't changed? (Confounded if the trait *does* change between administrations.)
- **Internal consistency** — do the items hang together, all tapping the same construct? Measured by **split-half** correlation or, standardly, **Cronbach's α** (0–1; **~0.70+** is the usual acceptable floor, ~0.80+ good) [S11]. This is the number quoted for the PHQ-9 (α ≈ .86) and GAD-7 (α ≈ .88).
- **Inter-rater reliability** — do two clinicians scoring the same client agree? Matters most for judgment-based ratings (an MSE, a structured interview). Poor inter-rater reliability is exactly the crack the dimensional critics drove through DSM categories ([[concept-categorical-vs-dimensional]]).
- **Parallel/alternate-forms** — do two versions of the test agree? (Relevant when you need to re-test without practice effects.)

## Validity — does it measure the right thing, for this use?

Validity is "the degree to which evidence and theory support the **interpretations of test scores for proposed uses**" — and the key subtlety is that **validity attaches to the interpretation and use, not to the test itself** [S5]. The same test can be valid for one purpose and invalid for another. Kinds of validity evidence, roughly weakest to strongest:

- **Face validity** — does it *look* like it measures the thing? (Weakest; about appearance/buy-in, not evidence.)
- **Content validity** — do the items cover the *whole* construct, not just part? (A depression scale that omitted sleep and appetite would have poor content validity.)
- **Criterion validity** — does the score correlate with an external benchmark (the "criterion")? Two timings: **concurrent** (correlates with a criterion measured *now* — e.g., PHQ-9 vs. a structured diagnostic interview) and **predictive** (predicts a *future* outcome — e.g., a risk scale predicting later attempts).
- **Construct validity** — does the test behave the way the *theory* of the construct says it should? Supported by **convergent** evidence (correlates with things it should — GAD-7 with the BAI, r≈.69) and **discriminant** evidence (does *not* correlate with things it shouldn't) [S10].

## The one relationship to never get backwards

> **Reliability is necessary but not sufficient for validity. A test can be reliable without being
> valid — but it cannot be valid without being reliable.** [S5][S11]

The dartboard image: **reliable but invalid** = a tight cluster of darts in the wrong corner (consistent, consistently wrong — a bathroom scale 10 lb heavy every time). **Valid** requires the darts cluster *on the bullseye* — which means they must cluster at all (reliable) *and* land in the right place. So reliability is the floor: an unreliable measure is just noise, and noise can't be valid; but a rock-solid reliable measure can still measure the wrong construct entirely. **Consistency is not correctness.**

## Standardization and norms — the quiet third requirement

A number is meaningless without a **comparison group.** **Standardization** = fixed administration procedures (same instructions, same conditions) *plus* a **representative normative sample** the score is compared against [S5]. This is where clinical assessment collides with Unit 4: **a test validated and normed on one population can misfire on another.** A "score in the clinical range" means "clinical relative to *these norms*" — apply it outside that population and the interpretation may be invalid even if the test is impeccable. Psychometric quality **does not license use**: trustworthy assessment needs reliability + validity evidence + standardized administration + representative norms + qualified interpretation + fairness across groups [S5]. This is [[concept-cultural-humility | cultural humility]] in numeric form.

## Screening statistics: sensitivity, specificity, and predictive value

A slightly different question: not "is the scale consistent?" but "**when it flags someone, how much should I believe it?**" Four terms [S9]:

- **Sensitivity** = of everyone who *has* the condition, the fraction the test catches (true positives). A **sensitive** test, when **negative**, helps **rule OUT** — *SnNOut.*
- **Specificity** = of everyone who *doesn't*, the fraction the test correctly clears (true negatives). A **specific** test, when **positive**, helps **rule IN** — *SpPin.*
- **PPV / NPV** — of those the test flags positive/negative, the fraction who truly are/aren't. Unlike sensitivity/specificity, **PPV and NPV depend on prevalence**: the *same* test yields a lower PPV in a low-prevalence setting (more of its positives are false alarms).

### The trade-off, and why screens are built to over-flag

Sensitivity and specificity **trade off**: move a cut-point to catch more cases and you catch more false alarms too [S9]. **Screening instruments are deliberately tuned toward high sensitivity** — missing a case (a suicidal client cleared as fine) is worse than a false positive (a well client sent for a closer look). That's *why* the PHQ-9/GAD-7 cut-points feel low and why a positive screen is a **flag to assess further, never a diagnosis** ([[concept-screening-tools]]). A **diagnostic** test (or, here, the clinical interview) can afford higher specificity because it comes *after* the screen has already narrowed the field.

## Sources

[S5] IOM, *Overview of Psychological Testing* (NBK305233). [S9] StatPearls, *Sensitivity and Specificity* (NBK557491). [S10] Rutter & Brown (2017), GAD-7 psychometrics. [S11] *Research Methods in Psychology*, 2nd Canadian Ed. (OER). Full notes in [`../research/unit07-assessment-sources.md`](../research/unit07-assessment-sources.md).
