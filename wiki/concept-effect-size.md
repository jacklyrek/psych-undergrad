---
title: Effect Size, Statistical Significance & Clinical Significance
type: concept
tags: [effect-size, cohens-d, p-value, statistical-significance, clinical-significance, confidence-interval, reliable-change]
unit: 12
source_units: [12]
cluster: significance-and-effect
---

# Effect Size, Statistical Significance & Clinical Significance

Three different numbers get collapsed into one vague idea — "the study found something" — and keeping them apart is the most transferable statistical skill a counselor can have. A study can be **statistically significant** (unlikely to be a fluke), have a **large effect size** (the difference is big), and still be **clinically insignificant** (it doesn't help a real person enough to matter) — or any combination of those. Three questions, three numbers:

- **Is it real / not just noise?** → the **p-value** (statistical significance).
- **How big is it?** → the **effect size**.
- **Does it matter to this person?** → **clinical (practical) significance**.

You will almost never compute these. You need to **read** them and know which question each answers [S7][S8].

## The p-value: what it is, and the misreadings to unlearn

A **p-value** is the probability of getting a result **at least as extreme as the one observed, *if the null hypothesis were true*** [S8]. By convention, **p < .05** is called "statistically significant" — but .05 is an arbitrary line, not a law of nature.

The misinterpretations are so common the American Statistical Association issued a formal statement to correct them [S9]. A p-value is **not**:

- **the probability that the null hypothesis is true** (or that the finding is "due to chance"),
- **the probability that the hypothesis/treatment is correct** (p < .05 does **not** mean "95% chance it works"),
- **a measure of how big or important the effect is.**

That last point is the one that bites clinically. Because the p-value depends on **both** the effect size **and** the sample size, a **huge study can make a trivial effect "significant."** A weight-loss drug that produces an average loss of half a pound will be wildly "significant" in a 50,000-person trial and still be clinically pointless. "Statistically significant" answers *whether*, never *how much* [S7][S9].

## Effect size: the "how big" number

**Effect size** quantifies the **magnitude** of a difference or relationship, **independent of sample size** — which is exactly what the p-value can't do. The two you'll see most [S7]:

- **Cohen's *d*** — a standardized **mean difference** (how far apart two group means are, in standard-deviation units). Rule-of-thumb: **≈0.2 small, 0.5 medium, 0.8 large** (below ~0.2 is trivial).
- **Pearson *r*** — the strength of a **correlation**, from −1 to +1; ≈0.1/0.3/0.5 small/medium/large. (*r*² is the proportion of variance shared.)

Treat the thresholds as **conventions, not verdicts** — Cohen himself warned against them, and what counts as "large" depends on the field and the stakes (a *d* of 0.2 for a cheap, safe, population-wide intervention can matter more than a *d* of 0.8 for an expensive, risky one). Effect sizes are also what make studies **comparable** and are the currency of **meta-analysis** ([[concept-evidence-based-practice]]). This is the number behind claims you've already met: psychotherapy's alliance–outcome correlation (*r* ≈ .28, Unit 1), antidepressants' modest average benefit (*d* ≈ 0.3, Unit 11), and the down-weighted SFBT effect sizes (Unit 9).

## Confidence intervals: precision, not just a verdict

A **95% confidence interval** gives the plausible **range** for the true effect, capturing the estimate's **precision** [S8]. It's more informative than a bare p-value for two reasons: it shows **how big** the effect might be (its width = how much uncertainty), and if the interval **excludes the null value** (0 for a difference, 1 for an odds ratio), the result is "significant" at .05 anyway — so the CI contains the p-value's information **and** the magnitude. A narrow CI far from zero is a strong, precise result; a wide CI straddling zero is "we don't really know." Best practice is to report **effect size + CI + p-value** together, because no one of them tells the whole story [S8][S9].

## Clinical (practical) significance: does it matter to a person?

Statistical significance is about **populations**; a clinician treats a **person**. **Clinical significance** asks whether a change is **large enough to matter in real life** — and psychotherapy research has a precise tool for it. Jacobson and Truax defined **clinically significant change** as moving from a score typical of the **dysfunctional** population to one typical of the **functional** population, paired with the **Reliable Change Index (RCI)** — the change divided by the standard error of the difference, which asks whether an individual moved **more than measurement error alone** would produce [S10].

Combine the two and every client sorts into one of four outcomes: **recovered** (reliable change **and** crossed into the functional range), **improved** (reliable change but still in the clinical range), **unchanged** (no reliable change), or **deteriorated** (reliably worse). This is the statistical backbone of **measurement-based care** and outcome monitoring — the individual-client meaning of "did therapy work," and the direct methods-level answer to Unit 7's [[concept-screening-tools | repeated PHQ-9]] question ("their score dropped 3 points — is that real, or noise?"). It lives on [[concept-single-case-design]] as a practice.

## The stance: the nomothetic–idiographic gap

Hold the whole page together with one idea. All of this machinery is **nomothetic** — about group averages and populations. Your work is **idiographic** — about one particular person. A large average treatment effect is real *and* leaves some clients unchanged or worse; a non-significant group finding doesn't mean it can't help **this** individual. That gap is not a flaw to be fixed; it's the permanent condition of applying research to a person, and it's why "the number is not the person" is the unit's stance. Effect sizes and significance **inform** the clinical decision; they don't **make** it.

## Connects to

- [[concept-evidence-based-practice]] — effect sizes are the currency of meta-analysis and the evidence hierarchy; "significant but tiny" is a core appraisal skill.
- [[concept-single-case-design]] — reliable change and clinical significance are how you read **one client's** outcome data.
- [[concept-validity-threats]] — statistical-conclusion validity is the home of p-values, power, and over-reliance on .05.
- [[concept-screening-tools]] and [[concept-treatment-planning]] (Unit 7) — the repeated-measure the RCI interprets; measurement-based care in practice.
- [[concept-psychotropic-classes]] (Unit 11) — antidepressants' "real but modest" (*d* ≈ 0.3) effect is this page's distinction in action.

## Sources

[S7] Cohen (1988) + Sullivan & Feinn (2012), *Using Effect Size*, JGME. [S8] p-value / confidence-interval education (PMC5133225; Andrade 2019). [S9] Wasserstein & Lazar (2016), the ASA statement on p-values. [S10] Jacobson & Truax (1991), clinical significance and the Reliable Change Index. Full notes in [`../research/unit12-research-sources.md`](../research/unit12-research-sources.md).
