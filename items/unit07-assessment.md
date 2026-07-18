# Unit 7 items — Assessment, Diagnosis & Case Conceptualization

Source of truth for Unit 7 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This unit's signature reps: the **confusable-pair
discriminations** the MSE and psychometrics are built on (clusters `mse-domains`,
`reliability-vs-validity`), the **screen-is-not-a-diagnosis** stance woven through the screening and
statistics items (cluster `screening-tools`), the **Five Ps** formulation scaffold and its
diagnosis-vs-formulation spine (cluster `formulation-ps`), and the syllabus practice rep (**a
one-page case conceptualization of a novel/show character**). Item ids use the `u7-` prefix. See
generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## The intake / clinical interview

```json
[
  {
    "id": "u7-intake-areas-recall-01",
    "prompt": "Sommers-Flanagan collapses the intake into three core areas. Name them and one thing each covers.",
    "answer": "(1) The PRESENTING PROBLEM — what brings them in, in their own words, and its story. (2) The BIOPSYCHOSOCIAL HISTORY — the context the problem grew in (biological, psychological, social). (3) CURRENT FUNCTIONING — how they're doing right now, including the mental status exam and a risk screen.",
    "type": "recall",
    "source_page": "wiki/concept-intake-interview.md",
    "topic": "intake-structure",
    "bloom_level": "remember"
  },
  {
    "id": "u7-intake-structure-compare-01",
    "prompt": "Interview structure runs on a dial from unstructured to structured. Name what each end maximizes and what it costs, and say where most skilled clinical intakes actually sit.",
    "answer": "UNSTRUCTURED (follow the client, few fixed questions): maximizes rapport and richness; costs coverage (you can miss a whole domain) and reliability (two clinicians get different pictures). STRUCTURED (fixed script): maximizes coverage and reliability; costs the alliance (can feel like an interrogation and starve rapport). SEMI-STRUCTURED: a mental checklist of domains you WILL cover, asked conversationally in whatever order the client's story opens them — structure in your head, not on the page. Most skilled intakes live here.",
    "type": "compare",
    "source_page": "wiki/concept-intake-interview.md",
    "topic": "interview-structure",
    "bloom_level": "analyze"
  },
  {
    "id": "u7-intake-whynow-cloze-01",
    "prompt": "In the intake, asking 'why now — what changed that made today the day they called?' is your first read on the {{precipitating}} factor of the case formulation.",
    "answer": "precipitating",
    "type": "cloze",
    "source_page": "wiki/concept-intake-interview.md",
    "topic": "why-now",
    "bloom_level": "understand"
  },
  {
    "id": "u7-intake-bps-cloze-01",
    "prompt": "The intake history is organized by the {{biopsychosocial}} model — biological, psychological, and social domains — so you don't tunnel on symptoms; DSM-5 dropped the multiaxial scaffold that used to force this context, so it's now a habit you supply.",
    "answer": "biopsychosocial",
    "type": "cloze",
    "source_page": "wiki/concept-intake-interview.md",
    "topic": "biopsychosocial-history",
    "bloom_level": "remember"
  },
  {
    "id": "u7-intake-drift-evaluate-01",
    "prompt": "A trainee runs an intake as rapid-fire closed questions and comes out with a full form and no relationship. Name the stance trap, why it's self-defeating as ASSESSMENT (not just as rapport), and the corrective.",
    "answer": "INTERROGATION DRIFT. Self-defeating because the interview IS an assessment method and its data quality depends on the relationship: a client who feels processed, judged, or rushed hands you a thinner, more defended history — so the closed-question barrage that feels efficient actually degrades the data it collects. Corrective: lead with open questions and reflections, hold the domain checklist in your head, and let the history come THROUGH the alliance. Rapport and information-gathering are not a trade-off.",
    "type": "explain",
    "source_page": "wiki/concept-intake-interview.md",
    "topic": "intake-stance",
    "bloom_level": "evaluate"
  },
  {
    "id": "u7-intake-alldata-vignette-01",
    "prompt": "A new client mentions 'something that happened' and then goes quiet. You feel a strong pull to get the whole trauma story now, to 'assess properly.' What does the completeness reflex actually serve, what do you actually need at intake, and what's the move?",
    "answer": "The 'I need all the data' reflex serves the COUNSELOR'S anxiety, not the client. You do NOT need the trauma narrative to screen, to assess safety, or to start — and pushing for it before trust and stability exist is a classic way helpers re-traumatize. What you actually need: whether something happened that still intrudes on their life, current symptoms and safety, and the client's pace. The move: screen plainly ('Has something happened that still affects you?'), accept the answer, and let the story come if and when the client chooses.",
    "type": "vignette",
    "source_page": "wiki/concept-intake-interview.md",
    "topic": "intake-stance",
    "bloom_level": "evaluate"
  }
]
```

## The mental status examination (cluster: mse-domains)

```json
[
  {
    "id": "u7-mse-def-recall-01",
    "prompt": "The MSE is often called 'the psychiatric physical exam.' State what it is in one sentence and name the two things it is NOT.",
    "answer": "It is a structured, cross-sectional description of the client's CURRENT mental state, written in shared vocabulary so another clinician sees roughly what you saw. It is NOT a diagnosis (it describes present state and only SUPPORTS a diagnosis when combined with history and collateral data) and it is NOT objective (a subjective assessment that varies between clinicians).",
    "type": "recall",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "mse-definition",
    "cluster": "mse-domains",
    "bloom_level": "understand"
  },
  {
    "id": "u7-mse-moodaffect-compare-01",
    "prompt": "Distinguish MOOD from AFFECT in the MSE — including who reports each, and the axes affect is described on.",
    "answer": "MOOD is the client's SUBJECTIVE, self-reported emotional state, documented in their own words ('I feel empty') — the climate they report over time. AFFECT is the clinician's OBSERVED emotional expression — the weather you see right now — described by quality (euthymic, dysphoric, euphoric, anxious), range (full, constricted, blunted, flat), stability (labile = rapidly shifting), and congruence with mood and content. Mood = what they tell you; affect = what you see.",
    "type": "compare",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "mood-vs-affect",
    "cluster": "mse-domains",
    "bloom_level": "analyze"
  },
  {
    "id": "u7-mse-incongruent-mcq-01",
    "prompt": "A client says 'honestly, I'm doing great' while tearful, trembling, and avoiding eye contact. How is this best documented, and why does it matter?",
    "options": [
      "Incongruent affect — the mismatch between reported mood and observed expression is itself diagnostic",
      "Labile affect — the client's emotion is shifting rapidly moment to moment",
      "Flat affect — a near-absence of emotional expression",
      "Dysphoric mood — the client reports feeling down"
    ],
    "correct": "Incongruent affect — the mismatch between reported mood and observed expression is itself diagnostic",
    "answer": "Stated mood ('great') clashes with observed affect (tearful, trembling) = INCONGRUENT affect, and that gap is often more informative than either alone. Not labile (that's rapid SHIFTING, not a mood-affect mismatch); not flat (expression is present, not reduced); 'dysphoric mood' misreads it as the client's self-report when the tell is the clinician's OBSERVATION contradicting that report.",
    "type": "mcq",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "mood-vs-affect",
    "cluster": "mse-domains",
    "bloom_level": "apply"
  },
  {
    "id": "u7-mse-processcontent-compare-01",
    "prompt": "Thought PROCESS and thought CONTENT dissociate completely. Define each, give two examples of each, and state the dissociation.",
    "answer": "PROCESS = the FORM/organization of thinking (how ideas connect): circumstantial (over-detailed but returns to the point), tangential (wanders off and never returns), flight of ideas (rapid, loosely connected — mania), loose associations (no logical link — psychosis), perseveration, thought blocking. CONTENT = WHAT is thought about (the subject): delusions, obsessions, phobias, and — always assessed — suicidal/homicidal ideation. Dissociation: you can have a perfectly organized PROCESS delivering floridly delusional CONTENT, and vice versa — describe them separately.",
    "type": "compare",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "process-vs-content",
    "cluster": "mse-domains",
    "bloom_level": "analyze"
  },
  {
    "id": "u7-mse-process-mcq-01",
    "prompt": "A client answers every question with a long, detail-stuffed reply that — after several detours — eventually arrives at the point. Which thought-PROCESS term fits?",
    "options": [
      "Circumstantial — over-inclusive but eventually reaches the goal",
      "Tangential — wanders off and never returns to the point",
      "Flight of ideas — rapid, loosely connected jumps between topics",
      "Loose associations — no logical link between successive ideas"
    ],
    "correct": "Circumstantial — over-inclusive but eventually reaches the goal",
    "answer": "Eventually REACHING the point after detours = circumstantial. Tangential never gets there; flight of ideas is rapid, pressured jumping (mania); loose associations have no logical connection at all (psychosis). The hinge is whether the train arrives at the station.",
    "type": "mcq",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "process-vs-content",
    "cluster": "mse-domains",
    "bloom_level": "apply"
  },
  {
    "id": "u7-mse-insightjudgment-explain-01",
    "prompt": "Insight and judgment are both rated in the MSE, and beginners collapse them. Define each and give a concrete case where they DISSOCIATE.",
    "answer": "INSIGHT = the client's understanding that they have a condition and grasp of its nature (rated poor/limited/fair/good). JUDGMENT = the capacity to make sound, safe decisions and anticipate consequences. Dissociation: a client with POOR insight ('I'm not ill') can still show FAIR judgment — takes the medication anyway to avoid another hospitalization; conversely, someone with GOOD insight can repeatedly make dangerous choices. Understanding the illness and deciding well about it are separate capacities.",
    "type": "explain",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "insight-vs-judgment",
    "cluster": "mse-domains",
    "bloom_level": "understand"
  },
  {
    "id": "u7-mse-insightjudgment-mcq-01",
    "prompt": "A client with schizophrenia says: 'I don't really buy that I'm sick — but the last hospital stay was awful, so I take the injection every month like they ask.' How are insight and judgment best rated?",
    "options": [
      "Poor insight, fair judgment — denies illness but makes a sound safety decision",
      "Good insight, poor judgment — accepts illness but chooses badly",
      "Poor insight, poor judgment — impaired on both",
      "Good insight, good judgment — intact on both"
    ],
    "correct": "Poor insight, fair judgment — denies illness but makes a sound safety decision",
    "answer": "He denies having an illness (POOR insight) yet chooses the action that keeps him safe and out of hospital (FAIR judgment). This is the classic insight/judgment dissociation — rating them as a single 'impaired' or 'intact' score erases the very information the two-way split exists to capture.",
    "type": "mcq",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "insight-vs-judgment",
    "cluster": "mse-domains",
    "bloom_level": "analyze"
  },
  {
    "id": "u7-mse-describe-evaluate-01",
    "prompt": "A trainee's MSE note reads, in full: 'Client was depressed and paranoid.' Critique it against the MSE's core discipline, then give an observation-level rewrite.",
    "answer": "It INTERPRETS instead of DESCRIBING — 'depressed' and 'paranoid' are conclusions, not observations, and they smuggle a diagnosis into a note whose job is to record what was seen and heard. The discipline is describe, not interpret: an MSE FEEDS a diagnosis but does not equal one. Rewrite: 'Tearful, spoke slowly with long response latencies, reported feeling empty (mood); constricted, dysphoric affect. Expressed a fixed belief that neighbors are monitoring her (thought content), not shifted by contrary evidence.' Now the reader can evaluate the inference instead of inheriting it.",
    "type": "explain",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "describe-not-interpret",
    "cluster": "mse-domains",
    "bloom_level": "evaluate"
  },
  {
    "id": "u7-mse-orientation-cloze-01",
    "prompt": "In the MSE cognition screen, acute disorientation to person, place, or time should raise suspicion of {{delirium}} or intoxication — an easily-missed medical emergency, not a primary psychiatric illness.",
    "answer": "delirium",
    "type": "cloze",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "cognition-orientation",
    "cluster": "mse-domains",
    "bloom_level": "remember"
  },
  {
    "id": "u7-mse-affect-cloze-01",
    "prompt": "Affect that shifts rapidly from moment to moment is termed {{labile}} (pointing toward mania or intoxication), while a near-absence of emotional expression is termed flat (pointing toward psychosis or severe depression).",
    "answer": "labile",
    "type": "cloze",
    "source_page": "wiki/concept-mental-status-exam.md",
    "topic": "affect-terms",
    "cluster": "mse-domains",
    "bloom_level": "remember"
  }
]
```

## Screening & outcome-monitoring tools (cluster: screening-tools)

```json
[
  {
    "id": "u7-phq9-recall-01",
    "prompt": "Give the PHQ-9's mechanics: number of items and what each maps to, score range, the four severity cut-points with their labels, and its internal-consistency reliability.",
    "answer": "9 items, one for EACH of the nine DSM major-depression symptoms (so it doubles as a criteria refresher), each scored 0-3 over the last two weeks → total 0-27. Severity anchors 5 / 10 / 15 / 20 = mild / moderate / moderately severe / severe (0-4 minimal). At the ≥10 cut-point, sensitivity and specificity for major depression are both ~88%. Internal consistency: Cronbach's α ≈ 0.86-0.89.",
    "type": "recall",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "phq-9",
    "cluster": "screening-tools",
    "bloom_level": "remember"
  },
  {
    "id": "u7-gad7-cloze-01",
    "prompt": "The GAD-7 has 7 items scored 0-3 over the last two weeks (total 0-{{21}}), with cut-points 5 / 10 / 15 marking mild / moderate / severe anxiety.",
    "answer": "21",
    "type": "cloze",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "gad-7",
    "cluster": "screening-tools",
    "bloom_level": "remember"
  },
  {
    "id": "u7-phq9-item9-apply-01",
    "prompt": "A client's PHQ-9 comes back at 11 (moderate), with a '1 — several days' on item 9 ('thoughts that you would be better off dead, or of hurting yourself'). What does the item-9 answer specifically obligate, and what must you NOT do?",
    "answer": "ANY non-zero answer on item 9 obligates a direct, in-person suicide-risk follow-up THIS session — you ask plainly about thoughts, plan, intent, and means (full protocol in Unit 8). What you must NOT do: let the self-report scale stand in for the conversation, or be reassured that it's 'only a 1' — the item is a trip-wire that triggers assessment, not a measure of risk severity. (The total of 11 is a separate severity flag; item 9 is handled on its own regardless of the total.)",
    "type": "vignette",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "suicide-screen",
    "cluster": "screening-tools",
    "bloom_level": "apply"
  },
  {
    "id": "u7-screen-notdx-evaluate-01",
    "prompt": "A busy colleague writes 'PHQ-9 = 17, so MDD' in a chart. Give the two-part reason this is wrong — one about what a screen IS, one about the statistics behind the cut-point.",
    "answer": "(1) A screen names a DOMAIN of distress and grades SEVERITY; it does not make a diagnosis — the diagnosis is made by the clinical interview and the DSM criteria (a 17 can't tell grief from depression, or a bad week from an episode). (2) The cut-points are deliberately set for HIGH SENSITIVITY (miss few cases), which guarantees false positives by design — so a positive screen is a flag to assess further, not a verdict. Diagnosing from the number does exactly what the instrument is built to prevent.",
    "type": "explain",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "screen-not-diagnosis",
    "cluster": "screening-tools",
    "bloom_level": "evaluate"
  },
  {
    "id": "u7-gad7-which-mcq-01",
    "prompt": "A client scores 16 on the GAD-7 (severe range). What is the correct NEXT step, and why not simply diagnose GAD?",
    "options": [
      "Interview to find out WHICH anxiety-related condition it is — the GAD-7 also screens positive for panic, social anxiety, and PTSD",
      "Diagnose generalized anxiety disorder — a severe GAD-7 is diagnostic",
      "Re-administer the GAD-7 in two weeks before doing anything else",
      "Diagnose panic disorder — a severe anxiety score implies panic attacks"
    ],
    "correct": "Interview to find out WHICH anxiety-related condition it is — the GAD-7 also screens positive for panic, social anxiety, and PTSD",
    "answer": "Though built for GAD, the GAD-7 screens positive for panic disorder (~74%), social anxiety disorder (~72%), and PTSD (~66%) — a high score names a broad DOMAIN of distress, not a specific disorder. The next step is the clinical interview to identify WHICH anxiety-related condition, not writing 'GAD' from a number.",
    "type": "mcq",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "gad-7",
    "cluster": "screening-tools",
    "bloom_level": "apply"
  },
  {
    "id": "u7-phq9-gad7-compare-01",
    "prompt": "Compare the PHQ-9 and GAD-7 on: what each screens, number of items, score range, and standard cut-point. Then state the one caution both share.",
    "answer": "PHQ-9: DEPRESSION, 9 items, range 0-27, standard flag ≥10 (mild/mod/mod-severe/severe at 5/10/15/20). GAD-7: ANXIETY (generalized, and more broadly), 7 items, range 0-21, standard flag ≥10 (mild/mod/severe at 5/10/15). Shared caution: both are SCREENS tuned for high sensitivity — a positive result flags a domain and grades severity but is not a diagnosis; the clinical interview decides.",
    "type": "compare",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "phq9-vs-gad7",
    "cluster": "screening-tools",
    "bloom_level": "understand"
  },
  {
    "id": "u7-mbc-understand-01",
    "prompt": "Explain measurement-based care (MBC) and the single mechanism that makes it improve outcomes.",
    "answer": "MBC = routinely re-administering a validated symptom scale (PHQ-9, GAD-7, etc.) at EACH visit and feeding the score back into treatment decisions — not a one-time intake flag but continuous tracking. The mechanism: it detects NON-RESPONSE and DETERIORATION earlier than unaided clinical impression (clinicians relying on judgment alone routinely fail to notice a client worsening), and the benefit is largest precisely for the patients who would otherwise quietly fail to improve.",
    "type": "explain",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "measurement-based-care",
    "cluster": "screening-tools",
    "bloom_level": "understand"
  },
  {
    "id": "u7-phq2-cloze-01",
    "prompt": "The ultra-brief pre-screen made of the PHQ-9's first two items (depressed mood + anhedonia) is the {{PHQ-2}}; a positive result on it prompts administering the full PHQ-9.",
    "answer": "PHQ-2",
    "type": "cloze",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "pre-screen",
    "cluster": "screening-tools",
    "bloom_level": "remember"
  },
  {
    "id": "u7-cutpoint-vignette-01",
    "prompt": "You read that the PHQ-9/GAD-7 flag is '≥10,' but a psychometric study of a heterogeneous psychiatric sample reports ≥8 as the optimal GAD-7 cut. A colleague says one of the studies must be wrong. What's the actual resolution?",
    "answer": "Neither is wrong — cut-points are POPULATION-DEPENDENT, not universal constants. The optimal threshold trades sensitivity against specificity and shifts with the base rate and severity mix of the population being screened, so a psychiatric sample can have a different optimal cut (≥8) than a primary-care one (≥10). Treat a cut-score as a CALIBRATED FLAG for a given setting, not a threshold of truth — which is also part of why you never diagnose from the number alone.",
    "type": "vignette",
    "source_page": "wiki/concept-screening-tools.md",
    "topic": "cut-points",
    "cluster": "screening-tools",
    "bloom_level": "analyze"
  }
]
```

## Reliability, validity & screening statistics (cluster: reliability-vs-validity)

```json
[
  {
    "id": "u7-relval-def-recall-01",
    "prompt": "Define reliability and validity as they apply to a test, and state the subtle point about what validity attaches to.",
    "answer": "RELIABILITY = the stability/consistency of scores (does the measurement repeat?). VALIDITY = the degree to which evidence and theory support the INTERPRETATIONS of test scores FOR PROPOSED USES (does it measure what we think, for this purpose?). The subtlety: validity attaches to the INTERPRETATION AND USE, not to the test itself — the same test can be valid for one purpose and invalid for another.",
    "type": "recall",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "reliability-validity-definitions",
    "cluster": "reliability-vs-validity",
    "bloom_level": "remember"
  },
  {
    "id": "u7-rel-types-recall-01",
    "prompt": "Name the four kinds of reliability, each by 'what could vary,' and which statistic standardly indexes internal consistency.",
    "answer": "TEST-RETEST (across time — same test, same person, two time points). INTERNAL CONSISTENCY (across items — do they hang together?), indexed by split-half or, standardly, CRONBACH'S α. INTER-RATER (across scorers — do two clinicians agree?). PARALLEL/ALTERNATE-FORMS (across two versions of the test).",
    "type": "recall",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "reliability-types",
    "cluster": "reliability-vs-validity",
    "bloom_level": "remember"
  },
  {
    "id": "u7-relval-dartboard-compare-01",
    "prompt": "Use the dartboard image to contrast a reliable-but-invalid measure with a valid one, and give an everyday example of reliable-but-invalid.",
    "answer": "RELIABLE BUT INVALID = a tight cluster of darts in the WRONG corner: consistent, consistently wrong. VALID = the darts cluster ON the bullseye — which requires that they cluster at all (reliable) AND land in the right place. Everyday example of reliable-but-invalid: a bathroom scale that reads 10 lb heavy every single time — perfectly consistent, consistently incorrect. Consistency is not correctness.",
    "type": "compare",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "reliable-not-valid",
    "cluster": "reliability-vs-validity",
    "bloom_level": "understand"
  },
  {
    "id": "u7-relval-necessary-explain-01",
    "prompt": "'Reliability is necessary but not sufficient for validity.' Unpack both halves — why necessary, why not sufficient.",
    "answer": "NECESSARY: an unreliable measure is just noise, and noise can't be valid — you cannot be valid without first being reliable (a test can't correctly measure a construct if it can't even measure consistently). NOT SUFFICIENT: a rock-solid reliable measure can still measure the WRONG construct entirely (the bathroom scale 10 lb off) — consistency guarantees repeatability, not correctness. So reliability is the floor validity stands on, not validity itself.",
    "type": "explain",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "reliability-necessary-not-sufficient",
    "cluster": "reliability-vs-validity",
    "bloom_level": "understand"
  },
  {
    "id": "u7-validity-types-mcq-01",
    "prompt": "Researchers show that PHQ-9 scores taken today correlate strongly with the result of a full structured diagnostic interview conducted the SAME day. Which kind of validity evidence is that?",
    "options": [
      "Concurrent (criterion) validity — correlation with a benchmark measured at the same time",
      "Predictive (criterion) validity — correlation with a future outcome",
      "Content validity — the items cover the whole construct",
      "Construct validity — the test fits the broader theoretical network"
    ],
    "correct": "Concurrent (criterion) validity — correlation with a benchmark measured at the same time",
    "answer": "Correlating with an external criterion (the structured interview) measured NOW = CONCURRENT criterion validity. Predictive would correlate with a FUTURE outcome (e.g., a risk scale predicting later attempts); content is about whether items cover the whole construct; construct is about fitting the broader theoretical network (convergent/discriminant). The 'same day' benchmark is the concurrent tell.",
    "type": "mcq",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "validity-types",
    "cluster": "reliability-vs-validity",
    "bloom_level": "apply"
  },
  {
    "id": "u7-snsp-recall-01",
    "prompt": "Define sensitivity and specificity, and give the two mnemonics (SnNout / SpPin) for what a negative or positive result on each lets you do.",
    "answer": "SENSITIVITY = of everyone who HAS the condition, the fraction the test catches (true positives). A highly SENSITIVE test, when NEGATIVE, helps RULE OUT — SnNout. SPECIFICITY = of everyone who does NOT have it, the fraction the test correctly clears (true negatives). A highly SPECIFIC test, when POSITIVE, helps RULE IN — SpPin. The two trade off: pushing a cut-point to catch more cases raises sensitivity and lowers specificity.",
    "type": "recall",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "sensitivity-specificity",
    "cluster": "reliability-vs-validity",
    "bloom_level": "remember"
  },
  {
    "id": "u7-screen-highsens-mcq-01",
    "prompt": "Screening instruments like the PHQ-9 are deliberately built with cut-points that favor high SENSITIVITY over high specificity. What is the design rationale?",
    "options": [
      "Missing a true case is worse than a false positive, so it's better to over-flag and assess further",
      "High sensitivity makes the test cheaper and faster to administer",
      "It lets the screen be used to diagnose without a follow-up interview",
      "It eliminates false positives, so every flag is guaranteed to be a true case"
    ],
    "correct": "Missing a true case is worse than a false positive, so it's better to over-flag and assess further",
    "answer": "For a screen, a miss (a genuinely depressed or suicidal client cleared as fine) is worse than a false alarm (a well client sent for a closer look). Tuning for high sensitivity accepts more false positives to catch nearly all true cases — which is exactly WHY a positive screen is a flag to assess, not a diagnosis. It doesn't make the test cheaper, doesn't license diagnosing without an interview, and does NOT eliminate false positives (it increases them).",
    "type": "mcq",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "screens-high-sensitivity",
    "cluster": "reliability-vs-validity",
    "bloom_level": "understand"
  },
  {
    "id": "u7-ppv-prevalence-analyze-01",
    "prompt": "The same suicide-screening instrument, with identical sensitivity and specificity, is used in a general primary-care clinic and in an emergency psychiatric unit. Why will its positive predictive value (PPV) differ, and in which setting is a positive result more likely to be a true case?",
    "answer": "PPV depends on PREVALENCE (sensitivity and specificity do not). In the low-prevalence primary-care clinic, most people don't have the condition, so a larger share of the test's positives are FALSE alarms → lower PPV. In the high-prevalence psychiatric unit, positives are more often TRUE cases → higher PPV. So a positive result carries more weight in the psychiatric unit — the same number means different things depending on the base rate, which is why a positive screen must always be read against the population it came from.",
    "type": "explain",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "ppv-prevalence",
    "cluster": "reliability-vs-validity",
    "bloom_level": "analyze"
  },
  {
    "id": "u7-norms-evaluate-01",
    "prompt": "A perfectly reliable, well-validated depression inventory — normed on U.S. college students — is used to score a recently immigrated older adult with limited English. Assess what can go wrong even though the instrument's psychometrics are excellent.",
    "answer": "Psychometric quality does NOT license use. 'A score in the clinical range' means 'clinical relative to THESE norms' — apply the instrument outside its representative normative sample and the INTERPRETATION can be invalid even though the test is impeccable. Add measurement bias from language, literacy, culture-bound item content, and motive-to-present, and the number may misfire. Trustworthy assessment requires standardized administration + representative norms + fairness across groups, not just good reliability and validity coefficients — this is cultural humility in numeric form (Unit 4).",
    "type": "explain",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "standardization-norms",
    "cluster": "reliability-vs-validity",
    "bloom_level": "evaluate"
  },
  {
    "id": "u7-alpha-cloze-01",
    "prompt": "Internal consistency is standardly indexed by Cronbach's α (0-1); the usual acceptable floor is about {{0.70}}, with ~0.80+ considered good — the PHQ-9's α of ≈0.86 sits comfortably above it.",
    "answer": "0.70",
    "type": "cloze",
    "source_page": "wiki/concept-reliability-validity.md",
    "topic": "cronbach-alpha",
    "cluster": "reliability-vs-validity",
    "bloom_level": "remember"
  }
]
```

## Case conceptualization — the Five Ps (cluster: formulation-ps)

```json
[
  {
    "id": "u7-dx-formulation-compare-01",
    "prompt": "Contrast DIAGNOSIS with CASE CONCEPTUALIZATION on: the question each answers, whether it is categorical or idiographic, and what each produces.",
    "answer": "DIAGNOSIS answers WHAT is it — a CATEGORICAL, shared label from DSM criteria — and produces a CODE (for communication, billing, research). CASE CONCEPTUALIZATION answers HOW did it come to be and what maintains it — an IDIOGRAPHIC, this-person causal story from history + theory + the client's meaning — and produces a PLAN. The diagnosis is an INPUT to the formulation, not a substitute: two clients with the identical label can need opposite treatments.",
    "type": "compare",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "diagnosis-vs-formulation",
    "cluster": "formulation-ps",
    "bloom_level": "analyze"
  },
  {
    "id": "u7-fiveps-recall-01",
    "prompt": "Name the Five Ps of case conceptualization and give the memory hook (the gun metaphor) for the four causal ones.",
    "answer": "PRESENTING problem (the concern, in the client's words); PREDISPOSING factors (standing vulnerabilities that loaded the gun before anything happened — genetics, early adversity, attachment); PRECIPITATING factors (the proximal trigger that pulled it — the loss, conflict, med change; 'why now'); PERPETUATING factors (what keeps it going now — avoidance, reassurance-seeking, sleep loss, reinforcing patterns); PROTECTIVE factors (strengths and buffers — supports, insight, a reason for living). Hook: predisposing = loaded gun, precipitating = trigger pulled, perpetuating = finger that won't come off, protective = safety catch.",
    "type": "recall",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "five-ps",
    "cluster": "formulation-ps",
    "bloom_level": "remember"
  },
  {
    "id": "u7-perpetuating-understand-01",
    "prompt": "Of the Five Ps, which is called the 'load-bearing' one, and why does it — rather than the others — carry that weight?",
    "answer": "PERPETUATING factors. They're load-bearing because they're what your interventions actually TARGET: you can't change a past predisposition or undo a precipitant that already happened, but you CAN interrupt what maintains the problem NOW (avoidance, reassurance-seeking, substance use, hopeless beliefs, sleep loss). The perpetuating analysis is the step that turns a formulation into a workable treatment — skip it and you're treating a category, not a person.",
    "type": "explain",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "perpetuating-factors",
    "cluster": "formulation-ps",
    "bloom_level": "understand"
  },
  {
    "id": "u7-classifyp-mcq-01",
    "prompt": "A client develops depression after a sudden layoff. Her mother had severe recurrent depression, and she was bullied throughout adolescence. In the Five Ps, the LAYOFF is best classified as which factor?",
    "options": [
      "Precipitating — the proximal trigger of the current episode",
      "Predisposing — a standing vulnerability that raised baseline risk",
      "Perpetuating — what maintains the problem now",
      "Protective — a strength or buffer against the problem"
    ],
    "correct": "Precipitating — the proximal trigger of the current episode",
    "answer": "The layoff is the PROXIMAL TRIGGER that pulled the current episode — a precipitating factor ('why now'). The mother's depression (genetic loading) and the adolescent bullying (early adversity) are PREDISPOSING — standing vulnerabilities present before the episode. The distinction is timing and role: predisposing loads the gun; precipitating pulls the trigger.",
    "type": "mcq",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "classify-the-p",
    "cluster": "formulation-ps",
    "bloom_level": "apply"
  },
  {
    "id": "u7-classifyp-mcq-02",
    "prompt": "The same depressed client has, since the layoff, stopped seeing friends, stays in bed most of the day, and drinks nightly to fall asleep. In the Five Ps, these ongoing behaviors are best classified as which factor — and why do they matter most for treatment?",
    "options": [
      "Perpetuating — they maintain the problem now and are what interventions target",
      "Precipitating — they triggered the current episode",
      "Predisposing — they are long-standing background vulnerabilities",
      "Protective — they buffer the client against the problem"
    ],
    "correct": "Perpetuating — they maintain the problem now and are what interventions target",
    "answer": "Withdrawal, inactivity, and nightly drinking are PERPETUATING — they keep the depression going now, often independent of the layoff that started it. They matter most for treatment because they're the load-bearing P: the one set of factors you can actually change in the present (behavioral activation, sleep/alcohol work), whereas the precipitant is already past and the predisposition can't be undone.",
    "type": "mcq",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "classify-the-p",
    "cluster": "formulation-ps",
    "bloom_level": "apply"
  },
  {
    "id": "u7-sameps-evaluate-01",
    "prompt": "Two counselors — one CBT, one family-systems — build the SAME Five-Ps formulation of the same client but propose different treatments. Is one of them wrong? Explain what actually determines the plan.",
    "answer": "Neither is necessarily wrong. The Five Ps are deliberately THEORY-NEUTRAL — but the counselor is not: your orientation (Unit 2) decides WHICH perpetuating factors you foreground and what counts as changing them. The CBT counselor locates the maintaining factors in thoughts and behaviors (avoidance, distortions) and plans to test/change them; the family-systems counselor locates them in the RELATIONAL structure and plans to shift the system. Same client, same Ps, different plan — because conceptualization IS theory applied. The lens determines the plan, and both can be defensible if each traces honestly from the formulation.",
    "type": "explain",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "theory-chooses-plan",
    "cluster": "formulation-ps",
    "bloom_level": "evaluate"
  },
  {
    "id": "u7-formulation-rep-01",
    "prompt": "PRACTICE REP (syllabus): Pick a character from a novel or show you know well. Out loud, give a one-page case conceptualization: (1) the presenting problem in their words, (2) relevant history, (3) what MAINTAINS the problem now, and (4) two measurable goals. Then check it against the model.",
    "answer": "Model shape (generic example): (1) PRESENTING PROBLEM in their words — 'I keep blowing up the relationships I care about and I don't know why.' (2) HISTORY — early loss or instability, attachment disruptions, prior episodes, substance use, and strengths. (3) WHAT MAINTAINS IT (the load-bearing step) — e.g., a push-pull pattern where testing loved ones provokes the very rejection he fears, confirming the belief and repeating the cycle; plus poor sleep and isolation. (4) TWO MEASURABLE GOALS, written SMART — e.g., 'reduce conflict incidents from ~5/week to ≤1/week, logged, within 8 weeks' and 'initiate and complete one repair conversation per week for 4 weeks.' Self-check: did you EXPLAIN (not just describe), name a maintaining MECHANISM, and make the goals measurable and time-bound?",
    "type": "recall",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "formulation-practice-rep",
    "cluster": "formulation-ps",
    "bloom_level": "apply"
  },
  {
    "id": "u7-formulate-with-vignette-01",
    "prompt": "You've built what feels like an airtight formulation of your client. What does 'formulate WITH the client, not ABOUT them' require you to do with it, and what's the risk of keeping it to yourself?",
    "answer": "Share it, tentatively, and check its fit: 'Here's how I'm making sense of what's happening — does this match your experience?' Sharing a formulation is itself therapeutic and collaborative, and the client's correction is data that improves it. A formulation is a testable HYPOTHESIS, not a verdict — held loosely and revised as the work reveals more. The risk of keeping it to yourself: an 'airtight' formulation the client never sees or disagrees with is the fix-it reflex in a lab coat — you end up treating your model of the person instead of the person.",
    "type": "vignette",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "formulation-stance",
    "cluster": "formulation-ps",
    "bloom_level": "apply"
  },
  {
    "id": "u7-4ps-bps-cloze-01",
    "prompt": "Formulation gets sharper when each of the 4 Ps is asked across the three domains of the {{biopsychosocial}} model — e.g., predisposing-biological = genetics/temperament, perpetuating-psychological = maladaptive coping, protective-social = supportive relationships.",
    "answer": "biopsychosocial",
    "type": "cloze",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "four-ps-bps-grid",
    "cluster": "formulation-ps",
    "bloom_level": "remember"
  },
  {
    "id": "u7-idiographic-recall-01",
    "prompt": "Case conceptualization is described as 'idiographic.' What does idiographic mean here, and how does it contrast with the diagnostic label it complements?",
    "answer": "IDIOGRAPHIC = specific to THIS individual — a person-particular causal story of what's wrong, how it got that way, what maintains it, and what to do. It contrasts with the diagnosis, which is categorical/nomothetic — a shared label that applies the same way to everyone who meets criteria. The label sorts the person into a category; the idiographic formulation explains this person. You need both, but only the second points to a treatment.",
    "type": "recall",
    "source_page": "wiki/concept-case-conceptualization.md",
    "topic": "idiographic-formulation",
    "cluster": "formulation-ps",
    "bloom_level": "understand"
  }
]
```

## Treatment planning & measurable goals

```json
[
  {
    "id": "u7-goldenthread-recall-01",
    "prompt": "Write out the 'golden thread' chain in order, and state the test you should be able to run on any single progress note.",
    "answer": "assessment/diagnosis → goal → measurable objective → interventions → progress notes → review. The test: pull ANY session note and trace it BACKWARD — which objective was this working on? which goal does that objective serve? which diagnosis and impairment make that goal medically necessary? A note that can't be traced back (or a diagnosis with no matching goal) is a broken thread: an audit failure, and a sign the work has lost its aim.",
    "type": "recall",
    "source_page": "wiki/concept-treatment-planning.md",
    "topic": "golden-thread",
    "bloom_level": "remember"
  },
  {
    "id": "u7-goalobjective-compare-01",
    "prompt": "Distinguish a GOAL from an OBJECTIVE in a treatment plan, and give the most common beginner error that breaks the distinction.",
    "answer": "A GOAL is the BROAD clinical outcome the client is working toward ('reduce depressive symptoms to the mild range,' 'rebuild a supportive network') — directional, often not directly measurable on its own. An OBJECTIVE is a SMALL, MEASURABLE, TIME-BOUND step toward the goal ('reduce PHQ-9 from 18 to below 10 in 12 weeks,' 'initiate one social contact per week for four weeks'). One goal usually has several objectives. Beginner error: swapping the levels — a 'goal' of 'attend three sessions' (a task, not an outcome) or an 'objective' of 'feel better' (not measurable) — which breaks the golden thread.",
    "type": "compare",
    "source_page": "wiki/concept-treatment-planning.md",
    "topic": "goal-vs-objective",
    "bloom_level": "understand"
  },
  {
    "id": "u7-smart-mcq-01",
    "prompt": "Which of the following is written as a proper SMART treatment OBJECTIVE?",
    "options": [
      "Within 8 weeks, client will reduce GAD-7 from 15 to ≤9 and use a paced-breathing skill in ≥3 anxiety-provoking situations per week, tracked on a log",
      "Client will manage their anxiety better over the course of treatment",
      "Client will feel less overwhelmed by work and family stress",
      "Client will work on their anxiety in weekly sessions"
    ],
    "correct": "Within 8 weeks, client will reduce GAD-7 from 15 to ≤9 and use a paced-breathing skill in ≥3 anxiety-provoking situations per week, tracked on a log",
    "answer": "Only the first is Specific (named behaviors/target), Measurable (a GAD-7 criterion plus a counted behavior), Achievable, Relevant, and Time-bound (8 weeks). 'Manage anxiety better' and 'feel less overwhelmed' are mood words with no measurable criterion or deadline; 'work on it in weekly sessions' names attendance, not a measurable change. The validated score is exactly where the screens earn their keep in a plan.",
    "type": "mcq",
    "source_page": "wiki/concept-treatment-planning.md",
    "topic": "smart-objectives",
    "bloom_level": "apply"
  },
  {
    "id": "u7-smart-cloze-01",
    "prompt": "In the clinical adaptation of the SMART objective format the letters stand for Specific, Measurable, Achievable, {{Relevant}}, and Time-bound — a format (borrowed from management, Doran 1981) for writing objectives, not a therapy in itself.",
    "answer": "Relevant",
    "type": "cloze",
    "source_page": "wiki/concept-treatment-planning.md",
    "topic": "smart-objectives",
    "bloom_level": "remember"
  },
  {
    "id": "u7-measurable-evaluate-01",
    "prompt": "A supervisor insists every goal on a treatment plan be reducible to a scale score. A client's most important aim is 'to stop feeling so alone.' Evaluate the supervisor's rule and say what you'd actually do.",
    "answer": "The rule is half-right and half-dangerous. RIGHT: SMART objectives and measurement-based care genuinely catch non-response the eye misses and keep the plan accountable. DANGEROUS: a plan built ONLY from what a scale can score shrinks a person to a trend line and quietly imports the medical model's billing incentives — and some of the most important goals (feeling less alone, forgiving oneself) resist clean measurement. What I'd do: name the meaningful goal anyway, then find the nearest HONEST proxy (frequency of initiated social contact; a loneliness scale as one imperfect indicator) rather than dropping the goal because it won't fit a form. Measure to serve the work, not the reverse.",
    "type": "explain",
    "source_page": "wiki/concept-treatment-planning.md",
    "topic": "measurable-vs-meaningful",
    "bloom_level": "evaluate"
  },
  {
    "id": "u7-mbc-loop-understand-01",
    "prompt": "A client's objective was 'PHQ-9 from 18 to <10 in 12 weeks.' At the 12-week review it's still 16. In a measurement-based-care model, what does 'not met' trigger, and why is a fixed review date part of the design?",
    "answer": "'Not met' triggers a REVISION — a different intervention, a stepped-up level of care, a referral — rather than more of what isn't working. The whole point of measurement-based care is to catch non-response and deterioration EARLIER than clinical impression would, so the plan can change course. The review date is built in so that 'not met' is a SIGNAL, not a surprise: without a deadline, a stalled plan just quietly continues. The plan is a living document, re-measured and revised as the formulation evolves.",
    "type": "explain",
    "source_page": "wiki/concept-treatment-planning.md",
    "topic": "mbc-revision-loop",
    "bloom_level": "understand"
  }
]
```
