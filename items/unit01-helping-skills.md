# Unit 1 items — Helping Skills & the Therapeutic Relationship

Source of truth for Unit 1 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. Items span Bloom levels and lean toward
**application/stance** per this unit's emphasis. Clusters: `rogers-conditions`, `microskill-types`,
`alliance-components`, `common-factors`. See generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## Cluster: rogers-conditions

```json
[
  {
    "id": "u1-coreconditions-cloze-01",
    "prompt": "Rogers' three core conditions are unconditional positive regard, {{empathy}}, and congruence.",
    "answer": "empathy",
    "type": "cloze",
    "source_page": "wiki/concept-core-conditions.md",
    "topic": "core-conditions",
    "cluster": "rogers-conditions",
    "bloom_level": "remember"
  },
  {
    "id": "u1-upr-understand-01",
    "prompt": "Why is unconditional positive regard NOT the same as approving of or agreeing with what the client does?",
    "answer": "UPR prizes the person's worth independent of their behavior. You keep their worth non-contingent while still being honest that a choice may be harmful. Approval/agreement makes regard conditional on doing the 'right' thing.",
    "type": "explain",
    "source_page": "wiki/concept-core-conditions.md",
    "topic": "upr",
    "cluster": "rogers-conditions",
    "bloom_level": "understand"
  },
  {
    "id": "u1-upr-apply-01",
    "prompt": "A client admits they relapsed and immediately braces for you to be disappointed. You respond in a way that conveys they still matter to you fully, without approving of the relapse. Which condition is this, and what is the discipline it requires?",
    "answer": "Unconditional positive regard. The discipline is keeping the client's worth non-contingent on their behavior — not endorsing the relapse, but refusing to let it change how you value them as a person.",
    "type": "vignette",
    "source_page": "wiki/concept-core-conditions.md",
    "topic": "upr",
    "cluster": "rogers-conditions",
    "bloom_level": "apply"
  },
  {
    "id": "u1-empathy-analyze-01",
    "prompt": "Distinguish empathy from sympathy and from interpretation, using one short client-facing example of each.",
    "answer": "Empathy = understanding from inside the client's frame and conveying it ('It sounds like that left you frightened'). Sympathy = feeling for them from outside ('I'm so sorry that happened to you'). Interpretation = adding your own explanation of cause/meaning ('I think you get frightened because it echoes your childhood'). Empathy stays in their frame; sympathy distances; interpretation leaves their frame.",
    "type": "compare",
    "source_page": "wiki/concept-core-conditions.md",
    "topic": "empathy",
    "cluster": "rogers-conditions",
    "bloom_level": "analyze"
  },
  {
    "id": "u1-coreconditions-evaluate-01",
    "prompt": "Rogers claimed his conditions were 'necessary AND sufficient' for change. What is the mainstream critique of the 'sufficient' part?",
    "answer": "Most clinicians accept the conditions as necessary but NOT sufficient: warmth, empathy, and genuineness are vital ground but most clients also need active methods on top. Critics add that the principles can be too vague to operationalize and the efficacy evidence is mixed (e.g., possibly inferior to CBT for depression at 12 months).",
    "type": "explain",
    "source_page": "wiki/concept-core-conditions.md",
    "topic": "core-conditions",
    "cluster": "rogers-conditions",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: microskill-types

```json
[
  {
    "id": "u1-attending-cloze-01",
    "prompt": "In Ivey's hierarchy, the foundational physical skill of being present — eye contact, vocal quality, verbal tracking, and open body language — is called {{attending behavior}}.",
    "answer": "attending behavior",
    "type": "cloze",
    "source_page": "wiki/concept-microskills-hierarchy.md",
    "topic": "attending",
    "cluster": "microskill-types",
    "bloom_level": "remember"
  },
  {
    "id": "u1-microskills-recall-01",
    "prompt": "List Ivey's microskills hierarchy from base to top (the major levels).",
    "answer": "1) Foundation: core conditions + ethics + cultural competence. 2) Attending behavior. 3) Observation skills. 4) Open/closed questions. 5) Reflecting skills (paraphrase, reflection of feeling, summarizing). 6) Influencing skills (interpretation, self-disclosure, confrontation). Master lower before higher.",
    "type": "recall",
    "source_page": "wiki/concept-microskills-hierarchy.md",
    "topic": "microskills",
    "cluster": "microskill-types",
    "bloom_level": "understand"
  },
  {
    "id": "u1-reflect-analyze-01",
    "prompt": "A client says: 'My sister keeps making plans for me without asking.' Write (a) a paraphrase, (b) a reflection of feeling, and (c) an interpretation. Then say which one leaves the client's frame and why that makes it higher-risk.",
    "answer": "(a) Paraphrase: 'So she arranges things for you without checking first.' (b) Reflection of feeling: 'It sounds like that leaves you frustrated — maybe a bit dismissed.' (c) Interpretation: 'I wonder if you let it slide because saying no to family feels dangerous.' The interpretation leaves the client's frame (adds your explanation), so it's an influencing skill — powerful but presumptuous if premature; earn it with the lower skills first.",
    "type": "vignette",
    "source_page": "wiki/concept-microskills-hierarchy.md",
    "topic": "reflection-types",
    "cluster": "microskill-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u1-reflect-apply-01",
    "prompt": "Classify this counselor response. Client: 'I bombed the interview, I always do this.' Counselor: 'You're feeling pretty defeated, and like this is a pattern you can't break.' Is it a paraphrase, reflection of feeling, or interpretation?",
    "answer": "Reflection of feeling. It names the emotion ('defeated') the client implied, staying inside their frame. It is not a bare content paraphrase, and it doesn't add an outside causal explanation (which would make it interpretation).",
    "type": "vignette",
    "source_page": "wiki/concept-microskills-hierarchy.md",
    "topic": "reflection-types",
    "cluster": "microskill-types",
    "bloom_level": "apply"
  },
  {
    "id": "u1-stance-apply-01",
    "prompt": "STANCE DRILL. A client describes a scheduling mess at work and you feel the urge to suggest a fix. Per this unit, what should you do instead, and why?",
    "answer": "Default down the ladder to a reflection of content or feeling, then go quiet. A reflection invites the client to say more and feel understood; a solution interrupts that and steers them to your agenda. Noticing the fix-it urge and choosing the reflection IS the skill being trained here.",
    "type": "vignette",
    "source_page": "wiki/concept-microskills-hierarchy.md",
    "topic": "stance",
    "cluster": "microskill-types",
    "bloom_level": "apply"
  },
  {
    "id": "u1-stance-evaluate-01",
    "prompt": "Why is the 'find the problem and fix it' reflex (familiar from technical work) often counterproductive in an early counseling session?",
    "answer": "Most early-session work is helping the person feel understood; a premature solution interrupts that, signals you weren't really listening, and imposes your frame. It also skips the bond-building (attending, empathy, reflection) that the relationship — a primary active ingredient — depends on. The fix can wait; being understood usually can't.",
    "type": "explain",
    "source_page": "wiki/unit01-helping-skills.md",
    "topic": "stance",
    "cluster": "microskill-types",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: alliance-components

```json
[
  {
    "id": "u1-bordin-cloze-01",
    "prompt": "Bordin's three transtheoretical components of the working alliance are bond, goal, and {{task}}.",
    "answer": "task",
    "type": "cloze",
    "source_page": "wiki/concept-therapeutic-alliance.md",
    "topic": "alliance",
    "cluster": "alliance-components",
    "bloom_level": "remember"
  },
  {
    "id": "u1-bordin-apply-01",
    "prompt": "Six sessions in, rapport feels warm but the client keeps not doing the agreed between-session exercises and seems lukewarm about them. Using Bordin's model, which component is most likely frayed, and what does that suggest?",
    "answer": "The TASK component (and possibly GOAL), not the bond. Warm rapport = intact bond, but disagreement or disbelief about the in-session/between-session activities stalls therapy. The repair is to revisit whether the client agrees the tasks will help and whether they share the goal — not to push harder on the bond.",
    "type": "vignette",
    "source_page": "wiki/concept-therapeutic-alliance.md",
    "topic": "alliance",
    "cluster": "alliance-components",
    "bloom_level": "apply"
  },
  {
    "id": "u1-bordin-understand-01",
    "prompt": "According to Bordin, HOW does the alliance influence outcome — is the relationship itself the cure?",
    "answer": "No. Bordin held the alliance is not curative on its own; it's the ingredient that lets the client accept, follow, and believe in the treatment. The bond makes the work possible; the work does the changing.",
    "type": "explain",
    "source_page": "wiki/concept-therapeutic-alliance.md",
    "topic": "alliance",
    "cluster": "alliance-components",
    "bloom_level": "understand"
  }
]
```

## Cluster: common-factors

```json
[
  {
    "id": "u1-alliance-evidence-recall-01",
    "prompt": "Roughly what is the alliance–outcome correlation, and on what scale of evidence (studies/patients) does it rest?",
    "answer": "About r ≈ .28 (Flückiger et al., 2018), across ~295 studies and more than 30,000 patients, holding across treatment types — one of the most replicated associations in psychotherapy research.",
    "type": "recall",
    "source_page": "wiki/theory-common-factors.md",
    "topic": "common-factors",
    "cluster": "common-factors",
    "bloom_level": "remember"
  },
  {
    "id": "u1-commonfactors-evaluate-01",
    "prompt": "Critique the slogan 'the relationship beats technique.' Where does it overshoot the evidence?",
    "answer": "Two problems. (1) The alliance–outcome link is correlational — a strong alliance may cause improvement, or early improvement may strengthen the alliance, or both; it isn't proven one-directional. (2) The modern view is relationship and technique are interdependent: technique works THROUGH the relationship, not instead of it. Taken too far, the slogan slides into 'all therapies are equivalent,' which is stronger than the data — specific treatments do outperform controls for specific conditions.",
    "type": "explain",
    "source_page": "wiki/theory-common-factors.md",
    "topic": "common-factors",
    "cluster": "common-factors",
    "bloom_level": "evaluate"
  },
  {
    "id": "u1-contextual-understand-01",
    "prompt": "Name the three pathways in Wampold's Contextual Model by which a therapy helps.",
    "answer": "(1) A cogent rationale the client accepts; (2) a genuine therapeutic relationship with the clinician; (3) therapeutic actions the client expects will help. Techniques matter largely because they give client and clinician something credible to do together inside a working relationship.",
    "type": "recall",
    "source_page": "wiki/theory-common-factors.md",
    "topic": "common-factors",
    "cluster": "common-factors",
    "bloom_level": "understand"
  }
]
```
