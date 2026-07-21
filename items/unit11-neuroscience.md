# Unit 11 items — Neuroscience & Biological Bases of Behavior

Source of truth for Unit 11 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This unit's job is a **working mental model** of the
brain/body in mental health — enough to answer client questions responsibly, coordinate with
prescribers, and refer — so the items lean on **discrimination** (which neurotransmitter / which ANS
branch / which stress axis / which medication class?) and on the unit's **stance thread**: *biology
is one lens, not the master lens; you educate, coordinate, and refer, but never prescribe; and
talking is itself biological.* Item ids use the `u11-` prefix. Clusters: `neurotransmitters`,
`autonomic-branches`, `stress-systems`, `psychotropic-classes` (the prime interleaving/differential
set). Neuroplasticity/"therapy changes the brain" items are the unit's **throughline** and are
intentionally unclustered. See generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## Neurotransmitters & neurotransmission (cluster: neurotransmitters)

```json
[
  {
    "id": "u11-six-nts-recall-01",
    "prompt": "Name the six neurotransmitters worth knowing for counseling, and for each say whether it is primarily excitatory, inhibitory, or modulatory.",
    "answer": "GLUTAMATE — the master EXCITATORY (the brain's main 'go'); GABA — the master INHIBITORY (the main 'stop'/brake); DOPAMINE — modulatory (reward/motivation, movement, executive function); SEROTONIN — modulatory (mood, sleep, appetite, gut); NOREPINEPHRINE — modulatory (arousal, alertness, stress); ACETYLCHOLINE — mostly excitatory (muscle movement, memory, the parasympathetic transmitter). The key framing: glutamate and GABA carry most of the traffic; dopamine and serotonin TUNE it (modulators), which is why 'your serotonin is low' treats a fine-tuning knob like the main power supply.",
    "type": "recall",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "key-neurotransmitters",
    "cluster": "neurotransmitters",
    "bloom_level": "remember"
  },
  {
    "id": "u11-gaba-glutamate-cloze-01",
    "prompt": "The brain runs on a balance of an accelerator and a brake: the principal EXCITATORY neurotransmitter is {{glutamate}}, and the principal INHIBITORY neurotransmitter is GABA.",
    "answer": "glutamate. Glutamate is the main 'go' signal (and the primary mediator of plasticity); GABA is the main 'stop' signal (~40% of inhibitory processing) — the system benzodiazepines and alcohol enhance.",
    "type": "cloze",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "glutamate-excitatory",
    "cluster": "neurotransmitters",
    "bloom_level": "remember"
  },
  {
    "id": "u11-gaba-glutamate-compare-01",
    "prompt": "Contrast glutamate and GABA — the two neurotransmitters that carry most of the brain's traffic — and explain why they, rather than serotonin or dopamine, are called the workhorses.",
    "answer": "GLUTAMATE is the master EXCITATORY transmitter (makes neurons more likely to fire — the accelerator, central to learning/memory and plasticity); GABA is the master INHIBITORY transmitter (makes neurons less likely to fire — the brake, ~40% of inhibitory processing). They're the WORKHORSES because most of the brain actually runs on this excitation/inhibition balance — they carry the bulk of the signaling. Serotonin and dopamine are MODULATORS: they don't carry most of the traffic, they fine-tune it. That distinction is the seed of the myth-busting later: framing depression as 'low serotonin' treats a tuning knob as if it were the main power supply.",
    "type": "compare",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "glutamate-vs-gaba",
    "cluster": "neurotransmitters",
    "bloom_level": "analyze"
  },
  {
    "id": "u11-dopamine-roles-explain-01",
    "prompt": "A client says 'dopamine is the pleasure chemical, right?' Explain why that's too narrow by naming dopamine's several roles and their clinical tie-ins.",
    "answer": "'Pleasure chemical' captures one slice. Dopamine is a modulator involved in REWARD and MOTIVATION (the wanting/seeking system, central to addiction's reward circuit), MOVEMENT (its loss in the nigrostriatal pathway causes Parkinson's), and EXECUTIVE FUNCTION/attention (implicated in ADHD). Clinically: TOO MUCH mesolimbic dopamine activity is linked to PSYCHOSIS (antipsychotics block dopamine D2 receptors); TOO LITTLE nigrostriatal dopamine causes Parkinson's. So dopamine isn't a simple 'feel-good' dial — it's a multi-purpose modulator for motivation, movement, and salience, which is why the same system shows up in reward, ADHD, Parkinson's, and schizophrenia.",
    "type": "explain",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "dopamine-roles",
    "cluster": "neurotransmitters",
    "bloom_level": "understand"
  },
  {
    "id": "u11-serotonin-modulator-explain-01",
    "prompt": "Explain what it means to call serotonin a 'modulator,' and note the fact that surprises most people about where serotonin is.",
    "answer": "Calling serotonin a MODULATOR means it doesn't carry most of the brain's signal traffic (glutamate and GABA do that); instead it TUNES or biases activity across circuits — influencing mood, sleep, appetite, and more. The surprising fact: the large majority of the body's serotonin (~90%) is in the GASTROINTESTINAL tract, not the brain — it's a gut regulator as much as a brain chemical. The 'modulator, not main supply' framing matters clinically: it's why the simple 'depression = low serotonin, so top it up' story doesn't hold together (a tuning knob isn't a fuel gauge).",
    "type": "explain",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "serotonin-modulator",
    "cluster": "neurotransmitters",
    "bloom_level": "understand"
  },
  {
    "id": "u11-norepinephrine-apply-01",
    "prompt": "A client on an SNRI for both depression and chronic pain asks what the 'NE' part does. Using norepinephrine's roles, give a plain-language answer and note where else in the body this same chemical works.",
    "answer": "Norepinephrine (NE) is the arousal/alertness/attention and stress-response transmitter — it sharpens focus and helps the body gear up. In an SNRI, boosting NE (on top of serotonin) is thought to add benefit for energy/attention and for some pain pathways. The same chemical is the SYMPATHETIC nervous system's main transmitter at the organs — the 'fight or flight' messenger — so it links the brain's arousal system to the body's (see the autonomic nervous system). Plain version for the client: 'It nudges up the system that handles alertness and stress signaling — in the brain and in the body's fight-or-flight wiring.' (And: bring the specifics to your prescriber.)",
    "type": "vignette",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "norepinephrine-roles",
    "cluster": "neurotransmitters",
    "bloom_level": "apply"
  },
  {
    "id": "u11-mechanism-mcq-01",
    "prompt": "An SSRI raises serotonin in the synapse not by mimicking it and not by blocking its receptor, but by blocking the pump that clears it away. Which drug-action category is this?",
    "options": [
      "Reuptake inhibitor",
      "Receptor agonist",
      "Receptor antagonist",
      "Positive allosteric modulator"
    ],
    "correct": "Reuptake inhibitor",
    "answer": "This is a REUPTAKE INHIBITOR: it blocks the transporter that pumps serotonin back into the sending neuron, so the transmitter lingers and keeps acting (an INDIRECT way to turn the system up). An AGONIST mimics/boosts a transmitter directly; an ANTAGONIST blocks a receptor (e.g., antipsychotics block dopamine D2); a POSITIVE ALLOSTERIC MODULATOR (e.g., a benzodiazepine on GABA-A) makes the receptor more responsive to the real transmitter without acting on its own. Owning these four mechanisms is what lets you make sense of the whole medication map.",
    "type": "mcq",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "reuptake-inhibitor",
    "cluster": "neurotransmitters",
    "bloom_level": "apply"
  },
  {
    "id": "u11-antagonist-cloze-01",
    "prompt": "A drug that blocks a receptor so the neurotransmitter can't act — turning that system DOWN — is an antagonist. Antipsychotics work this way: they are dopamine (specifically D2) {{antagonists}}.",
    "answer": "antagonists. Antipsychotics block dopamine D2 receptors, damping the aberrant-salience signaling linked to positive psychotic symptoms — the opposite move from an agonist (which would turn dopamine up).",
    "type": "cloze",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "antagonist-mechanism",
    "cluster": "neurotransmitters",
    "bloom_level": "remember"
  },
  {
    "id": "u11-delayed-onset-analyze-01",
    "prompt": "An SSRI raises synaptic serotonin within hours, yet its antidepressant effect takes 2–6 weeks. Explain why this 'immediate-effect / delayed-benefit gap' is evidence against the simple 'low serotonin, top it up' story.",
    "answer": "If depression were just low serotonin and the drug just raised it, mood should improve within a day — because the serotonin rise IS immediate. It doesn't; the benefit takes weeks. That lag implies the therapeutic action comes not from the raised chemical itself but from SLOW, DOWNSTREAM ADAPTATIONS the raised serotonin sets in motion — receptor/autoreceptor changes, increased BDNF (a growth factor), and synaptic plasticity/neurogenesis. In other words the medication seems to work by helping the brain REWIRE over weeks (neuroplasticity), the same route therapy works — not by refilling a depleted tank. The timing is the tell that 'imbalance corrected' is the wrong model.",
    "type": "explain",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "delayed-onset-gap",
    "cluster": "neurotransmitters",
    "bloom_level": "analyze"
  },
  {
    "id": "u11-nt-imbalance-oversimplified-evaluate-01",
    "prompt": "Evaluate the everyday claim that mental disorders are caused by 'having too much or too little of a brain chemical.'",
    "answer": "It's a seductive oversimplification that's mostly wrong as stated. Problems: (1) the big carriers of brain signaling are glutamate/GABA, while the 'famous' chemicals (serotonin, dopamine) are MODULATORS that tune circuits, not simple level-gauges; (2) for depression specifically, the serotonin/'chemical imbalance' theory is NOT supported by the evidence; (3) the immediate-effect/delayed-benefit gap of antidepressants shows the story isn't 'level low → raise level → fixed.' Disorders involve circuits, networks, plasticity, development, and context — not a single dial set wrong. The kernel of truth: neurotransmission is genuinely involved and medications that act on it can help. The error is collapsing a complex, networked, experience-shaped system into one chemical being 'off' — which is also clinically deflating (it tells a client they're a broken part, not a life to understand and change).",
    "type": "explain",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "imbalance-oversimplified",
    "cluster": "neurotransmitters",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-benzo-target-apply-01",
    "prompt": "A benzodiazepine calms a person down within minutes. Which neurotransmitter system is it acting on, and is it turning that system up or down (in terms of the brain's overall activity)?",
    "answer": "It acts on the GABA system — the brain's master INHIBITORY (brake) transmitter. A benzodiazepine is a positive allosteric modulator of the GABA-A receptor: it makes the receptor MORE responsive to GABA, amplifying inhibition. So in terms of overall brain activity it turns things DOWN (more braking) — which is the sedating/anxiolytic effect. (It doesn't open the channel on its own; it only boosts GABA's own action — which is why it's a modulator, not an agonist.)",
    "type": "vignette",
    "source_page": "wiki/concept-neuron-neurotransmission.md",
    "topic": "benzo-gaba-target",
    "cluster": "neurotransmitters",
    "bloom_level": "apply"
  }
]
```

## The autonomic nervous system (cluster: autonomic-branches)

```json
[
  {
    "id": "u11-ans-branches-recall-01",
    "prompt": "Name the two branches of the autonomic nervous system, and for each give its nickname, its anatomical origin, and its main transmitter at the target organ.",
    "answer": "(1) SYMPATHETIC — nickname 'fight or flight'; anatomy THORACOLUMBAR (spinal cord T1–L2); main transmitter at the organ NOREPINEPHRINE (adrenergic). (2) PARASYMPATHETIC — nickname 'rest and digest'; anatomy CRANIOSACRAL (cranial nerves III/VII/IX/X and sacral S2–S4); main transmitter ACETYLCHOLINE (muscarinic). They work as an antagonistic seesaw to keep the body in homeostasis. (Wrinkle: acetylcholine also runs the first relay of BOTH branches, so it isn't cleanly 'sympathetic = NE only.')",
    "type": "recall",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "ans-two-branches",
    "cluster": "autonomic-branches",
    "bloom_level": "remember"
  },
  {
    "id": "u11-adrenal-medulla-cloze-01",
    "prompt": "The sympathetic branch has a hormonal shortcut: sympathetic fibers stimulate the adrenal medulla to release {{epinephrine}} (adrenaline) straight into the bloodstream — which is why a fright hits the whole body within a second or two.",
    "answer": "epinephrine (adrenaline). This fast, blood-borne arm is the SAM axis (sympathetic-adrenal-medullary), the 'seconds' half of the two-speed stress response.",
    "type": "cloze",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "adrenal-medulla-epinephrine",
    "cluster": "autonomic-branches",
    "bloom_level": "remember"
  },
  {
    "id": "u11-sns-pns-compare-01",
    "prompt": "Contrast the sympathetic and parasympathetic branches on their job and their bodily effects (heart rate, pupils, digestion), and state the 'seesaw' principle that governs them.",
    "answer": "SYMPATHETIC ('fight or flight') MOBILIZES for threat/effort: heart rate UP, pupils DILATE, airways OPEN, digestion SHUTS DOWN, glucose and blood sent to big muscles. PARASYMPATHETIC ('rest and digest') CONSERVES and restores: heart rate DOWN, pupils CONSTRICT, salivation and digestion RAMP UP. The seesaw principle: the two are ANTAGONISTIC and usually BOTH partly active, in shifting balance (an accelerator and a brake working moment to moment). Health is flexible tone — the ability to ramp up for a challenge AND to come back down afterward; chronic stress/trauma degrade that recovery, not the ramp-up.",
    "type": "compare",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "sympathetic-vs-parasympathetic",
    "cluster": "autonomic-branches",
    "bloom_level": "analyze"
  },
  {
    "id": "u11-sympathetic-effects-apply-01",
    "prompt": "A client in session suddenly has a pounding heart, dry mouth, cold hands, shallow fast breathing, and tunnel vision. Name the system driving this and explain, physiologically, why these particular symptoms cluster together.",
    "answer": "This is SYMPATHETIC (fight-or-flight) activation — hyperarousal — with the adrenal-medulla adrenaline dump hitting the whole body at once. The symptoms cluster because they're one coordinated program: heart pounds (↑rate/contractility to pump blood to muscles), mouth goes dry and gut shuts down (digestion is deprioritized under threat), hands go cold (blood shunted from skin to big muscles), breathing speeds up (more oxygen for action), and vision narrows (attention locked onto the threat). Naming it as one physiological package — not random scary symptoms — is itself calming, and it points to the intervention: help the body back down (slow exhale/grounding recruits the parasympathetic brake) before doing cognitive work.",
    "type": "vignette",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "sympathetic-symptom-cluster",
    "cluster": "autonomic-branches",
    "bloom_level": "apply"
  },
  {
    "id": "u11-vagus-apply-01",
    "prompt": "Why does coaching a distressed client to breathe out slowly, with a long exhale, actually calm the body — not just distract the mind? Answer at the level of the nerve.",
    "answer": "Because a slow, lengthened EXHALE (also humming, cold water on the face) raises VAGAL TONE — it recruits the vagus nerve (cranial nerve X), which carries the majority of parasympathetic ('rest and digest') output to the heart and lungs. Activating the vagus pulls the autonomic seesaw back toward parasympathetic dominance: heart rate down, arousal down. So grounding and paced breathing aren't gimmicks or mere distraction — they're direct levers on a real physiological system (the parasympathetic brake), which is exactly why body-based regulation belongs alongside talk, not beneath it. It's the mechanism under Unit 8's de-escalation and grounding moves.",
    "type": "explain",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "vagal-tone-breathing",
    "cluster": "autonomic-branches",
    "bloom_level": "apply"
  },
  {
    "id": "u11-which-branch-mcq-01",
    "prompt": "After a big meal on a quiet afternoon, a person feels drowsy, their heart rate is low, and their digestion is active. Which autonomic state predominates?",
    "options": [
      "Parasympathetic ('rest and digest') dominance",
      "Sympathetic ('fight or flight') dominance",
      "Adrenal-medullary (SAM) surge",
      "Tonic immobility / freeze"
    ],
    "correct": "Parasympathetic ('rest and digest') dominance",
    "answer": "Low heart rate + active digestion + drowsiness are the signature of PARASYMPATHETIC dominance ('rest and digest') — the conserve-and-restore branch, run largely by the vagus nerve. Sympathetic dominance and a SAM surge would raise heart rate and SHUT DOWN digestion (the opposite); freeze/tonic immobility is an involuntary threat shutdown, not post-meal relaxation.",
    "type": "mcq",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "which-branch-rest",
    "cluster": "autonomic-branches",
    "bloom_level": "apply"
  },
  {
    "id": "u11-freeze-vignette-01",
    "prompt": "A survivor describes that during an assault she 'went completely still and couldn't move or scream,' and blames herself for not fighting back. Name the response, and give the reframe grounded in the nervous system.",
    "answer": "This is FREEZE / tonic immobility — an INVOLUNTARY, hardwired shutdown under inescapable threat (often described as a dorsal-vagal collapse: a parasympathetic emergency brake slammed down on top of high sympathetic arousal). The reframe: freeze is NOT a choice, not consent, and not weakness — it's an automatic response below conscious control, mediated by the brainstem, that the body deploys when neither fight nor flight is possible. Naming it as automatic physiology ('your nervous system did that FOR you, not something you failed to override') directly lifts the self-blame ('why didn't I fight back?') — and that reframe is often itself therapeutic. (Clinically it presents as hypoarousal: numbness, going far away.)",
    "type": "vignette",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "freeze-not-a-choice",
    "cluster": "autonomic-branches",
    "bloom_level": "apply"
  },
  {
    "id": "u11-freeze-not-rest-analyze-01",
    "prompt": "Both the parasympathetic 'rest and digest' state and the 'freeze' response involve parasympathetic activity, yet they are clinically opposite. Distinguish them.",
    "answer": "REST-AND-DIGEST is the healthy, low-arousal restorative state — the body safely standing down (calm heart rate, active digestion, a sense of ease). FREEZE / tonic immobility is an EMERGENCY shutdown under inescapable threat — often framed as a dorsal-vagal collapse slammed down ON TOP of high sympathetic activation, producing hypoarousal that LOOKS flat but is a threat state, not safety: numbness, dissociation, collapse, 'going far away.' So the tell isn't 'parasympathetic or not' — it's the CONTEXT and the layering: calm safety versus a defensive shutdown co-occurring with alarm. Clinically they call for opposite moves: rest needs nothing; freeze needs gentle re-orienting and re-engagement to bring the person back into the window of tolerance.",
    "type": "compare",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "freeze-vs-rest",
    "cluster": "autonomic-branches",
    "bloom_level": "analyze"
  },
  {
    "id": "u11-polyvagal-evaluate-01",
    "prompt": "A workshop presents polyvagal theory's 'ventral vagal / sympathetic / dorsal vagal' ladder as established brain science. Evaluate how much confidence that framing deserves.",
    "answer": "Hold it as USEFUL LANGUAGE, not established anatomy. Polyvagal theory (Porges) is clinically popular and its vocabulary ('your nervous system feels unsafe / went into shutdown') is a genuinely helpful bridge to clients — it names states in a way people recognize. But its SPECIFIC neurophysiological claims (the evolutionary two-vagus story, the precise mapping of social engagement to a 'ventral vagal' circuit) are SCIENTIFICALLY CONTESTED. So: use the language to build understanding and safety with a client, but don't teach it as proven neuroscience or build a rigid protocol on its literal truth. This is the same 'direction useful, details soft' posture Unit 8 takes toward the window of tolerance and 'the body keeps the score.'",
    "type": "explain",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "polyvagal-contested",
    "cluster": "autonomic-branches",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-homeostasis-understand-01",
    "prompt": "Explain what it means to say the sympathetic and parasympathetic branches maintain 'homeostasis,' and why 'flexible tone' — not permanent calm — is the marker of health.",
    "answer": "HOMEOSTASIS is the body's steady internal balance (heart rate, blood pressure, digestion, temperature), and the two ANS branches maintain it by pushing in OPPOSITE directions — an accelerator (sympathetic) and a brake (parasympathetic) usually both partly on, adjusting moment to moment. Health is NOT permanent parasympathetic calm; it's FLEXIBLE TONE — the capacity to ramp UP appropriately for a real demand and, crucially, to come back DOWN once it passes. A healthy system is responsive and recovers; the problem in chronic stress and trauma is a system that gets stuck up (can't come down) or collapses (freeze) — a loss of flexibility, not the mere presence of arousal.",
    "type": "explain",
    "source_page": "wiki/concept-autonomic-nervous-system.md",
    "topic": "homeostasis-flexible-tone",
    "cluster": "autonomic-branches",
    "bloom_level": "understand"
  }
]
```

## The stress response — SAM, HPA, allostatic load (cluster: stress-systems)

```json
[
  {
    "id": "u11-hpa-chain-recall-01",
    "prompt": "Spell out the HPA axis as a chain (which structure releases what, to what effect), and name the step that acts as the off-switch.",
    "answer": "HYPOTHALAMUS releases CRH → tells the PITUITARY to release ACTH → tells the ADRENAL CORTEX to release CORTISOL → cortisol mobilizes glucose, sharpens attention, and sustains the stress response. The OFF-SWITCH is NEGATIVE FEEDBACK: cortisol (with hippocampal output) feeds back to the hypothalamus/pituitary to shut CRH off. A working stress response turns on fast and turns off cleanly — much stress-related pathology is a failure of the OFF, not the ON.",
    "type": "recall",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "hpa-axis-chain",
    "cluster": "stress-systems",
    "bloom_level": "remember"
  },
  {
    "id": "u11-sam-hpa-cloze-01",
    "prompt": "The stress response runs at two speeds: the fast SAM axis releases {{adrenaline}} (catecholamines) in seconds, while the slower HPA axis releases cortisol over minutes.",
    "answer": "adrenaline (epinephrine/noradrenaline). SAM = the instant jolt (pounding heart, dry mouth) via the adrenal medulla; HPA = the sustained mobilization (energy, wakefulness) via the adrenal cortex and cortisol.",
    "type": "cloze",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "sam-fast-adrenaline",
    "cluster": "stress-systems",
    "bloom_level": "remember"
  },
  {
    "id": "u11-sam-hpa-compare-01",
    "prompt": "Contrast the two stress systems — SAM and HPA — on speed, chemical, and route, and explain how they work together.",
    "answer": "SAM (sympathetic-adreno-medullary): FAST (seconds), chemical = ADRENALINE/noradrenaline (catecholamines), route = nerves → adrenal MEDULLA → bloodstream — the instant jolt. HPA (hypothalamic-pituitary-adrenal): SLOW (minutes), chemical = CORTISOL (a glucocorticoid), route = hormones (CRH→ACTH) → adrenal CORTEX → bloodstream — the sustained mobilization. They work in SEQUENCE and synergy: SAM fires first for the immediate emergency (fight/flight), then HPA follows through to keep energy and focus mobilized for the longer haul, before negative feedback shuts it down. Fast catecholamine surge, then slow cortisol follow-through.",
    "type": "compare",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "sam-vs-hpa",
    "cluster": "stress-systems",
    "bloom_level": "analyze"
  },
  {
    "id": "u11-negative-feedback-explain-01",
    "prompt": "Explain why the negative-feedback loop of the HPA axis is clinically important — i.e., why 'the problem is usually the off-switch, not the on-switch.'",
    "answer": "Negative feedback is the HPA axis's built-in shut-off: cortisol (and hippocampal output) signal back to the hypothalamus/pituitary to stop releasing CRH, ending the stress response once the threat passes. It's clinically important because a stress response is SUPPOSED to fire — turning ON is adaptive and healthy. The pathology is usually in turning OFF: when the loop is worn down or overridden (chronic or early-life stress), the system stays activated or fails to recover cleanly, and it's the FAILURE TO STAND DOWN — not having a stress response at all — that produces wear and tear. So clinically you're rarely trying to eliminate a client's stress response; you're trying to restore its recovery.",
    "type": "explain",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "negative-feedback-offswitch",
    "cluster": "stress-systems",
    "bloom_level": "understand"
  },
  {
    "id": "u11-allostatic-load-explain-01",
    "prompt": "Distinguish 'allostasis' from 'allostatic load' (McEwen), and say which one is the problem.",
    "answer": "ALLOSTASIS = 'stability through change' — the body doesn't hold one fixed set-point but SHIFTS its set-points to meet demand (raising blood pressure, cortisol, glucose for a stressor, then returning them). This is healthy and efficient. ALLOSTATIC LOAD = the cumulative 'wear and tear' the brain and body accrue when the allostatic systems (SAM + HPA) are run TOO OFTEN, TOO LONG, or FAIL TO SHUT OFF — 'how chronic stress gets under our skin and skull.' The PROBLEM is allostatic LOAD (chronic activation), not allostasis (the normal, adaptive adjustment). Slogan version: acute stress is a feature; allostatic load is the bug.",
    "type": "explain",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "allostasis-vs-load",
    "cluster": "stress-systems",
    "bloom_level": "understand"
  },
  {
    "id": "u11-allostatic-load-apply-01",
    "prompt": "A client under two years of relentless work-and-caregiving stress reports tension headaches, gut problems, poor sleep, and constant edginess, and worries 'it's all in my head.' Use the stress-response model to reframe this for them.",
    "answer": "Reframe it as ALLOSTATIC LOAD — the real, whole-body wear-and-tear of a stress system (SAM + HPA) that's been running too hard for too long without fully standing down. The headaches, gut trouble, broken sleep, and edginess are the SOMATIC SIGNATURE of an alarm system stuck in the 'on' position, not imaginary and not weakness. 'It's all in my head' is exactly backwards: it's in the body, produced by a normal system overworked. This validates the physical symptoms, links them to a nameable process, and points to the intervention — recovery and downregulation (rest, the parasympathetic brake, reducing the load) are how the body DISCHARGES allostatic load, which is also the biological case for self-care being a duty, not a luxury.",
    "type": "vignette",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "allostatic-load-somatic",
    "cluster": "stress-systems",
    "bloom_level": "apply"
  },
  {
    "id": "u11-stress-adaptive-evaluate-01",
    "prompt": "Evaluate the assumption behind a client's goal 'I want to get rid of my stress response entirely.'",
    "answer": "The goal is based on a false premise and isn't even desirable. The stress response is an ADAPTIVE, coordinated program that mobilizes the body to meet demands — you WANT it to fire in the face of a real threat or challenge; a person with no stress response would be endangered, not healthy. So the clinical target is not ELIMINATING the response but restoring its REGULATION: firing appropriately to real demands and — crucially — RECOVERING cleanly afterward (the off-switch). The reframe to offer: 'We're not trying to delete your alarm; we're trying to get it to go off at the right times and, especially, to switch back off when the threat has passed.' Naming stress as adaptive-but-dysregulated (not broken) is more accurate and less shaming.",
    "type": "explain",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "stress-is-adaptive",
    "cluster": "stress-systems",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-cortisol-biomarker-evaluate-01",
    "prompt": "A wellness clinic offers a saliva cortisol test that will 'measure your stress and diagnose trauma.' Evaluate this against what the science actually supports.",
    "answer": "Overclaimed and misleading. There is NO clean cortisol biomarker for stress or trauma: findings are INCONSISTENT — some stressed/traumatized populations show ELEVATED cortisol, others BLUNTED/low — and dysregulated HPA responses are 'not consistently associated with psychopathology.' So a single cortisol reading cannot 'measure your stress' in any diagnostic sense, and it certainly cannot diagnose trauma (a clinical, not a lab, determination). The defensible statement is that chronic stress can DYSREGULATE the stress axis — in variable directions — not that 'high cortisol = stress' or that a test reveals a hidden diagnosis. Never let a client (or yourself) treat a cortisol number as a verdict. Direction of the biology is real; the decimals and the diagnostic claims are not.",
    "type": "explain",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "no-clean-cortisol-biomarker",
    "cluster": "stress-systems",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-circuit-mcq-01",
    "prompt": "In the brain circuit that gates the stress response, which structure normally TIME-STAMPS an event as 'past' and helps apply the brakes to the HPA axis — the structure whose under-functioning lets a memory intrude as if it were happening now?",
    "options": [
      "Hippocampus",
      "Amygdala",
      "Prefrontal cortex",
      "Adrenal medulla"
    ],
    "correct": "Hippocampus",
    "answer": "The HIPPOCAMPUS is the context-stamp and part of the brake: it marks events in time ('this already happened') and, being rich in cortisol receptors, INHIBITS the HPA axis (negative feedback). When it under-functions (as in trauma), the memory loses its 'past' tag and intrudes as if NOW, and the HPA brake weakens. The AMYGDALA is the smoke alarm that DRIVES the response; the PREFRONTAL CORTEX is the top-down rational brake; the adrenal medulla is an endocrine gland (adrenaline), not a brain-circuit gate. This is the same circuit Unit 8 draws for trauma — here with the endocrine (HPA) half added.",
    "type": "mcq",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "which-structure-hippocampus",
    "cluster": "stress-systems",
    "bloom_level": "apply"
  },
  {
    "id": "u11-adrenal-fatigue-evaluate-01",
    "prompt": "A client has been told they have 'adrenal fatigue' from chronic stress 'burning out their adrenals,' and asks you about it. Evaluate the concept.",
    "answer": "'Adrenal fatigue' is NOT a recognized medical diagnosis, and the mechanism it claims — that chronic stress exhausts the adrenal glands until they can't make enough cortisol — is not supported by evidence. The scientifically grounded frame for the harms of chronic stress is ALLOSTATIC LOAD (McEwen): multi-system wear-and-tear from stress systems run too long, with cortisol patterns that vary (sometimes high, sometimes blunted) rather than a simple 'burnout to empty.' So: validate the client's real experience of chronic stress and exhaustion — that's genuine — while gently noting that 'adrenal fatigue' is a popular label, not a diagnosis, and that any testing/treatment claims around it should be checked with a physician. (And this is a medical-boundary moment: you don't diagnose or treat it either way.)",
    "type": "explain",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "adrenal-fatigue-not-a-diagnosis",
    "cluster": "stress-systems",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-stress-selfcare-analyze-01",
    "prompt": "Using the allostatic-load model, explain why a counselor's own self-care is better understood as a biological necessity than as a personal indulgence — connecting it to Unit 8.",
    "answer": "Because a counselor is exposed to chronic and vicarious stress, and under the allostatic-load model that exposure produces real, cumulative wear-and-tear whenever the stress systems (SAM + HPA) are activated repeatedly without full recovery. Self-care — rest, downregulation, recovery, the parasympathetic brake — is literally how the body DISCHARGES allostatic load and lets the negative-feedback off-switch do its job. So self-care isn't an indulgence layered on top of the 'real' work; it's the physiological process that prevents the accumulating load from degrading the counselor's health and clinical capacity. This is the biological backing for Unit 8's framing of self-care as an ETHICAL duty (ACA C.2.g) and of burnout prevention as organizational, not just personal.",
    "type": "explain",
    "source_page": "wiki/concept-stress-response.md",
    "topic": "allostatic-load-selfcare",
    "cluster": "stress-systems",
    "bloom_level": "analyze"
  }
]
```

## Psychotropic medication classes (cluster: psychotropic-classes)

```json
[
  {
    "id": "u11-five-classes-recall-01",
    "prompt": "Name the five main psychotropic medication classes and what each primarily treats.",
    "answer": "(1) ANTIDEPRESSANTS (SSRIs, SNRIs, others) — depression AND most anxiety disorders, OCD, PTSD. (2) ANTI-ANXIETY / BENZODIAZEPINES — acute anxiety, panic, insomnia (short-term). (3) ANTIPSYCHOTICS (typical/atypical) — psychosis and schizophrenia, plus bipolar and adjunctive uses. (4) MOOD STABILIZERS (lithium, anticonvulsants) — bipolar disorder (mania + maintenance). (5) STIMULANTS — ADHD and narcolepsy. A high-yield twist: SSRIs/SNRIs — not benzodiazepines — are the FIRST-LINE, long-term treatment for chronic anxiety, because they don't build dependence.",
    "type": "recall",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "five-classes",
    "cluster": "psychotropic-classes",
    "bloom_level": "remember"
  },
  {
    "id": "u11-ssri-onset-cloze-01",
    "prompt": "A counselor's most useful med fact for an anxiety/depression caseload: although an SSRI raises synaptic serotonin within hours, its clinical benefit typically takes about {{4-8 weeks}} to appear, so a client saying 'it's been three days and nothing's changed' needs the timeline explained, not a reason to quit.",
    "answer": "4-8 weeks (roughly 2–6+ weeks). The delay is the tell that the benefit comes from downstream neuroplastic adaptation, not from instantly 'topping up' a chemical — and it's the single most common thing clients misread as 'the medication isn't working.'",
    "type": "cloze",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "ssri-onset-timeline",
    "cluster": "psychotropic-classes",
    "bloom_level": "remember"
  },
  {
    "id": "u11-ssri-vs-benzo-compare-01",
    "prompt": "Clients routinely conflate SSRIs and benzodiazepines because both are 'for anxiety.' Contrast them on mechanism, timeline, dependence risk, and clinical role.",
    "answer": "They're near-opposites. MECHANISM: an SSRI blocks SEROTONIN reuptake (raising serotonin, working via downstream plasticity); a benzodiazepine is a GABA-A positive allosteric modulator (amplifying the brain's main inhibitory brake). TIMELINE: SSRI builds over WEEKS; a benzo acts in MINUTES. DEPENDENCE: SSRIs are essentially NOT dependence-forming; benzodiazepines carry REAL tolerance and dependence (and dangerous withdrawal). ROLE: SSRIs are the FIRST-LINE, daily, long-term/maintenance treatment for chronic anxiety; benzos are for SHORT-TERM or acute/rescue use only. The practical payoff: a client complaining the 'anxiety pill isn't working after three days' is almost certainly on an SSRI and needs the TIMELINE explained — not a switch to something faster and riskier.",
    "type": "compare",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "ssri-vs-benzo",
    "cluster": "psychotropic-classes",
    "bloom_level": "analyze"
  },
  {
    "id": "u11-anxiety-firstline-mcq-01",
    "prompt": "A client with generalized anxiety disorder wants a medication they can take long-term without building dependence. Which class is the first-line, long-term choice?",
    "options": [
      "An SSRI or SNRI (antidepressant)",
      "A benzodiazepine",
      "A stimulant",
      "A typical antipsychotic"
    ],
    "correct": "An SSRI or SNRI (antidepressant)",
    "answer": "Counterintuitively, the first-line LONG-TERM treatment for chronic anxiety is an ANTIDEPRESSANT (SSRI/SNRI), precisely because it doesn't build dependence. Benzodiazepines act fast but are for SHORT-TERM use only because of tolerance/dependence and withdrawal risk. Stimulants would tend to worsen anxiety; antipsychotics aren't a first-line anxiety treatment. (This is a prescriber's decision — but knowing it lets you explain to an anxious client why the psychiatrist chose the 'slow' pill over the fast one.)",
    "type": "mcq",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "anxiety-first-line",
    "cluster": "psychotropic-classes",
    "bloom_level": "apply"
  },
  {
    "id": "u11-benzo-mechanism-explain-01",
    "prompt": "Explain how benzodiazepines work at the receptor, and why that mechanism connects to their risk of tolerance and dependence.",
    "answer": "Benzodiazepines are POSITIVE ALLOSTERIC MODULATORS of the GABA-A receptor: they bind a site distinct from GABA's own and increase the probability the chloride channel opens IN RESPONSE to GABA — they don't open it themselves, they amplify the brain's main inhibitory brake, producing sedation/anxiolysis. The dependence link: with prolonged use the brain ADAPTS to the boosted inhibition (downregulating GABA-A subunits and sensitizing excitatory glutamate) → TOLERANCE (needing more for the same effect) and physical DEPENDENCE. That adaptation is also why WITHDRAWAL is dangerous — removing the drug leaves the brain in a hyper-excitable state (rebound anxiety, insomnia, tremor, and potentially SEIZURES) — so benzos must be TAPERED, never stopped abruptly, and are meant for short-term use.",
    "type": "explain",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "benzo-mechanism-dependence",
    "cluster": "psychotropic-classes",
    "bloom_level": "understand"
  },
  {
    "id": "u11-antipsychotic-d2-explain-01",
    "prompt": "Explain how antipsychotics work in broad strokes, and contrast the main risk of 'typical' (first-generation) versus 'atypical' (second-generation) agents.",
    "answer": "Antipsychotics work chiefly by BLOCKING dopamine D2 receptors, damping the aberrant-salience signaling tied to POSITIVE symptoms (delusions, hallucinations) — which is why they help positive symptoms more than negative/cognitive ones. Risk contrast: TYPICAL (first-generation) agents carry a notable risk of movement side effects, especially TARDIVE DYSKINESIA (involuntary, sometimes irreversible movements) from long-term use; ATYPICAL (second-generation) agents shift the main risk toward METABOLIC effects (weight gain, elevated glucose and lipids), requiring regular metabolic monitoring. (Also: clozapine, for treatment-resistant cases, needs blood monitoring; antipsychotics carry a black-box warning for increased death in older adults with dementia.)",
    "type": "explain",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "antipsychotic-typical-vs-atypical",
    "cluster": "psychotropic-classes",
    "bloom_level": "understand"
  },
  {
    "id": "u11-lithium-apply-01",
    "prompt": "A client with bipolar I mentions their psychiatrist has them on lithium and orders blood tests 'all the time.' Explain to the client, in scope, why the monitoring matters and one hopeful fact about lithium.",
    "answer": "In-scope explanation: lithium is a mood stabilizer with a NARROW THERAPEUTIC WINDOW — the dose that helps and the dose that becomes toxic are close together — so regular blood tests check the lithium LEVEL to keep it in the safe/effective range, and also monitor KIDNEY and THYROID function, which lithium can affect over time. So the frequent labs aren't fussiness; they're how the prescriber keeps it both safe and effective. The hopeful fact: lithium is one of the few psychiatric medications shown to REDUCE SUICIDE RISK in long-term maintenance. (Then stay in your lane: encourage them to keep the monitoring appointments and bring any questions or side effects to their prescriber — you don't advise on the dose.)",
    "type": "vignette",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "lithium-monitoring",
    "cluster": "psychotropic-classes",
    "bloom_level": "apply"
  },
  {
    "id": "u11-which-class-mcq-01",
    "prompt": "A client with bipolar I disorder is entering a manic episode and their prescriber wants a medication for both the acute mania and long-term maintenance. Which class fits?",
    "options": [
      "A mood stabilizer (e.g., lithium)",
      "An SSRI antidepressant",
      "A stimulant",
      "A benzodiazepine for maintenance"
    ],
    "correct": "A mood stabilizer (e.g., lithium)",
    "answer": "A MOOD STABILIZER (lithium or an anticonvulsant; atypical antipsychotics are also used for acute mania) targets mania and provides bipolar maintenance. An SSRI given alone can DESTABILIZE bipolar disorder (risk of flipping into mania), so antidepressant monotherapy is the wrong move here; stimulants would worsen mania; benzodiazepines might be a very short-term adjunct for agitation but are not a maintenance treatment. The tell is 'bipolar mania + maintenance' → mood stabilizer.",
    "type": "mcq",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "which-class-mania",
    "cluster": "psychotropic-classes",
    "bloom_level": "apply"
  },
  {
    "id": "u11-which-class-mcq-02",
    "prompt": "A client experiencing active hallucinations and delusions during a first psychotic episode is referred for medication. Which class most directly targets these positive symptoms?",
    "options": [
      "Antipsychotics",
      "SSRIs",
      "Benzodiazepines",
      "Stimulants"
    ],
    "correct": "Antipsychotics",
    "answer": "ANTIPSYCHOTICS (dopamine D2 antagonists) most directly target the POSITIVE symptoms of psychosis — hallucinations and delusions — by damping aberrant-salience dopamine signaling. SSRIs treat depression/anxiety; benzodiazepines are sedatives (sometimes a short-term adjunct for agitation, but they don't treat psychosis); stimulants can actually WORSEN or precipitate psychosis. The tell is hallucinations/delusions → antipsychotic.",
    "type": "mcq",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "which-class-psychosis",
    "cluster": "psychotropic-classes",
    "bloom_level": "apply"
  },
  {
    "id": "u11-chemical-imbalance-myth-evaluate-01",
    "prompt": "A client says, 'I have a serotonin imbalance, so I just need this pill to fix it.' Evaluate the 'chemical imbalance' framing and describe how you'd respond honestly without discouraging medication.",
    "answer": "The chemical-imbalance framing is NOT supported: a 2022 umbrella review found no consistent evidence that depression is caused by low serotonin (across metabolites, receptors, the transporter, tryptophan-depletion, and gene studies). But antidepressants STILL help many people (all 21 in a major meta-analysis beat placebo, if modestly), likely by helping the brain adapt/rewire over weeks — not by correcting a known deficiency. The honest, hope-preserving response holds BOTH: 'We don't actually think depression is one chemical being low — that didn't hold up. But medication can still genuinely help, probably by helping your brain adapt over a few weeks. And the encouraging part is that therapy and the things you do change the brain the same way — so it's not the pill versus you; it can be both.' This corrects the myth, keeps medication on the table, and restores the client's agency (the framing that distress is a fixed broken part can make people feel MORE helpless). Note: the review is itself contested, so teach it as 'the simple story is wrong,' not 'serotonin is irrelevant.'",
    "type": "explain",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "chemical-imbalance-myth",
    "cluster": "psychotropic-classes",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-antidepressant-efficacy-evaluate-01",
    "prompt": "Evaluate the two opposite claims a counselor hears: 'antidepressants are basically placebos' versus 'antidepressants are a miracle cure.' What does the evidence actually support?",
    "answer": "Both extremes are wrong; the accurate position is in between. Cipriani's network meta-analysis of 21 antidepressants found ALL of them MORE effective than placebo for acute major depression — so they are NOT inert placebos. But the AVERAGE effect is MODEST (a standardized mean difference around 0.3), and it's larger for SEVERE depression than for mild (where the drug-placebo gap narrows). So the honest read: real and genuinely useful for many people — especially in more severe depression — but oversold when pitched as a miracle or as the only real treatment. A counselor's job is to be neither a medication cheerleader nor a skeptic, but accurate: 'They help a lot of people, the effect is real but usually moderate, and they tend to work best combined with therapy and for more severe depression.'",
    "type": "explain",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "antidepressant-efficacy-modest",
    "cluster": "psychotropic-classes",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-discontinuation-apply-01",
    "prompt": "A client who has been on an SNRI for a year feels much better and tells you, 'I'm just going to stop taking it — I don't need it anymore.' What do you say and do, and why?",
    "answer": "Do NOT endorse (or direct) stopping — that's a prescriber decision — and actively steer them to that conversation, because abruptly stopping (especially an SNRI, after long use) commonly causes a real DISCONTINUATION/WITHDRAWAL syndrome (dizziness, 'brain zaps,' flu-like feelings, anxiety, insomnia), which is REDUCED by slow tapering and is easily MISTAKEN FOR RELAPSE. Response: 'It's great you're feeling better — that's exactly the kind of thing to bring to your prescriber, because stopping this one suddenly can cause withdrawal effects, and they can help you taper safely if it's the right time. Let's not change anything until you've talked with them.' You also explore what's driving the wish to stop (side effects? cost? feeling 'fixed'?) and support the coordinated plan. What you never do is tell a client it's fine to stop or how to taper — that's practicing medicine.",
    "type": "vignette",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "discontinuation-dont-advise-stopping",
    "cluster": "psychotropic-classes",
    "bloom_level": "apply"
  },
  {
    "id": "u11-scope-dont-prescribe-vignette-01",
    "prompt": "A client says, 'This SSRI isn't doing much and gives me headaches — do you think I should switch to a different one, or bump up the dose?' Give an in-scope response and name the boundary you're honoring.",
    "answer": "In-scope response: don't recommend a switch or a dose change — that's prescribing, which is outside a counselor's scope. Instead, VALIDATE, EDUCATE enough to inform a prescriber conversation, and REFER/COORDINATE: 'Those headaches and the sense that it's not doing enough are important and exactly what your prescriber needs to hear — sometimes early side effects settle, and sometimes they adjust the medication, but that's their call. Want to plan out what to tell them, and would it help if I coordinated with them (with your okay)?' The boundary honored is SCOPE OF PRACTICE (Unit 3): counselors recognize, educate, coordinate, and refer regarding medication, but never start, stop, change, or second-guess a prescription. Offering to help the client prepare for and get to the prescriber IS the counselor's contribution.",
    "type": "vignette",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "scope-educate-refer",
    "cluster": "psychotropic-classes",
    "bloom_level": "apply"
  },
  {
    "id": "u11-scope-supplements-evaluate-01",
    "prompt": "To be helpful, a counselor is tempted to suggest a client 'try St. John's Wort or some melatonin instead of waiting for the psychiatrist.' Evaluate this.",
    "answer": "It's outside scope and potentially dangerous. Counselors do not prescribe — and that extends to NOT recommending over-the-counter, herbal, or dietary remedies, which are pharmacological interventions outside counseling scope of practice (CACREP is explicit that the medication competency is for referral/consultation, not recommending agents). It's also unsafe specifically: St. John's Wort has serious INTERACTIONS with SSRIs (serotonin syndrome risk) and other drugs. The in-scope move is to ENCOURAGE and PREPARE the client to raise these options with their physician/psychiatrist/pharmacist — 'that's a good question for your prescriber, who can check it against what you're taking' — rather than to supply the recommendation yourself. Good intentions don't expand your scope.",
    "type": "explain",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "scope-no-supplements",
    "cluster": "psychotropic-classes",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-addictive-vs-discontinuation-analyze-01",
    "prompt": "A client insists 'antidepressants are addictive — my friend had terrible withdrawal.' Untangle the two ideas being fused here (addiction vs. discontinuation) so the client gets accurate information.",
    "answer": "Two different things are being fused. ADDICTION (dependence with compulsive use, craving, tolerance, drug-seeking despite harm) is characteristic of BENZODIAZEPINES and STIMULANTS, not standard antidepressants — SSRIs/SNRIs are NOT addictive in that sense (no craving, no compulsive use, no getting 'high'). DISCONTINUATION/WITHDRAWAL SYNDROME is a separate phenomenon: stopping an antidepressant — especially abruptly, after long use, at high dose, or with SNRIs/paroxetine — can cause real physical symptoms (dizziness, 'brain zaps,' flu-like feelings, anxiety) because the brain adapted to the drug. So the friend's 'terrible withdrawal' is real and worth taking seriously, but it's a discontinuation reaction, not evidence the drug is addictive. Accurate message: 'Antidepressants aren't addictive the way some drugs are, but your body does adapt, so you shouldn't stop suddenly — a prescriber can taper you off to avoid those effects.' Keeping the two concepts separate reduces a needless barrier to care.",
    "type": "explain",
    "source_page": "wiki/concept-psychotropic-classes.md",
    "topic": "addiction-vs-discontinuation",
    "cluster": "psychotropic-classes",
    "bloom_level": "analyze"
  }
]
```

## Neuroplasticity & how therapy changes the brain — the throughline (unclustered)

```json
[
  {
    "id": "u11-neuroplasticity-recall-01",
    "prompt": "Define neuroplasticity, and name the three kinds of change it includes.",
    "answer": "NEUROPLASTICITY is the brain's lifelong capacity to reorganize its structure and function in response to experience, learning, and injury. The three kinds of change: (1) forming NEW synaptic connections; (2) STRENGTHENING or WEAKENING/PRUNING existing ones; and (3) in a few regions (like the hippocampus), growing NEW NEURONS (neurogenesis). The key implication: the brain is not fixed hardware — it's shaped by experience and can be reshaped by new experience, which is the biological basis for the possibility of change through therapy.",
    "type": "recall",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "neuroplasticity-definition",
    "bloom_level": "remember"
  },
  {
    "id": "u11-hebbian-cloze-01",
    "prompt": "Hebb's rule, the cellular basis of learning, is captured in the phrase: neurons that {{fire together, wire together}} — repeated co-activation strengthens the synapse between two neurons, while disuse weakens and prunes it.",
    "answer": "fire together, wire together. Repeated co-activation → long-term potentiation (a stronger synapse); disuse → long-term depression / pruning ('use it or lose it'). This is how a skill, a fear, or a relational expectation becomes durable — and, cutting both ways, how a NEW pattern can be wired in with new repeated experience.",
    "type": "cloze",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "hebbian-rule",
    "bloom_level": "remember"
  },
  {
    "id": "u11-kandel-explain-01",
    "prompt": "Lay out Eric Kandel's three-step argument that psychotherapy is a 'biological' treatment.",
    "answer": "(1) LEARNING changes the brain — it alters gene expression and changes the strength and structure of synapses. (2) PSYCHOTHERAPY is a form of learning — of new associations, regulation, narratives, and behaviors. (3) THEREFORE effective psychotherapy produces real, lasting changes in the brain — it is, when it works, a BIOLOGICAL treatment. The payoff: this dissolves the mind/brain and 'real (medical) vs. just psychological' split. The question 'is my problem biological or psychological?' is malformed, because psychological experience IS biological and biological change can come THROUGH psychological means. For a counselor it's the antidote to medication-envy: you're not offering the lesser option, but a different route to the same neuroplastic endpoint.",
    "type": "explain",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "kandel-therapy-is-biological",
    "bloom_level": "understand"
  },
  {
    "id": "u11-baxter-ocd-evaluate-01",
    "prompt": "A skeptic says 'there's no actual evidence that talk therapy changes the brain — that's just a feel-good slogan.' Use Baxter's OCD studies to evaluate the skeptic's claim.",
    "answer": "The skeptic is out of date. Baxter's PET studies in OCD showed that SUCCESSFUL behavior/cognitive-behavior therapy CHANGED metabolism in a specific brain circuit (the caudate nucleus / CSTC loop) — and the change RESEMBLED the change produced by SSRI medication. So 'talking' and 'chemistry' converged on the SAME circuit: two routes to one neuroplastic endpoint, and the therapy-driven change was IMAGED, not imagined. OCD is the cleanest demonstration because it maps onto a single identifiable loop, but imaging reviews find psychotherapy produces measurable brain-function changes across a range of conditions. So 'therapy changes the brain' is an empirical finding, not a slogan. (The honest caveat, held separately: that a region changes shows THAT something changed, not the exact mechanism by which it causes improvement — correlates aren't full mechanism.)",
    "type": "explain",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "baxter-ocd-evidence",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-therapy-vs-med-brain-compare-01",
    "prompt": "Compare how psychotherapy and antidepressant medication each change the brain, and use the comparison to counter the idea that medication is the 'real' treatment and therapy is a soft add-on.",
    "answer": "Both change the brain through NEUROPLASTICITY, and they can land on the same circuits. MEDICATION (e.g., an SSRI) raises a neurotransmitter immediately but produces its benefit over WEEKS via downstream plastic adaptation (receptor changes, BDNF, synaptic plasticity/neurogenesis) — which is why it's slow. THERAPY drives plastic change directly through new learning and experience (Hebbian wiring, neural integration). The OCD PET studies show both routes normalizing the SAME loop. So the 'medication is real, therapy is soft' hierarchy is false: neither is more biological than the other; they're two routes to one kind of endpoint (a rewired brain), and they often COMBINE well. This lets you support a client's medication AND their therapy without implying one is primary — and it reframes therapy as real biological work, not consolation.",
    "type": "compare",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "therapy-vs-medication-brain-change",
    "bloom_level": "analyze"
  },
  {
    "id": "u11-cozolino-social-brain-explain-01",
    "prompt": "Summarize Cozolino's core claims about how psychotherapy heals 'the social brain,' including what he means by neural integration and why a moderate level of arousal matters.",
    "answer": "Cozolino's core claims: (1) Therapy works — across ALL modalities — by promoting NEURAL INTEGRATION: connecting previously disconnected networks (cortical with subcortical, thinking with feeling, top-down regulation with bottom-up alarm), using empathy, affect regulation, narrative construction, and gentle exposure. (This is the common-factors insight in neural terms.) (2) The brain is a SOCIAL ORGAN — relationships BUILD and rebuild the brain across the lifespan, so a warm, attuned, safe therapeutic relationship acts like an ENRICHED ENVIRONMENT that stimulates plasticity. (3) MODERATE AROUSAL is required: new learning consolidates best when a client is emotionally engaged but not overwhelmed — too flat and nothing rewires, too flooded and the stress systems shut learning down. This is precisely Unit 8's window of tolerance, which is why pacing and regulation aren't preliminaries to the 'real' work — they ARE the conditions for rewiring.",
    "type": "explain",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "cozolino-social-brain",
    "bloom_level": "understand"
  },
  {
    "id": "u11-neuroplasticity-overhyped-evaluate-01",
    "prompt": "Evaluate the claim, common in pop-neuroscience marketing, that you can 'rewire your brain in seven days' with the right app or program.",
    "answer": "It abuses a real science. Neuroplasticity IS real — the brain genuinely rewires with experience, and therapy leverages that — but the pop version overstates it badly: real plastic change is GRADUAL, EFFORTFUL, and repetition-dependent (Hebbian wiring takes reps over weeks-plus), not a seven-day hack. 'Neuroplasticity' has become a marketing word attached to a great deal of unfounded brain-training and 'rewire your anxiety fast' content. Two honest cautions: (1) the timeline and effort are real constraints — quick-fix claims are red flags; (2) even in legitimate research, NEURAL CORRELATES ARE NOT MECHANISM — a brain region changing after an intervention shows THAT something changed, not that the brain change is the 'real' cause or how it produces improvement. Use plasticity as a hopeful, accurate frame ('your brain can change, with practice, over time'), not as a promise of fast, effortless transformation.",
    "type": "explain",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "neuroplasticity-overhyped",
    "bloom_level": "evaluate"
  },
  {
    "id": "u11-reps-agency-apply-01",
    "prompt": "A client is frustrated: 'Why do I have to keep practicing the new response and doing the between-session stuff? I already understand the idea.' Answer using Hebbian plasticity, in a way that restores their agency.",
    "answer": "Because understanding an idea and WIRING IN a new pattern are different things. The old pattern (the fear, the avoidance, the automatic reaction) got durable through REPETITION — it fired so many times it wired together (Hebb: 'neurons that fire together wire together'). Wiring in a NEW pattern works the same way: it takes reps. The between-session practice IS the repetition that strengthens the new synaptic connections until the new response becomes as automatic as the old one; insight alone doesn't lay down that wiring. The agency-restoring frame: 'Your brain wired the old pattern in through repetition, and it can wire a new one in the same way — that's what the practice is doing, literally. It's not that you're failing to 'get it'; it's that change is built with reps, and every rep is you reshaping the circuit.'",
    "type": "vignette",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "reps-restore-agency",
    "bloom_level": "apply"
  },
  {
    "id": "u11-whats-wrong-with-brain-vignette-01",
    "prompt": "A demoralized client asks, 'What's actually wrong with my brain — and can just talking really change it?' Give a response that is accurate, hopeful, and within scope.",
    "answer": "A response that's honest and agency-restoring: 'Your brain isn't a broken machine with one part wrong — it's been SHAPED by your experiences, the way everyone's is, and the same capacity that shaped it (neuroplasticity) means it can be RE-shaped by new experience. And yes — talking genuinely changes the brain: therapy is a form of learning, and learning rewires neural connections. We can even see it — in OCD, successful therapy changes brain activity the same way medication does. So talking isn't the soft, lesser option; it's real biological work, done through relationship and practice, over time.' This corrects the 'fixed broken brain' frame (which deepens helplessness), keeps hope grounded in real science, and stays in scope — you're educating and reframing, not diagnosing a neurological condition or making medical claims. If medication is in the picture, you can add that meds and therapy change the brain the same way and can work together.",
    "type": "vignette",
    "source_page": "wiki/concept-neuroplasticity-therapy.md",
    "topic": "whats-wrong-with-my-brain",
    "bloom_level": "apply"
  },
  {
    "id": "u11-biology-one-lens-evaluate-01",
    "prompt": "This unit is the most tempting place to slip into 'the biology is the REAL cause and everything else is downstream.' Evaluate that neuro-reductionist stance against the biopsychosocial model.",
    "answer": "Neuro-reductionism — treating neurochemistry/brain structure as the master level under which meaning, relationships, and social conditions are mere epiphenomena — is both usually wrong and clinically harmful. Wrong: the biopsychosocial model holds that biological, psychological, and social factors are CO-CAUSES, and the biological one is not automatically the most fundamental; experience shapes biology (neuroplasticity) as much as biology shapes experience, so the causal arrows run both ways. Harmful: collapsing a person into 'a chemical imbalance' or 'a broken circuit' is deflating — it tells a client their problem is a defective part rather than a life to be understood and changed, which can INCREASE helplessness and undercut their sense that therapy or effort matters. The disciplined stance for this whole unit: hold biology as ONE lens among three (a leg of the stool), not the floor the others stand on — a working model that lets you answer questions, coordinate, and refer, without reducing the person to their neurons.",
    "type": "explain",
    "source_page": "wiki/unit11-neuroscience.md",
    "topic": "biology-is-one-lens",
    "bloom_level": "evaluate"
  }
]
```
