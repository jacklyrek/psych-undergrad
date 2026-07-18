# Unit 5 items — Human Development Across the Lifespan

Source of truth for Unit 5 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This unit's signature reps: **which-attachment-style
vignettes** (cluster `attachment-styles` — the prime interleaving/discrimination set, incl. the
avoidant-vs-resistant *deactivation/hyperactivation* contrast and disorganized-as-risk),
**which-Erikson-stage** and **which-Piaget-stage** discrimination (clusters `erikson-stages`,
`piaget-stages`), **which-theorist** cross-framework items (cluster `developmental-theorists`),
biopsychosocial case formulation, and stance probes on **risk-not-destiny / don't-type-the-client**
plus the syllabus practice rep (sketch your own attachment history + Erikson stage). See generate
rules in [`../CLAUDE.md`](../CLAUDE.md).

## Attachment: the theory and the mechanism (Bowlby & Ainsworth)

```json
[
  {
    "id": "u5-attach-secure-base-recall-01",
    "prompt": "Explain the twin concepts at 'the heart of attachment theory' — the secure base and the safe haven — and state the counterintuitive relationship between attachment security and exploration.",
    "answer": "A trusted caregiver is simultaneously a SECURE BASE the child explores FROM and a SAFE HAVEN the child returns TO when distressed. Counterintuitive part: security increases exploration rather than clinginess — a confidently attached child explores MORE, using the caregiver as a home base, because they trust the base will be there. (A counselor who is a secure base does the same: steadies the client enough to approach hard material.)",
    "type": "recall",
    "source_page": "wiki/theory-attachment.md",
    "topic": "secure-base",
    "bloom_level": "understand"
  },
  {
    "id": "u5-attach-iwm-cloze-01",
    "prompt": "Bowlby held that early attachment experiences build a mental template — the {{internal working model}} — of whether the self is worth caring for and whether others are reliable, which then shapes relationships for life largely outside awareness.",
    "answer": "internal working model",
    "type": "cloze",
    "source_page": "wiki/theory-attachment.md",
    "topic": "internal-working-models",
    "bloom_level": "remember"
  },
  {
    "id": "u5-attach-not-feeding-explain-01",
    "prompt": "Bowlby rejected the idea that a baby bonds to the mother because she feeds it. What evidence (from ethology) supported his view that attachment is a primary system, and why does this distinction matter clinically?",
    "answer": "Harlow's rhesus monkeys clung to a soft cloth surrogate that gave no food over a wire one that dispensed milk — contact comfort, not feeding, drove the bond (Lorenz's imprinting made the same 'evolved, not learned-via-reward' point). It matters clinically because it reframes the need for closeness as a basic survival system, not dependency or weakness to be trained out — so a client's bids for connection (including toward you) are read as normal attachment, not pathology.",
    "type": "explain",
    "source_page": "wiki/person-bowlby-ainsworth.md",
    "topic": "attachment-theory",
    "bloom_level": "understand"
  },
  {
    "id": "u5-attach-phases-recall-01",
    "prompt": "Name Bowlby's four phases of attachment development in order, and say which phase separation anxiety peaks in.",
    "answer": "1) Pre-attachment (birth–~6 wks: signals to any adult); 2) Attachment-in-the-making (~6 wks–6–8 mo: prefers familiar people); 3) Clear-cut attachment (~7–24 mo: specific primary figure — SEPARATION ANXIETY and stranger wariness PEAK here); 4) Reciprocal / goal-corrected partnership (24 mo+: grasps the caregiver has separate goals and will return).",
    "type": "recall",
    "source_page": "wiki/theory-attachment.md",
    "topic": "attachment-theory",
    "bloom_level": "remember"
  },
  {
    "id": "u5-attach-reunion-analyze-01",
    "prompt": "In the Strange Situation, two infants both cry hard when the mother leaves. Why can't you classify their attachment from that fact — and what moment actually determines the classification?",
    "answer": "Separation distress is not the diagnostic signal — plenty of secure and insecure infants protest separation. What classifies is the REUNION: how the baby USES the caregiver to recover. Secure infants seek comfort and are soothed, then return to play; avoidant infants ignore/avoid the returning caregiver; resistant infants seek contact but can't be settled by it. The tell is the recovery behavior, not the intensity of the protest.",
    "type": "explain",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "strange-situation",
    "bloom_level": "analyze"
  },
  {
    "id": "u5-attach-sensitivity-evaluate-01",
    "prompt": "Ainsworth's maternal-sensitivity hypothesis says sensitive, consistent responsiveness causes secure attachment. Give two findings that show this clean causal story is incomplete, and state the current interactionist position.",
    "answer": "(1) The measured sensitivity–security correlation is only MODEST (r ≈ .24) — sensitivity matters but is far from the whole cause. (2) The TRANSMISSION GAP: a parent's own state of mind (AAI) predicts the infant's classification BEYOND what observed sensitive behavior explains — something transmitted we can't see in the behavior. Add temperament (Kagan) as a rival driver. Current position (Belsky & Rovine): interactionist — temperament AND caregiving, interacting — not caregiving alone.",
    "type": "explain",
    "source_page": "wiki/theory-attachment.md",
    "topic": "transmission-gap",
    "bloom_level": "evaluate"
  },
  {
    "id": "u5-attach-aai-recall-01",
    "prompt": "What does the Adult Attachment Interview (AAI) assess, and how does that differ from a self-report 'attachment style' quiz?",
    "answer": "The AAI (George, Kaplan & Main) assesses an adult's current STATE OF MIND with respect to attachment, scored from the COHERENCE of their narrative about their own attachment history (secure-autonomous, dismissing, preoccupied, unresolved). A self-report style quiz (e.g., Hazan & Shaver) measures conscious beliefs about ROMANTIC relationships. The AAI taps something closer to the unconscious working model — and it's the AAI that revealed intergenerational transmission (and the transmission gap).",
    "type": "recall",
    "source_page": "wiki/theory-attachment.md",
    "topic": "transmission-gap",
    "bloom_level": "understand"
  }
]
```

## Attachment styles — the discrimination cluster

```json
[
  {
    "id": "u5-style-secure-vignette-01",
    "prompt": "In the Strange Situation, a 14-month-old plays and explores while occasionally glancing back at her mother. She's upset when mom leaves, but when mom returns she reaches up, is quickly soothed, and goes back to playing. Which attachment style?",
    "options": [
      "Secure (B)",
      "Avoidant (A)",
      "Resistant/ambivalent (C)",
      "Disorganized (D)"
    ],
    "correct": "Secure (B)",
    "answer": "Secure (B): uses mom as a secure base to explore, shows distress at separation, and — the tell — is comforted at reunion and returns to play. Ainsworth's original ~70%. Associated with sensitive, consistent caregiving.",
    "type": "mcq",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "secure-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "apply"
  },
  {
    "id": "u5-style-avoidant-vignette-01",
    "prompt": "A 14-month-old explores the toys but rarely looks at his mother. When she leaves he shows little distress; when she returns he ignores or turns away from her and keeps playing, treating the stranger about the same as his mother. Which attachment style, and what caregiving pattern typically produces it?",
    "options": [
      "Avoidant (A) — from consistently unresponsive/rejecting-of-distress caregiving",
      "Secure (B) — from sensitive, consistent caregiving",
      "Resistant/ambivalent (C) — from inconsistent caregiving",
      "Disorganized (D) — from frightening caregiving"
    ],
    "correct": "Avoidant (A) — from consistently unresponsive/rejecting-of-distress caregiving",
    "answer": "Avoidant (A). The low distress and reunion avoidance are the tell — the baby has learned that showing need gets nothing, so it DEACTIVATES the attachment system (looks independent, self-soothes). Note: minimal distress does NOT mean most secure. Typically follows consistently unavailable/rejecting caregiving.",
    "type": "mcq",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "avoidant-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "apply"
  },
  {
    "id": "u5-style-resistant-vignette-01",
    "prompt": "A 14-month-old is wary and clingy from the start and barely explores. She's intensely distressed when her mother leaves. At reunion she rushes to mom but then arches away, hits at her, and stays upset — she can't be settled even while seeking contact. Which attachment style, and what caregiving pattern typically produces it?",
    "options": [
      "Resistant/ambivalent (C) — from inconsistent caregiving",
      "Avoidant (A) — from rejecting caregiving",
      "Disorganized (D) — from frightening caregiving",
      "Secure (B) — from sensitive caregiving"
    ],
    "correct": "Resistant/ambivalent (C) — from inconsistent caregiving",
    "answer": "Resistant/ambivalent (C). The signature is seeking contact AND resisting it — reaching to be picked up, then fighting it, unable to be soothed. The baby HYPERACTIVATES the attachment system (protests loudly, won't let go) because caregiving was INCONSISTENT, so comfort is unreliable and must be signaled for constantly.",
    "type": "mcq",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "anxious-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "apply"
  },
  {
    "id": "u5-style-disorganized-vignette-01",
    "prompt": "A 14-month-old, on reunion, starts to approach his mother, then freezes halfway with a dazed expression, then backs toward her while looking away. His behavior has no consistent pattern across the episodes. Which classification, and why is it categorically different from the other three?",
    "options": [
      "Disorganized (D) — it is the ABSENCE of an organized strategy, not another strategy",
      "Resistant/ambivalent (C) — he is seeking and resisting contact",
      "Avoidant (A) — he is avoiding his mother",
      "Secure (B) — he approaches his mother"
    ],
    "correct": "Disorganized (D) — it is the ABSENCE of an organized strategy, not another strategy",
    "answer": "Disorganized (D). Secure, avoidant, and resistant are all organized (if costly) STRATEGIES; disorganized is the breakdown of any strategy — freezing, contradictory approach-avoidance, dazed/trance-like states. It appears where the caregiver is both the source of AND the solution to fear ('fright without solution'), and is linked to frightening/frightened parenting, maltreatment, or a parent's unresolved loss/trauma.",
    "type": "mcq",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "disorganized-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "apply"
  },
  {
    "id": "u5-style-avoidant-vs-resistant-compare-01",
    "prompt": "Avoidant and resistant attachment are the most-confused pair. Distinguish them by the underlying STRATEGY and the CAREGIVING each is a response to.",
    "answer": "Both manage the same alarm, in opposite directions. AVOIDANT = DEACTIVATION: the baby turns need DOWN — looks independent, self-soothes, doesn't seek comfort — because the caregiver was CONSISTENTLY unavailable/rejecting, so the lesson is 'don't ask.' RESISTANT/AMBIVALENT = HYPERACTIVATION: the baby turns need UP — clings, protests loudly, can't settle even when comforted — because the caregiver was INCONSISTENT, so the lesson is 'ask louder and don't let go.' Consistent unavailability → deactivate; unpredictable availability → hyperactivate.",
    "type": "compare",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "avoidant-vs-resistant",
    "cluster": "attachment-styles",
    "bloom_level": "analyze"
  },
  {
    "id": "u5-style-caregiving-recall-01",
    "prompt": "Map each of the three ORGANIZED attachment styles to the caregiving pattern Ainsworth associated with it.",
    "answer": "Secure ← sensitive, CONSISTENT responsiveness to the infant's signals. Avoidant ← CONSISTENTLY unresponsive / rejecting of the infant's distress. Resistant/ambivalent ← INCONSISTENT responsiveness (sometimes attentive, sometimes not). The through-line: consistency (of availability or unavailability) breeds an organized strategy; unpredictability breeds the anxious, unsettled resistant pattern.",
    "type": "recall",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "attachment-styles",
    "cluster": "attachment-styles",
    "bloom_level": "understand"
  },
  {
    "id": "u5-style-deactivation-cloze-01",
    "prompt": "The avoidant infant's strategy is to {{deactivate}} the attachment system (turn need down, self-soothe, look independent); the resistant infant's opposite strategy is to hyperactivate it (turn need up, cling, protest).",
    "answer": "deactivate",
    "type": "cloze",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "avoidant-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "understand"
  },
  {
    "id": "u5-style-adult-map-recall-01",
    "prompt": "The adult four-style attachment model is built on two dimensions. Name the two dimensions and place all four adult styles on them.",
    "answer": "Dimensions: ANXIETY (about abandonment/self-worth) and AVOIDANCE (of intimacy/dependence). Secure = low anxiety / low avoidance. Preoccupied = high anxiety / low avoidance (adult echo of resistant). Dismissing = low anxiety / high avoidance (adult echo of avoidant). Fearful = high anxiety / high avoidance (nearest adult echo of disorganized). Because they're dimensions, adults sit on a gradient and can shift by relationship and over time.",
    "type": "recall",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "adult-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "understand"
  },
  {
    "id": "u5-style-adult-vignette-01",
    "prompt": "Two clients. Client A texts between sessions, escalates distress when you seem less available, and can't hold onto reassurance for long. Client B keeps sessions abstract, says 'I don't really do feelings,' and treats needing you as weakness. Name each adult attachment style.",
    "options": [
      "A = preoccupied (high anxiety/low avoidance); B = dismissing (low anxiety/high avoidance)",
      "A = dismissing; B = preoccupied",
      "A = fearful; B = secure",
      "A = secure; B = fearful"
    ],
    "correct": "A = preoccupied (high anxiety/low avoidance); B = dismissing (low anxiety/high avoidance)",
    "answer": "A is preoccupied — hyperactivating: high abandonment anxiety, low avoidance, so they seek and escalate for reassurance. B is dismissing — deactivating: high avoidance, low expressed anxiety, so they minimize needs and keep the alliance at arm's length. Clinically the pulls invert (rescue vs. give up); steadiness disconfirms both models.",
    "type": "mcq",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "adult-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "apply"
  },
  {
    "id": "u5-style-disorg-risk-evaluate-01",
    "prompt": "Disorganized attachment is the classification most robustly linked to later psychopathology. State precisely what that does and does NOT license you to conclude about a specific person.",
    "answer": "It IS a broad, transdiagnostic RELATIONAL RISK FACTOR — associated with later internalizing and (especially) externalizing problems, dissociation, and adult borderline features. It does NOT license: (a) treating it as deterministic — the link is probabilistic and moderated by later context; many disorganized infants develop no disorder; (b) equating it with a diagnosis or with 'reactive attachment disorder' (a separate, rarer condition); (c) writing off a client — early interventions REDUCE disorganization, and later relationships (incl. therapy) can revise the working model. Risk, not destiny.",
    "type": "explain",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "disorganized-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "evaluate"
  },
  {
    "id": "u5-style-stance-01",
    "prompt": "STANCE PROBE. A supervisee tells you: 'My client is clearly avoidant/dismissing — he intellectualizes and won't go near feelings — so he's not really a good fit for therapy, and I told him he has an avoidant attachment style so he'd understand himself.' Two things are off here. Name them and give the better stance.",
    "answer": "(1) Reading dismissing behavior as 'not a good fit' repeats the original rejection — the intellectualizing IS the attachment strategy (deactivation), i.e., exactly the material to work with, not a reason to give up; a steady, non-abandoning stance is what slowly disconfirms his model. (2) Announcing 'you have an avoidant attachment style' hands the client a category/verdict — attachment is a lens for YOUR empathy and prediction, not a label to pin on a person. Better: hold the pattern privately to understand him, stay a reliable secure base, and let the relationship do the slow work.",
    "type": "vignette",
    "source_page": "wiki/concept-attachment-styles.md",
    "topic": "adult-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "evaluate"
  },
  {
    "id": "u5-style-preoccupied-inroom-vignette-01",
    "prompt": "A preoccupied client floods with distress near the end of most sessions and asks if you 'actually care.' You notice an urge to either extend the session and over-reassure, or to pull back and get clinical. Using attachment theory, explain why BOTH urges are traps and what the secure-base move is.",
    "answer": "Both urges confirm the internal working model. Over-reassuring/extending rewards hyperactivation and teaches that escalation is how to hold you — feeding the anxiety. Pulling back/getting cool re-enacts the inconsistent caregiver who withdrew — confirming abandonment fear. The secure-base move is steady, predictable, WARM-but-bounded consistency: reliable frame, empathic acknowledgment without dramatic rescue, and holding the ending kindly and firmly. Consistency (neither flooding nor withdrawing) is what slowly updates the model.",
    "type": "vignette",
    "source_page": "wiki/theory-attachment.md",
    "topic": "adult-attachment",
    "cluster": "attachment-styles",
    "bloom_level": "analyze"
  }
]
```

## Erikson's psychosocial stages

```json
[
  {
    "id": "u5-erik-stages-recall-01",
    "prompt": "List Erikson's eight psychosocial stages in order as 'conflict → virtue.'",
    "answer": "1) Trust vs. Mistrust → Hope; 2) Autonomy vs. Shame & Doubt → Will; 3) Initiative vs. Guilt → Purpose; 4) Industry vs. Inferiority → Competence; 5) Identity vs. Role Confusion → Fidelity; 6) Intimacy vs. Isolation → Love; 7) Generativity vs. Stagnation → Care; 8) Integrity vs. Despair → Wisdom.",
    "type": "recall",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "erikson-stages",
    "cluster": "erikson-stages",
    "bloom_level": "remember"
  },
  {
    "id": "u5-erik-virtue-cloze-01",
    "prompt": "In Erikson's model, the adolescent stage is Identity vs. Role Confusion, and its associated virtue (ego strength) is {{fidelity}}.",
    "answer": "fidelity",
    "type": "cloze",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "erikson-stages",
    "cluster": "erikson-stages",
    "bloom_level": "remember"
  },
  {
    "id": "u5-erik-syntonic-dystonic-explain-01",
    "prompt": "Erikson's stages pit a positive (syntonic) tendency against a negative (dystonic) one. Explain why healthy resolution is NOT getting 100% of the positive pole, using one stage as an example.",
    "answer": "Health is landing on a FAVORABLE RATIO of the two poles, not eliminating the negative — some of the dystonic pole is adaptive. E.g., in Trust vs. Mistrust, a baby who developed pure trust and zero mistrust would be dangerously credulous; some mistrust is protective. The virtue (here, Hope) emerges from navigating the tension, not from winning it outright. This is also why an 'unresolved' stage isn't a failure and can be reworked later.",
    "type": "explain",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "erikson-stages",
    "cluster": "erikson-stages",
    "bloom_level": "understand"
  },
  {
    "id": "u5-erik-identity-vs-intimacy-compare-01",
    "prompt": "Distinguish Erikson's stage 5 (Identity vs. Role Confusion) from stage 6 (Intimacy vs. Isolation), and explain why Erikson's ordering is clinically meaningful.",
    "answer": "Identity (stage 5, adolescence) = figuring out WHO YOU ARE and what you believe, on your own. Intimacy (stage 6, young adulthood) = the capacity to MERGE that self with another without dissolving it. The order matters clinically because you need a self before you can share one: someone who skips identity work tends to do 'intimacy' as enmeshment or serial fusing — losing themselves in each partner — rather than true intimacy. The virtues track this: Fidelity (a stable self to be true to) precedes Love.",
    "type": "compare",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "identity-vs-intimacy",
    "cluster": "erikson-stages",
    "bloom_level": "analyze"
  },
  {
    "id": "u5-erik-initiative-vs-industry-compare-01",
    "prompt": "Initiative (stage 3) and Industry (stage 4) are easy to confuse. Distinguish the drive each is about and what its failure pole looks like.",
    "answer": "Initiative (play age, ~3–6) = the drive to START and imagine — planning, initiating, 'let's build a rocket ship'; failure pole is GUILT over wanting/doing. Industry (school age, ~6–12) = the drive to COMPLETE and be COMPETENT at real tasks, measured against peers; failure pole is INFERIORITY. Shorthand: initiative = the impulse to BEGIN; industry = the capacity to FINISH and be good at it.",
    "type": "compare",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "initiative-vs-industry",
    "cluster": "erikson-stages",
    "bloom_level": "analyze"
  },
  {
    "id": "u5-erik-adolescent-vignette-01",
    "prompt": "A 16-year-old is trying on different friend groups, political views, and styles, and keeps asking 'but who am I really?' Which Erikson stage is this, and is it typical or a red flag?",
    "options": [
      "Identity vs. Role Confusion — and this is TYPICAL developmental work",
      "Intimacy vs. Isolation — and this is a red flag",
      "Industry vs. Inferiority — and this is typical",
      "Generativity vs. Stagnation — and this is a red flag"
    ],
    "correct": "Identity vs. Role Confusion — and this is TYPICAL developmental work",
    "answer": "Identity vs. Role Confusion (adolescence). Exploring roles, values, and identities is the NORMAL task of the stage — not pathology. Reading ordinary identity churn as disorder is exactly the over-pathologizing this unit warns against; you can't tell typical from clinical without knowing the age-appropriate task.",
    "type": "mcq",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "erikson-stages",
    "cluster": "erikson-stages",
    "bloom_level": "apply"
  },
  {
    "id": "u5-erik-midlife-vignette-01",
    "prompt": "A 52-year-old says he feels his life hasn't 'added up to anything' and is preoccupied with whether he's leaving anything behind or contributing to anyone beyond himself. Which Erikson stage/conflict is he in?",
    "options": [
      "Generativity vs. Stagnation",
      "Integrity vs. Despair",
      "Identity vs. Role Confusion",
      "Intimacy vs. Isolation"
    ],
    "correct": "Generativity vs. Stagnation",
    "answer": "Generativity vs. Stagnation (adulthood, ~40–65) — the task of contributing to the next generation / something beyond the self; its failure pole is stagnation/self-absorption. Naming this as a developmental task (virtue: Care) reframes his distress as midlife work rather than simply 'depression.'",
    "type": "mcq",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "erikson-stages",
    "cluster": "erikson-stages",
    "bloom_level": "apply"
  },
  {
    "id": "u5-erik-carried-forward-vignette-01",
    "prompt": "A 34-year-old client repeatedly tests whether you'll really show up — cancels, watches for you to give up on her, struggles to believe the alliance is safe. Using Erikson (and linking to attachment), what earlier stage might her presentation be reworking, and how does that reframe the work?",
    "answer": "Her difficulty trusting the relationship echoes Stage 1, Trust vs. Mistrust — the psychosocial face of early attachment. Erikson's point that stages can be REWORKED later means the alliance itself is a chance to re-negotiate that crisis toward 'hope.' Reframe: her testing isn't resistance to fix but the old trust question live in the room; being a reliable, non-abandoning secure base IS the intervention. (Erikson trust ≈ attachment security — same developmental moment, two vocabularies.)",
    "type": "vignette",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "erikson-stages",
    "cluster": "erikson-stages",
    "bloom_level": "analyze"
  },
  {
    "id": "u5-erik-critique-evaluate-01",
    "prompt": "Give two reasons Erikson's stages should be held as a clinical heuristic rather than a measured developmental law.",
    "answer": "(1) It's hard to falsify and the ages/boundaries are approximate — real 'crises' aren't cleanly sequential or separable. (2) It's culturally and historically situated: an extended ADOLESCENCE devoted to IDENTITY exploration is largely a modern, Western, industrialized arrangement, and 'autonomy'/'generativity' carry individualist assumptions that don't travel unchanged (link to multicultural competence). Use it to locate 'which task is live for this client,' not to grade development pass/fail.",
    "type": "explain",
    "source_page": "wiki/theory-eriksons-stages.md",
    "topic": "erikson-stages",
    "cluster": "erikson-stages",
    "bloom_level": "evaluate"
  }
]
```

## Piaget's cognitive-development stages

```json
[
  {
    "id": "u5-piaget-stages-recall-01",
    "prompt": "Name Piaget's four cognitive-development stages in order with their approximate ages and the signature achievement of each.",
    "answer": "1) Sensorimotor (0–2): object permanence (knowledge through sensory/motor action). 2) Pre-operational (2–7): symbols & language, but egocentrism and no conservation. 3) Concrete operational (7–11): logical operations on concrete material — conservation, reversibility, classification. 4) Formal operational (12+): abstract and hypothetical-deductive reasoning.",
    "type": "recall",
    "source_page": "wiki/theory-piaget.md",
    "topic": "piaget-stages",
    "cluster": "piaget-stages",
    "bloom_level": "remember"
  },
  {
    "id": "u5-piaget-object-permanence-cloze-01",
    "prompt": "The hallmark achievement of Piaget's sensorimotor stage, emerging around 6 months, is {{object permanence}} — the understanding that objects continue to exist even when they can't be seen.",
    "answer": "object permanence",
    "type": "cloze",
    "source_page": "wiki/theory-piaget.md",
    "topic": "piaget-stages",
    "cluster": "piaget-stages",
    "bloom_level": "remember"
  },
  {
    "id": "u5-piaget-assim-accom-compare-01",
    "prompt": "Distinguish assimilation from accommodation in Piaget's theory, with an example of each.",
    "answer": "ASSIMILATION = taking in new information by fitting it into an EXISTING schema (a child sees a cat and calls it 'dog' — the world is bent to fit the mind). ACCOMMODATION = REVISING the schema when it doesn't fit (learning 'that's a cat, a different thing' — the mind is bent to fit the world). Shorthand: assimilation bends the world to the mind; accommodation bends the mind to the world. Equilibration is the drive to resolve the tension between them.",
    "type": "compare",
    "source_page": "wiki/theory-piaget.md",
    "topic": "assimilation-accommodation",
    "cluster": "piaget-stages",
    "bloom_level": "analyze"
  },
  {
    "id": "u5-piaget-conservation-vignette-01",
    "prompt": "You pour water from a short wide glass into a tall thin glass while a child watches, then ask which glass has more. The child confidently says the tall one 'because it's higher.' Which Piaget stage is the child in, and what limitation does the error reveal?",
    "options": [
      "Pre-operational — lacks conservation (centration + no reversibility)",
      "Concrete operational — has just mastered conservation",
      "Sensorimotor — lacks object permanence",
      "Formal operational — using hypothetical reasoning"
    ],
    "correct": "Pre-operational — lacks conservation (centration + no reversibility)",
    "answer": "Pre-operational (2–7). The child lacks CONSERVATION: they CENTER on one dimension (height) and can't mentally REVERSE the pour to see the amount is unchanged. Passing this task is the tell that a child has crossed into concrete operations.",
    "type": "mcq",
    "source_page": "wiki/theory-piaget.md",
    "topic": "piaget-stages",
    "cluster": "piaget-stages",
    "bloom_level": "apply"
  },
  {
    "id": "u5-piaget-formal-vignette-01",
    "prompt": "A 14-year-old suddenly spends hours arguing about whether justice can ever be truly fair 'in principle,' reasoning through hypotheticals and abstract ideals. Which Piaget stage does this signal?",
    "options": [
      "Formal operational — abstract, hypothetical-deductive reasoning",
      "Concrete operational — logic tied to concrete situations",
      "Pre-operational — symbolic but pre-logical",
      "Sensorimotor — action-based knowledge"
    ],
    "correct": "Formal operational — abstract, hypothetical-deductive reasoning",
    "answer": "Formal operational (12+): the capacity for abstract, hypothetical, and idealistic reasoning — theories, 'what if,' justice and love as concepts — comes online. (Caveat: formal-operational reasoning is used inconsistently and isn't universal even in adults.)",
    "type": "mcq",
    "source_page": "wiki/theory-piaget.md",
    "topic": "piaget-stages",
    "cluster": "piaget-stages",
    "bloom_level": "apply"
  },
  {
    "id": "u5-piaget-clinical-apply-01",
    "prompt": "Why do clinicians use play, drawing, and stories rather than 'how does that make you feel about your family?' talk-therapy with a 5-year-old? Answer in Piagetian terms.",
    "answer": "A 5-year-old is PRE-OPERATIONAL: they work in the concrete and symbolic and cannot yet handle the abstract, reflective, hypothetical questions insight-oriented talk requires (that's formal-operational, 12+). Play, drawing, and stories meet the child's actual cognitive level — symbolic expression without demanding abstract self-reflection. General principle: match your language and method to the client's reasoning stage, not their chronological age.",
    "type": "explain",
    "source_page": "wiki/theory-piaget.md",
    "topic": "piaget-stages",
    "cluster": "piaget-stages",
    "bloom_level": "apply"
  },
  {
    "id": "u5-piaget-critique-evaluate-01",
    "prompt": "Summarize three well-established critiques of Piaget's theory, including the sociocultural one associated with Vygotsky.",
    "answer": "(1) He UNDERESTIMATED infants/children — object permanence and theory of mind arrive EARLIER than he claimed (ToM by ~4–5). (2) He OVERESTIMATED adolescents/adults — formal-operational reasoning is used inconsistently and isn't universal. (3) He NEGLECTED the social/cultural — Vygotsky's critique: cognition is SCAFFOLDED by social interaction and language; the 'zone of proximal development' (what a child can do WITH help) is where learning happens, and culture shapes what develops. Bonus: stages describe a real SEQUENCE better than they fix real AGES.",
    "type": "explain",
    "source_page": "wiki/theory-piaget.md",
    "topic": "piaget-stages",
    "cluster": "piaget-stages",
    "bloom_level": "evaluate"
  }
]
```

## Telling the theorists apart (cross-framework)

```json
[
  {
    "id": "u5-theorists-compare-01",
    "prompt": "Erikson, Piaget, and Bowlby all describe childhood. State, in one line each, what DOMAIN of development each one primarily explains.",
    "answer": "ERIKSON = PSYCHOSOCIAL/emotional development — the central relational task ('crisis') the person wrestles with at each life phase (trust, identity, intimacy...). PIAGET = COGNITIVE development — how thinking itself is reorganized (sensorimotor → formal operations). BOWLBY = the ATTACHMENT relationship — how early caregiving builds a template (internal working model) for later closeness. They chart the same childhood on different axes: emotion/task, thought, and bond.",
    "type": "compare",
    "source_page": "wiki/unit05-development.md",
    "topic": "developmental-theorists",
    "cluster": "developmental-theorists",
    "bloom_level": "analyze"
  },
  {
    "id": "u5-theorists-vignette-01",
    "prompt": "A clinician wants to understand why a specific client tends to expect people to abandon her and struggles to trust closeness in relationships. Whose framework most directly addresses this, and why not the others?",
    "options": [
      "Bowlby — it's about the internal working model of relationships (attachment)",
      "Piaget — it's about her stage of logical reasoning",
      "Erikson — it's about which of eight virtues she has achieved",
      "Engel — it's about her serotonin levels"
    ],
    "correct": "Bowlby — it's about the internal working model of relationships (attachment)",
    "answer": "Bowlby/attachment: expecting abandonment and struggling to trust closeness is the signature of an insecure INTERNAL WORKING MODEL of relationships. Piaget is about cognition (wrong domain); Erikson's trust-vs-mistrust is adjacent and complementary but frames it as a psychosocial virtue rather than a relational template; Engel/biopsychosocial is the umbrella frame, not a specific account of relational expectations.",
    "type": "mcq",
    "source_page": "wiki/unit05-development.md",
    "topic": "developmental-theorists",
    "cluster": "developmental-theorists",
    "bloom_level": "analyze"
  },
  {
    "id": "u5-theorists-trust-parallel-explain-01",
    "prompt": "Erikson's first stage (Trust vs. Mistrust) and Bowlby's attachment describe overlapping developmental territory. Explain how they line up and how they differ in emphasis.",
    "answer": "Both concern the infant learning whether the caregiving world is reliable in the first ~year. Erikson frames it as a PSYCHOSOCIAL crisis whose favorable resolution yields the virtue HOPE (a general stance toward the world). Bowlby frames the same period as the formation of an ATTACHMENT bond and an internal working model of self-and-other (a specific relational template measurable via the Strange Situation). Same moment, two lenses: Erikson's is broader/virtue-oriented; Bowlby's is relationship-specific and operationalized.",
    "type": "explain",
    "source_page": "wiki/theory-attachment.md",
    "topic": "developmental-theorists",
    "cluster": "developmental-theorists",
    "bloom_level": "understand"
  }
]
```

## The biopsychosocial model

```json
[
  {
    "id": "u5-bps-recall-01",
    "prompt": "Who proposed the biopsychosocial model and when, what two features of the biomedical model was it reacting against, and what broader theory is it grounded in?",
    "answer": "George Engel, in a 1977 Science paper ('The Need for a New Medical Model'). It reacted against the biomedical model's REDUCTIONISM (collapsing complex illness to a single physical cause) and MIND–BODY DUALISM (treating mind and body as separate, only the body as causally real). It's grounded in GENERAL SYSTEMS THEORY — biological, psychological, and social levels as nested, reciprocally interacting domains.",
    "type": "recall",
    "source_page": "wiki/concept-biopsychosocial-model.md",
    "topic": "biopsychosocial",
    "bloom_level": "remember"
  },
  {
    "id": "u5-bps-apply-01",
    "prompt": "A client presents with panic attacks. Sketch a biopsychosocial formulation by naming one plausible contributor in EACH of the three domains.",
    "answer": "BIO: e.g., high trait anxiety/temperament, too much caffeine, poor sleep, a thyroid issue, or family history. PSYCHO: e.g., catastrophic misinterpretation of bodily sensations ('I'm having a heart attack'), an anxious/preoccupied attachment pattern, avoidance-based coping. SOCIAL: e.g., a high-stress job, relationship conflict, financial precarity, isolation, or discrimination-related stress. The point is to look ACROSS all three and theorize their interaction rather than collapsing panic into any one domain.",
    "type": "vignette",
    "source_page": "wiki/concept-biopsychosocial-model.md",
    "topic": "biopsychosocial",
    "bloom_level": "apply"
  },
  {
    "id": "u5-bps-critique-evaluate-01",
    "prompt": "The biopsychosocial model is both the field's default formulation frame and heavily criticized. State the core criticism and how a counselor should use the model in light of it.",
    "answer": "Core criticism (Ghaemi, Kendler): it's vague and unfalsifiable — 'permission to do everything but no specific guidance,' a 'slogan' rather than a scientific model; asserting bio/psycho/social matter EQUALLY in all cases is wrong. Use it well by treating it not as an explanation but as an organizing CHECKLIST you must make specific to THIS client — recognizing domains carry different weight for different problems and stages, and that its real job is to force you to theorize the INTERACTIONS between domains, not to claim equal weight everywhere.",
    "type": "explain",
    "source_page": "wiki/concept-biopsychosocial-model.md",
    "topic": "biopsychosocial",
    "bloom_level": "evaluate"
  }
]
```

## Typical vs. clinical, risk-not-destiny & the practice rep

```json
[
  {
    "id": "u5-typical-clinical-stance-01",
    "prompt": "STANCE PROBE. A new counselor, fresh from reading about disorders, describes a defiant, boundary-testing 2.5-year-old as showing 'oppositional traits' and an identity-exploring 15-year-old as 'unstable sense of self.' What error is this, and what's the corrective discipline?",
    "answer": "It's OVER-PATHOLOGIZING normal development — reading age-appropriate tasks (a toddler's autonomy/'no'; an adolescent's identity exploration) as symptoms. The corrective is knowing the developmental baseline first (Erikson's autonomy stage; identity stage) and treating deviations as QUESTIONS, not answers — most variation is normal variation. Over-pathologizing ordinary turbulence is the mirror-image error to missing a real delay; both are failures of knowing what's normal for the age.",
    "type": "vignette",
    "source_page": "wiki/unit05-development.md",
    "topic": "typical-vs-clinical",
    "bloom_level": "evaluate"
  },
  {
    "id": "u5-risk-not-destiny-explain-01",
    "prompt": "Define equifinality and multifinality, and explain why together they mean a developmental history is 'a hypothesis about a client, not a diagnosis of one.'",
    "answer": "EQUIFINALITY = many different developmental paths can lead to the SAME outcome (many roads into depression). MULTIFINALITY = the SAME starting point can lead to many DIFFERENT outcomes (an insecure infancy leads to varied futures). Together they mean no single early factor determines a later outcome and no outcome implies a single cause — so an attachment history or stuck stage predicts TENDENCIES probabilistically, moderated by everything after. Hence: use a developmental history to understand and hypothesize, never to file or sentence the client.",
    "type": "explain",
    "source_page": "wiki/unit05-development.md",
    "topic": "risk-not-destiny",
    "bloom_level": "evaluate"
  },
  {
    "id": "u5-milestones-surveillance-recall-01",
    "prompt": "What is 'developmental surveillance,' and how do milestone norms help distinguish typical development from clinical concern?",
    "answer": "Developmental surveillance is the longitudinal clinical habit of eliciting concerns, taking a milestone history, observing the child, and applying judgment across visits. Milestones provide AGE-DEPENDENT POPULATION NORMS, so a missed milestone calibrates HOW concerned to be and whether to screen/refer — the operational form of 'you can't tell what's wrong if you don't know what's normal for the age.' The same logic (know the norm, treat deviations as questions) scales to any age.",
    "type": "recall",
    "source_page": "wiki/unit05-development.md",
    "topic": "typical-vs-clinical",
    "bloom_level": "understand"
  },
  {
    "id": "u5-practice-rep-production-01",
    "prompt": "PRODUCTION REP (the syllabus practice rep). In a few sentences, (a) place yourself on the four attachment styles and give one concrete piece of adult-relationship evidence, and (b) name the Erikson stage you are actually working on now. Then state one way your own attachment pattern might bias how you sit with a clinging (preoccupied) or a distant (dismissing) client.",
    "answer": "Self-graded. A strong response: (a) picks a style and grounds it in behavior, not a label ('I tend dismissing — I go quiet and self-reliant under stress and rarely ask for help'), ideally noting styles are dimensional/shiftable; (b) names a plausible current Erikson stage with a reason (e.g., intimacy vs. isolation, or generativity vs. stagnation); (c) derives a specific countertransference risk — e.g., a dismissing counselor may under-respond to a preoccupied client's bids (reading them as 'too much') and over-identify with a dismissing client's distance. The rep's value is seeing your own pattern before it runs the room.",
    "type": "explain",
    "source_page": "wiki/unit05-development.md",
    "topic": "risk-not-destiny",
    "bloom_level": "apply"
  }
]
```
