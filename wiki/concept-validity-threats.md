---
title: Threats to Validity — the Four Validities
type: concept
tags: [validity, internal-validity, external-validity, construct-validity, statistical-conclusion-validity, confounds, campbell]
unit: 12
source_units: [12]
cluster: validity-threats
---

# Threats to Validity — the Four Validities

Once you can name the designs ([[concept-experimental-vs-correlational]]), the next question is sharper: *even granting the design, what could make this study's conclusion wrong?* Cook and Campbell's answer — the framework nearly every methods text still uses — is that any study makes **four** separate inferential leaps, and each has its own characteristic **threats**. Learning the four kinds of validity gives you a checklist for critiquing any study, and it clears up a confusion beginners carry for years: that "valid" is one thing. It is four things, and a study can be strong on one and fatally weak on another [S4].

Note the word **validity** is doing double duty in this curriculum. Unit 7's [[concept-reliability-validity]] is about the **validity of a measure** (does this test measure what it claims?). This page is about the **validity of a study's inferences** (can we trust the conclusion?). They are related — a study using an invalid measure has a **construct-validity** problem below — but they are not the same topic.

## The four validities, as four questions

Read them as a chain from the analysis outward to the world [S4][S5]:

| Validity | The question it answers | Threatened by… |
| --- | --- | --- |
| **Statistical-conclusion** | Is there a **real covariation**, and was it analyzed correctly? | low power, violated statistical assumptions, unreliable measures, **fishing** / inflated error rate from many tests, over-reliance on p < .05 |
| **Internal** | Did the **treatment** — not something else — cause the change? | the classic confounds below (history, maturation, selection…) |
| **Construct** | Do the **measures and operations** match the **constructs** we name? | a bad operationalization; a "depression" measure that really taps fatigue; demand characteristics; mono-method bias |
| **External** | Do the findings **generalize** to other people, settings, and times? | unrepresentative samples (the undergraduate-subject-pool problem), artificial settings, one narrow context |

A useful order of attack when reading a study: **internal** first (is the causal claim even defensible?), then **construct** (are they measuring what they say?), then **external** (who does this apply to?), with **statistical-conclusion** underneath all of it (are the numbers trustworthy?).

## The classic threats to internal validity

These are the alternative explanations random assignment is designed to kill — and the ones a **single-group** or **quasi-experimental** study leaves wide open [S4][S6]. Worth memorizing as a differential, because "which threat is this?" is exactly the kind of discrimination the unit quizzes:

- **History** — an outside event (not the treatment) happens between pre- and post-test (a news event, a policy change, a pandemic).
- **Maturation** — participants simply **change over time** (grow, age, heal, get tired) regardless of treatment. (Much "improvement" in untreated conditions is natural recovery.)
- **Testing** — taking the pre-test itself changes the post-test (practice effects, sensitization).
- **Instrumentation** — the **measure** changes (a rater gets more lenient; a form is revised) between assessments.
- **Statistical regression (regression to the mean)** — people selected for **extreme** scores drift back toward average on retest, with or without treatment. This one is a chronic clinical illusion: clients often enter at their **worst** (that's when they call), so *some* improvement is expected no matter what you do — mistaking it for treatment effect is a real error.
- **Selection** — the groups **differed to begin with** (the core flaw of any non-randomized comparison).
- **Attrition (mortality)** — participants **drop out** non-randomly, so the survivors no longer represent the starting groups (if the sickest quit, the treatment looks better than it is).

Random assignment plus a **control group** neutralizes most of these at once, because whatever history/maturation/regression is happening also happens **in the control group**, so it cancels out. That is the whole reason a control group exists — and why an uncontrolled "everyone got better after my program" claim is nearly worthless: you cannot separate the program from maturation, regression, and history.

## The internal ↔ external tradeoff

The deep tension of research design: the moves that buy **internal** validity often cost **external** validity, and vice versa [S6].

- A **tightly controlled lab experiment** (random assignment, standardized procedure, screened sample) maximizes internal validity — you can trust the causal claim — but the artificial, homogeneous conditions may not resemble a real clinic with real, comorbid clients.
- A **naturalistic field study** in an actual clinic maximizes external validity — it looks like practice — but admits confounds that muddy the causal claim.

No single study optimizes both. This is one of the strongest arguments for **replication across contexts** and for **systematic reviews** that pool many studies ([[concept-evidence-based-practice]]): the lab establishes *that* it works, the field establishes that it works *here*, and confidence comes from the convergence, not from any one study.

## Where this lands clinically

You don't design trials, but you constantly consume their conclusions and make your own informal ones. When a client says "the new supplement fixed my mood," the counselor who knows the threats hears the **rival explanations**: regression to the mean (they started it at rock bottom), history (their situation also changed), maturation (time), placebo/expectancy (construct issue). Not to debunk the client — to hold the causal claim at the right confidence, which is the same discipline you bring to a published study. And when you read that a program "improved outcomes," the reflex question is: *compared to what?* No control group, no defensible causal claim.

## Connects to

- [[concept-experimental-vs-correlational]] — random assignment (internal validity) vs. random sampling (external validity); the designs each validity favors.
- [[concept-effect-size]] — statistical-conclusion validity is where p-values, power, and effect sizes live; over-trusting p < .05 is a threat here.
- [[concept-evidence-based-practice]] — the evidence hierarchy and replication are the field's answer to no-single-study-does-everything.
- [[concept-reliability-validity]] (Unit 7) — the **measurement** sense of validity; an unreliable/invalid measure is a construct- and statistical-conclusion-validity threat.
- [[concept-single-case-design]] — how single-case designs use **baseline logic** to defend internal validity without a control group.

## Sources

[S4] Cook & Campbell (1979) / Shadish, Cook & Campbell (2002) — the four validities and the internal-validity threats. [S5] García-Pérez (2012), *Statistical Conclusion Validity*, Frontiers in Psychology. [S6] Trochim, *Research Methods Knowledge Base*; Portland State / Rakes teaching treatments — threat enumeration and the internal↔external tradeoff. Full notes in [`../research/unit12-research-sources.md`](../research/unit12-research-sources.md).
