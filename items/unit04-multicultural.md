# Unit 4 items — Multicultural & Social-Justice Competence

Source of truth for Unit 4 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This unit's signature reps: **the cultural
autobiography** (the syllabus practice rep, as a production item), **which-dimension-failed
vignettes** (cluster `mc-competence-dimensions`), **framework discrimination** (cluster
`mc-frameworks` — tripartite vs. MSJCC vs. cultural humility), Berry's 2×2 as **which-strategy
vignettes** (cluster `acculturation-strategies`), the **broaching continuum** (cluster
`broaching-styles`), and the **microaggression taxonomy + repair** (cluster
`microaggression-types`). Many items are stance probes — this unit's content *is* stance. See
generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## Frameworks: tripartite, MSJCC, cultural humility, and the evidence

```json
[
  {
    "id": "u4-tripartite-recall-01",
    "prompt": "Name the three dimensions of the tripartite model of multicultural counseling competence (Sue, Arredondo & McDavis, 1992), and give a one-line gloss of each — including whose values the first dimension is about.",
    "answer": "Awareness — of the COUNSELOR'S OWN values, biases, assumptions, and worldview (not the client's). Knowledge — of the client's worldview, customs, and sociopolitical context. Skills — culturally appropriate intervention strategies: the ability to adapt what you actually do.",
    "type": "recall",
    "source_page": "wiki/theory-tripartite-model.md",
    "topic": "tripartite",
    "cluster": "mc-competence-dimensions",
    "bloom_level": "remember"
  },
  {
    "id": "u4-tripartite-cloze-01",
    "prompt": "The tripartite model's awareness dimension is awareness of {{the counselor's own values, biases, and worldview}} — the exam trap is thinking it means awareness of the client's culture (that's the knowledge dimension).",
    "answer": "the counselor's own values, biases, and worldview",
    "type": "cloze",
    "source_page": "wiki/theory-tripartite-model.md",
    "topic": "tripartite",
    "cluster": "mc-competence-dimensions",
    "bloom_level": "remember"
  },
  {
    "id": "u4-dimension-vignette-01",
    "prompt": "A first-generation Chinese American client is torn between changing majors and her parents' opposition. Her counselor responds: 'It sounds like it's time to set some boundaries with your parents — this is YOUR life.' Which tripartite dimension has failed?",
    "options": [
      "Awareness — the counselor is exporting their own individualist values as if they were mental health itself",
      "Knowledge — the counselor lacks facts about Chinese American family norms",
      "Skills — the counselor chose a culturally inappropriate technique",
      "None — this is sound empowerment counseling"
    ],
    "correct": "Awareness — the counselor is exporting their own individualist values as if they were mental health itself",
    "answer": "Awareness. The counselor isn't missing facts about the client's culture (knowledge) or misapplying a technique (skills); they are treating their own autonomy/individuation norms as the neutral default. That unexamined-default move is precisely what the awareness dimension exists to catch.",
    "type": "mcq",
    "source_page": "wiki/theory-tripartite-model.md",
    "topic": "tripartite",
    "cluster": "mc-competence-dimensions",
    "bloom_level": "apply"
  },
  {
    "id": "u4-dimension-vignette-02",
    "prompt": "Same client. A different counselor has read extensively about filial piety and family-as-unit decision-making — then proposes: 'Let's do a two-chair exercise where you confront your mother.' Which tripartite dimension has failed?",
    "options": [
      "Skills — culturally informed knowledge delivered through an unadapted technique",
      "Awareness — the counselor hasn't examined their own biases",
      "Knowledge — the counselor doesn't understand the client's worldview",
      "Action — the counselor failed to advocate for the client"
    ],
    "correct": "Skills — culturally informed knowledge delivered through an unadapted technique",
    "answer": "Skills. The counselor HAS the knowledge (filial piety, family norms) but selected a confrontation exercise straight from their default toolkit — imposing a direct-confrontation frame on a client for whom confronting a parent may be the problem framing itself. Skills = the ability to adapt what you DO, not just what you know.",
    "type": "mcq",
    "source_page": "wiki/theory-tripartite-model.md",
    "topic": "tripartite",
    "cluster": "mc-competence-dimensions",
    "bloom_level": "apply"
  },
  {
    "id": "u4-dimension-compare-01",
    "prompt": "Awareness and knowledge are the two most-confused tripartite dimensions. Distinguish them, and describe what the characteristic failure of each looks like in session.",
    "answer": "Awareness = knowing what YOU bring into the room (your values, biases, defaults); its failure is a counselor who treats their own norms as neutral mental health ('time to individuate from your family'). Knowledge = knowing what shapes the CLIENT'S world (customs, history, sociopolitical context); its failure is warm, well-meaning cluelessness ('wow, your parents are really controlling, huh?'). Awareness looks inward, knowledge looks outward — real competence needs both plus skills.",
    "type": "compare",
    "source_page": "wiki/theory-tripartite-model.md",
    "topic": "tripartite",
    "cluster": "mc-competence-dimensions",
    "bloom_level": "analyze"
  },
  {
    "id": "u4-msjcc-aksa-cloze-01",
    "prompt": "The MSJCC's aspirational competencies keep the tripartite triad (attitudes & beliefs, knowledge, skills) and add a fourth: {{action}} — what you actually DID about it.",
    "answer": "action",
    "type": "cloze",
    "source_page": "wiki/concept-msjcc.md",
    "topic": "msjcc",
    "cluster": "mc-competence-dimensions",
    "bloom_level": "remember"
  },
  {
    "id": "u4-msjcc-domains-recall-01",
    "prompt": "List the MSJCC's four developmental domains in order, and explain why the order matters.",
    "answer": "1) Counselor self-awareness, 2) Client worldview, 3) Counseling relationship, 4) Counseling and advocacy interventions. The order encodes the theory of change: know yourself before you can understand the client; both before you can read the dyad's dynamics; all three before intervening. Skipping to domain 4 is activism without a clinician attached; stopping at domain 3 is insight without consequences.",
    "type": "recall",
    "source_page": "wiki/concept-msjcc.md",
    "topic": "msjcc",
    "cluster": "mc-frameworks",
    "bloom_level": "understand"
  },
  {
    "id": "u4-msjcc-quadrants-recall-01",
    "prompt": "What do the MSJCC's four quadrants cross, and what is the key caveat about placing yourself or a client in one?",
    "answer": "They cross counselor status × client status on privileged vs. marginalized (I: privileged counselor–marginalized client; II: privileged–privileged; III: marginalized counselor–privileged client; IV: marginalized–marginalized). Caveat: identities are fluid and intersectional — everyone holds privileged AND marginalized statuses at once on different axes — so quadrants describe moments and dimensions of a relationship, not fixed types of people.",
    "type": "recall",
    "source_page": "wiki/concept-msjcc.md",
    "topic": "msjcc",
    "cluster": "mc-frameworks",
    "bloom_level": "understand"
  },
  {
    "id": "u4-msjcc-socioeco-recall-01",
    "prompt": "Name the MSJCC's six socioecological levels of advocacy, from innermost to outermost.",
    "answer": "Intrapersonal → interpersonal → institutional → community → public policy → international/global.",
    "type": "recall",
    "source_page": "wiki/concept-msjcc.md",
    "topic": "msjcc",
    "cluster": "mc-frameworks",
    "bloom_level": "remember"
  },
  {
    "id": "u4-msjcc-vignette-01",
    "prompt": "A school counselor notices a student who uses a wheelchair loses instructional time daily because the accessible route to class is roundabout, and works with the school to get a direct accessible route opened. In MSJCC terms, which domain and which socioecological level is this?",
    "options": [
      "Counseling and advocacy interventions — institutional level",
      "Counseling and advocacy interventions — public policy level",
      "Counseling relationship — interpersonal level",
      "Client worldview — community level"
    ],
    "correct": "Counseling and advocacy interventions — institutional level",
    "answer": "Domain 4 (counseling and advocacy interventions) at the institutional level — changing a school's practices/environment. It's not public policy (no law or regulation involved) and not interpersonal (the target is the institution's arrangement, not a relationship). This is one of the MSJCC authors' own worked examples.",
    "type": "mcq",
    "source_page": "wiki/concept-msjcc.md",
    "topic": "msjcc",
    "cluster": "mc-frameworks",
    "bloom_level": "apply"
  },
  {
    "id": "u4-frameworks-compare-01",
    "prompt": "Compare the 1992 tripartite model with the 2015 MSJCC: name at least two structural things the MSJCC added and the assumption of the 1992 model it corrected.",
    "answer": "Added: (1) the four privileged/marginalized quadrants built on intersectionality — everyone holds both statuses at once; (2) 'action' as a fourth aspirational competency (AKSA) and a whole advocacy domain organized across six socioecological levels; (also: four developmental domains as an ordered path). Corrected assumption: the 1992 model quietly assumed a majority counselor working with a minority client — MSJCC makes privilege bidirectional and fluid across every dyad.",
    "type": "compare",
    "source_page": "wiki/concept-msjcc.md",
    "topic": "msjcc",
    "cluster": "mc-frameworks",
    "bloom_level": "analyze"
  },
  {
    "id": "u4-humility-recall-01",
    "prompt": "State Tervalon & Murray-García's (1998) three commitments of cultural humility.",
    "answer": "1) Lifelong self-evaluation and self-critique (no endpoint, no certificate). 2) Redressing the power imbalance in the clinician–client dyad (the client is the expert on their own experience). 3) Institutional accountability / developing mutually beneficial, non-paternalistic partnerships with communities.",
    "type": "recall",
    "source_page": "wiki/concept-cultural-humility.md",
    "topic": "cultural-humility",
    "cluster": "mc-frameworks",
    "bloom_level": "remember"
  },
  {
    "id": "u4-humility-compare-01",
    "prompt": "What is the core critique 'cultural humility' makes of 'cultural competence,' and how does the field currently resolve the tension between the two terms?",
    "answer": "Critique: 'competence' implies a masterable ENDPOINT — a finite body of knowledge you can complete and be certified in — which misrepresents culture and invites false confidence. Current resolution: treat them as complements — competencies name the learnable content (awareness, knowledge, skills, action); humility names the stance that keeps that content from hardening into stereotype-with-a-syllabus. But the tension is real: the official frameworks still say 'competencies' while training culture increasingly says 'humility.'",
    "type": "compare",
    "source_page": "wiki/concept-cultural-humility.md",
    "topic": "cultural-humility",
    "cluster": "mc-frameworks",
    "bloom_level": "analyze"
  },
  {
    "id": "u4-humility-vignette-01",
    "prompt": "A counselor tells a new Latina client: 'I did a training on Latino family culture — I know familismo is central for you, so let's make sure any plan keeps your family's approval front and center.' The counselor is warm and informed. What's wrong here, and what would the culturally humble version sound like?",
    "answer": "The counselor has replaced the individual with a category — a stereotype with good intentions. Knowledge applied without humility treats a cultural generalization as a fact about this client. Humble version holds the same knowledge as a hypothesis the client can veto: 'I've read family can weigh heavily in decisions like this in some Latino families — I don't know how much that describes your family, or you. What's true in your house?' The client's veto power is the power-redress commitment at conversational scale.",
    "type": "vignette",
    "source_page": "wiki/concept-cultural-humility.md",
    "topic": "cultural-humility",
    "cluster": "mc-frameworks",
    "bloom_level": "evaluate"
  },
  {
    "id": "u4-humility-stance-01",
    "prompt": "You misgender a client in session and realize it immediately. One instinct is to apologize at length so they know how bad you feel. Why is that the wrong move on cultural-humility grounds, and what does the right move look like?",
    "answer": "An extended apology recenters the counselor — the client ends up managing YOUR feelings and granting absolution, which is self-focused, the opposite pole of humility's other-oriented stance. Right move: correct yourself, own it briefly ('I'm sorry — she. Let me continue'), and return the floor to the client. Repair over performance.",
    "type": "explain",
    "source_page": "wiki/concept-cultural-humility.md",
    "topic": "cultural-humility",
    "bloom_level": "evaluate"
  },
  {
    "id": "u4-evidence-recall-01",
    "prompt": "In Hook et al. (2013), whose rating of the therapist's cultural humility predicted therapy outcomes, and through what mediator did the effect run?",
    "answer": "The CLIENT'S rating (not the therapist's self-rating). Client-perceived cultural humility predicted better outcomes, mediated by a stronger working alliance — the effect runs through the bond.",
    "type": "recall",
    "source_page": "wiki/concept-cultural-humility.md",
    "topic": "mcc-evidence",
    "bloom_level": "understand"
  },
  {
    "id": "u4-evidence-cloze-01",
    "prompt": "Tao et al.'s (2015) meta-analysis: client-perceived multicultural competence correlates strongly with process variables like alliance (r ≈ .58–.72) but only moderately with outcomes (r ≈ {{.29}}).",
    "answer": ".29",
    "type": "cloze",
    "source_page": "wiki/unit04-multicultural.md",
    "topic": "mcc-evidence",
    "bloom_level": "remember"
  },
  {
    "id": "u4-evidence-analyze-01",
    "prompt": "Constantine & Ladany (2000) found that after controlling for social desirability, therapists' self-reported multicultural competence had no association with their actual multicultural case-conceptualization ability. Explain why this measurement finding is itself an argument for cultural humility.",
    "answer": "The finding means counselors cannot accurately grade their own cultural competence — self-ratings track wanting-to-look-good, not skill. What does predict process and outcome is the CLIENT'S perception (Tao; Hook). So the empirical situation enacts humility's claim: your confidence in your own competence is untrustworthy, the client's experience is the authoritative gauge, and lifelong self-questioning beats self-certification. The data deny you the certificate that 'competence' framing implies.",
    "type": "explain",
    "source_page": "wiki/theory-tripartite-model.md",
    "topic": "mcc-evidence",
    "bloom_level": "evaluate"
  }
]
```

## Acculturation, worldview & help-seeking

```json
[
  {
    "id": "u4-accult-recall-01",
    "prompt": "State the two independent questions (dimensions) that generate Berry's four acculturation strategies.",
    "answer": "1) Does the person value MAINTAINING their heritage culture and identity? 2) Does the person value CONTACT and participation with the larger society? The dimensions are independent — that two-dimensionality is what separates Berry's model from a one-line 'how assimilated are you?' scale.",
    "type": "recall",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "acculturation",
    "cluster": "acculturation-strategies",
    "bloom_level": "remember"
  },
  {
    "id": "u4-accult-cloze-01",
    "prompt": "In Berry's model, valuing BOTH heritage-culture maintenance AND contact with the larger society is the strategy called {{integration}} — the strategy consistently associated with the best adaptation.",
    "answer": "integration",
    "type": "cloze",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "acculturation",
    "cluster": "acculturation-strategies",
    "bloom_level": "remember"
  },
  {
    "id": "u4-accult-vignette-01",
    "prompt": "A recent immigrant lives in an ethnic enclave, works for a co-ethnic employer, consumes home-country media, and by preference has minimal contact with the wider society; her heritage identity is strong and central. Which of Berry's strategies is this?",
    "options": [
      "Separation — heritage maintained, contact with larger society not sought",
      "Marginalization — disconnected from both cultures",
      "Integration — bicultural engagement",
      "Assimilation — new culture adopted, heritage released"
    ],
    "correct": "Separation — heritage maintained, contact with larger society not sought",
    "answer": "Separation: yes to heritage maintenance, no to contact with the larger society. Not marginalization — her heritage connection is strong and sustaining; marginalization requires losing BOTH anchors.",
    "type": "mcq",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "acculturation",
    "cluster": "acculturation-strategies",
    "bloom_level": "apply"
  },
  {
    "id": "u4-accult-vignette-02",
    "prompt": "A refugee client has worked hard to adopt the new country's language and customs and has let go of most heritage practices — but discrimination keeps blocking his entry into workplaces and friendships, and his ties to his heritage community have withered. He belongs nowhere. Which of Berry's strategies describes his situation, and what nuance about 'choice' does his case illustrate?",
    "options": [
      "Marginalization — and it is often imposed by the receiving society, not chosen",
      "Assimilation — he chose to release his heritage culture",
      "Separation — he is being kept separate from the larger society",
      "Integration — he is between two cultures"
    ],
    "correct": "Marginalization — and it is often imposed by the receiving society, not chosen",
    "answer": "Marginalization: connected to neither culture — the strategy with the worst adaptation outcomes. The nuance: he TRIED assimilation; exclusion by the receiving society blocked it while his heritage ties eroded. Berry pairs each individual strategy with a society-level condition (here: exclusion) — 'strategy' is constrained by how open the society actually is, and marginalization especially is usually done TO people.",
    "type": "mcq",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "acculturation",
    "cluster": "acculturation-strategies",
    "bloom_level": "apply"
  },
  {
    "id": "u4-accult-compare-01",
    "prompt": "Assimilation and marginalization both involve low heritage-culture maintenance. Distinguish them — on the second dimension, on typical adaptation outcomes, and on voluntariness.",
    "answer": "Assimilation = low heritage maintenance WITH successful contact/participation in the larger society (belongs to the new culture); intermediate adaptation outcomes; often chosen. Marginalization = low heritage maintenance AND no connection to the larger society (belongs to neither); the WORST adaptation and highest-risk profile; typically imposed — discrimination blocks entry while heritage ties erode. The difference is whether the second anchor (larger society) actually holds.",
    "type": "compare",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "acculturation",
    "cluster": "acculturation-strategies",
    "bloom_level": "analyze"
  },
  {
    "id": "u4-accult-society-recall-01",
    "prompt": "Berry pairs each individual acculturation strategy with a society-level condition. Give the four pairings.",
    "answer": "Integration ↔ multiculturalism (society allows dual belonging). Assimilation ↔ melting pot (society demands absorption). Separation ↔ segregation (society imposes distance). Marginalization ↔ exclusion (society blocks entry while heritage ties erode). Point: the individual's 'choice' of strategy is constrained by the receiving society's openness.",
    "type": "recall",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "acculturation",
    "cluster": "acculturation-strategies",
    "bloom_level": "understand"
  },
  {
    "id": "u4-accult-family-vignette-01",
    "prompt": "Parents bring in their 15-year-old, immigrated with them at age 6, as a 'defiant teenager': she refuses to speak the heritage language at home, resists family obligations, and calls her parents' rules 'not normal here.' Using acculturation theory (and a systems lens), reframe what may be happening.",
    "answer": "A parent–child acculturation gap: children typically acculturate faster than parents, so the family holds two different strategies under one roof (daughter moving toward assimilation/integration; parents toward maintenance/separation). The 'defiance' may be a family-level acculturative strain carried by the teenager — the identified patient (family-systems lens) — rather than an individual conduct problem. Assessment should map each member's acculturation position, not just the teen's behavior.",
    "type": "vignette",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "acculturation",
    "cluster": "acculturation-strategies",
    "bloom_level": "analyze"
  },
  {
    "id": "u4-accult-critique-01",
    "prompt": "Give two standard critiques of Berry's fourfold acculturation model, and state how a counselor should hold the model in light of them.",
    "answer": "1) The categories are static and context-blind — real people integrate at work and separate at home, and strategies shift over time. 2) It can overstate free choice — the receiving society's openness (multiculturalism vs. exclusion) constrains which strategies are even available. Hold it as a vocabulary for describing patterns and starting assessment conversations, not as a personality typing to file clients under.",
    "type": "explain",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "acculturation",
    "cluster": "acculturation-strategies",
    "bloom_level": "evaluate"
  },
  {
    "id": "u4-helpseek-recall-01",
    "prompt": "Summarize the U.S. mental-health service disparity data this unit is built on: treatment rates, dropout, and two contributing barriers beyond cost.",
    "answer": "Among U.S. adults with mental disorders, racial/ethnic minority clients are roughly HALF as likely as White clients to receive treatment, and those who begin are MORE likely to drop out before completing it. Contributing barriers include higher stigma in several minority communities, provider mistrust, language access, and culturally different understandings of distress and of whom one appropriately turns to for help.",
    "type": "recall",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "help-seeking",
    "bloom_level": "remember"
  },
  {
    "id": "u4-worldview-explain-01",
    "prompt": "Explain the claim 'counseling is itself a cultural practice,' with two concrete features of counseling that are culturally specific rather than universal.",
    "answer": "Counseling packages culturally particular assumptions as if they were neutral: e.g., (1) disclosing private feelings to a paid stranger is help (in many cultures, private matters stay in the family and telling outsiders is shameful or disloyal); (2) the individual, seen alone, is the unit of treatment (vs. family-as-unit norms); also 'talking' as the healing mechanism, and emotional expression as health. A client for whom these are foreign isn't resisting treatment — the treatment format itself is culturally strange.",
    "type": "explain",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "help-seeking",
    "bloom_level": "understand"
  },
  {
    "id": "u4-helpseek-stance-01",
    "prompt": "STANCE PROBE. Your client has canceled twice; today he says his family believes these matters should be handled privately, not with a stranger. Your case notes draft reads 'client is ambivalent/resistant to treatment.' What's wrong with that formulation, and what would you say in session instead?",
    "answer": "It pathologizes a cultural norm as an individual symptom. His hesitancy may be a REASONABLE cultural position — in many communities, taking family matters to an outsider is genuinely not done. Instead, name and work with the norm: 'In a lot of families, bringing something like this to an outsider isn't done — it can even feel disloyal. If some of that's true for you, it makes sense this feels strange. What might getting support look like in a way that doesn't cost you your family's respect?' Formulation and stance both shift from 'overcoming resistance' to negotiating a culturally workable form of help.",
    "type": "vignette",
    "source_page": "wiki/concept-acculturation.md",
    "topic": "help-seeking",
    "bloom_level": "evaluate"
  }
]
```

## Privilege, power & broaching

```json
[
  {
    "id": "u4-privilege-cloze-01",
    "prompt": "McIntosh (1989) defined privilege as 'an invisible package of {{unearned assets}}' — the knapsack metaphor.",
    "answer": "unearned assets",
    "type": "cloze",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "privilege",
    "bloom_level": "remember"
  },
  {
    "id": "u4-privilege-explain-01",
    "prompt": "McIntosh's account gives privilege two defining properties. Name both, and explain why the second one means counselor self-awareness must be deliberately trained rather than assumed.",
    "answer": "Privilege is (1) UNEARNED — conferred by group membership, not merit — and (2) INVISIBLE TO ITS HOLDER — experienced as simply 'normal,' the way things are. Because it is invisible from the inside, introspection alone won't surface it: the privileged counselor's defaults feel like neutral reality, not like a culture. That's why awareness is a trained discipline (cultural autobiography, supervision, feedback) rather than a natural byproduct of good intentions.",
    "type": "explain",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "privilege",
    "bloom_level": "understand"
  },
  {
    "id": "u4-privilege-power-recall-01",
    "prompt": "Before culture even enters, the counseling dyad is already a power asymmetry. List three built-in asymmetries — then add the further asymmetry of perception that a marginalized client may bring.",
    "answer": "Built-in: one person discloses while the other doesn't; one is in distress while the other holds diagnostic language, records, and fees; the counselor holds reporting/gatekeeping power (Unit 3). Perceptual asymmetry: the client may have spent a lifetime learning to read the privileged group accurately as a survival skill, while the counselor never needed the reverse — assume the client sees you more clearly than you see them.",
    "type": "recall",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "privilege",
    "bloom_level": "understand"
  },
  {
    "id": "u4-privilege-stance-01",
    "prompt": "STANCE PROBE. A counselor opens a first session with a Black client: 'I want to acknowledge my white privilege and the harm my community has caused yours. I have a lot of work to do, and I'm committed to doing it.' The client shifts uncomfortably. What went wrong, and what is the clinical use of privilege-awareness instead?",
    "answer": "The counselor confessed privilege AT the client — recentering the session on the counselor's moral status and implicitly handing the client the job of granting absolution. That's performance, not humility (self-focused, not other-oriented). The clinical use of privilege-awareness is quieter: it calibrates your hypotheses (is this 'resistance' or a rational read of systems that have burned them?), your broaching (invite, don't presume), and your advocacy. The client's session stays about the client.",
    "type": "vignette",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "privilege",
    "bloom_level": "evaluate"
  },
  {
    "id": "u4-broach-recall-01",
    "prompt": "Define broaching (Day-Vines), and explain why counselor silence about an obvious cultural difference is not a neutral choice.",
    "answer": "Broaching = the counselor's ability to consider — and RAISE — how race, ethnicity, culture, and other sociopolitical factors bear on the client's concerns, rather than waiting for the client to risk the topic first. Silence isn't neutral because the client is often scanning for whether this counselor can handle the topic: an unbroached difference reads as 'we don't talk about that here,' which suppresses material and erodes trust.",
    "type": "recall",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "broaching",
    "cluster": "broaching-styles",
    "bloom_level": "understand"
  },
  {
    "id": "u4-broach-recall-02",
    "prompt": "Name the five styles on Day-Vines' broaching continuum, in order, with a phrase for each.",
    "answer": "Avoidant (never raises culture) → isolating (broaches once, ritually, never returns) → continuing/incongruent (keeps trying but awkward and mechanical) → integrated/congruent (raises culture naturally where it bears on the work; can stay in the conversation) → infusing (cultural responsiveness extends beyond sessions into the counselor's whole professional life).",
    "type": "recall",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "broaching",
    "cluster": "broaching-styles",
    "bloom_level": "remember"
  },
  {
    "id": "u4-broach-vignette-01",
    "prompt": "At intake, a counselor tells every minority client, 'I want you to know this is a safe space for people of all backgrounds' — reading it in roughly those words each time — and then never raises culture again in the entire course of treatment. Which broaching style is this?",
    "options": [
      "Isolating — a one-time, ritual broach that is never returned to",
      "Avoidant — the counselor refuses to raise cultural topics",
      "Continuing/incongruent — repeated but awkward attempts",
      "Integrated/congruent — culture raised where relevant"
    ],
    "correct": "Isolating — a one-time, ritual broach that is never returned to",
    "answer": "Isolating: the box is checked once, mechanically, then closed. Not avoidant — a broach did occur; avoidant never raises it at all. The tell is the combination of ritual delivery and zero follow-through.",
    "type": "mcq",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "broaching",
    "cluster": "broaching-styles",
    "bloom_level": "apply"
  },
  {
    "id": "u4-broach-vignette-02",
    "prompt": "A counselor-in-training keeps trying to raise race with her client — several sessions, visibly effortful — but it comes out stilted and scripted ('So... how is your, um, cultural identity impacting this?'), and she can't sustain the conversation when the client engages. Which broaching style, and what does the continuum say about her trajectory?",
    "options": [
      "Continuing/incongruent — persistent but mechanical; a normal developmental stage en route to congruence",
      "Isolating — she broached once and moved on",
      "Avoidant — her awkwardness means she is avoiding the topic",
      "Infusing — she is working on it outside sessions"
    ],
    "correct": "Continuing/incongruent — persistent but mechanical; a normal developmental stage en route to congruence",
    "answer": "Continuing/incongruent: genuine, repeated effort without integration yet — technique without ease. The continuum parallels the counselor's own identity development: you broach at the depth you've done your own work, so the path forward is her own awareness work (and reps), not abandoning the attempts.",
    "type": "mcq",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "broaching",
    "cluster": "broaching-styles",
    "bloom_level": "apply"
  },
  {
    "id": "u4-broach-compare-01",
    "prompt": "Distinguish integrated/congruent broaching from infusing — where does each 'live,' and why is infusing the endpoint of the continuum?",
    "answer": "Integrated/congruent lives INSIDE sessions: the counselor raises culture naturally where it bears on the work and can stay in the conversation substantively. Infusing extends BEYOND the counseling hour: cultural responsiveness becomes part of the counselor's whole professional life (advocacy, institutional work, how they practice everywhere). It's the endpoint because it mirrors full identity development — cultural responsiveness stops being a session technique and becomes who the professional is; it also dovetails with the MSJCC's advocacy domain.",
    "type": "compare",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "broaching",
    "cluster": "broaching-styles",
    "bloom_level": "analyze"
  },
  {
    "id": "u4-broach-production-01",
    "prompt": "PRODUCTION REP. You are a White counselor; your new client is a Black man presenting with work stress who has mentioned being the only Black manager on his floor. Write, in your own words, a congruent broach — 2 to 4 sentences you would actually say. It should (a) name the difference, (b) name your limits, and (c) invite rather than presume relevance.",
    "answer": "Model: 'You mentioned being the only Black manager on your floor. I'm aware I'm a White counselor, and there may be parts of that experience I'll need you to teach me. Some of the stress you're describing may have to do with race — or it may not — and I'm open to it either way. How does it feel to be talking about this with me?' Grade yourself on the three moves: names the difference; owns limits without self-flagellation; leaves the client in charge of whether race is on the table ('it may not').",
    "type": "vignette",
    "source_page": "wiki/concept-privilege-power.md",
    "topic": "broaching",
    "cluster": "broaching-styles",
    "bloom_level": "apply"
  },
  {
    "id": "u4-autobiography-production-01",
    "prompt": "PRODUCTION REP (the syllabus practice rep, one slice). Write one paragraph of your cultural autobiography on ASKING FOR HELP: in the culture you grew up in, who was it acceptable to take a personal problem to, what happened to people who took private matters outside the family/community, and what does that history predispose you to assume about clients who hesitate to open up?",
    "answer": "Self-graded. A strong paragraph does three things: names concrete norms (not 'we were pretty open' but who/what/when), treats them as A culture rather than THE default ('in my house, self-reliance was moralized' vs. 'I'm just independent'), and derives a specific counter-transference risk (e.g., 'I'm predisposed to read help-refusal as dysfunction' or 'to over-respect privacy and under-broach'). The point of the rep is seeing your own water — the sections that feel like 'just how things are' are the blind spots.",
    "type": "explain",
    "source_page": "wiki/unit04-multicultural.md",
    "topic": "privilege",
    "bloom_level": "apply"
  }
]
```

## Microaggressions & the debate

```json
[
  {
    "id": "u4-microagg-recall-01",
    "prompt": "Give Sue et al.'s (2007) definition of racial microaggressions, and the three features that do the conceptual work.",
    "answer": "'Brief and commonplace daily verbal, behavioral, or environmental indignities, whether intentional or UNINTENTIONAL, that communicate hostile, derogatory, or negative racial slights and insults.' Three working features: they are SMALL (each instance deniable), CUMULATIVE (the cost is the drip, not the drop), and usually delivered by people who believe themselves unprejudiced (which ties them to the invisibility of privilege).",
    "type": "recall",
    "source_page": "wiki/concept-microaggressions.md",
    "topic": "microaggressions",
    "cluster": "microaggression-types",
    "bloom_level": "remember"
  },
  {
    "id": "u4-microagg-cloze-01",
    "prompt": "Sue's taxonomy: microassault (explicit, usually conscious derogation), microinsult (subtle demeaning of identity), and {{microinvalidation}} (negating or nullifying the person's experiential reality).",
    "answer": "microinvalidation",
    "type": "cloze",
    "source_page": "wiki/concept-microaggressions.md",
    "topic": "microaggressions",
    "cluster": "microaggression-types",
    "bloom_level": "remember"
  },
  {
    "id": "u4-microagg-vignette-01",
    "prompt": "A colleague tells a Black attorney after a presentation: 'You're so articulate!' In Sue's taxonomy this is the textbook example of which type — and what makes it that type rather than a compliment?",
    "options": [
      "Microinsult — the compliment contains a demeaning low expectation about the person's group",
      "Microassault — an explicit, conscious derogation",
      "Microinvalidation — it negates the person's experiential reality",
      "None — it is simply a compliment"
    ],
    "correct": "Microinsult — the compliment contains a demeaning low expectation about the person's group",
    "answer": "Microinsult: subtle rudeness/insensitivity that demeans identity — an insult wearing a compliment's clothes. The demeaning content is the embedded surprise ('articulate — for one of them'). Not a microassault (no conscious hostile intent) and not a microinvalidation (it doesn't negate her account of her own experience).",
    "type": "mcq",
    "source_page": "wiki/concept-microaggressions.md",
    "topic": "microaggressions",
    "cluster": "microaggression-types",
    "bloom_level": "apply"
  },
  {
    "id": "u4-microagg-vignette-02",
    "prompt": "A client describes a racist encounter at work. Her counselor responds warmly: 'I'm sure they didn't mean anything by it — and honestly, I don't even see color; I just see people.' Which microaggression type(s) has the counselor just committed?",
    "options": [
      "Microinvalidation (twice) — both moves negate the client's experiential reality",
      "Microinsult — the counselor demeaned the client's identity",
      "Microassault — the counselor consciously derogated the client",
      "None — the counselor was being supportive"
    ],
    "correct": "Microinvalidation (twice) — both moves negate the client's experiential reality",
    "answer": "Microinvalidation, twice, in a warm voice: 'they didn't mean anything' explains her reality away; 'I don't see color' erases the racial dimension of her experience altogether. This type is the counselor's occupational hazard because it can be delivered as reassurance — and in-session it is an alliance rupture with clinical consequences.",
    "type": "mcq",
    "source_page": "wiki/concept-microaggressions.md",
    "topic": "microaggressions",
    "cluster": "microaggression-types",
    "bloom_level": "apply"
  },
  {
    "id": "u4-microagg-compare-01",
    "prompt": "Microinsult vs. microinvalidation — the two 'often unconscious' types. Distinguish them by what each DOES to the target, with one example of each.",
    "answer": "Microinsult DEMEANS: it communicates rudeness or a low valuation of the person's identity ('you're so articulate'; asking the Latina physician when the doctor will arrive). Microinvalidation ERASES: it negates or nullifies the person's experiential reality ('I don't see color'; 'anyone can succeed if they work hard'; 'where are you REALLY from?' — which erases belonging). Test: does the remark put the person down (insult) or tell them their reality didn't happen (invalidation)? Microassault differs from both by conscious intent.",
    "type": "compare",
    "source_page": "wiki/concept-microaggressions.md",
    "topic": "microaggressions",
    "cluster": "microaggression-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u4-microagg-repair-01",
    "prompt": "Your client says: 'When you called my standards for my kids \"maybe a little intense,\" it felt like you were writing off how our family does education.' You reply: 'Oh — that's not what I meant at all! I'm honestly the least judgmental person about parenting. I meant intense in a good way!' Critique your reply, then produce a better one.",
    "answer": "The reply denies, defends the counselor's innocence, and explains the client's reaction away — committing a microinvalidation WHILE apologizing for one, and recentering the counselor. Repair version: 'Thank you for telling me — I can see that landed as a judgment on your family's values, and I'm sorry. I think I was measuring against my own defaults without noticing. Can you tell me more about what those standards mean in your family?' Own it briefly, name the mechanism, return the floor. Ruptures repaired this way can strengthen the alliance — the client learns difference is discussable here.",
    "type": "vignette",
    "source_page": "wiki/concept-microaggressions.md",
    "topic": "microaggressions",
    "cluster": "microaggression-types",
    "bloom_level": "evaluate"
  },
  {
    "id": "u4-microagg-critique-01",
    "prompt": "Summarize Lilienfeld's (2017) critique of the microaggression research program — at least three specific objections — plus Sue's response, and state how a practicing counselor can coherently hold both sides.",
    "answer": "Objections: definitions are ELASTIC (almost anything qualifies post hoc); classification rests on SUBJECTIVE REPORT alone (no observer-independent criteria); the 'AGGRESSION' label imputes motives the data can't show; same-group members disagree about whether a remark is offensive; the causal harm claim rests on correlational self-report designs. He proposed the neutral term 'perceived racial slight.' Sue's rejoinder conceded many points while defending documentation of lived experience (Williams 2019 later answered Lilienfeld point-by-point). Coherent position: the PHENOMENON (subtle, cumulative, deniable slights that wear on people) is well-attested and clinically real; the research program's strong causal/taxonomic claims outrun current evidence. In session the debate barely matters — a perceived slight ruptures the alliance whatever it's named, and repair is the same move.",
    "type": "explain",
    "source_page": "wiki/concept-microaggressions.md",
    "topic": "microaggressions",
    "cluster": "microaggression-types",
    "bloom_level": "evaluate"
  },
  {
    "id": "u4-microagg-clinical-analyze-01",
    "prompt": "Connect microaggressions to two other constructs: why is an in-session microaggression best understood as an alliance rupture (Unit 1), and how might microaggressions help explain the minority dropout gap (this unit)?",
    "answer": "Alliance rupture: an in-session microaggression damages Bordin's bond and can covertly break task/goal agreement — the client recalibrates how safe and understood they are, often without saying so; unrepaired, engagement quietly dies. Dropout: minority clients already face higher barriers to arriving; if early sessions add microinvalidations ('I don't see color') from a well-meaning counselor, termination is a rational exit — making microaggressions one plausible mechanism behind the disproportionate minority dropout rates. Repair skill is therefore retention infrastructure, not etiquette.",
    "type": "explain",
    "source_page": "wiki/concept-microaggressions.md",
    "topic": "microaggressions",
    "cluster": "microaggression-types",
    "bloom_level": "analyze"
  }
]
```
