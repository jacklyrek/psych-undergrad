# Unit 6 items — Psychopathology & the DSM-5-TR

Source of truth for Unit 6 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This unit's signature reps: **cross-category
differential vignettes** (cluster `differential-vignettes` — the big interleaving target the
course-map flags), per-category discrimination clusters (`mood-disorders`, `anxiety-disorders`,
`trauma-disorders`, `psychotic-spectrum`, `personality-disorders`, `eating-disorders`), the
syllabus practice rep (**explain MDD / GAD / PTSD to a layperson in two minutes**), and stance
probes on **diagnosis-as-shorthand / over-pathologizing / person-first language**. See generate
rules in [`../CLAUDE.md`](../CLAUDE.md).

## The manual: structure, history, culture, and what diagnosis is for

```json
[
  {
    "id": "u6-dsmtr-recall-01",
    "prompt": "Name the headline changes the DSM-5-TR (2022) made beyond revising text, and say why two of them preview Unit 8's territory.",
    "answer": "Added PROLONGED GRIEF DISORDER (yearning/preoccupation with the deceased, 12+ months, impairing); added free-standing SYMPTOM CODES FOR SUICIDAL BEHAVIOR AND NONSUICIDAL SELF-INJURY (recordable with or without any diagnosis); unspecified mood disorder; criteria/specifier changes to 70+ disorders; terminology updates with a full ethnoracial-equity review. The suicide/self-injury codes matter for Unit 8: risk can now be documented directly, independent of diagnosis.",
    "type": "recall",
    "source_page": "wiki/concept-dsm-structure.md",
    "topic": "dsm-5-tr-changes",
    "bloom_level": "remember"
  },
  {
    "id": "u6-multiaxial-recall-01",
    "prompt": "DSM-IV diagnoses came on five axes. Name the five, and what DSM-5 replaced the system with.",
    "answer": "I clinical disorders; II personality disorders + intellectual disability; III relevant medical conditions; IV psychosocial/environmental stressors; V Global Assessment of Functioning (GAF, 0-100). DSM-5 dropped all five for NONAXIAL documentation (one list, ordered by clinical priority), with WHODAS 2.0 optionally replacing the GAF (which had poor psychometrics) and expanded V/Z codes carrying Axis IV's psychosocial context.",
    "type": "recall",
    "source_page": "wiki/concept-dsm-structure.md",
    "topic": "multiaxial-system",
    "bloom_level": "remember"
  },
  {
    "id": "u6-disorder-def-explain-01",
    "prompt": "Nearly every DSM criteria set ends with a distress-or-impairment clause. Explain what the clause does, and why beginners who skip it over-diagnose.",
    "answer": "It requires that symptoms cause clinically significant distress or functional impairment before they count as disorder. It is the line between having experiences (occasional voice, double-checking the stove, weeks of sadness after loss) and having a disorder. Skipping it turns symptom checklists into diagnoses — the over-pathologizing error. When impairment is absent, the diagnosis usually is too.",
    "type": "explain",
    "source_page": "wiki/unit06-psychopathology.md",
    "topic": "definition-of-disorder",
    "bloom_level": "understand"
  },
  {
    "id": "u6-culture-dx-mcq-01",
    "prompt": "A recently arrived client from a country with pervasive state surveillance says he is careful about what he says on the phone and suspects some neighbors report on others. Before reading this as paranoid ideation, what does the DSM itself direct you to do?",
    "options": [
      "Run a cultural formulation (e.g., the CFI): the same behavior can be normative and rational in his context",
      "Document paranoid personality traits provisionally and monitor",
      "Screen for schizophrenia spectrum disorders, since suspicion is a Criterion A symptom",
      "Reassure him that surveillance is not a concern in this country"
    ],
    "correct": "Run a cultural formulation (e.g., the CFI): the same behavior can be normative and rational in his context",
    "answer": "Behavior aberrant in one culture can be standard (or adaptive) in another — apparent paranoia can be a rational learning from state surveillance. The DSM's Cultural Formulation Interview and cultural-concepts framework exist precisely so criteria aren't applied context-blind. This is Unit 4's competence doing diagnostic work.",
    "type": "mcq",
    "source_page": "wiki/concept-dsm-structure.md",
    "topic": "culture-and-diagnosis",
    "bloom_level": "apply"
  },
  {
    "id": "u6-culture-terms-cloze-01",
    "prompt": "DSM-5 retired the term 'culture-bound syndrome' for three concepts: cultural {{syndromes}} (recognized symptom clusters like ataque de nervios), cultural idioms of distress (shared ways of talking about suffering), and cultural explanations (causal models, e.g., susto as soul loss).",
    "answer": "syndromes",
    "type": "cloze",
    "source_page": "wiki/concept-dsm-structure.md",
    "topic": "culture-and-diagnosis",
    "bloom_level": "remember"
  },
  {
    "id": "u6-insurance-evaluate-01",
    "prompt": "In U.S. practice, reimbursement generally requires a covered diagnosis code. Name two distinct ways this structural fact can distort diagnosis, and the counselor's ethical anchor against it.",
    "answer": "(1) Pressure to diagnose at all — clients with real but subthreshold problems get upgraded to a billable label; (2) pressure toward COVERED diagnoses — choosing the reimbursable code over the accurate one (e.g., MDD instead of a V/Z-code relational problem). Anchor: the record must reflect clinical reality, not billing convenience — accuracy is an honesty/integrity obligation (Unit 3), and the diagnosis follows the client permanently.",
    "type": "explain",
    "source_page": "wiki/concept-dsm-structure.md",
    "topic": "diagnosis-and-insurance",
    "bloom_level": "evaluate"
  },
  {
    "id": "u6-personfirst-explain-01",
    "prompt": "Why does professional convention insist on 'a person with schizophrenia' rather than 'a schizophrenic' — what is the argument beyond politeness?",
    "answer": "Labels that fuse person and disorder objectify — they promote biased, disparaging assumptions and make the diagnosis the person's identity. A disorder is something a person HAS, not what they ARE. The wording also does clinical work: it keeps the counselor seeing a person with a condition (and a context, strengths, a culture) instead of a category walking in.",
    "type": "explain",
    "source_page": "wiki/unit06-psychopathology.md",
    "topic": "person-first-language",
    "bloom_level": "understand"
  }
]
```

## Mood disorders — depressive & bipolar

```json
[
  {
    "id": "u6-mdd-rep-01",
    "prompt": "PRACTICE REP (syllabus): Explain major depressive disorder to a layperson in two minutes — what it is, what it is not, and what would make a clinician think of it. Say it out loud, then compare.",
    "answer": "Model: 'Depression, the disorder, is more than sadness. For at least two weeks, nearly every day, the person is either down most of the day or has lost interest in things they used to enjoy — plus other changes: sleep and appetite shift, energy drains, concentration fails, they feel worthless or guilty, and sometimes they think about death. It has to be enough symptoms (five of nine) causing real trouble functioning. It is NOT ordinary sadness after a hard event, which comes in waves and lifts with support — and it is not laziness or weakness. A clinician thinks of it when the low mood is persistent, pervasive, and pulling the person's life apart.' (Cover: 2 weeks, 5/9 incl. mood or anhedonia, impairment, not-just-sadness.)",
    "type": "recall",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "mdd",
    "cluster": "mood-disorders",
    "bloom_level": "apply"
  },
  {
    "id": "u6-mdd-cloze-01",
    "prompt": "MDD requires {{five}} or more of nine symptoms, nearly every day for at least two weeks, and at least one must be depressed mood or anhedonia.",
    "answer": "five",
    "type": "cloze",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "mdd",
    "cluster": "mood-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-mdd-recur-cloze-01",
    "prompt": "MDD's recurrence staircase: about 50% recur after a first episode, 70% after a second, and {{90}}% after a third — which is why episode history changes maintenance-treatment conversations.",
    "answer": "90",
    "type": "cloze",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "mdd",
    "cluster": "mood-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-griefmdd-compare-01",
    "prompt": "Contrast ordinary grief with a major depressive episode on: self-esteem, the shape of the pain over time, and consolability.",
    "answer": "Grief: self-esteem PRESERVED; pain comes in WAVES with positive memories and even laughter between; the person is CONSOLABLE by support and connection; oriented to the loss. MDD: WORTHLESSNESS and self-loathing; PERVASIVE misery without relief; largely INCONSOLABLE; oriented to the self. Grief that stays intense, yearning-centered, and impairing 12+ months out is prolonged grief disorder (DSM-5-TR).",
    "type": "compare",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "grief-vs-depression",
    "cluster": "mood-disorders",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-bereave-evaluate-01",
    "prompt": "DSM-5 removed the bereavement exclusion from MDD. Make the strongest case FOR the removal and the strongest case AGAINST it, then state the clinical position that survives both.",
    "answer": "FOR: bereavement-triggered depression doesn't demonstrably differ in nature, course, or outcome from depression after any other precipitant; depression is potentially lethal (~4% suicide), so excluding the bereaved 'closes the door on potentially life-saving interventions.' AGAINST: it risks medicalizing mourning — reading a universal human process as illness and prescribing it away. Surviving position: bereavement doesn't immunize against MDD, AND grief isn't MDD by default — use the qualitative markers (self-esteem, waves, consolability), diagnose when they say depression, and don't when they say love.",
    "type": "explain",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "grief-vs-depression",
    "cluster": "mood-disorders",
    "bloom_level": "evaluate"
  },
  {
    "id": "u6-maniahypo-compare-01",
    "prompt": "A manic episode and a hypomanic episode share the same symptom list. Name the three things that make it MANIA, and the duration line for each episode type.",
    "answer": "Same symptoms (grandiosity, decreased need for sleep, pressured speech, racing thoughts, distractibility, goal-directed overdrive, high-risk behavior; 3+ needed, 4+ if mood only irritable). It is MANIA if there is (1) marked functional impairment, (2) hospitalization, or (3) psychotic features — any one suffices. Duration: mania 7+ days (or any length if hospitalized); hypomania 4+ days, observable by others, WITHOUT marked impairment/hospitalization/psychosis.",
    "type": "compare",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "mania-vs-hypomania",
    "cluster": "mood-disorders",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-bipolar-mcq-01",
    "prompt": "A 28-year-old has had two major depressive episodes. Last spring she had five days of unusual energy — slept 4 hours yet felt great, talked fast, started three projects, friends said she 'wasn't herself' — but she kept working and nothing bad happened. Diagnosis territory?",
    "options": [
      "Bipolar II — hypomanic episode plus major depression, never full mania",
      "Bipolar I — the energy episode counts as mania",
      "MDD, recurrent — the spring episode was just a good mood",
      "Cyclothymic disorder — alternating highs and lows"
    ],
    "correct": "Bipolar II — hypomanic episode plus major depression, never full mania",
    "answer": "Five days of elevated energy with decreased need for sleep, pressured speech, and increased activity, observable to others but WITHOUT marked impairment/hospitalization/psychosis = hypomania. Hypomania + at least one major depressive episode, no mania ever = Bipolar II. Not Bipolar I (no mania); not cyclothymia (these reached full episode thresholds); not 'just a good mood' — that miss is exactly how bipolar hides as MDD.",
    "type": "mcq",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "bipolar-i-vs-ii",
    "cluster": "mood-disorders",
    "bloom_level": "apply"
  },
  {
    "id": "u6-maniascreen-explain-01",
    "prompt": "Before agreeing with a new client that this is 'depression,' you always ask about lifetime highs. Give the two numbers that justify the habit, and one screening question in plain words.",
    "answer": "(1) 20-30% of apparent MDD presentations transition to a bipolar diagnosis within 3 years; (2) correct bipolar diagnosis lags first clinical contact by ~6-10 years on average — because people seek help while depressed and nobody asks about the highs. Stakes: antidepressants alone can destabilize undetected bipolar. Question: 'Has there ever been a stretch of days when you needed almost no sleep and still felt full of energy — when friends said you weren't yourself?'",
    "type": "explain",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "bipolar-screening",
    "cluster": "mood-disorders",
    "bloom_level": "apply"
  }
]
```

## Anxiety disorders

```json
[
  {
    "id": "u6-gad-rep-01",
    "prompt": "PRACTICE REP (syllabus): Explain generalized anxiety disorder to a layperson in two minutes — what it is, what it is not, what makes a clinician think of it. Out loud, then compare.",
    "answer": "Model: 'Everyone worries. GAD is worry that has taken over the controls: for six months or more, most days, the person is anxious about many ordinary things — work, health, family, money — and crucially they CAN'T turn it off, even when they know it's out of proportion. The body keeps score: restlessness, tiring easily, trouble concentrating, irritability, muscle tension, bad sleep (three or more of those). It is NOT a rational response to one big problem, and not a phobia of one specific thing — the worry migrates from topic to topic. A clinician thinks of it when worry is chronic, uncontrollable, multi-topic, and wearing the person down.' (Cover: 6 months, uncontrollable, multiple domains, 3/6 somatic symptoms.)",
    "type": "recall",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "gad",
    "cluster": "anxiety-disorders",
    "bloom_level": "apply"
  },
  {
    "id": "u6-gad-cloze-01",
    "prompt": "GAD requires excessive, hard-to-control worry more days than not for at least {{6 months}}, plus 3+ of: restlessness, easy fatigue, poor concentration, irritability, muscle tension, sleep disturbance.",
    "answer": "6 months",
    "type": "cloze",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "gad",
    "cluster": "anxiety-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-panicattack-explain-01",
    "prompt": "Why is 'panic attack' not a diagnosis, and what two things convert attacks into panic DISORDER?",
    "answer": "Panic attacks (abrupt surge of fear peaking within minutes, 4+ of 13 symptoms) occur across many disorders and in medical conditions — they're a symptom, like fever. Panic disorder requires (1) recurrent UNEXPECTED attacks — out of a clear blue sky, not cued — and (2) a month or more of worry about further attacks and/or maladaptive behavior change (avoiding exercise, ERs, going out alone). The disorder is fear of the fear.",
    "type": "explain",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "panic-disorder",
    "cluster": "anxiety-disorders",
    "bloom_level": "understand"
  },
  {
    "id": "u6-panic-cued-mcq-01",
    "prompt": "A client has intense panic attacks — racing heart, can't breathe, sure he'll die — but only ever right before presentations at work, which he now schemes to avoid. Best diagnostic territory?",
    "options": [
      "Social anxiety disorder — the attacks are cued by feared scrutiny",
      "Panic disorder — recurrent attacks plus avoidance",
      "Agoraphobia — avoidance of situations where escape is difficult",
      "GAD — work-related worry with physical symptoms"
    ],
    "correct": "Social anxiety disorder — the attacks are cued by feared scrutiny",
    "answer": "The attacks are EXPECTED — reliably cued by one situation type (evaluated performance), which points to the underlying disorder doing the cueing: social anxiety disorder. Panic disorder requires recurrent UNEXPECTED attacks. This expected-vs-unexpected hinge is the chapter's central discrimination.",
    "type": "mcq",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "expected-vs-unexpected",
    "cluster": "anxiety-disorders",
    "bloom_level": "apply"
  },
  {
    "id": "u6-agorasocial-mcq-01",
    "prompt": "Two clients avoid crowded places. Ana fears she'll have a panic-like episode and be unable to get out or get help. Ben fears he'll do something embarrassing and people will judge him. Which is which?",
    "options": [
      "Ana: agoraphobia (fear of being trapped without help); Ben: social anxiety disorder (fear of negative evaluation)",
      "Ana: social anxiety disorder; Ben: agoraphobia",
      "Both agoraphobia — the avoided situation is the same",
      "Both social anxiety disorder — crowds imply an audience"
    ],
    "correct": "Ana: agoraphobia (fear of being trapped without help); Ben: social anxiety disorder (fear of negative evaluation)",
    "answer": "Same avoidance, different fear — and the FEAR, not the situation, is what diagnoses. Agoraphobia: escape might be difficult, help unavailable if symptoms strike. Social anxiety: scrutiny and negative evaluation. Always ask 'what's the feared outcome?' before mapping situation to label.",
    "type": "mcq",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "agoraphobia-vs-social",
    "cluster": "anxiety-disorders",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-anxietymap-compare-01",
    "prompt": "Give the one-phrase 'what the fear is about' for each: GAD, panic disorder, agoraphobia, social anxiety disorder, specific phobia, separation anxiety disorder.",
    "answer": "GAD: 'everything could go wrong' (diffuse, migrating). Panic disorder: 'the attack itself' (fear of fear). Agoraphobia: 'I'll be trapped where help can't reach me.' Social anxiety: 'they'll judge me' (scrutiny). Specific phobia: 'that one thing.' Separation anxiety: 'losing my person' (attachment figure). The chapter solves itself by naming the fear's object and trigger pattern.",
    "type": "compare",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "anxiety-differentials",
    "cluster": "anxiety-disorders",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-reassure-evaluate-01",
    "prompt": "An anxious client asks, session after session, 'But do you think it will be okay?' Warm reassurance feels kind and helps for a day. What is it actually doing, and what does the alternative stance look like?",
    "answer": "Reassurance is relief-on-demand: like avoidance, it teaches the alarm that it was right to fire and that safety requires an external answer — maintaining the disorder and making you part of its loop. The alternative isn't coldness: empathize with the fear (reflect it accurately), decline to issue certainty verdicts, and help the client approach rather than escape the uncertainty ('You're asking me to make the dread stop — I care more about helping you carry not-knowing'). Same principle scales to exposure-based treatment in Unit 9.",
    "type": "explain",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "reassurance-trap",
    "cluster": "anxiety-disorders",
    "bloom_level": "evaluate"
  }
]
```

## Trauma- and stressor-related disorders

```json
[
  {
    "id": "u6-ptsd-rep-01",
    "prompt": "PRACTICE REP (syllabus): Explain PTSD to a layperson in two minutes — what it is, what it is not, what makes a clinician think of it. Out loud, then compare.",
    "answer": "Model: 'After something horrific — actual or threatened death, serious injury, or sexual violence, experienced or witnessed — most people are shaken and gradually recover. In PTSD the event doesn't file itself away as past. It intrudes (memories, nightmares, flashbacks); the person avoids reminders; their mood and beliefs turn dark (shame, blame, numbness, 'the world is dangerous'); and their alarm system stays stuck on (jumpy, sleepless, hypervigilant). When that four-part picture lasts beyond a month and disrupts life, that's PTSD. It is NOT weakness, and it is NOT the automatic result of trauma — most trauma-exposed people don't develop it. A clinician thinks of it when a specific event keeps replaying and reorganizing someone's life.' (Cover: Criterion-A event, 4 clusters, >1 month, most exposed don't develop it.)",
    "type": "recall",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "ptsd",
    "cluster": "trauma-disorders",
    "bloom_level": "apply"
  },
  {
    "id": "u6-criteriona-mcq-01",
    "prompt": "Which of these satisfies PTSD's Criterion A gate?",
    "options": [
      "A paramedic repeatedly exposed to gruesome accident scenes over years",
      "Watching extensive news coverage of a distant disaster",
      "A painful divorce with prolonged custody conflict",
      "Being laid off without warning after twenty years"
    ],
    "correct": "A paramedic repeatedly exposed to gruesome accident scenes over years",
    "answer": "Criterion A: actual/threatened death, serious injury, or sexual violence — directly experienced, witnessed in person, learned of happening to someone close, or REPEATED INDIRECT PROFESSIONAL exposure (first responders). Media exposure is explicitly excluded; divorce and job loss are serious stressors but route to ADJUSTMENT DISORDER. (Note the drawn-line caveat: many clinicians argue chronic non-Criterion-A adversity can be traumatogenic — the gate is a definition, not a fact of nature.)",
    "type": "mcq",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "criterion-a",
    "cluster": "trauma-disorders",
    "bloom_level": "apply"
  },
  {
    "id": "u6-ptsdclusters-recall-01",
    "prompt": "Name PTSD's four symptom clusters with the count required from each, and the duration criterion.",
    "answer": "B INTRUSION (1+): memories, nightmares, flashbacks, cued distress/reactivity. C AVOIDANCE (1+): of internal reminders and/or external cues. D NEGATIVE ALTERATIONS IN COGNITIONS AND MOOD (2+): amnesia for aspects, 'I am bad / world is dangerous,' distorted blame, persistent negative emotions, detachment, diminished interest, no positive emotion. E AROUSAL AND REACTIVITY (2+): irritability, recklessness, hypervigilance, startle, concentration, sleep. Duration: more than 1 MONTH (plus impairment).",
    "type": "recall",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "ptsd",
    "cluster": "trauma-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-asd-cloze-01",
    "prompt": "Acute stress disorder shares PTSD's trauma gate and symptom pool, but its window is 3 days to {{1 month}} post-event — still symptomatic past that line, the diagnosis converts to PTSD.",
    "answer": "1 month",
    "type": "cloze",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "acute-stress-disorder",
    "cluster": "trauma-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-adjust-mcq-01",
    "prompt": "Six weeks after being laid off, a client can't stop ruminating, sleeps badly, has withdrawn from friends, and is underperforming in his job search — but doesn't meet full MDD criteria. Most accurate diagnosis?",
    "options": [
      "Adjustment disorder — impairing response to an identifiable non-Criterion-A stressor, within 3 months",
      "PTSD — the layoff was experienced as catastrophic",
      "Major depressive disorder — sadness, sleep, and withdrawal are present",
      "No diagnosis — this is a normal reaction and coding it pathologizes it"
    ],
    "correct": "Adjustment disorder — impairing response to an identifiable non-Criterion-A stressor, within 3 months",
    "answer": "Identifiable stressor (not Criterion-A trauma), onset within 3 months, distress/impairment beyond expectable, full criteria for MDD not met: adjustment disorder — the honest middle between 'nothing' and force-fitting MDD/PTSD. It's what accurate modest diagnosis looks like; expected to resolve within 6 months of the stressor (and its consequences) ending.",
    "type": "mcq",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "adjustment-disorder",
    "cluster": "trauma-disorders",
    "bloom_level": "apply"
  },
  {
    "id": "u6-traumaclock-compare-01",
    "prompt": "Sort the four trauma/stressor diagnoses by their two-part grammar: WHICH stressor and WHICH clock. (PTSD, acute stress disorder, adjustment disorder, prolonged grief disorder.)",
    "answer": "Criterion-A trauma + 3 days-1 month = ACUTE STRESS DISORDER. Criterion-A trauma + >1 month = PTSD. Any identifiable stressor + onset within 3 months (resolving within 6 of stressor ending) = ADJUSTMENT DISORDER. Death of someone close + 12+ months of yearning-centered, impairing grief beyond cultural norms = PROLONGED GRIEF DISORDER. Every diagnosis in the chapter = an event + a clock; it's the only DSM chapter with etiology in the criteria.",
    "type": "compare",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "trauma-differentials",
    "cluster": "trauma-disorders",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-pgd-cloze-01",
    "prompt": "Prolonged grief disorder (DSM-5-TR) requires that the death occurred at least {{12 months}} ago (6 in children), with intense yearning or preoccupation most days plus impairing grief symptoms beyond cultural norms.",
    "answer": "12 months",
    "type": "cloze",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "prolonged-grief",
    "cluster": "trauma-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-disclosure-evaluate-01",
    "prompt": "A new client alludes to 'something that happened' last year. You suspect trauma, and part of you wants the full story to 'assess properly.' What does trauma-informed practice say about pushing for the narrative, and what do you actually need?",
    "answer": "Don't push. Detailed disclosure is NOT required for diagnosis, screening, or safety — and pressing for the narrative before the person has stability and trust is a classic way helpers re-traumatize (Unit 8's core principle, previewed). You need: whether something happened that still intrudes on their life, current symptoms and safety, and their pace. Screening is asking plainly and accepting the answer; the story comes when and if the client chooses. The 'I need all the data' reflex serves the helper, not the client.",
    "type": "explain",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "trauma-stance",
    "cluster": "trauma-disorders",
    "bloom_level": "evaluate"
  }
]
```

## OCD & related disorders

```json
[
  {
    "id": "u6-ocd-def-recall-01",
    "prompt": "Define obsessions and compulsions, including the functional relationship between them, and the threshold that makes them a disorder.",
    "answer": "OBSESSIONS: recurrent, persistent, INTRUSIVE AND UNWANTED thoughts, urges, or images (contamination, harm, blasphemy, doubt). COMPULSIONS: repetitive behaviors or MENTAL ACTS the person feels driven to perform in response to an obsession or per rigid rules (washing, checking, counting, praying, reviewing). The compulsion buys short-term relief, which reinforces the obsession — an anxiety loop wound tight. Disorder threshold: time-consuming (≥1 hour/day) or causing marked distress/impairment.",
    "type": "recall",
    "source_page": "wiki/concept-ocd.md",
    "topic": "ocd",
    "bloom_level": "remember"
  },
  {
    "id": "u6-ocd-egodystonic-cloze-01",
    "prompt": "OCD is typically ego-{{dystonic}}: only 2-4% lack insight — most sufferers know the fear is irrational and are tormented precisely because the thoughts feel alien to who they are.",
    "answer": "dystonic",
    "type": "cloze",
    "source_page": "wiki/concept-ocd.md",
    "topic": "ocd",
    "bloom_level": "understand"
  },
  {
    "id": "u6-ocd-family-recall-01",
    "prompt": "OCD left the anxiety chapter in DSM-5. What chapter did it get, which disorders came with it, and what's the shared signature?",
    "answer": "Obsessive-Compulsive and Related Disorders: OCD, body dysmorphic disorder (perceived appearance flaw + checking/grooming rituals), hoarding disorder, trichotillomania (hair-pulling), excoriation (skin-picking). Shared signature: repetitive, driven behavior locked to distressing internal experience, with overlapping neurobiology. Clinical payoff of the move: OCD is not generic anxiety, and treating it like worry misses its engine.",
    "type": "recall",
    "source_page": "wiki/concept-ocd.md",
    "topic": "ocd-related",
    "bloom_level": "remember"
  },
  {
    "id": "u6-ocd-reassure-apply-01",
    "prompt": "A client with OCD asks for the fourth time this session, 'But you're sure I would never actually hurt my kids, right?' You know reassurance calms her for a few minutes. What is happening functionally, and how do you respond?",
    "answer": "Your reassurance has become a COMPULSION — an anxiety-relieving ritual she's outsourced to you; each 'I'm sure' relieves briefly and strengthens the obsession (family members are usually deep in this loop too). Respond with warmth minus the verdict: name the pattern ('That's the OCD asking me to do the ritual'), empathize with the distress, and hold the frame that intrusive harm-thoughts in OCD are ego-dystonic — horror at the thought is not intent (genuine risk assessment is a different, deliberate process). This is the ERP principle before ERP starts.",
    "type": "vignette",
    "source_page": "wiki/concept-ocd.md",
    "topic": "reassurance-trap",
    "bloom_level": "apply"
  }
]
```

## Schizophrenia spectrum & other psychotic disorders

```json
[
  {
    "id": "u6-psychosis-domains-recall-01",
    "prompt": "Name schizophrenia's five Criterion A symptom domains, the count rule, and which domains are 'positive' vs 'negative.'",
    "answer": "(1) Delusions, (2) hallucinations, (3) disorganized speech, (4) grossly disorganized or catatonic behavior, (5) negative symptoms (diminished expression, avolition). Rule: 2+ for a significant portion of a month, at least one from the first three. Positive symptoms = additions to experience (1-4); negative = subtractions (5). Antipsychotics treat positive symptoms far better; negative symptoms carry much of the disability.",
    "type": "recall",
    "source_page": "wiki/concept-psychotic-disorders.md",
    "topic": "schizophrenia",
    "cluster": "psychotic-spectrum",
    "bloom_level": "remember"
  },
  {
    "id": "u6-schizo-duration-cloze-01",
    "prompt": "Schizophrenia requires continuous signs for at least {{6 months}}, including at least 1 month of active-phase symptoms, with functional decline.",
    "answer": "6 months",
    "type": "cloze",
    "source_page": "wiki/concept-psychotic-disorders.md",
    "topic": "schizophrenia",
    "cluster": "psychotic-spectrum",
    "bloom_level": "remember"
  },
  {
    "id": "u6-duration-mcq-01",
    "prompt": "A 22-year-old has had hallucinations, delusions, and disorganized speech for three months, with recovery expected but uncertain. Which diagnosis fits the picture right now?",
    "options": [
      "Schizophreniform disorder — schizophrenia's picture, 1 to <6 months",
      "Schizophrenia — the symptom picture is definitive regardless of duration",
      "Brief psychotic disorder — any psychosis under six months",
      "Schizoaffective disorder — psychosis in a young adult"
    ],
    "correct": "Schizophreniform disorder — schizophrenia's picture, 1 to <6 months",
    "answer": "The spectrum is a duration ladder over one symptom pool: brief psychotic disorder (1 day to <1 month, full return); SCHIZOPHRENIFORM (1 to <6 months); schizophrenia (≥6 months incl. 1 month active-phase, with decline). Three months of full symptoms = schizophreniform; if it persists past six, the diagnosis converts. Schizoaffective requires concurrent mood episodes plus a mood-free psychosis window.",
    "type": "mcq",
    "source_page": "wiki/concept-psychotic-disorders.md",
    "topic": "duration-ladder",
    "cluster": "psychotic-spectrum",
    "bloom_level": "apply"
  },
  {
    "id": "u6-schizoaffective-mcq-01",
    "prompt": "A client has had major depressive episodes with hallucinations. Records show a stretch of 3+ weeks where the hallucinations and delusions continued while her mood was fine. Which does that window establish?",
    "options": [
      "Schizoaffective disorder — psychosis persisting ≥2 weeks without a mood episode",
      "MDD with psychotic features — psychosis occurred during depressions",
      "Schizophrenia — hallucinations plus delusions suffice",
      "Bipolar I with psychotic features — psychosis implies mania"
    ],
    "correct": "Schizoaffective disorder — psychosis persisting ≥2 weeks without a mood episode",
    "answer": "The discriminator is WHEN psychosis happens relative to mood: in MDD (or bipolar) with psychotic features, psychosis lives ONLY inside mood episodes; schizoaffective requires ≥2 weeks of delusions/hallucinations WITHOUT a mood episode (plus mood episodes concurrent with active-phase symptoms across the illness). Her 3-week mood-free psychotic window is exactly that evidence.",
    "type": "mcq",
    "source_page": "wiki/concept-psychotic-disorders.md",
    "topic": "schizoaffective",
    "cluster": "psychotic-spectrum",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-spectrum-compare-01",
    "prompt": "Lay out the psychotic-spectrum duration ladder plus the two off-ladder diagnoses, one line each: brief psychotic disorder, schizophreniform, schizophrenia, delusional disorder, schizoaffective disorder.",
    "answer": "BRIEF PSYCHOTIC: 1 day to <1 month, full return to functioning, often stress-precipitated. SCHIZOPHRENIFORM: 1 to <6 months, no decline requirement. SCHIZOPHRENIA: ≥6 months continuous signs incl. ≥1 month active phase, with decline. DELUSIONAL DISORDER: ≥1 month of delusions ONLY — no other domains prominent, functioning largely intact. SCHIZOAFFECTIVE: mood episodes concurrent with active-phase symptoms PLUS ≥2 weeks of psychosis without mood symptoms.",
    "type": "compare",
    "source_page": "wiki/concept-psychotic-disorders.md",
    "topic": "duration-ladder",
    "cluster": "psychotic-spectrum",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-delusion-stance-01",
    "prompt": "A client tells you, matter-of-factly, that her neighbors broadcast her thoughts. Arguing feels wrong; agreeing feels worse. What is the working stance, and why do both extremes fail?",
    "answer": "Neither argue nor endorse. Arguing entrenches (a delusion is by definition held against contrary evidence — debate makes you another doubter to defend against); colluding betrays trust and reality both. Reflect the EXPERIENCE without ruling on content: 'That sounds frightening — feeling watched everywhere, even at home.' You're validating the emotion, building alliance, and keeping the door open for care coordination (psychosis is coordinated-care, often scope-boundary territory). The aberrant-salience frame helps empathy: everything genuinely FEELS meaningful to her.",
    "type": "vignette",
    "source_page": "wiki/concept-psychotic-disorders.md",
    "topic": "psychosis-stance",
    "cluster": "psychotic-spectrum",
    "bloom_level": "apply"
  }
]
```

## Personality disorders

```json
[
  {
    "id": "u6-pd-def-recall-01",
    "prompt": "What makes something a personality DISORDER rather than an episode of illness? Give the four definitional properties, and the discrimination this creates against the rest of the unit.",
    "answer": "An ENDURING pattern of inner experience and behavior deviating from the person's own culture's expectations that is (1) PERVASIVE across contexts, (2) INFLEXIBLE, (3) STABLE with onset by adolescence/early adulthood, (4) causing distress or impairment — affecting cognition, affect, interpersonal functioning, impulse control. Discrimination: everything else in the unit is an episode that arrives and can remit; a PD is the person's baseline style. Two weeks of low mood = episode; a lifetime of stormy relationships = pattern.",
    "type": "recall",
    "source_page": "wiki/concept-personality-disorders.md",
    "topic": "pd-definition",
    "cluster": "personality-disorders",
    "bloom_level": "understand"
  },
  {
    "id": "u6-pd-clusters-recall-01",
    "prompt": "Name the three personality-disorder clusters with their one-word flavors and the ten disorders sorted into them.",
    "answer": "CLUSTER A — odd/eccentric: paranoid, schizoid, schizotypal. CLUSTER B — dramatic/emotional/erratic: antisocial, borderline, histrionic, narcissistic. CLUSTER C — anxious/fearful: avoidant, dependent, obsessive-compulsive (OCPD). Mnemonic flavor: A = weird, B = wild, C = worried.",
    "type": "recall",
    "source_page": "wiki/concept-personality-disorders.md",
    "topic": "pd-clusters",
    "cluster": "personality-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-schizoid-avoidant-mcq-01",
    "prompt": "Two clients are socially isolated. Cara has no close friends and, as far as she can tell, no wish for any — solitary work suits her, praise and criticism both leave her flat. Dev has no close friends and aches for them, but is certain he'd be found inadequate and avoids anyone who might reject him. Which is which?",
    "options": [
      "Cara: schizoid (indifference to relationships); Dev: avoidant (longing blocked by fear of rejection)",
      "Cara: avoidant; Dev: schizoid",
      "Both schizoid — isolation is the criterion",
      "Cara: schizotypal; Dev: dependent"
    ],
    "correct": "Cara: schizoid (indifference to relationships); Dev: avoidant (longing blocked by fear of rejection)",
    "answer": "Identical behavior (isolation), opposite motivation — and motivation diagnoses. Schizoid: genuine detachment and disinterest, restricted affect (Cluster A). Avoidant: WANTS connection, blocked by felt inadequacy and hypersensitivity to negative evaluation (Cluster C). Treatment implications diverge completely — Dev's longing is the therapeutic lever; Cara may not want the goal you'd assume.",
    "type": "mcq",
    "source_page": "wiki/concept-personality-disorders.md",
    "topic": "schizoid-vs-avoidant",
    "cluster": "personality-disorders",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-ocpd-ocd-compare-01",
    "prompt": "OCD and OCPD share a name and get confused constantly. Contrast them on: chapter, phenomenology (obsessions/compulsions?), and the ego-syntonic/dystonic axis.",
    "answer": "OCD: an obsessive-compulsive-and-related DISORDER (episodic-symptomatic) — true intrusive obsessions answered by compulsions, EGO-DYSTONIC (the person knows it's irrational and suffers from the alienness). OCPD: a Cluster C PERSONALITY disorder — a lifelong pattern of perfectionism and rigid control with NO true obsessions/compulsions, EGO-SYNTONIC (the standards feel correct; it's everyone else who has a problem). One is a tormenting loop the person fights; the other is a character style the person defends.",
    "type": "compare",
    "source_page": "wiki/concept-personality-disorders.md",
    "topic": "ocd-vs-ocpd",
    "cluster": "personality-disorders",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-ampd-explain-01",
    "prompt": "The DSM-5-TR carries an Alternative Model of Personality Disorders (AMPD). What does it rate instead of the ten categories, and why do personality disorders make the natural beachhead for dimensional diagnosis?",
    "answer": "AMPD rates (1) LEVEL OF IMPAIRMENT in personality functioning — self (identity, self-direction) and interpersonal (empathy, intimacy) — plus (2) PATHOLOGICAL TRAITS in five domains: negative affectivity, detachment, antagonism, disinhibition, psychoticism. PDs are the categorical system's weakest corner: massive overlap between the ten, extreme within-category heterogeneity, and arbitrary thresholds — so a trait-profile approach fits the data better here than anywhere. It's the categorical-vs-dimensional debate already inside the manual.",
    "type": "explain",
    "source_page": "wiki/concept-personality-disorders.md",
    "topic": "ampd",
    "cluster": "personality-disorders",
    "bloom_level": "understand"
  },
  {
    "id": "u6-pd-stigma-evaluate-01",
    "prompt": "'She's such a borderline' gets said in staff rooms as shorthand for 'difficult.' Name three disciplines that keep a counselor from that use of these diagnoses.",
    "answer": "(1) DIAGNOSE THE PATTERN, NOT THE MOMENT: criteria require a longitudinal, cross-context pattern an intake can't see — a person in crisis can look borderline, a person in a custody fight can look paranoid; be slow. (2) COUNTERTRANSFERENCE IS DATA, NOT A VERDICT: these patterns pull (rescue, dread, anger) — notice the pull, don't act or diagnose from it. (3) DEVELOPMENT REFRAMES: borderline features track disorganized attachment and early adversity — an old survival strategy, not manipulation; risk-not-destiny applies. Also: DBT's evidence means the prognosis-nihilism behind the slur is factually wrong.",
    "type": "explain",
    "source_page": "wiki/concept-personality-disorders.md",
    "topic": "pd-stance",
    "cluster": "personality-disorders",
    "bloom_level": "evaluate"
  }
]
```

## Substance use disorders (the DSM view — full depth in aux-addiction)

```json
[
  {
    "id": "u6-sud-structure-explain-01",
    "prompt": "Describe how DSM-5 restructured substance diagnosis: what replaced abuse/dependence, how severity works, and why SUD is the manual's most openly dimensional diagnosis.",
    "answer": "DSM-IV's abuse-vs-dependence split collapsed into ONE substance use disorder per substance class, diagnosed against 11 criteria in four groups (impaired control, social impairment, risky use, pharmacological: tolerance/withdrawal). Severity is a straight symptom count — mild 2-3, moderate 4-5, severe 6+ — a graded dial rather than a category switch, which is dimensional diagnosis already inside the tent (compare the AMPD).",
    "type": "explain",
    "source_page": "wiki/concept-substance-use-disorders.md",
    "topic": "sud-structure",
    "bloom_level": "understand"
  },
  {
    "id": "u6-sud-mimic-apply-01",
    "prompt": "A new client presents with panic attacks and depressed mood. Why does the substance history come before any diagnosis in this unit — give the two mechanisms and the intake habit.",
    "answer": "(1) Substances MIMIC: intoxication and withdrawal can produce depression, anxiety, panic, and psychosis (substance-induced disorders are on every differential — heavy caffeine/stimulants for panic, alcohol/sedative withdrawal for anxiety, stimulant psychosis). (2) Substances CO-TRAVEL: SUDs are comorbid with nearly every category, and comorbidity concentrates severity. Missing either reroutes the entire treatment plan. Habit: ask about substances matter-of-factly in every intake, whatever the presenting problem — tone from the addiction module (no moralizing, no righting reflex).",
    "type": "vignette",
    "source_page": "wiki/concept-substance-use-disorders.md",
    "topic": "substance-induced",
    "bloom_level": "apply"
  }
]
```

## Neurodevelopmental disorders

```json
[
  {
    "id": "u6-adhd-recall-01",
    "prompt": "Give ADHD's diagnostic mechanics: symptom counts (child vs 17+), onset rule, settings rule, and the three presentations.",
    "answer": "6+ of 9 inattention symptoms and/or 6+ of 9 hyperactivity-impulsivity symptoms (5+ suffices at age 17+); several symptoms BEFORE AGE 12; present in 2+ SETTINGS (school-only problems suggest a classroom issue, not ADHD); clear functional interference. Presentations: predominantly inattentive (the underdiagnosed, no-fireworks one), predominantly hyperactive/impulsive, combined.",
    "type": "recall",
    "source_page": "wiki/concept-neurodevelopmental-disorders.md",
    "topic": "adhd",
    "bloom_level": "remember"
  },
  {
    "id": "u6-adhd-timeline-explain-01",
    "prompt": "A 30-year-old with low mood says she 'can't focus on anything anymore' and wonders if she has ADHD. What single feature of the history does the discrimination turn on, and why does the trap run both directions?",
    "answer": "The TIMELINE. ADHD is developmental: childhood onset (before 12), lifelong, cross-context. Concentration failure that began at 30 alongside low mood points to depression (or anxiety), not ADHD. Both directions: anxiety/depression impair concentration and get misread as ADHD; ADHD's demoralized, scattered adult (often the inattentive presentation, often a woman missed in childhood) gets misread as anxious/depressed. So take the childhood history seriously in both cases — report cards, parent memories, lifelong patterns.",
    "type": "explain",
    "source_page": "wiki/concept-neurodevelopmental-disorders.md",
    "topic": "adhd-differential",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-asd-recall-01",
    "prompt": "Autism spectrum disorder has two symptom pillars. Name them with their count rules, and what DSM-5 merged into the single spectrum.",
    "answer": "(1) Persistent deficits in social communication/interaction — ALL THREE areas: social-emotional reciprocity; nonverbal communication; developing/maintaining/understanding relationships. (2) Restricted, repetitive behaviors — AT LEAST 2 OF 4: stereotyped movements/speech; insistence on sameness/routines; highly restricted fixated interests; sensory hyper-/hypo-reactivity. Onset in early development; severity levels 1-3. DSM-5 merged autistic disorder, Asperger's, and PDD-NOS into the one spectrum.",
    "type": "recall",
    "source_page": "wiki/concept-neurodevelopmental-disorders.md",
    "topic": "asd",
    "bloom_level": "remember"
  },
  {
    "id": "u6-neurodiversity-evaluate-01",
    "prompt": "An autistic adult client says: 'I'm not disordered — my brain is different, and the world is built for yours.' The DSM calls his differences deficits. How does a counselor hold both?",
    "answer": "Without forcing either. The neurodiversity frame is a legitimate self-understanding with real momentum (difference to accommodate, not deficit to cure), and the client is the expert on his experience; the DSM frame still does necessary work (naming real struggles, unlocking services/accommodations that require diagnosis). Working stance: adopt the client's language for his identity, keep the diagnostic frame for the functions it serves, and put the biopsychosocial lens on the ENVIRONMENT too — impairment is partly an interaction between person and context, not a property of the person alone. What you don't do: argue him into deficit language or romanticize away struggles he names.",
    "type": "explain",
    "source_page": "wiki/concept-neurodevelopmental-disorders.md",
    "topic": "neurodiversity",
    "bloom_level": "evaluate"
  }
]
```

## Feeding & eating disorders

```json
[
  {
    "id": "u6-an-recall-01",
    "prompt": "Give anorexia nervosa's three criteria (all required) and its two subtypes.",
    "answer": "(1) Restriction of energy intake leading to SIGNIFICANTLY LOW BODY WEIGHT; (2) INTENSE FEAR of gaining weight/becoming fat (or persistent gain-preventing behavior) — a fear that intensifies as weight falls; (3) DISTURBANCE in experienced body weight/shape, undue influence of weight/shape on self-worth, or failure to recognize the seriousness of the low weight. Subtypes: RESTRICTING (diet/fast/exercise only) and BINGE-EATING/PURGING (with binge or purge behavior — still AN because weight is low).",
    "type": "recall",
    "source_page": "wiki/concept-eating-disorders.md",
    "topic": "anorexia",
    "cluster": "eating-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-anbn-mcq-01",
    "prompt": "A client at a significantly low body weight binges weekly and induces vomiting afterward, terrified of gaining weight. Diagnosis?",
    "options": [
      "Anorexia nervosa, binge-eating/purging subtype — low weight decides it",
      "Bulimia nervosa — binge plus compensatory behavior is definitional",
      "Binge-eating disorder — recurrent binges are present",
      "Both AN and BN concurrently"
    ],
    "correct": "Anorexia nervosa, binge-eating/purging subtype — low weight decides it",
    "answer": "The AN/BN line is the WEIGHT CRITERION, not the behavior: binge-purge behavior at significantly low weight = AN, binge-eating/purging subtype. BN requires normal-or-above weight. The distinction matters medically — AN carries the higher mortality and the low-weight complications.",
    "type": "mcq",
    "source_page": "wiki/concept-eating-disorders.md",
    "topic": "an-vs-bn",
    "cluster": "eating-disorders",
    "bloom_level": "apply"
  },
  {
    "id": "u6-eating-compare-01",
    "prompt": "Sort AN, BN, BED, and ARFID on the chapter's hinge questions: low weight? binges? compensation? body-image driver?",
    "answer": "AN: low weight YES; binges maybe; compensation maybe; body-image YES. BN: weight normal-or-above; binges YES; compensation YES (vomiting, laxatives, fasting, driven exercise; weekly, 3 months); body-image YES. BED: binges YES with loss of control and distress; compensation NO (the BN line); most common ED in the US, more gender-balanced. ARFID: restriction with nutritional consequences but NO body-image disturbance (sensory aversion, choking fear, low interest) — what separates impairing picky eating from AN.",
    "type": "compare",
    "source_page": "wiki/concept-eating-disorders.md",
    "topic": "eating-differentials",
    "cluster": "eating-disorders",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-an-mortality-cloze-01",
    "prompt": "Anorexia nervosa is among the deadliest psychiatric diagnoses — via medical complications plus suicide, which accounts for roughly a {{quarter}} of AN deaths. Outpatient counseling therefore always runs alongside medical monitoring.",
    "answer": "quarter",
    "type": "cloze",
    "source_page": "wiki/concept-eating-disorders.md",
    "topic": "anorexia",
    "cluster": "eating-disorders",
    "bloom_level": "remember"
  },
  {
    "id": "u6-eating-screen-apply-01",
    "prompt": "Why is screening for eating disorders by appearance a double failure, and what does behavioral screening sound like?",
    "answer": "Failure 1: most people with eating disorders are NOT visibly underweight — BN and BED by definition occur at normal-or-above weight, so the eye misses most cases. Failure 2: appearance-focus repeats the disorder's own logic, and casual weight/body comments (including compliments on loss) can reinforce restriction. Behavioral screening: 'Do you ever eat in a way that feels out of control?' 'What happens after?' 'How much time do thoughts about food, weight, or your body take up?' Ask everyone, not just thin young women — and remember AN is often ego-syntonic: expect the disorder to defend itself.",
    "type": "explain",
    "source_page": "wiki/concept-eating-disorders.md",
    "topic": "eating-screening",
    "cluster": "eating-disorders",
    "bloom_level": "apply"
  }
]
```

## Categorical vs. dimensional — comorbidity and the limits of diagnosis

```json
[
  {
    "id": "u6-cracks-recall-01",
    "prompt": "The dimensional critique indicts categorical diagnosis on four counts. Name and explain all four.",
    "answer": "(1) RELIABILITY: ~40% of diagnoses tested in the DSM-5 field trials showed poor inter-rater agreement — same patient, different labels. (2) COMORBIDITY: 'distinct' disorders co-occur constantly (45% of 12-month cases carry 2+), questioning their distinctness. (3) HETEROGENEITY: same-diagnosis patients can share few or no symptoms (MDD's 5-of-9 allows near-disjoint presentations). (4) CONTINUITY: most psychopathology lies on a continuum with normality — no common disorder has been shown to be a true natural category; thresholds are drawn lines.",
    "type": "recall",
    "source_page": "wiki/concept-categorical-vs-dimensional.md",
    "topic": "categorical-critique",
    "bloom_level": "understand"
  },
  {
    "id": "u6-comorbid-cloze-01",
    "prompt": "In the NCS-R, among people meeting 12-month criteria for any disorder, {{45}}% met criteria for two or more (22% two, 23% three+) — and the most comorbid ~7% of the sample held ~44% of all serious cases.",
    "answer": "45",
    "type": "cloze",
    "source_page": "wiki/concept-categorical-vs-dimensional.md",
    "topic": "comorbidity",
    "bloom_level": "remember"
  },
  {
    "id": "u6-comorbid-explain-01",
    "prompt": "Comorbidity's numbers support two different lessons — one clinical, one scientific. Give both.",
    "answer": "CLINICAL: never stop assessing after the first criteria set fits — a second (and third) disorder is present nearly half the time, severity concentrates in the comorbid few, and anxiety+depression / SUD+everything are the everyday pairs. SCIENTIFIC: categories that co-travel this reliably may not be separate things at all — comorbidity is the crack in the categorical system that launched the dimensional research program (HiTOP, p factor).",
    "type": "explain",
    "source_page": "wiki/concept-categorical-vs-dimensional.md",
    "topic": "comorbidity",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-hitop-explain-01",
    "prompt": "In HiTOP terms, what happens to a client who would carry six comorbid DSM diagnoses (MDD, PTSD, social anxiety, panic, borderline and avoidant PD) — and what honest limitation do HiTOP's own authors state?",
    "answer": "She becomes a PROFILE on continuous dimensions instead of a stack of labels — e.g., 'internalizing spectrum: severe' (with elevations in dysphoria, panic, social anxiety, trauma symptoms, emotional lability) plus 'antagonistic externalizing: mild.' Six 'comorbidities' collapse into one coherent picture that points at shared mechanisms. Limitation, in their words: there is no direct evidence yet that using HiTOP clinically improves treatment outcomes — better prediction of chronicity/impairment, yes; outcome trials, not yet.",
    "type": "explain",
    "source_page": "wiki/concept-categorical-vs-dimensional.md",
    "topic": "hitop",
    "bloom_level": "understand"
  },
  {
    "id": "u6-pfactor-cloze-01",
    "prompt": "Caspi & Moffitt found disorder co-occurrence fits three spectra (internalizing, externalizing, thought disorder) under one general psychopathology factor — the {{p}} factor, analogous to g in intelligence; higher scores predict more impairment, stronger family history, and worse developmental course.",
    "answer": "p",
    "type": "cloze",
    "source_page": "wiki/concept-categorical-vs-dimensional.md",
    "topic": "p-factor",
    "bloom_level": "remember"
  },
  {
    "id": "u6-rdoc-mcq-01",
    "prompt": "A classmate says: 'NIMH's RDoC has replaced the DSM — clinicians should diagnose with it.' What's wrong with that?",
    "options": [
      "RDoC is a research framework and explicitly not a diagnostic guide or DSM replacement",
      "Nothing — RDoC superseded the DSM for federal purposes in 2013",
      "RDoC is the ICD's American name, so it's redundant, not wrong",
      "RDoC applies only to neurodevelopmental disorders"
    ],
    "correct": "RDoC is a research framework and explicitly not a diagnostic guide or DSM replacement",
    "answer": "NIMH's own language: RDoC 'is not meant to serve as a diagnostic guide, nor is it intended to replace current diagnostic systems.' It reorganizes RESEARCH around functional domains (threat, reward...) studied genes-to-behavior across the normal-to-abnormal range, because DSM categories are too heterogeneous and comorbid to be good research targets. Clinics still run on DSM/ICD.",
    "type": "mcq",
    "source_page": "wiki/concept-categorical-vs-dimensional.md",
    "topic": "rdoc",
    "bloom_level": "understand"
  },
  {
    "id": "u6-inflation-evaluate-01",
    "prompt": "Frances's 'diagnostic inflation' charge vs. the early-intervention defense: state each side's strongest evidence, and where a working counselor lands.",
    "answer": "FRANCES (chaired DSM-IV): ADHD diagnoses tripled in 20 years, childhood bipolar up 40-fold, autism 20-fold; one cohort accumulated 83% prevalence of 'some disorder' by 21; drug companies market diagnoses to convert 'expectable life problems' into patients. DEFENSE: rising counts partly reflect better detection and broadened criteria catching people who were always there suffering (the inattentive girl, the masked autistic adult); lowered thresholds catch treatable conditions earlier. LANDING: both error costs are real — false positives medicalize normal life, false negatives abandon treatable suffering. Practical guardrails: the impairment clause, honest modest diagnoses (adjustment disorder, other-specified), and treating every diagnosis as revisable.",
    "type": "explain",
    "source_page": "wiki/concept-categorical-vs-dimensional.md",
    "topic": "diagnostic-inflation",
    "bloom_level": "evaluate"
  },
  {
    "id": "u6-synthesis-evaluate-01",
    "prompt": "'Diagnose categorically; think dimensionally.' Unpack what each half means in practice, and why the field keeps the categorical DSM despite the evidence against categories.",
    "answer": "DIAGNOSE CATEGORICALLY: the system runs on categories — shared clinical shorthand, research entry criteria, billable ICD codes, and sometimes real relief for the client (a name that converts 'I'm broken' into 'this is a known, treatable thing'). THINK DIMENSIONALLY: hold severity as a dial, expect comorbidity to be one underlying picture, expect same-label clients to differ, and treat thresholds as drawn lines. Why the DSM survives: usability — the dimensional models' own proponents list the barriers (assessment burden, no validated cutoffs, no reimbursement pathway, no outcome evidence yet). The synthesis IS the syllabus line: diagnosis as shorthand, not verdict.",
    "type": "explain",
    "source_page": "wiki/concept-categorical-vs-dimensional.md",
    "topic": "categorical-vs-dimensional",
    "bloom_level": "evaluate"
  }
]
```

## Differential vignettes — the cross-category discrimination set

```json
[
  {
    "id": "u6-diff-grief-mcq-01",
    "prompt": "Six weeks after her husband's death, a client cries daily and aches for him — but laughs at a memory mid-session, says friends' visits genuinely help, and doesn't feel worthless, just heartbroken. Best reading?",
    "options": [
      "Grief within the normal range — waves, consolability, preserved self-esteem; support, don't diagnose",
      "Major depressive disorder — low mood and crying past two weeks",
      "Prolonged grief disorder — the grief is intense and daily",
      "Adjustment disorder with depressed mood — identifiable stressor"
    ],
    "correct": "Grief within the normal range — waves, consolability, preserved self-esteem; support, don't diagnose",
    "answer": "The qualitative markers all say grief: pain in WAVES with positive memories between, CONSOLABLE by connection, self-esteem PRESERVED, oriented to the loss not the self. The bereavement exclusion's removal means MDD *may* be diagnosed post-loss — not that it *should* be by default. PGD isn't available until 12 months. Over-pathologizing normal love-and-loss is this unit's signature error.",
    "type": "mcq",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "grief-vs-depression",
    "cluster": "differential-vignettes",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-diff-ocdgad-mcq-01",
    "prompt": "Client A spends two hours nightly reviewing whether he might have offended coworkers, and must mentally replay each conversation exactly three times to feel 'clean.' Client B lies awake worrying about money, then her son's grades, then her health. Which is which?",
    "options": [
      "A: OCD (intrusive doubt + ritualized mental compulsion); B: GAD (migrating real-life worry)",
      "A: GAD (worry about relationships); B: OCD (multiple obsessions)",
      "Both OCD — repetitive nighttime cognition",
      "Both GAD — anxiety with different content"
    ],
    "correct": "A: OCD (intrusive doubt + ritualized mental compulsion); B: GAD (migrating real-life worry)",
    "answer": "A has an OBSESSION (intrusive doubt with signature content) answered by a COMPULSION with rigid rules (exactly three mental replays) — compulsions can be invisible. B has GAD's free-floating, topic-HOPPING worry about plausible life concerns, with no ritual. Worry drifts; obsessions repeat and demand ritual payment.",
    "type": "mcq",
    "source_page": "wiki/concept-ocd.md",
    "topic": "ocd-vs-gad",
    "cluster": "differential-vignettes",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-diff-panicphobia-mcq-01",
    "prompt": "A client has had six severe panic attacks this year — every one within moments of encountering a large dog, which she now crosses streets to avoid. No attacks otherwise. Diagnosis territory?",
    "options": [
      "Specific phobia (animal type) — the attacks are cued, not unexpected",
      "Panic disorder — six attacks with avoidance behavior",
      "Agoraphobia — street-level avoidance",
      "GAD — persistent anxiety about encounters"
    ],
    "correct": "Specific phobia (animal type) — the attacks are cued, not unexpected",
    "answer": "Panic attacks in the presence of a circumscribed cue belong to the disorder that owns the cue — here, specific phobia. Panic DISORDER requires recurrent UNEXPECTED attacks plus a month of fear-of-the-fear. The attack is a symptom; ask what fired it.",
    "type": "mcq",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "expected-vs-unexpected",
    "cluster": "differential-vignettes",
    "bloom_level": "apply"
  },
  {
    "id": "u6-diff-ptsdadjust-mcq-01",
    "prompt": "Since a bitter divorce four months ago, a client has intrusive angry memories of the marriage, avoids their old neighborhood, sleeps poorly, and calls themself a failure. They ask: 'Is this PTSD?' Best answer?",
    "options": [
      "No — a divorce isn't a Criterion-A stressor; this maps to adjustment disorder (or depression if criteria fill in)",
      "Yes — intrusion, avoidance, negative cognitions, and arousal are all present",
      "Yes, delayed-expression PTSD, since symptoms persist past a month",
      "No — it's acute stress disorder until six months post-event"
    ],
    "correct": "No — a divorce isn't a Criterion-A stressor; this maps to adjustment disorder (or depression if criteria fill in)",
    "answer": "The symptom picture can rhyme with all four PTSD clusters, but Criterion A is a GATE: actual/threatened death, serious injury, or sexual violence. Divorce — however devastating — routes to adjustment disorder (any stressor, within 3 months) or a depressive diagnosis if criteria are met. Severity isn't the PTSD line; the stressor type is. (Validate the suffering while declining the label — accuracy and empathy aren't rivals.)",
    "type": "mcq",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "ptsd-vs-adjustment",
    "cluster": "differential-vignettes",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-diff-flash-compare-01",
    "prompt": "A combat veteran 'sees the convoy again' when a truck backfires; a client with schizophrenia hears a voice narrating her actions. Both report 'seeing/hearing things.' Contrast flashback and hallucination — origin, content, and chapter.",
    "answer": "FLASHBACK: a dissociative RE-EXPERIENCING of a real past event, typically cue-triggered, with the person transiently losing present-moment awareness — an intrusion symptom (trauma chapter). HALLUCINATION: a perception WITHOUT any external source or past-event referent, not tied to trauma cues — a positive psychotic symptom. One replays memory; the other manufactures perception. The distinction routes the whole workup (PTSD vs psychotic spectrum), and mislabeling a flashback as psychosis badly misdirects treatment.",
    "type": "compare",
    "source_page": "wiki/concept-trauma-stressor-disorders.md",
    "topic": "flashback-vs-hallucination",
    "cluster": "differential-vignettes",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-diff-maniaadhd-mcq-01",
    "prompt": "Two adults report distractibility, restlessness, and talking fast. Omar has been this way since grade school, in every job and relationship. Priya is normally measured — this started ten days ago, along with 3-hour nights that leave her energized and a plan to remortgage the house for a 'can't-fail' venture. Which is which?",
    "options": [
      "Omar: ADHD (lifelong trait pattern); Priya: manic episode (acute change with decreased need for sleep)",
      "Omar: manic episode; Priya: ADHD",
      "Both ADHD — adult presentations differ",
      "Both mania — distractibility plus pressured speech"
    ],
    "correct": "Omar: ADHD (lifelong trait pattern); Priya: manic episode (acute change with decreased need for sleep)",
    "answer": "Shared surface (distractibility, restlessness, talkativeness), opposite time signatures: ADHD is a LIFELONG, cross-context developmental pattern (onset before 12); mania is an EPISODE — a marked change from baseline with the tells ADHD never has: decreased NEED for sleep (rested on 3 hours), grandiosity, high-risk plans. Priya needs urgent psychiatric involvement, not a planner app.",
    "type": "mcq",
    "source_page": "wiki/concept-mood-disorders.md",
    "topic": "mania-vs-adhd",
    "cluster": "differential-vignettes",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-diff-bpdbipolar-mcq-01",
    "prompt": "A client describes 'mood swings': fine at breakfast, despairing by noon after a curt text from her partner, enraged by evening, fine again after they reconcile — a pattern running years, with frantic fear of being left and impulsive self-harm at the worst moments. Which frame fits?",
    "options": [
      "Borderline personality pattern — hours-scale, interpersonally triggered instability with abandonment fear",
      "Bipolar II — recurrent mood elevation and depression",
      "Cyclothymic disorder — chronic alternating mood symptoms",
      "Bipolar I, rapid cycling — multiple mood states in one day"
    ],
    "correct": "Borderline personality pattern — hours-scale, interpersonally triggered instability with abandonment fear",
    "answer": "The discriminators: TIMESCALE (hours, not the days-to-weeks of bipolar episodes — even 'rapid cycling' means 4+ episodes/year, not 4 moods/day), TRIGGER (interpersonal events, especially abandonment cues, vs episodes that arrive with changed sleep/energy), and the PATTERN's chronicity (a stable instability since adolescence). Bipolar episodes also change vegetative signs (sleep need, energy); borderline shifts are affective weather around attachment. Frequently confused, differently treated (DBT vs mood stabilization).",
    "type": "mcq",
    "source_page": "wiki/concept-personality-disorders.md",
    "topic": "borderline-vs-bipolar",
    "cluster": "differential-vignettes",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-diff-asdsocial-mcq-01",
    "prompt": "Two college students avoid parties. Lena reads social cues fluently and desperately wants to go, but is certain she'll say something humiliating and be judged. Marcus has never quite followed the rhythm of group conversation, finds eye contact effortful, has one intense interest, and has been this way since childhood. Which is which?",
    "options": [
      "Lena: social anxiety disorder (intact social machinery + fear of evaluation); Marcus: possible ASD (lifelong social-communication differences)",
      "Lena: possible ASD; Marcus: social anxiety disorder",
      "Both social anxiety disorder — avoidance is shared",
      "Both ASD — party avoidance suggests the spectrum"
    ],
    "correct": "Lena: social anxiety disorder (intact social machinery + fear of evaluation); Marcus: possible ASD (lifelong social-communication differences)",
    "answer": "Social anxiety = intact social UNDERSTANDING plus fear of scrutiny (wants connection, fears judgment). ASD = differences in the social-communication machinery itself (reciprocity, nonverbal signals) from early development, plus restricted/repetitive features. Both can co-occur — and autistic adults often develop secondary social anxiety from accumulated rejection — but the childhood-onset machinery question is the discriminator. Marcus warrants referral for formal evaluation, not an exposure hierarchy.",
    "type": "mcq",
    "source_page": "wiki/concept-neurodevelopmental-disorders.md",
    "topic": "asd-vs-social-anxiety",
    "cluster": "differential-vignettes",
    "bloom_level": "analyze"
  },
  {
    "id": "u6-diff-substance-mcq-01",
    "prompt": "A 24-year-old is brought in paranoid and hallucinating after three days awake on methamphetamine; symptoms largely clear within two weeks of abstinence. What keeps this from being schizophrenia, and what's the diagnostic frame?",
    "options": [
      "Substance/medication-induced psychotic disorder — psychosis during intoxication/withdrawal that remits with abstinence",
      "Brief psychotic disorder — psychosis under one month",
      "Schizophreniform disorder — provisional, pending six months",
      "Schizophrenia — hallucinations plus paranoia suffice"
    ],
    "correct": "Substance/medication-induced psychotic disorder — psychosis during intoxication/withdrawal that remits with abstinence",
    "answer": "Psychosis with onset during intoxication/withdrawal from a known psychotogenic substance, remitting with sustained abstinence = substance-induced, not primary. This is why the substance history precedes every diagnosis in this unit — stimulant psychosis, alcohol-withdrawal anxiety, and depressant-induced depression all mimic primary disorders. (If psychosis persists well beyond abstinence, reopen the primary-psychosis question.)",
    "type": "mcq",
    "source_page": "wiki/concept-substance-use-disorders.md",
    "topic": "substance-induced",
    "cluster": "differential-vignettes",
    "bloom_level": "apply"
  },
  {
    "id": "u6-diff-medical-mcq-01",
    "prompt": "A client presents with new anxiety, restlessness, palpitations, sweating, and weight loss despite normal appetite. Before any DSM anxiety diagnosis, what must happen?",
    "options": [
      "Medical rule-out — this picture matches hyperthyroidism (and stimulant/caffeine effects) as well as it matches GAD",
      "Begin GAD criteria count — the symptom set matches",
      "Screen for panic disorder — palpitations suggest attacks",
      "Start relaxation training while monitoring"
    ],
    "correct": "Medical rule-out — this picture matches hyperthyroidism (and stimulant/caffeine effects) as well as it matches GAD",
    "answer": "Nearly every criteria set carries the clause 'not attributable to a substance or another medical condition' — and this vignette is the classic reason: hyperthyroidism produces anxiety, palpitations, sweating, and weight loss. Weight loss WITH normal appetite is the medical red flag. Counselors don't run labs, but they must know when to insist on a medical workup before a psychological label sticks (coordinated care, scope of practice).",
    "type": "mcq",
    "source_page": "wiki/concept-anxiety-disorders.md",
    "topic": "medical-rule-out",
    "cluster": "differential-vignettes",
    "bloom_level": "apply"
  }
]
```
