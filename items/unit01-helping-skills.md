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
    "source_page": "wiki/concept-unconditional-positive-regard.md",
    "topic": "upr",
    "cluster": "rogers-conditions",
    "bloom_level": "understand"
  },
  {
    "id": "u1-upr-apply-01",
    "prompt": "A client admits they relapsed and immediately braces for you to be disappointed. You respond in a way that conveys they still matter to you fully, without approving of the relapse. Which condition is this, and what is the discipline it requires?",
    "answer": "Unconditional positive regard. The discipline is keeping the client's worth non-contingent on their behavior — not endorsing the relapse, but refusing to let it change how you value them as a person.",
    "type": "vignette",
    "source_page": "wiki/concept-unconditional-positive-regard.md",
    "topic": "upr",
    "cluster": "rogers-conditions",
    "bloom_level": "apply"
  },
  {
    "id": "u1-empathy-analyze-01",
    "prompt": "Distinguish empathy from sympathy and from interpretation, using one short client-facing example of each.",
    "answer": "Empathy = understanding from inside the client's frame and conveying it ('It sounds like that left you frightened'). Sympathy = feeling for them from outside ('I'm so sorry that happened to you'). Interpretation = adding your own explanation of cause/meaning ('I think you get frightened because it echoes your childhood'). Empathy stays in their frame; sympathy distances; interpretation leaves their frame.",
    "type": "compare",
    "source_page": "wiki/concept-empathy.md",
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
  },
  {
    "id": "u1-upr-conditionsofworth-understand-01",
    "prompt": "In Rogers' theory, how do 'conditions of worth' form, and why is unconditional positive regard the antidote?",
    "answer": "When significant others give conditional positive regard ('you're valued WHEN you achieve/are quiet/agree'), the person internalizes those terms as conditions of worth and starts valuing their own experience by others' criteria instead of their own organismic valuing process. That creates incongruence between the self-concept and actual experience — the root of distress. UPR reverses it: regard with no conditions attached lets the client stop performing for worth and re-contact their own experience.",
    "type": "explain",
    "source_page": "wiki/concept-unconditional-positive-regard.md",
    "topic": "conditions-of-worth",
    "cluster": "rogers-conditions",
    "bloom_level": "understand"
  },
  {
    "id": "u1-upr-compare-01",
    "prompt": "Distinguish unconditional positive regard from its three most common look-alikes — approval, agreement, and liking/niceness — and give the single discipline that separates UPR from all three.",
    "answer": "APPROVAL endorses the behavior; UPR prizes the person while staying honest a choice is harmful. AGREEMENT accepts the client's views as correct; UPR values their worth even when you disagree or name a hard reality. LIKING/NICENESS is a feeling of fondness or a policy of being pleasant; UPR is a stance toward fundamental worth you can hold even for a client you find difficult or must set a firm limit with. The one discipline behind all three: keep the client's worth NON-CONTINGENT — the moment it becomes 'I value you because you did/agreed/stopped,' it isn't unconditional.",
    "type": "compare",
    "source_page": "wiki/concept-unconditional-positive-regard.md",
    "topic": "upr",
    "cluster": "rogers-conditions",
    "bloom_level": "analyze"
  },
  {
    "id": "u1-carkhuff-cloze-01",
    "prompt": "On Carkhuff's five-level empathy scale, a response that reflects the client's expressed content and feeling exactly — no more, no less — is a Level {{3}} (interchangeable) response, the minimum for effective helping.",
    "answer": "3",
    "type": "cloze",
    "source_page": "wiki/concept-empathy.md",
    "topic": "carkhuff-levels",
    "cluster": "rogers-conditions",
    "bloom_level": "remember"
  },
  {
    "id": "u1-carkhuff-apply-01",
    "prompt": "Client: 'I finally told my dad how I felt, and he just changed the subject.' Counselor: 'That sounds like it really stung — like you took a big risk and he left you hanging, and maybe underneath there's some old hurt about never quite reaching him.' On Carkhuff's scale, which level is this?",
    "answer": "Level 4 (additive)",
    "options": [
      "Level 1 (non-empathic)",
      "Level 2 (subtractive)",
      "Level 3 (interchangeable)",
      "Level 4 (additive)"
    ],
    "correct": "Level 4 (additive)",
    "type": "mcq",
    "source_page": "wiki/concept-empathy.md",
    "topic": "carkhuff-levels",
    "cluster": "rogers-conditions",
    "bloom_level": "apply"
  },
  {
    "id": "u1-empathy-additive-analyze-01",
    "prompt": "Additive empathy (Carkhuff Level 4-5) and interpretation both go BEYOND what the client literally said. What keeps additive empathy a core condition while interpretation is a higher-risk influencing skill?",
    "answer": "Additive empathy names what is IMPLICITLY PRESENT in the client's own experience — the feeling they were reaching for but hadn't quite said — so it stays inside their frame. Interpretation imports an explanation of cause or meaning from OUTSIDE the client's frame (the counselor's theory of why). Additive empathy deepens the client's own account; interpretation adds the counselor's. That's why the first is still empathy and the second, if premature, feels presumptuous.",
    "type": "explain",
    "source_page": "wiki/concept-empathy.md",
    "topic": "empathy",
    "cluster": "rogers-conditions",
    "bloom_level": "analyze"
  },
  {
    "id": "u1-congruence-selfdisclosure-vignette-01",
    "prompt": "STANCE DRILL. A grieving client pauses and you feel an urge to say 'I lost my mom last year too, it was the hardest thing I've been through.' Is this congruent self-disclosure or a misstep? What's the test?",
    "answer": "Potential misstep — the test is WHOSE need it serves. Genuineness is not 'say whatever you feel'; disclosure is appropriate only when it's brief, relevant, and FOR THE CLIENT'S benefit (to normalize or build the bond). Volunteering your own loss here risks shifting focus onto you — the same failure mode as sympathy. Congruent alternative: stay with their experience, and if you disclose at all, keep it minimal and hand the floor straight back ('I have some sense of how heavy this is — tell me what it's like for you').",
    "type": "vignette",
    "source_page": "wiki/concept-congruence.md",
    "topic": "self-disclosure",
    "cluster": "rogers-conditions",
    "bloom_level": "apply"
  },
  {
    "id": "u1-congruence-tension-evaluate-01",
    "prompt": "You notice you feel genuine judgment toward a client's choices. Congruence says be real; UPR says hold their worth non-contingently. How do you resolve the clash without violating either condition?",
    "answer": "Not by faking regard (incongruent) and not by unloading the judgment (unregarding). First work your own reaction — judgment is often YOUR material, addressed in supervision. Where relevant, voice it as immediacy in a way that keeps worth non-contingent: 'I notice I want to jump in and steer you when this comes up' is congruent AND preserves regard; 'you're being self-destructive and it's frustrating' is neither. Holding all three conditions at once is the actual skill — that's why they're taught together.",
    "type": "explain",
    "source_page": "wiki/concept-congruence.md",
    "topic": "congruence",
    "cluster": "rogers-conditions",
    "bloom_level": "evaluate"
  },
  {
    "id": "u1-rogers-actualizing-understand-01",
    "prompt": "Rogers' 'actualizing tendency' explains why the person-centered therapist doesn't have to DRIVE change. Explain the logic.",
    "answer": "Rogers held every organism has a single master motive — to maintain, grow, and fulfill itself (the actualizing tendency). Given the right relational conditions, clients move toward growth on their own. So the therapist's job isn't to push, diagnose, or engineer change but to REMOVE WHAT BLOCKS it — chiefly by lifting the conditions of worth through UPR, empathy, and congruence — and then trust the client's own tendency to do the work.",
    "type": "explain",
    "source_page": "wiki/person-carl-rogers.md",
    "topic": "actualizing-tendency",
    "cluster": "rogers-conditions",
    "bloom_level": "understand"
  },
  {
    "id": "u1-rogers-wisconsin-evaluate-01",
    "prompt": "Rogers' Wisconsin schizophrenia project (1967) is often cited when discussing whether the core conditions are 'sufficient.' What did it find, and what lesson did the field draw?",
    "answer": "It tested whether the core conditions would help hospitalized patients diagnosed with schizophrenia. Long read as a disappointment — the conditions did NOT produce the dramatic gains Rogers hoped for, and the project was marred by an internal data dispute — though it showed modest benefit, especially with patients more 'in contact.' The lesson: it's a large part of why the field came to treat the conditions as NECESSARY BUT NOT SUFFICIENT rather than a cure-all. Told honestly, it's a landmark that tempered the 'sufficient' claim, not a clean failure.",
    "type": "explain",
    "source_page": "wiki/person-carl-rogers.md",
    "topic": "wisconsin-project",
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
  },
  {
    "id": "u1-soler-cloze-01",
    "prompt": "Egan's acronym for nonverbal attending behavior is SOLER: face {{Squarely}}, Open posture, Lean in, Eye contact, Relax.",
    "answer": "Squarely",
    "type": "cloze",
    "source_page": "wiki/concept-attending-and-listening.md",
    "topic": "soler",
    "cluster": "microskill-types",
    "bloom_level": "remember"
  },
  {
    "id": "u1-silence-apply-01",
    "prompt": "STANCE DRILL. A client falls silent after saying something painful, eyes down, clearly still processing. You feel the urge to fill the gap. What should you do, and why?",
    "answer": "Hold the silence — don't fill it. Productive silence gives the client room to access the feeling, reach for a word, or finish a thought instead of being interrupted; it's most useful exactly here, mid-emotion and after a solid alliance. The trained move is to resist the reflex to speak (count if you have to) and let the client break the silence. Rushing in interrupts their process and re-centers you.",
    "type": "vignette",
    "source_page": "wiki/concept-attending-and-listening.md",
    "topic": "silence",
    "cluster": "microskill-types",
    "bloom_level": "apply"
  },
  {
    "id": "u1-attending-cultural-analyze-01",
    "prompt": "A client keeps their gaze down and avoids eye contact throughout the session. Why is 'the client is being evasive/resistant' a risky read, and what does good attending require here?",
    "answer": "SOLER and the 'three Vs' encode dominant US-white norms; sustained direct eye contact reads as respectful there but as rude, intrusive, or aggressive in many cultures, where a downcast gaze is appropriate deference — not evasion. Reading it as resistance imposes your cultural frame. Good attending means CALIBRATING these behaviors (eye contact, distance, silence) to the person in front of you rather than applying SOLER by rote — which is where the multicultural material picks up.",
    "type": "vignette",
    "source_page": "wiki/concept-attending-and-listening.md",
    "topic": "attending-cultural",
    "cluster": "microskill-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u1-observation-vignette-01",
    "prompt": "A client says 'No really, I'm totally fine with the divorce' while their jaw tightens and their voice drops. Which microskill is called for, and how would you use it without leaving their frame?",
    "answer": "Observation — noticing the mismatch between words ('fine') and nonverbals (tight jaw, dropped voice). Use it by gently naming the incongruence and inviting rather than interpreting: 'You say you're fine with it, and I also noticed your voice changed just then — what's that like?' That stays in the client's frame (an attending/observation move), unlike an interpretation that would assert why they're not fine.",
    "type": "vignette",
    "source_page": "wiki/concept-attending-and-listening.md",
    "topic": "observation",
    "cluster": "microskill-types",
    "bloom_level": "apply"
  },
  {
    "id": "u1-fivestage-recall-01",
    "prompt": "Name Ivey's five-stage interview structure in order, and state the discipline the ordering encodes.",
    "answer": "1) Empathic relationship (rapport + structure); 2) Story and strengths (draw out the concern AND the client's resources); 3) Goals (what does the client want?); 4) Restory (generate new ways of seeing it); 5) Action (change carried outside the room). The discipline: relationship and story come BEFORE goals and action — the same 'don't jump to the fix' stance, built into the shape of the session.",
    "type": "recall",
    "source_page": "wiki/concept-microskills-hierarchy.md",
    "topic": "five-stage-interview",
    "cluster": "microskill-types",
    "bloom_level": "understand"
  },
  {
    "id": "u1-reflecting-compare-01",
    "prompt": "Compare the three reflecting skills — paraphrase, reflection of feeling, and summarizing — on what each targets and when you'd reach for it. All three stay inside the client's frame; what distinguishes them?",
    "answer": "PARAPHRASE (reflect content) restates the CONTENT of what they said in fresh words — mirrors meaning, adds nothing new; use it to show you're tracking. REFLECTION OF FEELING names the EMOTION underneath, matched to intensity — surfaces what's implicit but present; use it to deepen and to help the client feel gotten (requires a wide feeling vocabulary). SUMMARIZING is the BROADEST — condenses several paraphrases/reflections across a stretch of talk; use it at the start or end of a session or to tie threads together. All three stay in-frame (unlike interpretation); they differ in what they target (content vs. feeling vs. the whole) and scope (narrow vs. narrow vs. wide).",
    "type": "compare",
    "source_page": "wiki/concept-microskills-hierarchy.md",
    "topic": "reflection-types",
    "cluster": "microskill-types",
    "bloom_level": "analyze"
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
  },
  {
    "id": "u1-alliance-compare-01",
    "prompt": "Compare Bordin's three alliance components — bond, goal, task — by pairing each with the rupture that signals it's the weak link. Then say why 'just build more rapport' is the wrong fix for two of the three.",
    "answer": "BOND = the affective relationship (trust, liking, feeling like a team). Rupture: guardedness, coldness, feeling unseen or judged — this is the one rapport actually repairs. GOAL = agreement on what you're working toward. Rupture: you and the client are pulling toward different destinations (they want symptom relief, you're chasing insight); the fix is renegotiating the target, not more warmth. TASK = agreement on the activities and each person's role, and belief they'll help. Rupture: polite compliance but skipped homework or lukewarm buy-in; the fix is revisiting whether the client believes the method works. Why 'more rapport' misfires: the bond can be perfectly warm while goal or task is frayed — the three are somewhat independent, so working harder to be liked leaves the real disagreement untouched and the therapy still stalls.",
    "type": "compare",
    "source_page": "wiki/concept-therapeutic-alliance.md",
    "topic": "alliance",
    "cluster": "alliance-components",
    "bloom_level": "analyze"
  },
  {
    "id": "u1-rupture-type-mcq-01",
    "prompt": "Mid-therapy, a client who used to talk freely now gives short answers, agrees with everything you say, and keeps changing the subject away from the hard topic. Which type of alliance rupture is this?",
    "answer": "A withdrawal rupture",
    "options": [
      "A confrontation rupture",
      "A withdrawal rupture",
      "Not a rupture — just a quiet session",
      "A goal-consensus rupture"
    ],
    "correct": "A withdrawal rupture",
    "type": "mcq",
    "source_page": "wiki/concept-therapeutic-alliance.md",
    "topic": "alliance-ruptures",
    "cluster": "alliance-components",
    "bloom_level": "apply"
  },
  {
    "id": "u1-rupture-repair-analyze-01",
    "prompt": "A supervisee says 'my client got angry at me last session — I clearly failed.' Using the rupture-repair evidence, reframe this, and name the skill for repairing it.",
    "answer": "A rupture (here a confrontation rupture — the client moving against) is routine, not proof of failure; what matters is the repair. Eubanks, Muran & Safran's 2018 meta-analysis links successful rupture repair to better outcomes (r ≈ .29), and Safran & Muran raised the possibility that living through a REPAIRED rupture can help a client more than an alliance that never ruptured — it models that conflict in a relationship can be survived. The repair skill is immediacy: gently name what happened between you and, where it was your misstep, own it. The real risk is an UNrepaired rupture, a leading path to dropout.",
    "type": "explain",
    "source_page": "wiki/concept-therapeutic-alliance.md",
    "topic": "alliance-ruptures",
    "cluster": "alliance-components",
    "bloom_level": "analyze"
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
  },
  {
    "id": "u1-commonfactors-compare-01",
    "prompt": "Contrast the common-factors / contextual-model account of why therapy works with the specific-ingredients ('medical') model: what does each say is doing the work, what evidence does each lean on, and where does the honest synthesis land?",
    "answer": "COMMON-FACTORS / CONTEXTUAL (Wampold): the work is mostly done by factors SHARED across schools — the relationship/alliance, the client's hope and expectation, and a cogent rationale plus credible actions the client believes in. Evidence: the alliance–outcome correlation (r ≈ .28, Flückiger 2018) holds across orientations, and outcome differences between bona fide therapies are small (the 'dodo bird verdict'). SPECIFIC-INGREDIENTS / MEDICAL model: the distinctive technique of a given therapy (e.g. exposure for a phobia) is the active drug, so treatments should differ in effect for specific conditions. Evidence: specific treatments do beat control conditions, and some disorders respond better to particular methods. SYNTHESIS: not either/or — technique and relationship are interdependent; the technique works THROUGH the relationship, giving client and clinician something credible to do together. Both 'relationship beats technique' and 'all therapies are equivalent' overshoot the data.",
    "type": "compare",
    "source_page": "wiki/theory-common-factors.md",
    "topic": "common-factors",
    "cluster": "common-factors",
    "bloom_level": "analyze"
  },
  {
    "id": "u1-dodobird-understand-01",
    "prompt": "What is the 'dodo bird verdict,' who first named it (and when), and what does it claim?",
    "answer": "It's the claim that different bona fide therapies produce roughly EQUIVALENT outcomes — that no school is clearly superior. Saul Rosenzweig coined the idea in 1936 (the paper that also coined 'common factors'), borrowing the Dodo's line from Alice in Wonderland: 'Everybody has won, and all must have prizes.' The point: if outcomes are similar across very different techniques, much of what heals must be shared FACTORS rather than any school's specific method.",
    "type": "recall",
    "source_page": "wiki/theory-common-factors.md",
    "topic": "dodo-bird",
    "cluster": "common-factors",
    "bloom_level": "understand"
  },
  {
    "id": "u1-frank-recall-01",
    "prompt": "In Frank & Frank's 'Persuasion and Healing,' clients arrive in what state, and what four features do all effective healing approaches share?",
    "answer": "Clients arrive DEMORALIZED (helpless, isolated, stuck). The four shared features: (1) an emotionally charged, confiding relationship; (2) a healing setting; (3) a rationale or myth that explains the suffering; (4) a ritual or procedure both parties believe in. On this view technique matters largely because it supplies a credible ritual and rationale that restore the client's expectation of help.",
    "type": "recall",
    "source_page": "wiki/theory-common-factors.md",
    "topic": "frank-shared-components",
    "cluster": "common-factors",
    "bloom_level": "remember"
  }
]
```
