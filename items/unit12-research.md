# Unit 12 items — Research Methods & Program Evaluation

Source of truth for Unit 12 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. Per the course-map, this unit **quizzes choosing the
method, not executing it** — no hand-calculation; the skill is telling designs apart, reading an
effect size, ranking evidence, spotting a threat to validity, matching an evaluation type, and
applying a research-ethics principle. Item ids use the `u12-` prefix. Clusters: `research-designs`
(the prime "which design?" interleaving set), `validity-threats`, `significance-and-effect`,
`evidence-hierarchy`, `evaluation-types`, `research-ethics`. The unit's **stance thread** ("the
number is not the person": evidence informs but never replaces clinical judgment; group averages
under-describe individuals; measurement serves the relationship) runs through the throughline and
evaluate-level items. See generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## Research designs & causation (cluster: research-designs)

```json
[
  {
    "id": "u12-designs-recall-01",
    "prompt": "Two yes/no questions sort almost every quantitative design: (1) did the researcher manipulate a variable? (2) was assignment random? Use them to define the true experiment, the quasi-experiment, and the correlational study, and say which one supports a causal claim.",
    "answer": "TRUE EXPERIMENT = yes to both — the researcher manipulates the independent variable AND uses random assignment to conditions; ONLY this design licenses a causal claim. QUASI-EXPERIMENT = yes manipulation, NO random assignment — there's an intervention but groups form by a pre-existing feature; it sits between the other two on internal validity. CORRELATIONAL (non-experimental) = NO manipulation at all — variables are measured as they naturally occur; supports ASSOCIATION, not causation. The randomized controlled trial (RCT) is just a true experiment applied to a treatment.",
    "type": "recall",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "three-designs",
    "cluster": "research-designs",
    "bloom_level": "remember"
  },
  {
    "id": "u12-causation-three-recall-01",
    "prompt": "Name the three requirements for a causal claim, and identify which one random assignment is specifically built to satisfy.",
    "answer": "(1) COVARIATION — the variables actually move together; (2) TEMPORAL PRECEDENCE — the cause comes before the effect; (3) NO PLAUSIBLE ALTERNATIVE EXPLANATION — nothing else explains the covariation (confounds ruled out). RANDOM ASSIGNMENT is built to buy the THIRD one: by allocating people to conditions by chance, it makes the groups equivalent on average at the outset (on everything, measured or not), so any later difference is attributable to the manipulation. Correlational designs can deliver only the first.",
    "type": "recall",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "three-requirements-causation",
    "cluster": "research-designs",
    "bloom_level": "remember"
  },
  {
    "id": "u12-quasi-cloze-01",
    "prompt": "A study that has an intervention but assigns people to groups by a pre-existing feature (clinic A vs. clinic B) rather than by chance is a quasi-experiment: it has a manipulation but no {{random assignment}}.",
    "answer": "random assignment. Without it, the groups may differ at the outset (a selection confound), so a quasi-experiment sits between a correlational study and a true experiment on internal validity — better than correlational (there IS an intervention), weaker than an RCT.",
    "type": "cloze",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "quasi-experiment",
    "cluster": "research-designs",
    "bloom_level": "remember"
  },
  {
    "id": "u12-corr-causation-explain-01",
    "prompt": "'People who journal are less depressed.' Explain why this correlation cannot support 'journaling reduces depression,' naming the two specific problems.",
    "answer": "A correlation between X (journaling) and Y (lower depression) can arise three ways, and the data alone can't tell which. (1) The DIRECTIONALITY PROBLEM: maybe it's Y -> X (being less depressed gives people the energy to journal), not X -> Y. (2) The THIRD-VARIABLE PROBLEM: some Z causes BOTH (e.g., having stability and free time drives both journaling and lower mood). Because a correlational design has no manipulation and no random assignment, it can establish covariation but neither temporal precedence nor the ruling-out of alternatives — so 'correlation does not imply causation.' It's a worth-exploring lead, not a causal verdict.",
    "type": "explain",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "correlation-not-causation",
    "cluster": "research-designs",
    "bloom_level": "understand"
  },
  {
    "id": "u12-rct-explain-01",
    "prompt": "Explain the specific job random assignment does — why it, more than anything else, is what lets an experiment say 'caused.'",
    "answer": "Random assignment allocates participants to conditions BY CHANCE, which makes the groups EQUIVALENT ON AVERAGE AT THE OUTSET — on every variable, measured or not, including confounds nobody thought of. So if the groups differ AFTER the manipulation, the manipulation is the only systematic difference left standing to explain it. That is what 'control' means: it rules out the alternative-explanation requirement for causation. Note it's not the same as random SAMPLING (drawing a representative sample) — assignment buys internal validity (causal inference), sampling buys external validity (generalization).",
    "type": "explain",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "random-assignment-causation",
    "cluster": "research-designs",
    "bloom_level": "understand"
  },
  {
    "id": "u12-random-assignment-vs-sampling-compare-01",
    "prompt": "Contrast random ASSIGNMENT and random SAMPLING — they sound alike and are constantly confused. What does each do, and which kind of validity does each serve?",
    "answer": "RANDOM ASSIGNMENT = dividing your participants into conditions by chance; it serves INTERNAL validity (equating the groups so you can infer causation) — an experiment isn't a true experiment without it. RANDOM SAMPLING/SELECTION = drawing your participants from the population at random; it serves EXTERNAL validity (a representative sample so the results generalize). They're independent: a tightly randomized experiment on 200 undergraduates has strong assignment but weak sampling; a national survey has strong sampling but no assignment at all. Assignment is about who's in which group; sampling is about who's in the study.",
    "type": "compare",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "assignment-vs-sampling",
    "cluster": "research-designs",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-which-design-mcq-01",
    "prompt": "A researcher recruits 120 depressed adults, uses a coin-flip procedure to place each into either a new therapy or a waitlist, delivers the therapy for 12 weeks, and compares outcomes. What design is this?",
    "options": [
      "A true experiment / randomized controlled trial",
      "A quasi-experiment",
      "A correlational study",
      "A case study"
    ],
    "correct": "A true experiment / randomized controlled trial",
    "answer": "It's a TRUE EXPERIMENT (an RCT): there is a manipulation (assigning the therapy) AND random assignment (the coin flip). That combination is what supports a causal claim — 'the therapy caused the difference.' A quasi-experiment would have the intervention but NO random assignment (e.g., comparing clients who chose therapy vs. those who didn't); a correlational study would only measure variables without any intervention; a case study is a descriptive account of one person with no manipulation.",
    "type": "mcq",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "which-design-rct",
    "cluster": "research-designs",
    "bloom_level": "apply"
  },
  {
    "id": "u12-which-design-mcq-02",
    "prompt": "A researcher surveys 500 teenagers, measuring their daily screen-time and their anxiety scores as they already are, and reports that the two are positively related. No intervention is given. What design is this, and what can it support?",
    "options": [
      "A correlational study — it supports association, not causation",
      "A true experiment — it supports a causal claim",
      "A quasi-experiment — it supports a weak causal claim",
      "A single-case design — it supports causal inference in one person"
    ],
    "correct": "A correlational study — it supports association, not causation",
    "answer": "CORRELATIONAL: nothing was manipulated — both variables were measured as they naturally occur. It can establish that screen-time and anxiety COVARY, but not that one causes the other (screen-time could worsen anxiety, anxious teens could retreat to screens, or a third variable like poor sleep or isolation could drive both). Perfectly legitimate and often the only ethical option — you can't randomly assign teens to heavy screen use — but it's a lead to test, not a causal verdict.",
    "type": "mcq",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "which-design-correlational",
    "cluster": "research-designs",
    "bloom_level": "apply"
  },
  {
    "id": "u12-quasi-apply-01",
    "prompt": "An agency compares outcomes for clients at its downtown clinic (which adopted a new model) against clients at its suburban clinic (which didn't), finds the downtown clients did better, and concludes the new model works. What design is this, and what's the built-in flaw?",
    "answer": "It's a QUASI-EXPERIMENT: there's a manipulation (the new model) but NO random assignment — clients weren't randomly placed at the two clinics. The built-in flaw is a SELECTION confound: the two clinics' clients probably differed to begin with (neighborhood, income, severity, insurance, transportation), so any outcome difference could be those pre-existing differences rather than the model. Better than a pure correlational claim, but you can't attribute the result to the model with confidence — the fix would be random assignment (an RCT) or at least statistically controlling for the known differences.",
    "type": "vignette",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "quasi-selection-confound",
    "cluster": "research-designs",
    "bloom_level": "apply"
  },
  {
    "id": "u12-abab-vs-multiple-baseline-compare-01",
    "prompt": "Contrast the two workhorse single-case experimental designs — the reversal (ABAB) design and the multiple-baseline design — on how each rules out history/maturation, and say when you'd choose multiple-baseline over reversal.",
    "answer": "REVERSAL (ABAB): introduce treatment (B), WITHDRAW it (back to A), then reintroduce it (B). If the behavior improves under treatment, drifts back when it's removed, and improves again when reapplied, the treatment — not a coincidental outside event — is almost certainly the cause. MULTIPLE-BASELINE: instead of withdrawing, STAGGER treatment onset across behaviors, settings, or people; if each baseline changes ONLY when treatment reaches it, that staggered pattern rules out history/maturation just as convincingly. Choose MULTIPLE-BASELINE when reversal is inappropriate: when withdrawing treatment would be UNETHICAL (a dangerous behavior) or when the gain WON'T reverse (a learned skill stays learned) — multiple-baseline demonstrates causation without ever removing an effective treatment.",
    "type": "compare",
    "source_page": "wiki/concept-single-case-design.md",
    "topic": "reversal-vs-multiple-baseline",
    "cluster": "research-designs",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-single-case-vs-case-study-compare-01",
    "prompt": "A single-case experimental design and a case study both involve 'N = 1,' yet they sit at opposite ends of the evidence hierarchy. Distinguish them.",
    "answer": "A CASE STUDY is DESCRIPTIVE — a rich narrative account of one person with NO manipulation and NO baseline logic — so it cannot support a causal claim and sits near the BOTTOM of the evidence hierarchy (a single anecdote). A SINGLE-CASE EXPERIMENTAL DESIGN systematically MANIPULATES the intervention against a STABLE BASELINE with repeated measurement (reversal or multiple-baseline), so it CAN support causal inference and can even contribute to empirically-supported-treatment status. Same 'N = 1,' opposite evidentiary weight — the tell is the presence of a baseline + manipulation, which only the experimental design has.",
    "type": "compare",
    "source_page": "wiki/concept-single-case-design.md",
    "topic": "single-case-vs-case-study",
    "cluster": "research-designs",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-visual-inspection-apply-01",
    "prompt": "How is single-case (single-subject) data typically read — and what three features of the graph make a treatment effect convincing?",
    "answer": "It's read primarily by VISUAL INSPECTION of the graphed data, not (mainly) by inferential statistics. Three features make an effect convincing: (1) LEVEL — the average height of the outcome jumps between phases; (2) TREND — the slope changes with the phase (the line wasn't already climbing on its own); (3) LATENCY — the change follows the phase change QUICKLY (a fast, tight response is more convincing than a slow, ambiguous drift). A strong single-case result shows changes that are large, immediate, and REPEATED at each phase change. Statistical methods exist but remain supplementary to the visual analysis.",
    "type": "explain",
    "source_page": "wiki/concept-single-case-design.md",
    "topic": "visual-inspection",
    "cluster": "research-designs",
    "bloom_level": "apply"
  },
  {
    "id": "u12-designs-evaluate-01",
    "prompt": "A classmate says correlational research is 'just weak science — real researchers run experiments.' Evaluate that claim.",
    "answer": "Too dismissive. Correlational research CAN'T establish causation, that's true — but that's a limit, not a mark of inferiority. It is ESSENTIAL when manipulation is impossible or unethical: you cannot randomly assign people to trauma, poverty, abuse, or a diagnosis, so for huge swaths of the most important questions, correlational (and quasi-experimental) designs are the ONLY ethical option. It also generates the hypotheses experiments later test, and large observational datasets can be very informative. The correct posture isn't 'correlational = weak' but 'match the strength of your causal belief to the design': read a correlation as a real association worth exploring, not proof of cause. Dismissing all non-experimental work would throw out most of developmental, clinical, and epidemiological knowledge.",
    "type": "explain",
    "source_page": "wiki/concept-experimental-vs-correlational.md",
    "topic": "correlational-not-inferior",
    "cluster": "research-designs",
    "bloom_level": "evaluate"
  }
]
```

## Threats to validity (cluster: validity-threats)

```json
[
  {
    "id": "u12-four-validities-recall-01",
    "prompt": "Name Cook and Campbell's four kinds of validity and the one question each one asks of a study.",
    "answer": "(1) STATISTICAL-CONCLUSION validity — is there a REAL covariation, analyzed correctly? (2) INTERNAL validity — did the TREATMENT (not something else) cause the change? (3) CONSTRUCT validity — do the MEASURES/OPERATIONS match the constructs we name? (4) EXTERNAL validity — do the findings GENERALIZE to other people, settings, and times? A useful order when critiquing a study: internal first (is the causal claim defensible?), then construct (are they measuring what they say?), then external (who does it apply to?), with statistical-conclusion underneath it all (are the numbers trustworthy?).",
    "type": "recall",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "four-validities",
    "cluster": "validity-threats",
    "bloom_level": "remember"
  },
  {
    "id": "u12-construct-validity-cloze-01",
    "prompt": "The kind of validity that concerns whether a study's measures and operations actually match the higher-order constructs they're meant to represent — e.g., whether a 'depression' scale really taps depression rather than fatigue — is {{construct}} validity.",
    "answer": "construct. A study can have airtight internal validity (the manipulation clearly caused the change in the measure) yet poor construct validity if the measure doesn't capture the intended construct — this is where Unit 7's 'validity of a measure' meets a study's inferences.",
    "type": "cloze",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "construct-validity",
    "cluster": "validity-threats",
    "bloom_level": "remember"
  },
  {
    "id": "u12-internal-external-compare-01",
    "prompt": "Contrast internal and external validity, and explain the tradeoff that usually forces a study to favor one over the other.",
    "answer": "INTERNAL validity = confidence that the TREATMENT (not a confound) caused the change — bought by control and random assignment. EXTERNAL validity = confidence the findings GENERALIZE beyond the specific sample/setting/time — bought by representative sampling and realistic conditions. The TRADEOFF: the moves that maximize internal validity (a tightly controlled lab, standardized procedure, screened homogeneous sample) tend to COST external validity (artificial, unlike a real clinic with comorbid clients) — and vice versa (a naturalistic field study looks like practice but admits confounds). No single study optimizes both, which is a core argument for REPLICATION across contexts and for systematic reviews that pool studies: the lab shows THAT it works, the field shows it works HERE, and confidence comes from the convergence.",
    "type": "compare",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "internal-vs-external",
    "cluster": "validity-threats",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-threat-regression-apply-01",
    "prompt": "A wellness program enrolls people scoring in the most-distressed 10% on a stress scale, retests them a month later, and reports a big average drop as proof the program works. Name the threat to internal validity this most obviously ignores, and why.",
    "answer": "REGRESSION TO THE MEAN (statistical regression). People selected for EXTREME scores tend to drift back toward the average on retest — with or without any treatment — because extreme scores partly reflect momentary/measurement noise that won't recur. Since the program deliberately enrolled the most-distressed 10% (their worst), SOME improvement is expected no matter what the program does. Without a control group of equally-distressed people who got no program, you can't separate the program's effect from regression. This is a chronic clinical illusion too: clients often enter at their worst (that's when they call), so early improvement is partly regression, not necessarily your brilliance.",
    "type": "vignette",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "regression-to-the-mean",
    "cluster": "validity-threats",
    "bloom_level": "apply"
  },
  {
    "id": "u12-threat-history-mcq-01",
    "prompt": "A researcher measures community anxiety, runs a 6-month resilience program, and measures again — but a major layoff at the town's largest employer happens in month 4. Anxiety rose. Which internal-validity threat best explains why the result is uninterpretable?",
    "options": [
      "History",
      "Maturation",
      "Instrumentation",
      "Attrition"
    ],
    "correct": "History",
    "answer": "HISTORY — an outside EVENT (the layoff), not the treatment, occurred between pre- and post-test and plausibly affected the outcome. You can't tell whether the program helped, hurt, or did nothing because the layoff confounds everything. MATURATION is participants changing naturally over time (aging, healing); INSTRUMENTATION is the MEASURE changing (a revised form, a drifting rater); ATTRITION is non-random dropout. A control group exposed to the same town-wide layoff would have neutralized this — history hits both groups and cancels out.",
    "type": "mcq",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "history-threat",
    "cluster": "validity-threats",
    "bloom_level": "apply"
  },
  {
    "id": "u12-which-threat-mcq-01",
    "prompt": "In a year-long study, the same clinician rates client functioning at intake and at follow-up. Over the year she becomes more experienced and unconsciously more lenient in her ratings, so scores 'improve.' Which threat is this?",
    "options": [
      "Instrumentation",
      "Maturation",
      "History",
      "Regression to the mean"
    ],
    "correct": "Instrumentation",
    "answer": "INSTRUMENTATION — the MEASURING INSTRUMENT changed. When a human rater is the instrument and her standards drift over time, the measurement scale itself shifted between pre- and post-test, creating apparent change that isn't real client change. (Contrast: MATURATION would be the CLIENTS changing naturally; HISTORY would be an external event; REGRESSION would be extreme-scorers drifting toward the mean.) Fixes include blinding raters to time-point, using anchored/operationalized criteria, and inter-rater reliability checks.",
    "type": "mcq",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "which-threat-instrumentation",
    "cluster": "validity-threats",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-threat-attrition-explain-01",
    "prompt": "Explain how attrition (dropout) can make an ineffective treatment look effective, even with random assignment.",
    "answer": "ATTRITION (mortality) is participants DROPPING OUT — and the danger is that it's usually NON-RANDOM. If the clients who aren't improving (or are getting worse) are the ones who quit, then the people REMAINING at follow-up are a self-selected 'success' subset who no longer represent the group that started. The average of the survivors looks good not because the treatment worked but because the failures left the dataset. Even a perfectly randomized trial can be undone this way if dropout is differential. Remedies: report dropout rates, compare completers vs. dropouts, and use intention-to-treat analysis (analyze everyone as originally assigned).",
    "type": "explain",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "attrition-threat",
    "cluster": "validity-threats",
    "bloom_level": "understand"
  },
  {
    "id": "u12-control-group-explain-01",
    "prompt": "Explain why adding a control group neutralizes several internal-validity threats at once — and why 'everyone in my program improved' is nearly worthless without one.",
    "answer": "Whatever history, maturation, testing, and regression are doing to the treatment group is ALSO happening to the control group (same time period, same natural recovery, same regression from extreme intake scores). So when you compare the two, those shared influences CANCEL OUT, and the leftover difference is attributable to the treatment. That's the whole point of a control group. 'Everyone in my program got better' has no control, so you cannot separate the program from maturation (natural recovery over time), regression (they entered at their worst), history (their circumstances also changed), and testing effects — the reflex question for any such claim is 'compared to WHAT?' No comparison, no defensible causal claim.",
    "type": "explain",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "why-control-group",
    "cluster": "validity-threats",
    "bloom_level": "understand"
  },
  {
    "id": "u12-validity-two-senses-analyze-01",
    "prompt": "The word 'validity' appears in both Unit 7 (reliability & validity of a test) and Unit 12 (threats to validity). Distinguish the two senses and show how they connect.",
    "answer": "Unit 7's sense = the validity of a MEASURE: does this test measure what it claims to (for the use we're putting it to)? Unit 12's sense = the validity of a STUDY'S INFERENCES: can we trust the conclusion (four validities — statistical-conclusion, internal, construct, external)? They CONNECT at CONSTRUCT VALIDITY: a study that uses an invalid or unreliable measure has a construct-validity problem (its operations don't match the constructs) AND a statistical-conclusion-validity problem (unreliable measures weaken the analysis). So a beautifully designed experiment built on a bad measure still fails — measurement quality (Unit 7) is one of the load-bearing supports under a trustworthy study (Unit 12).",
    "type": "compare",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "two-senses-of-validity",
    "cluster": "validity-threats",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-uncontrolled-claim-evaluate-01",
    "prompt": "A colleague markets a new intervention: 'In our clinic, 80% of clients improved after the program — the evidence speaks for itself.' Evaluate the strength of this evidence.",
    "answer": "Weak as a causal claim, because it's uncontrolled. With no comparison group, an 80% improvement rate is fully compatible with the program doing NOTHING: MATURATION (many conditions improve with time), REGRESSION (clients enter at their worst and drift back toward baseline), HISTORY (life circumstances change), placebo/expectancy, and ATTRITION (if the non-improvers dropped out, the survivors inflate the rate). 'The evidence speaks for itself' is exactly the phrase to distrust — the question is 'compared to what?' To support the causal claim you'd want random assignment to the program vs. a control, a defined outcome measure, and full accounting of dropouts. The 80% figure isn't fabricated; it's just uninterpretable as proof the program caused the improvement.",
    "type": "explain",
    "source_page": "wiki/concept-validity-threats.md",
    "topic": "uncontrolled-claim",
    "cluster": "validity-threats",
    "bloom_level": "evaluate"
  }
]
```

## Effect size, significance & clinical significance (cluster: significance-and-effect)

```json
[
  {
    "id": "u12-three-questions-recall-01",
    "prompt": "Three different numbers answer three different questions about a study finding — and collapsing them is a classic error. Name the three questions and the number that answers each.",
    "answer": "(1) 'Is it real / not just noise?' -> the P-VALUE (statistical significance). (2) 'How big is it?' -> the EFFECT SIZE (e.g., Cohen's d, Pearson r). (3) 'Does it matter to this person?' -> CLINICAL (practical) SIGNIFICANCE (e.g., the reliable change index / crossing into the functional range). A result can be statistically significant, have a large effect size, and still be clinically trivial — or any combination. You'll rarely COMPUTE these; the skill is reading them and knowing which question each answers.",
    "type": "recall",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "three-numbers",
    "cluster": "significance-and-effect",
    "bloom_level": "remember"
  },
  {
    "id": "u12-pvalue-definition-cloze-01",
    "prompt": "Definition to hold exactly: a p-value is the probability of obtaining a result at least as extreme as the one observed, assuming the {{null hypothesis}} is true.",
    "answer": "null hypothesis. Crucially, it is NOT the probability that the null (or the treatment hypothesis) is true, NOT the probability the result is 'due to chance,' and NOT a measure of effect size or importance. p < .05 is an arbitrary conventional threshold, not a law of nature.",
    "type": "cloze",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "p-value-definition",
    "cluster": "significance-and-effect",
    "bloom_level": "remember"
  },
  {
    "id": "u12-effect-size-explain-01",
    "prompt": "Explain what an effect size tells you that a p-value cannot, and give the rough Cohen's d thresholds.",
    "answer": "An EFFECT SIZE quantifies the MAGNITUDE of a difference or relationship, INDEPENDENT of sample size — it answers 'how big?', which the p-value can't. The p-value depends on both the effect AND the sample size, so it conflates 'real' with 'big': a huge study can make a trivial effect 'significant.' Cohen's d (a standardized mean difference) rule-of-thumb: about 0.2 = small, 0.5 = medium, 0.8 = large (below ~0.2 is trivial); Pearson r about 0.1/0.3/0.5. Treat these as CONVENTIONS, not verdicts — what counts as 'large enough to matter' depends on the stakes and cost. Effect sizes are also what make studies comparable and are the currency of meta-analysis.",
    "type": "explain",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "effect-size-magnitude",
    "cluster": "significance-and-effect",
    "bloom_level": "understand"
  },
  {
    "id": "u12-significant-but-tiny-apply-01",
    "prompt": "A 40,000-person trial reports that a supplement lowers depression scores by an average of 0.4 points on a 27-point scale, p < .001. A rep cites the p-value as proof it's a breakthrough. What's the problem?",
    "answer": "The problem is confusing statistical significance with importance. p < .001 here mostly reflects the ENORMOUS sample size, not a meaningful effect — with 40,000 people, even a trivially small true difference becomes 'highly significant.' The EFFECT SIZE is what matters, and a 0.4-point change on a 27-point scale is almost certainly clinically negligible (well below any reliable/meaningful change threshold). So: real (not noise) but trivially small and clinically pointless. The rep is citing the number that answers 'is it noise?' as if it answered 'is it a breakthrough?' Ask for the effect size and its confidence interval, and whether the change is clinically significant for actual patients.",
    "type": "vignette",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "significant-but-trivial",
    "cluster": "significance-and-effect",
    "bloom_level": "apply"
  },
  {
    "id": "u12-stat-vs-clinical-compare-01",
    "prompt": "Contrast statistical significance and clinical significance. How can a result have one without the other, in both directions?",
    "answer": "STATISTICAL significance (p) asks whether an effect is UNLIKELY TO BE NOISE — a statement about a group/population. CLINICAL significance asks whether a change is LARGE ENOUGH TO MATTER in a real person's life — operationalized by moving from the dysfunctional to the functional range and by the reliable change index. Both directions happen: (a) statistically significant but clinically trivial — a tiny effect made 'significant' by a massive sample (the 0.4-point supplement); (b) clinically meaningful but statistically non-significant — a real, life-changing improvement in a small pilot study that lacks the power to reach p < .05. The tell: statistical significance is about populations and noise; clinical significance is about magnitude and the individual. You want both, and you never let a p-value stand in for 'it helps people.'",
    "type": "compare",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "statistical-vs-clinical",
    "cluster": "significance-and-effect",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-confidence-interval-explain-01",
    "prompt": "What does a 95% confidence interval tell you that a bare p-value doesn't, and how do you read one that 'excludes the null value'?",
    "answer": "A 95% CI gives the plausible RANGE for the true effect, conveying the estimate's PRECISION — how much uncertainty there is (a narrow interval = precise; a wide one = 'we don't really know'). It's more informative than a bare p-value because it shows the MAGNITUDE and its uncertainty, not just a yes/no. Reading it: if the interval EXCLUDES the null value (0 for a mean difference, 1 for an odds/risk ratio), the result is statistically significant at .05 — so the CI contains the p-value's information AND the effect size. A narrow CI far from the null = a strong, precise result; a wide CI straddling the null = inconclusive. Best practice reports effect size + CI + p-value together.",
    "type": "explain",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "confidence-interval",
    "cluster": "significance-and-effect",
    "bloom_level": "understand"
  },
  {
    "id": "u12-reliable-change-apply-01",
    "prompt": "A client's PHQ-9 drops from 18 to 15 over a month. The client asks, 'Am I actually getting better, or is that just noise?' What concept answers this, and what does it consider?",
    "answer": "The RELIABLE CHANGE INDEX (RCI), from Jacobson & Truax. It asks whether an individual's pre-to-post change (here 3 points) exceeds what MEASUREMENT ERROR alone would produce — computed as the change divided by the standard error of the difference for that instrument. A 3-point PHQ-9 drop may or may not exceed that threshold (roughly ~5-6 points is often cited as reliable change on the PHQ-9), so honestly: it might be within the noise band. Paired with CLINICAL significance (has the client crossed from the 'dysfunctional' into the 'functional' range?), the RCI sorts outcomes into RECOVERED / IMPROVED / UNCHANGED / DETERIORATED. This is the individual-client, measurement-based-care meaning of 'is therapy working' — the methods answer to Unit 7's repeated-screening question.",
    "type": "vignette",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "reliable-change-index",
    "cluster": "significance-and-effect",
    "bloom_level": "apply"
  },
  {
    "id": "u12-clinical-sig-categories-recall-01",
    "prompt": "Combining the reliable change index with the functional/dysfunctional range distinction sorts a client's outcome into four categories. Name them and what each means.",
    "answer": "(1) RECOVERED — made reliable change AND crossed from the dysfunctional into the functional range (the full win). (2) IMPROVED — made reliable change but still remains in the dysfunctional/clinical range (real progress, not done). (3) UNCHANGED — no reliable change (movement within the noise band). (4) DETERIORATED — reliably WORSE. This Jacobson-Truax scheme is why outcome monitoring is valuable: it flags the 'deteriorated' and 'unchanged' clients — the ones clinical intuition alone tends to miss — precisely, using the instrument's own error to define what counts as real movement.",
    "type": "recall",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "clinical-significance-categories",
    "cluster": "significance-and-effect",
    "bloom_level": "remember"
  },
  {
    "id": "u12-nomothetic-idiographic-evaluate-01",
    "prompt": "'This therapy has a large average effect in RCTs, so it will work for my client.' Evaluate the reasoning, using the nomothetic/idiographic distinction.",
    "answer": "The reasoning over-reaches. RCT effects are NOMOTHETIC — statements about GROUP AVERAGES across populations. Your client is a single, particular person (the IDIOGRAPHIC level). A large average effect is real AND leaves some proportion of clients unchanged or even worse; conversely, a treatment with a modest average can be exactly right for this individual. So the RCT raises the PRIOR probability the treatment helps — a genuinely good reason to consider it — but it doesn't guarantee it for this person, and it's one leg of evidence-based practice, not the whole decision (clinical expertise + client values complete it). This gap isn't a flaw to fix; it's the permanent condition of applying group research to a person, and it's why you MONITOR outcomes for THIS client rather than assuming the average applies. 'The number is not the person.'",
    "type": "explain",
    "source_page": "wiki/concept-effect-size.md",
    "topic": "nomothetic-idiographic",
    "cluster": "significance-and-effect",
    "bloom_level": "evaluate"
  }
]
```

## Evidence-based practice & the evidence hierarchy (cluster: evidence-hierarchy)

```json
[
  {
    "id": "u12-ebp-three-legs-cloze-01",
    "prompt": "APA's definition of evidence-based practice is the integration of the best available research evidence with clinical expertise in the context of the client's {{characteristics, culture, and preferences}}.",
    "answer": "characteristics, culture, and preferences (the client's values). The load-bearing word is INTEGRATION: EBP is a three-legged stool — best research + clinical expertise + client values — not 'research evidence overrides everything else.'",
    "type": "cloze",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "ebp-three-legs",
    "cluster": "evidence-hierarchy",
    "bloom_level": "remember"
  },
  {
    "id": "u12-pyramid-recall-01",
    "prompt": "Rank the levels of the evidence hierarchy (pyramid) from strongest to weakest, and state the tradeoff you climb through.",
    "answer": "Strongest to weakest: (1) SYSTEMATIC REVIEWS & META-ANALYSES (syntheses of all the good studies), (2) RANDOMIZED CONTROLLED TRIALS, (3) COHORT studies, (4) CASE-CONTROL studies, (5) CROSS-SECTIONAL / case series, (6) CASE REPORTS & EXPERT OPINION (weakest; a single anecdote or authority). The tradeoff: as you climb, the evidence is LESS susceptible to bias but RARER. The hierarchy ranks DESIGN, not execution — a poorly conducted meta-analysis isn't automatically better than a well-run RCT — and top designs can still have poor external validity. So 'highest on the pyramid' is the starting question, not the final word.",
    "type": "recall",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "evidence-pyramid",
    "cluster": "evidence-hierarchy",
    "bloom_level": "remember"
  },
  {
    "id": "u12-est-criteria-recall-01",
    "prompt": "State the Chambless & Hollon criteria distinguishing a 'well-established' from a 'probably efficacious' treatment.",
    "answer": "WELL-ESTABLISHED: efficacy demonstrated in at least TWO good between-group design experiments conducted by INDEPENDENT research teams (or a large series of well-controlled single-case designs), using treatment manuals and clearly specified samples. PROBABLY EFFICACIOUS: the lower tier — supported by fewer studies, or by studies that are not independent (e.g., all from one lab). The load-bearing requirements are demonstrated EFFICACY and INDEPENDENT replication — the independence requirement specifically guards against allegiance effects (a developer's own lab finding their own therapy works).",
    "type": "recall",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "est-criteria",
    "cluster": "evidence-hierarchy",
    "bloom_level": "remember"
  },
  {
    "id": "u12-ebp-vs-est-compare-01",
    "prompt": "Distinguish 'evidence-based practice (EBP)' from 'an empirically supported treatment (EST)' — they're constantly conflated.",
    "answer": "An EST is a SPECIFIC THERAPY that has been shown to work for a specific problem in controlled trials (e.g., CBT for panic disorder) — it's a research designation, one INPUT to the 'best available research' leg. EBP is the whole INTEGRATIVE PROCESS a clinician does: combining the best available research (which includes but isn't limited to ESTs) WITH clinical expertise AND this client's characteristics, culture, and values. So: an EST is a thing on a list; EBP is what you DO with the evidence, your judgment, and the person in front of you. A clinician can practice EBP while using a treatment that isn't formally an EST (if that's the best-supported fit for the client), and can FAIL to practice EBP while rigidly applying an EST the client won't accept.",
    "type": "compare",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "ebp-vs-est",
    "cluster": "evidence-hierarchy",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-which-evidence-mcq-01",
    "prompt": "You want the strongest available evidence on whether a therapy works for adult PTSD. Which source should you weight most heavily?",
    "options": [
      "A systematic review / meta-analysis of multiple RCTs",
      "A single randomized controlled trial",
      "A published case report of one dramatic recovery",
      "A respected expert's clinical opinion"
    ],
    "correct": "A systematic review / meta-analysis of multiple RCTs",
    "answer": "A SYSTEMATIC REVIEW / META-ANALYSIS of multiple RCTs sits at the TOP of the evidence hierarchy — it synthesizes all the good trials, pooling their effect sizes and averaging out the quirks of any single study. A single RCT is strong but is just one study; a case report is a single anecdote near the bottom; expert opinion is the weakest tier. Caveat to keep: the pyramid ranks DESIGN, not execution — you'd still check that the review was well-conducted (a GRADE-style appraisal) rather than trusting the label alone.",
    "type": "mcq",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "which-evidence-strongest",
    "cluster": "evidence-hierarchy",
    "bloom_level": "apply"
  },
  {
    "id": "u12-ebp-integration-vignette-01",
    "prompt": "A supervisor tells you to use exposure therapy with a client because 'it's the evidence-based treatment,' but the client is adamantly unwilling to do exposure and wants a different approach. Using the EBP definition, how do you think about this?",
    "answer": "This is exactly where 'evidence-based' is misused as a trump card. EBP is the INTEGRATION of three legs — best research + clinical expertise + CLIENT characteristics, culture, and PREFERENCES. Exposure's strong research support is real (leg 1), but a treatment the client won't engage in isn't evidence-based practice FOR THIS CLIENT — forcing it ignores leg 3 and will likely fail or rupture the alliance. The EBP-consistent move is to hold the research seriously, discuss it transparently with the client (why it's well-supported, what it involves), explore the reluctance, and either work toward willingness collaboratively or select the best-supported approach the client WILL do. 'But it's evidence-based' names one leg; practicing EBP means standing on all three.",
    "type": "vignette",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "ebp-integration-stance",
    "cluster": "evidence-hierarchy",
    "bloom_level": "apply"
  },
  {
    "id": "u12-pyramid-caveat-evaluate-01",
    "prompt": "'It's a meta-analysis, so it's the highest level of evidence — the conclusion must be right.' Evaluate.",
    "answer": "Overconfident. The pyramid ranks study DESIGN by susceptibility to bias, not the QUALITY of any particular study's execution. A meta-analysis is only as good as the studies it pools and the rigor of its methods: 'garbage in, garbage out' — if it aggregates biased, underpowered, or allegiance-driven trials (and doesn't account for publication bias), its tidy summary effect can be confidently wrong. A poorly conducted meta-analysis is NOT automatically better than a single well-run RCT. That's why appraisal systems like GRADE judge quality WITHIN a level, and why you check for heterogeneity, included-study quality, and whether unpublished null results were sought. 'Highest design tier' raises the prior; it doesn't settle the question.",
    "type": "explain",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "pyramid-design-not-execution",
    "cluster": "evidence-hierarchy",
    "bloom_level": "evaluate"
  },
  {
    "id": "u12-est-not-best-evaluate-01",
    "prompt": "'If a therapy isn't on the empirically-supported-treatment list, it's worthless.' Evaluate this claim.",
    "answer": "Wrong on two counts. First, 'empirically supported' is a FLOOR, not a ranking: it means 'this treatment has been SHOWN to work for this problem in trials,' not 'everything unlisted is worthless.' Absence from the list often reflects absence of TRIALS (understudied approaches, or ones hard to manualize), not evidence of failure. Second, the common-factors / dodo-bird finding (Unit 9) shows that once the alliance and other shared factors are accounted for, differences BETWEEN bona fide therapies are often small — so 'on the list' doesn't reliably mean 'more effective than an unlisted bona fide therapy.' The honest read: the EST list is a useful guide to what has support, held alongside the common-factors caution and the three-legged EBP definition — not a purity test that renders everything else useless.",
    "type": "explain",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "est-floor-not-ranking",
    "cluster": "evidence-hierarchy",
    "bloom_level": "evaluate"
  },
  {
    "id": "u12-allegiance-analyze-01",
    "prompt": "Across many therapy comparisons, the biggest effect sizes tend to appear in trials run by the treatment's own developer or advocates. Name this bias and explain how it should change how you read a study.",
    "answer": "ALLEGIANCE BIAS (researcher allegiance): the investigator's own commitment to a treatment systematically inflates the effects reported for it — through design choices, a weaker comparison condition, enthusiasm transmitted to therapists/clients, and selective emphasis. It's why the Chambless & Hollon 'well-established' bar requires INDEPENDENT replication, and why Unit 9 down-weighted SFBT's largest (proponent-reported) effect sizes in favor of the peer-reviewed figure. How it changes your reading: check WHO ran the trial and against WHAT comparison; weight independent replications more than developer-run studies; and treat a lone, developer-run trial with a huge effect as a hypothesis, not a settled result. Allegiance bias sits alongside publication bias as a reason the visible literature overstates effects.",
    "type": "explain",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "allegiance-bias",
    "cluster": "evidence-hierarchy",
    "bloom_level": "analyze"
  }
]
```

## Program evaluation (cluster: evaluation-types)

```json
[
  {
    "id": "u12-eval-types-recall-01",
    "prompt": "Name the main types of program evaluation, organized by WHEN in a program's life they happen and WHAT each asks.",
    "answer": "NEEDS ASSESSMENT — before you build: what's needed, and by whom? FORMATIVE — during development/early implementation: gather information to IMPROVE the program while it's still malleable. PROCESS (implementation) — was the program DELIVERED as intended, to the intended people (fidelity, dose, reach)? SUMMATIVE — at/near the end: a final judgment of the program's overall worth and outcomes. OUTCOME/IMPACT — did the targeted conditions ACTUALLY CHANGE, and can the change be attributed to the program? Two orthogonal cuts: formative (improve) vs. summative (judge); process (was it done right?) vs. outcome (did it work?).",
    "type": "recall",
    "source_page": "wiki/concept-program-evaluation.md",
    "topic": "evaluation-types",
    "cluster": "evaluation-types",
    "bloom_level": "remember"
  },
  {
    "id": "u12-formative-vs-summative-compare-01",
    "prompt": "Contrast formative and summative evaluation, including the standard mnemonic and their timing and purpose.",
    "answer": "FORMATIVE evaluation happens DURING development/early implementation and aims to IMPROVE and strengthen the program while it can still be changed. SUMMATIVE evaluation happens AT/NEAR THE END and aims to JUDGE the program's overall worth and outcomes (continue, expand, or cut?). Mnemonic: FORMATIVE = steering the ship mid-voyage; SUMMATIVE = judging the whole trip once you've arrived. Same tools, different purpose and timing: formative feeds back into revision; summative renders a verdict.",
    "type": "compare",
    "source_page": "wiki/concept-program-evaluation.md",
    "topic": "formative-vs-summative",
    "cluster": "evaluation-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-process-vs-outcome-explain-01",
    "prompt": "Explain the difference between process evaluation and outcome evaluation, and why a program can pass one but fail the other.",
    "answer": "PROCESS (implementation) evaluation asks 'was it DELIVERED as intended, to the intended people?' — attendance, fidelity, dose, reach. OUTCOME evaluation asks 'did the targeted CONDITIONS actually change?' — symptoms, retention, well-being. They come apart both ways: a program can be delivered flawlessly (passes process) yet not move outcomes (the MODEL doesn't work); or it can improve outcomes despite sloppy delivery (fails process, passes outcome). That's exactly why you look at BOTH — if outcomes are flat, process evaluation tells you whether the model failed or was simply never really delivered (so you don't wrongly discard a good model that just wasn't implemented).",
    "type": "explain",
    "source_page": "wiki/concept-program-evaluation.md",
    "topic": "process-vs-outcome",
    "cluster": "evaluation-types",
    "bloom_level": "understand"
  },
  {
    "id": "u12-which-eval-mcq-01",
    "prompt": "Three months into a new 12-month school counseling program, the counselor collects student and teacher feedback specifically to tweak and strengthen the program before it's fully rolled out. Which type of evaluation is this?",
    "options": [
      "Formative evaluation",
      "Summative evaluation",
      "Needs assessment",
      "Outcome evaluation"
    ],
    "correct": "Formative evaluation",
    "answer": "FORMATIVE — it's happening DURING implementation and its purpose is to IMPROVE/strengthen the program while it's still malleable. A SUMMATIVE evaluation would come at the end to judge overall worth; a NEEDS ASSESSMENT would come BEFORE the program to determine what's needed; an OUTCOME evaluation would measure whether targeted conditions actually changed. The tell is timing (mid-stream) + purpose (to adjust, not to render a final verdict).",
    "type": "mcq",
    "source_page": "wiki/concept-program-evaluation.md",
    "topic": "which-eval-formative",
    "cluster": "evaluation-types",
    "bloom_level": "apply"
  },
  {
    "id": "u12-needs-assessment-apply-01",
    "prompt": "Before launching a new grief-support group at a community agency, a counselor surveys local clients and referral sources about what's most needed and who would use it. Name this activity and say what it prevents.",
    "answer": "This is a NEEDS ASSESSMENT — done BEFORE building a program to determine what's actually needed and by whom (it's a kind of formative activity at the front end). It prevents SOLVING THE WRONG PROBLEM: launching a service nobody needs, at a time nobody can attend, or aimed at the wrong population — a common and expensive failure. It also grounds the program's later goals and outcome measures in real, documented need, which is what a funder or a CACREP-style accountability process expects.",
    "type": "vignette",
    "source_page": "wiki/concept-program-evaluation.md",
    "topic": "needs-assessment",
    "cluster": "evaluation-types",
    "bloom_level": "apply"
  },
  {
    "id": "u12-eval-vs-research-analyze-01",
    "prompt": "Program evaluation and research use the same methods toolkit. What distinguishes them in AIM, and what practical consequence does that have (including for IRB review)?",
    "answer": "The difference is PURPOSE. RESEARCH aims for GENERALIZABLE knowledge — findings meant to apply beyond the sample, published for the field. PROGRAM EVALUATION aims for a JUDGMENT of a SPECIFIC program's merit/worth for LOCAL decision-making (continue/fund/fix it?). Consequences: evaluation is driven by stakeholders' questions and bounded to one program; internal quality-improvement evaluation often does NOT require IRB review the way research does — BUT the moment findings are intended to be PUBLISHED as generalizable knowledge, it becomes research and IRB review re-enters. Either way the ethics of consent and confidentiality still apply. So the same data-gathering can be evaluation or research depending on the intent to generalize.",
    "type": "explain",
    "source_page": "wiki/concept-program-evaluation.md",
    "topic": "evaluation-vs-research",
    "cluster": "evaluation-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-accountability-loop-explain-01",
    "prompt": "Program evaluation is described as a loop rather than a one-time report. Describe the loop and connect it to two things already built earlier in the curriculum.",
    "answer": "The accountability loop: ASSESS NEEDS -> set measurable GOALS -> DELIVER the program -> MEASURE process and outcomes -> FEED the results BACK into revising the program -> repeat. It's the program-level echo of two earlier loops: (1) Unit 7's GOLDEN THREAD (assessment -> goal -> intervention -> review) in treatment planning, and (2) the individual-client MEASUREMENT-BASED CARE loop (repeated PHQ-9/GAD-7 used to adjust treatment) from single-case/progress monitoring. Same logic — set a target, measure toward it, revise — scaled from one client up to a whole service. And the same caution carries: 'measurable' is not 'meaningful,' so pick outcome measures that capture the change you actually care about.",
    "type": "explain",
    "source_page": "wiki/concept-program-evaluation.md",
    "topic": "accountability-loop",
    "cluster": "evaluation-types",
    "bloom_level": "understand"
  }
]
```

## Research ethics & the IRB (cluster: research-ethics)

```json
[
  {
    "id": "u12-belmont-three-recall-01",
    "prompt": "Name the three principles of the Belmont Report and the concrete application each one maps onto.",
    "answer": "(1) RESPECT FOR PERSONS — treat people as autonomous agents and give extra protection to those with diminished autonomy -> application: INFORMED CONSENT (voluntary, informed, right to decline/withdraw). (2) BENEFICENCE — maximize benefits and minimize harms -> application: RISK/BENEFIT ASSESSMENT. (3) JUSTICE — distribute the burdens and benefits of research fairly -> application: FAIR SUBJECT SELECTION (don't load risks onto the vulnerable/convenient or reserve benefits for the privileged). IRBs enforce all three before a study begins.",
    "type": "recall",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "belmont-principles",
    "cluster": "research-ethics",
    "bloom_level": "remember"
  },
  {
    "id": "u12-respect-persons-cloze-01",
    "prompt": "In the Belmont Report, the principle of respect for persons — recognizing autonomy and protecting those with diminished autonomy — is applied primarily through the requirement of {{informed consent}}.",
    "answer": "informed consent. Voluntary, informed agreement with the right to decline or withdraw. It's the same conviction under Unit 3's clinical informed consent, extended to the research participant — consent is the floor, not a formality.",
    "type": "cloze",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "respect-persons-consent",
    "cluster": "research-ethics",
    "bloom_level": "remember"
  },
  {
    "id": "u12-beneficence-vs-justice-compare-01",
    "prompt": "Contrast the Belmont principles of beneficence and justice — they're easy to blur.",
    "answer": "BENEFICENCE is about the BALANCE OF HARMS AND BENEFITS in the study itself: maximize benefits, minimize harms ('do no harm' plus actively protect) — its application is the RISK/BENEFIT assessment (are the risks justified by the potential benefits?). JUSTICE is about the FAIR DISTRIBUTION of those risks and benefits ACROSS people: who bears the burden, and who gets the benefit? — its application is FAIR SUBJECT SELECTION (don't exploit the poor, captive, or convenient for research whose benefits flow to others). Shorthand: beneficence asks 'is this study worth its risks?'; justice asks 'is it FAIR who's carrying those risks and reaping the rewards?' Tuskegee violated justice most flagrantly.",
    "type": "compare",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "beneficence-vs-justice",
    "cluster": "research-ethics",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-belmont-apply-mcq-01",
    "prompt": "A researcher recruits only residents of a low-income shelter for a risky, uncomfortable study — because they're easy to access and unlikely to say no — while the eventual benefits would go to the general public. Which Belmont principle is most directly violated?",
    "options": [
      "Justice",
      "Respect for persons",
      "Beneficence",
      "Statistical-conclusion validity"
    ],
    "correct": "Justice",
    "answer": "JUSTICE — the FAIR DISTRIBUTION of research burdens and benefits. Loading the risks onto a vulnerable, convenient population while the benefits flow to others is precisely the injustice Belmont's fair-subject-selection application forbids (it's the core wrong of Tuskegee). Respect for persons would be at issue if consent were absent/coerced (plausibly also true here), and beneficence if the risk/benefit ratio were bad — but the DEFINING violation described (exploiting the vulnerable BECAUSE they're vulnerable) is justice. (Statistical-conclusion validity is a research-design concept, not an ethics principle — a distractor.)",
    "type": "mcq",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "which-principle-justice",
    "cluster": "research-ethics",
    "bloom_level": "apply"
  },
  {
    "id": "u12-tuskegee-explain-01",
    "prompt": "Briefly explain the Tuskegee Syphilis Study, which Belmont principles it violated, and what it produced in U.S. research regulation.",
    "answer": "From 1932-1972 the U.S. Public Health Service followed hundreds of Black men with syphilis, DECEIVED them about their condition, and WITHHELD penicillin even after it became the standard cure — in order to study the untreated disease. It violated RESPECT FOR PERSONS (deception, no real informed consent), BENEFICENCE (deliberate, grave harm; withholding an available cure), and JUSTICE (a vulnerable, exploited population bore the entire burden for knowledge benefiting others). Its exposure was the American scandal that forced reform: the National Research Act (1974), the commission that wrote the BELMONT REPORT (1978), and the IRB / Common Rule system requiring prospective ethics review, informed consent, and protection of vulnerable populations.",
    "type": "explain",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "tuskegee",
    "cluster": "research-ethics",
    "bloom_level": "understand"
  },
  {
    "id": "u12-irb-explain-01",
    "prompt": "What is an Institutional Review Board (IRB), and what does 'prospective review' mean and why does it matter?",
    "answer": "An IRB is the committee that, under the Common Rule (45 CFR 46), REVIEWS AND APPROVES research involving human subjects BEFORE it begins, checking it against the Belmont principles: adequate informed consent, a defensible risk/benefit ratio, protections for vulnerable populations, and privacy/confidentiality safeguards. 'PROSPECTIVE review' means the approval must happen BEFORE data collection — not after. It matters because you cannot retroactively make an unethical study ethical: if participants were harmed or deceived, an after-the-fact sign-off can't undo it. The IRB is the structural guarantee (like clinical informed consent and confidentiality protections) that the power imbalance between researcher and participant won't be exploited.",
    "type": "explain",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "irb-prospective-review",
    "cluster": "research-ethics",
    "bloom_level": "understand"
  },
  {
    "id": "u12-section-g-dualrole-vignette-01",
    "prompt": "A counselor-educator wants to run a study and plans to recruit participants from the graduate students she teaches and supervises. What does ACA Section G specifically require here, and why?",
    "answer": "Section G flags this as a DUAL-ROLE / boundary problem in research. When participants are also STUDENTS, SUPERVISEES, or CLIENTS, the researcher must make clear that the decision to participate (or not) will NOT affect their academic standing, supervisory relationship, or care — and their consent must be genuinely FREE. Why: the POWER DIFFERENTIAL makes 'voluntary' consent suspect — a student may fear that declining will hurt their grade or recommendation, which is coercion by circumstance. This is the research version of Unit 3's dual-relationship rule; safeguards include using someone else to recruit/collect consent, de-identifying participation from the instructor, and emphasizing the right to decline without penalty.",
    "type": "vignette",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "section-g-dual-role",
    "cluster": "research-ethics",
    "bloom_level": "apply"
  },
  {
    "id": "u12-consent-throughline-evaluate-01",
    "prompt": "A student argues that research ethics (IRB, Belmont, Section G) is really just bureaucratic paperwork that slows down important science. Evaluate this, using the through-line that connects research ethics to clinical ethics.",
    "answer": "The 'paperwork' framing misreads the history and the stakes. Every protection exists because of real, catastrophic abuses (Nazi experiments -> Nuremberg Code; Tuskegee -> Belmont/IRB), and each is, at bottom, an answer to a CONSENT FAILURE: vulnerable people used without genuine, informed, voluntary agreement. Research ethics is CLINICAL ETHICS one step removed — the same duty of care (honesty, consent, confidentiality, non-exploitation) you owe a client, owed to the person who agrees to be STUDIED. Yes, review adds friction; that friction is the point — it's the structural guarantee that the researcher's power and enthusiasm won't override the participant's dignity. 'Important science' is exactly the rationalization every abuse used. The mature position: streamline where you can, but treat informed, revocable consent as the non-negotiable floor, not a formality.",
    "type": "explain",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "consent-as-floor",
    "cluster": "research-ethics",
    "bloom_level": "evaluate"
  }
]
```

## Throughline — EBP stance, replication, and progress monitoring (unclustered)

```json
[
  {
    "id": "u12-replication-crisis-explain-01",
    "prompt": "Explain the 'replication crisis' in psychology — the landmark finding and the main practices that produced it.",
    "answer": "The replication crisis is the discovery that a large share of published psychology findings don't hold up when re-run. The landmark: the 2015 Open Science Collaboration re-ran 100 studies from top journals — about 97% of the ORIGINALS were 'significant,' but only ~36% of the REPLICATIONS reached significance, and effect sizes roughly HALVED. Main drivers: PUBLICATION BIAS (journals prefer positive/novel results, so nulls and failed replications go in the file drawer, making the literature look stronger than it is); P-HACKING / researcher degrees of freedom (flexing analytic choices — when to stop collecting, which covariates, which outcomes — until p < .05); HARKing (presenting a post-hoc finding as the original hypothesis); and ALLEGIANCE bias. The response is open science: preregistration, registered reports, larger samples, open data, and valuing replication and null results.",
    "type": "explain",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "replication-crisis",
    "cluster": "",
    "bloom_level": "understand"
  },
  {
    "id": "u12-phacking-cloze-01",
    "prompt": "Flexibly trying different analyses, samples, or outcome variables until a result crosses p < .05 — exploiting 'researcher degrees of freedom' to manufacture significance — is called {{p-hacking}}.",
    "answer": "p-hacking. Simmons, Nelson & Simonsohn showed these ordinary, often-unconscious choices can push the false-positive rate far above the nominal 5%. Preregistration (committing to hypotheses and analyses before seeing the data) is the main defense.",
    "type": "cloze",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "p-hacking",
    "cluster": "",
    "bloom_level": "remember"
  },
  {
    "id": "u12-replication-evaluate-01",
    "prompt": "A headline reads 'New study proves music therapy rewires the anxious brain.' Given the replication crisis, what's the calibrated way to react — avoiding both credulity and cynicism?",
    "answer": "Hold it as a provisional lead, not a proven fact — and not as proof the field is worthless either. Calibrated questions: Is it ONE study or a replicated body? What DESIGN (RCT? correlational dressed up as causal — 'proves' and 'rewires' are red flags)? How BIG is the effect, and is it clinically meaningful? Was it PREREGISTERED, and who funded/ran it (allegiance)? A single splashy, un-replicated study earns interest, not belief; a replicated, preregistered effect with a meaningful effect size earns real confidence. The replication crisis teaches CALIBRATION, not blanket dismissal: resist 'new study proves…' credulity AND 'it's all garbage' cynicism. Being a discerning consumer of the field's competing claims — the whole point of this unit — is exactly this middle posture.",
    "type": "explain",
    "source_page": "wiki/concept-evidence-based-practice.md",
    "topic": "calibrated-skepticism",
    "cluster": "",
    "bloom_level": "evaluate"
  },
  {
    "id": "u12-publication-bias-analyze-01",
    "prompt": "Connect a research-ethics duty (ACA Section G's honest reporting) to a threat to the evidence base (publication bias). How are they the same problem from two angles?",
    "answer": "PUBLICATION BIAS (the file-drawer problem) is that positive, novel results get published while null results and failed replications don't — so the VISIBLE literature overstates how well things work, distorting meta-analyses and the whole evidence base. ACA Section G's honest-reporting duties — don't fabricate, don't bury unfavorable results, report accurately, correct errors — are the ETHICS side of the same coin: burying a null result is simultaneously a research-integrity VIOLATION and a contribution to publication bias. So 'report your unfavorable findings' is both an ethical obligation to the field and a corrective to a systematic distortion of evidence. Reforms like preregistration and registered reports enforce the ethic structurally (publication is guaranteed regardless of outcome, removing the incentive to hide nulls).",
    "type": "explain",
    "source_page": "wiki/concept-irb-research-ethics.md",
    "topic": "publication-bias-ethics",
    "cluster": "",
    "bloom_level": "analyze"
  },
  {
    "id": "u12-mbc-not-on-track-apply-01",
    "prompt": "A counselor 'feels' a client is doing fine, but the routinely-administered outcome measure shows the client's scores have quietly worsened over six weeks. What does measurement-based care add here, and how does this fit the unit's stance that 'the number is not the person'?",
    "answer": "Measurement-based care (MBC) adds the thing clinical intuition most reliably MISSES: the quietly DETERIORATING or NOT-ON-TRACK client. Feedback-informed treatment improves outcomes precisely by flagging these cases so the clinician can change course before it's too late — a warm alliance can mask a lack of progress, and the data catches it. This is NOT a contradiction of 'the number is not the person'; it's the same value from the other side. Reducing the person TO a score would be the error; using a repeated score to make sure you're not comfortably missing someone's decline is measurement IN SERVICE OF the relationship. The reliable change index tells you whether the worsening is real (beyond error) rather than noise, so you respond to signal, not static.",
    "type": "vignette",
    "source_page": "wiki/concept-single-case-design.md",
    "topic": "mbc-catches-decline",
    "cluster": "",
    "bloom_level": "apply"
  },
  {
    "id": "u12-progress-monitoring-cloze-01",
    "prompt": "Stripped to its clinical core, a single-case design becomes routine {{progress monitoring}} — usually a simple AB design (repeated measurement of one client, no reversal or staggering), good enough to guide this client's care but not to prove the therapy caused the change.",
    "answer": "progress monitoring. Formalized as measurement-based care, it uses brief repeated outcome measures (PHQ-9/GAD-7) to adjust treatment — the individual-client, practice-level application of outcome measurement and the reliable-change idea.",
    "type": "cloze",
    "source_page": "wiki/concept-single-case-design.md",
    "topic": "progress-monitoring",
    "cluster": "",
    "bloom_level": "remember"
  },
  {
    "id": "u12-unit-capstone-evaluate-01",
    "prompt": "Summarize the single most important stance this research unit asks a counselor to hold, and why both worshipping and dismissing 'the evidence' are failures of it.",
    "answer": "The stance: 'the number is not the person' — research literacy is a tool FOR good clinical judgment, not a replacement for it, and the two opposite failures are equally bad. WORSHIPPING the evidence (treating 'the manual says' or a p-value as a trump card) ignores that findings are group averages generated under study conditions, that EBP is a three-legged integration (research + expertise + client values), and that some published findings don't even replicate. DISMISSING the evidence ('it's all biased/it's all garbage') throws away the genuine, hard-won signal that strong designs and replicated effects provide, and abandons the client to whatever's confidently marketed. The mature posture is CALIBRATION: match your confidence to the strength of the design and the replication, integrate it with your judgment and the person's values, and monitor whether it's actually helping THIS client. Discernment, not credulity or cynicism.",
    "type": "explain",
    "source_page": "wiki/unit12-research.md",
    "topic": "capstone-stance",
    "cluster": "",
    "bloom_level": "evaluate"
  }
]
```
