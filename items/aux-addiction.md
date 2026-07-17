# Elective module items — Understanding & Changing Addictive Behavior

Source of truth for this **elective/ad-hoc module** (off-spine; `aux-` namespace). Each fenced
`json` block is a JSON array merged by `apps/build_items.py` into `build/items.json`. Items span
Bloom levels and lean toward **application + stance** (meeting people where they are; relapse as
data, not verdict), per the generate rules in [`../CLAUDE.md`](../CLAUDE.md). Clusters:
`addiction-models`, `change-stages`, `relapse-concepts`, `addiction-treatments`. Item id prefix:
`ax-add-`.

## Cluster: addiction-models

```json
[
  {
    "id": "ax-add-sud-severity-cloze-01",
    "prompt": "DSM-5-TR rates substance use disorder on a severity continuum from the 11 criteria: mild = 2–3, moderate = 4–5, and severe = {{6}} or more criteria met.",
    "answer": "6",
    "type": "cloze",
    "source_page": "wiki/concept-addiction-models.md",
    "topic": "sud-criteria",
    "cluster": "addiction-models",
    "bloom_level": "remember"
  },
  {
    "id": "ax-add-sud-groups-recall-01",
    "prompt": "The 11 DSM-5-TR substance use disorder criteria fall into four groups. Name them.",
    "answer": "1) Impaired control (using more/longer than intended, failed attempts to cut down, much time spent, craving); 2) Social impairment (role failure, interpersonal problems, giving up activities); 3) Risky use (hazardous use, use despite known harm); 4) Pharmacological (tolerance, withdrawal). At least 2 of the 11 are required to diagnose.",
    "type": "recall",
    "source_page": "wiki/concept-addiction-models.md",
    "topic": "sud-criteria",
    "cluster": "addiction-models",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-dependence-vs-addiction-understand-01",
    "prompt": "Explain the difference between physical dependence and addiction, and why DSM-5-TR won't count tolerance/withdrawal toward a diagnosis when a drug is taken as prescribed.",
    "answer": "Physical dependence is a normal, expected pharmacological adaptation — tolerance (needing more) and withdrawal (symptoms on stopping) — that many drugs produce even when used correctly. Addiction is the behavioral syndrome of compulsive, harm-defying use and loss of control (craving is its marker). Because a pain patient stable on prescribed opioids can be physically dependent without being addicted, DSM-5-TR excludes tolerance/withdrawal from the criteria count when the drug is taken as prescribed under medical supervision — otherwise it would mislabel appropriate treatment as a disorder.",
    "type": "explain",
    "source_page": "wiki/concept-addiction-models.md",
    "topic": "dependence-vs-addiction",
    "cluster": "addiction-models",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-prescribed-vignette-01",
    "prompt": "A cancer patient on long-term prescribed opioids has clear tolerance and gets withdrawal symptoms if a dose is late, but takes the medication exactly as directed, has no cravings, and no loss of control. Does she meet criteria for a substance use disorder? Explain.",
    "answer": "Not on these facts. Tolerance and withdrawal are her only 'criteria,' and DSM-5-TR does NOT count them toward a diagnosis when the drug is taken as prescribed under medical supervision. She has physical dependence, not addiction — no impaired control, no craving, no harm-defying compulsive use. Calling her 'addicted' both misdiagnoses her and can wrongly restrict needed treatment.",
    "type": "vignette",
    "source_page": "wiki/concept-addiction-models.md",
    "topic": "dependence-vs-addiction",
    "cluster": "addiction-models",
    "bloom_level": "apply"
  },
  {
    "id": "ax-add-terms-analyze-01",
    "prompt": "Match each phenomenon to the right term: (a) needing a bigger dose for the same buzz; (b) sweating, nausea, and anxiety two days after stopping; (c) an intrusive urge to use triggered by walking past an old spot. Which of these is most central to ADDICTION as opposed to mere physical dependence?",
    "answer": "(a) tolerance; (b) withdrawal; (c) craving. Tolerance and withdrawal are physical dependence (can occur with proper medical use). Craving — the cue-triggered 'wanting' that persists after withdrawal ends — is central to addiction and a major driver of relapse. The loss of control it reflects, not the physical adaptations, is what makes it a disorder.",
    "type": "vignette",
    "source_page": "wiki/concept-addiction-models.md",
    "topic": "tolerance-withdrawal-craving",
    "cluster": "addiction-models",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-add-behavioral-mcq-01",
    "prompt": "Which is the ONLY behavioral (non-substance) addiction formally recognized as a disorder in DSM-5-TR?",
    "answer": "Gambling disorder — moved beside the substance use disorders on the basis of shared symptoms, reward-circuit neurobiology (incl. the 'near-miss' effect), and treatment response. Internet gaming disorder is only in Section III ('for further study'); 'sex/food/phone addiction' are popular terms, not DSM diagnoses.",
    "options": [
      "Internet gaming disorder",
      "Gambling disorder",
      "Sex addiction",
      "Food addiction"
    ],
    "correct": "Gambling disorder",
    "type": "mcq",
    "source_page": "wiki/concept-addiction-models.md",
    "topic": "behavioral-addiction",
    "cluster": "addiction-models",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-models-compare-01",
    "prompt": "Compare the brain-disease model with the learning/developmental (Lewis) model of addiction: what does each claim, and what is the clinical upside and risk of leaning too hard on the brain-disease view?",
    "answer": "Brain-disease model (NIDA/Volkow): addiction is a chronic brain disorder — lasting changes to reward/stress/control circuits. Learning/developmental model (Lewis): the same brain data reflect normal neuroplasticity and learned coping habits, not disease. Upside of the disease frame: it reduces moral blame, normalizes relapse, and supports treatment access/funding. Risk of over-leaning on it: it can imply permanence and helplessness ('my brain is broken forever'), undercutting the agency change actually requires. Best practice: hold the vocabulary of both (plus biopsychosocial), teach neither as settled fact.",
    "type": "compare",
    "source_page": "wiki/concept-addiction-models.md",
    "topic": "models-debate",
    "cluster": "addiction-models",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-add-bdm-evaluate-01",
    "prompt": "A colleague insists, 'Addiction is a brain disease, full stop — anything else is stigma.' Evaluate that position.",
    "answer": "Partly right, overstated. The brain-disease model has genuine clinical value (cuts blame, frames relapse as expected, supports access to care) and real neuroscientific backing. But it is a contested MODEL, not settled fact: learning/developmental theorists (Lewis) and 'disorder of choice' theorists read the same evidence differently, and a common middle view is that addiction is 'neither a brain disease nor a moral failing.' Treating one model as the whole truth risks implying helplessness and ignores the agency treatment must recruit. The honest stance holds the drive as real and biologically anchored AND the person as an agent you can engage.",
    "type": "explain",
    "source_page": "wiki/concept-addiction-models.md",
    "topic": "models-debate",
    "cluster": "addiction-models",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: change-stages

```json
[
  {
    "id": "ax-add-ttm-stages-recall-01",
    "prompt": "Name the five stages of Prochaska & DiClemente's Transtheoretical Model in order, plus the expected loop.",
    "answer": "Precontemplation → Contemplation → Preparation → Action → Maintenance, with Relapse/recycling as an expected event (not a failure). Change is a spiral: most people cycle through several times before it sticks.",
    "type": "recall",
    "source_page": "wiki/concept-stages-of-change.md",
    "topic": "ttm-stages",
    "cluster": "change-stages",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-precontemp-cloze-01",
    "prompt": "In the Transtheoretical Model, a person in {{precontemplation}} has no intention to change in the foreseeable future (about the next 6 months) and often doesn't see the behavior as a problem.",
    "answer": "precontemplation",
    "type": "cloze",
    "source_page": "wiki/concept-stages-of-change.md",
    "topic": "ttm-stages",
    "cluster": "change-stages",
    "bloom_level": "remember"
  },
  {
    "id": "ax-add-stage-id-apply-01",
    "prompt": "A client says: 'Honestly, I know the drinking is hurting my marriage and my health — part of me really wants to stop, but part of me can't imagine my life without it.' Which stage of change is this, and what does it tell you to do?",
    "answer": "Contemplation — aware of the problem and openly ambivalent (weighing pros and cons). The move is NOT to hand them a quit plan yet; it's to explore the ambivalence and evoke their own change talk (Motivational Interviewing), helping the decisional balance tip toward change. Pushing action now risks provoking resistance.",
    "type": "vignette",
    "source_page": "wiki/concept-stages-of-change.md",
    "topic": "stage-matching",
    "cluster": "change-stages",
    "bloom_level": "apply"
  },
  {
    "id": "ax-add-mismatch-analyze-01",
    "prompt": "A counselor gives a man who says 'I don't have a problem, my wife dragged me here' a detailed 30-day quit plan and a relapse-prevention worksheet. He grows argumentative and cancels the next session. Analyze what went wrong in TTM terms.",
    "answer": "Stage mismatch. He's in precontemplation (no intention to change, doesn't own the problem); the counselor delivered action-stage tools. Action-oriented advice to a precontemplator reliably produces defensiveness and dropout, not motion. Precontemplation calls for building a relationship, raising doubt, and offering information/concern — the goal is to help him leave merely QUESTIONING his use, which is real movement. Meet the stage he's in, not the one the counselor wishes he were in.",
    "type": "vignette",
    "source_page": "wiki/concept-stages-of-change.md",
    "topic": "stage-matching",
    "cluster": "change-stages",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-add-precontemp-vs-contemp-compare-01",
    "prompt": "Compare precontemplation and contemplation: what distinguishes them, and how should the helper's approach differ between the two?",
    "answer": "Precontemplation = no intention to change and often no acknowledged problem; the person isn't weighing change at all. Contemplation = aware of the problem and actively ambivalent — sees both pros and cons and is stuck between them. For precontemplation: build rapport, raise doubt, provide information/concern; don't demand action. For contemplation: explore the ambivalence and evoke change talk to tip the decisional balance. The error in both is jumping to an action plan before the person is ready.",
    "type": "compare",
    "source_page": "wiki/concept-stages-of-change.md",
    "topic": "stage-matching",
    "cluster": "change-stages",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-add-spiral-understand-01",
    "prompt": "Why did Prochaska & DiClemente revise the stages of change from a linear staircase to a 'spiral,' and what does that imply about relapse?",
    "answer": "Because most people don't move straight through to lasting change — they cycle through the stages several times, typically re-entering a bit further along rather than back at zero. The spiral implies relapse is a normal, expected turn of the process to be learned from, not proof the person 'can't change.' It reframes a return to use from failure to recycling, which keeps both helper and client engaged.",
    "type": "explain",
    "source_page": "wiki/concept-stages-of-change.md",
    "topic": "spiral-relapse",
    "cluster": "change-stages",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-precontemp-move-mcq-01",
    "prompt": "A client is in precontemplation about his cocaine use ('it's under control, I'm just here for my probation officer'). Which helper response best fits the stage?",
    "answer": "Building a relationship and gently raising doubt fits precontemplation; ultimatums and quit plans belong to later stages and tend to backfire here. The aim is to have him leave questioning his use, not to extract a commitment he isn't ready to make.",
    "options": [
      "'If you don't commit to quitting today, I'll have to note it in your report.'",
      "'Here's a 30-day abstinence plan — let's start now.'",
      "'Sounds like you're here mostly for probation. I'm curious — what would have to happen for you to think the coke was a problem?'",
      "'You clearly have a severe addiction and need inpatient rehab.'"
    ],
    "correct": "'Sounds like you're here mostly for probation. I'm curious — what would have to happen for you to think the coke was a problem?'",
    "type": "mcq",
    "source_page": "wiki/concept-stages-of-change.md",
    "topic": "stage-matching",
    "cluster": "change-stages",
    "bloom_level": "apply"
  },
  {
    "id": "ax-add-decisional-balance-cloze-01",
    "prompt": "In TTM, movement across the early stages tracks a shifting {{decisional balance}} — the felt weight of the pros versus cons of changing; progress looks like the pros of change gaining weight.",
    "answer": "decisional balance",
    "type": "cloze",
    "source_page": "wiki/concept-stages-of-change.md",
    "topic": "decisional-balance",
    "cluster": "change-stages",
    "bloom_level": "remember"
  }
]
```

## Cluster: relapse-concepts

```json
[
  {
    "id": "ax-add-ave-cloze-01",
    "prompt": "In Marlatt's model, the guilt/shame/'I've blown it' reaction that turns a single slip into a full return to use is called the {{abstinence violation effect}} (AVE).",
    "answer": "abstinence violation effect",
    "type": "cloze",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "ave",
    "cluster": "relapse-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "ax-add-hrs-recall-01",
    "prompt": "Name Marlatt's three classic categories of high-risk situations for relapse. Which is the biggest?",
    "answer": "1) Negative emotional states (anger, anxiety, boredom, sadness) — the biggest; 2) interpersonal conflict; 3) social pressure (direct or indirect). Also celebrations, cues, and testing one's control. Negative emotional states account for the largest share of relapses.",
    "type": "recall",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "high-risk-situations",
    "cluster": "relapse-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-lapse-vs-relapse-understand-01",
    "prompt": "Distinguish a 'lapse' from a 'relapse,' and explain why the difference is the hinge of Marlatt's whole model.",
    "answer": "A lapse is a single slip — one instance of use after a period of change. A relapse is a return to the prior pattern of problematic use. The distinction is the hinge because a lapse does NOT have to become a relapse — what determines which way it goes is less the slip itself than the person's reaction to it (an AVE shame spiral drives the collapse). This is why relapse prevention plans for the lapse in advance.",
    "type": "explain",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "lapse-vs-relapse",
    "cluster": "relapse-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-ave-apply-01",
    "prompt": "After 4 months sober, a woman has one drink at a wedding. She thinks, 'I'm a total failure, I've ruined everything, I clearly can't do this' — and drinks heavily the rest of the night. Name the mechanism and describe how you'd intervene BEFORE it happens next time.",
    "answer": "The abstinence violation effect: a rigid all-or-nothing rule + a global/internal/stable attribution ('I can't do this') collapses self-efficacy and licenses continued use ('I've already broken it'). Intervene in advance: reframe a lapse as a single, situational, learn-from-able event (not a verdict), write an 'if I slip' plan (stop, leave, call support), and correct the all-or-nothing belief. After a slip, respond with curiosity — what was the situation, what coping was available, what do we change — not condemnation.",
    "type": "vignette",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "ave",
    "cluster": "relapse-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "ax-add-sid-analyze-01",
    "prompt": "A man in recovery from opioid use 'happens' to keep his old dealer's number, takes a route home that passes his old use spot, and agrees to 'just give a ride' to a still-using friend. He then relapses and says it came out of nowhere. Analyze using Marlatt's framework.",
    "answer": "These are seemingly irrelevant decisions (covert antecedents) — small, deniable choices that quietly walk him into a high-risk situation. It did NOT come out of nowhere: each choice removed a barrier and stacked the odds. Relapse prevention targets exactly these by making the chain visible (delete the number, change the route, decline the ride) so the person intervenes upstream, before the high-risk situation where a slip is decided and self-efficacy is tested.",
    "type": "vignette",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "covert-antecedents",
    "cluster": "relapse-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-add-lapse-relapse-compare-01",
    "prompt": "Compare a lapse and a relapse in terms of what they are and what determines whether one becomes the other.",
    "answer": "A lapse is a single, discrete slip; a relapse is a full return to the prior problematic pattern. What most determines whether a lapse becomes a relapse is the person's REACTION to it, not the slip's severity: an abstinence violation effect (guilt/shame + 'I've failed, so why stop now') drives the slide, while an attribution of the lapse as a specific, situational, correctable event preserves self-efficacy and contains it. So the intervention targets the reaction and prepares for the lapse in advance.",
    "type": "compare",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "lapse-vs-relapse",
    "cluster": "relapse-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-add-halt-cloze-01",
    "prompt": "A common clinical shorthand for everyday states that raise relapse risk is HALT: beware being Hungry, Angry, Lonely, or {{Tired}}.",
    "answer": "Tired",
    "type": "cloze",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "high-risk-situations",
    "cluster": "relapse-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "ax-add-urge-surf-apply-01",
    "prompt": "A client says, 'When a craving hits, I have to use — it just keeps getting worse until I give in.' What's the factual correction, and what skill follows from it?",
    "answer": "The belief is false: cravings crest and pass (usually minutes, not hours) rather than rising forever. The skill is urge surfing — notice the craving, and ride it out without acting, knowing it will recede. Pairing this with distraction/leaving the cue and reaching out to support turns 'I have to use' into 'I can outlast this wave.' Teaching the wave shape is itself an intervention against the catastrophic expectancy.",
    "type": "vignette",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "cravings",
    "cluster": "relapse-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "ax-add-relapse-evaluate-01",
    "prompt": "STANCE DRILL. A client relapses after 6 months and says, 'Treatment obviously failed — I'm hopeless.' Evaluate that claim against the evidence and state the clinically correct framing.",
    "answer": "Both parts are wrong. 40–60% of people with addiction relapse — a rate comparable to diabetes, hypertension, and asthma — and in those diseases a relapse means resume or adjust treatment, not that it failed. The correct framing: relapse is an expected turn of the spiral and a signal to re-engage/modify care, not a verdict on the person or the treatment. The clinical move is curiosity about what happened (situation, coping, plan) and re-entry, explicitly countering the AVE 'I'm hopeless' attribution.",
    "type": "explain",
    "source_page": "wiki/concept-relapse-prevention.md",
    "topic": "relapse-not-failure",
    "cluster": "relapse-concepts",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: addiction-treatments

```json
[
  {
    "id": "ax-add-righting-cloze-01",
    "prompt": "In Motivational Interviewing, the helper's urge to correct, warn, and 'fix' the client toward health — which paradoxically makes the client defend their behavior — is called the {{righting reflex}}.",
    "answer": "righting reflex",
    "type": "cloze",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "motivational-interviewing",
    "cluster": "addiction-treatments",
    "bloom_level": "remember"
  },
  {
    "id": "ax-add-rule-recall-01",
    "prompt": "What does the MI heuristic RULE stand for?",
    "answer": "Resist the righting reflex; Understand the client's motivations; Listen with empathy; Empower the client. It captures MI's core stance: don't argue people into change — evoke their own reasons for it.",
    "type": "recall",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "motivational-interviewing",
    "cluster": "addiction-treatments",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-changetalk-apply-01",
    "prompt": "A client says, 'Everyone keeps telling me I drink too much. I don't see the big deal.' A counselor is tempted to list the health risks. In MI terms, why is that tempting move wrong, and what would you do instead?",
    "answer": "Listing risks is the righting reflex — arguing the 'change' side pushes the client to voice the 'sustain' side ('it's not that bad'), talking themselves deeper into it. Instead, roll with it and evoke the client's OWN change talk: reflect ('you're tired of being told what to do'), then ask open, evocative questions ('what have YOU noticed about the drinking, even a little?'). People are persuaded by what they hear themselves say, so the goal is to elicit their reasons, not supply yours.",
    "type": "vignette",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "motivational-interviewing",
    "cluster": "addiction-treatments",
    "bloom_level": "apply"
  },
  {
    "id": "ax-add-stimulant-mcq-01",
    "prompt": "A client has a stimulant (methamphetamine) use disorder. Which treatment has the strongest evidence base as a first-line, 'gold-standard' approach for this class?",
    "answer": "Contingency management — tangible rewards (vouchers/prizes) contingent on verified abstinence. Stimulants have NO FDA-approved medication, and CM has the strongest evidence for stimulant use disorder. Naltrexone/buprenorphine are for other drug classes; 'just willpower' isn't a treatment.",
    "options": [
      "Buprenorphine maintenance",
      "Contingency management",
      "Naltrexone",
      "Encouraging willpower and abstinence pledges"
    ],
    "correct": "Contingency management",
    "type": "mcq",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "contingency-management",
    "cluster": "addiction-treatments",
    "bloom_level": "apply"
  },
  {
    "id": "ax-add-moud-mcq-01",
    "prompt": "Of the three FDA-approved medications for opioid use disorder, which have been proven to reduce overdose and all-cause mortality?",
    "answer": "Methadone (full agonist) and buprenorphine (partial agonist) — both are proven to reduce opioid-overdose and all-cause deaths (roughly halving fatal-overdose risk). Extended-release naltrexone (antagonist) is approved for OUD but does NOT have the same proven mortality benefit.",
    "options": [
      "Methadone and buprenorphine",
      "Naltrexone only",
      "Buprenorphine and naltrexone",
      "All three equally"
    ],
    "correct": "Methadone and buprenorphine",
    "type": "mcq",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "moud",
    "cluster": "addiction-treatments",
    "bloom_level": "understand"
  },
  {
    "id": "ax-add-moud-evaluate-01",
    "prompt": "A sober-living house refuses residents on buprenorphine, saying 'that's just replacing one addiction with another — real recovery is drug-free.' Evaluate this claim.",
    "answer": "It's wrong and dangerous. At therapeutic doses, buprenorphine (and methadone) stabilize brain chemistry and suppress cravings rather than intoxicate, and — critically — methadone and buprenorphine are PROVEN to cut overdose and all-cause mortality. Withholding MOUD for a 'medication-free' ideal is not evidence-based and raises the risk of death, especially after abstinence lowers tolerance. Taking a proven medication for a chronic condition is treatment, not addiction — the same way insulin isn't a diabetic's 'drug habit.'",
    "type": "explain",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "moud",
    "cluster": "addiction-treatments",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-add-harm-reduction-compare-01",
    "prompt": "Compare harm reduction and abstinence-only approaches. Why does the field increasingly treat them as integrated rather than opposed?",
    "answer": "Abstinence-only makes stopping a precondition of help. Harm reduction reduces the DANGERS of use for people not ready or able to stop — naloxone, clean supplies/needle exchange, safer-use education, reduced-use goals, MOUD. They're increasingly integrated because harm reduction keeps people alive and in contact with care, which is the precondition for any later abstinence; a rigid abstinence-only stance can push the highest-risk people away from help entirely. The stance: meet the goal the client will actually pursue, and keep them alive to revise it.",
    "type": "compare",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "harm-reduction",
    "cluster": "addiction-treatments",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-add-aa-evidence-evaluate-01",
    "prompt": "For decades people said 'there's no real evidence AA works.' What did the 2020 Cochrane review actually find, and how should that update a clinician's stance?",
    "answer": "The 2020 Cochrane review (Kelly, Humphreys & Ferri) found that manualized AA/Twelve-Step Facilitation is MORE effective than other established treatments (including CBT) for continuous abstinence, and at least as effective on other outcomes — at substantially lower cost, largely by linking people to a free, durable recovery network. So 'no evidence for AA' is outdated: TSF is an evidence-based referral. Caveat: it's spiritually framed and lifelong, which fits some clients and not others — match to fit, and know the secular alternative (SMART Recovery).",
    "type": "explain",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "mutual-help",
    "cluster": "addiction-treatments",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-add-aa-vs-smart-compare-01",
    "prompt": "A client is a committed atheist who bounces off talk of a 'higher power' but wants group support and structure. Compare AA/12-step with SMART Recovery to guide the referral.",
    "answer": "AA/12-step: spiritually framed (higher power), sponsor-based, lifelong identity ('I'm an alcoholic'); strong Cochrane evidence for abstinence but a poor fit for someone who rejects the spiritual frame. SMART Recovery: secular, self-empowerment, built on CBT/REBT and MI via a 4-Point Program (build motivation; cope with urges; manage thoughts/feelings/behaviors; balanced life), no higher power or lifelong label — a better fit here, though its evidence base is thinner than AA's. Matching the group's frame to the client's worldview matters; forcing the 12-step frame on this client is a fit mismatch likely to drive him out.",
    "type": "compare",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "mutual-help",
    "cluster": "addiction-treatments",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-add-match-method-analyze-01",
    "prompt": "Two failure modes in addiction treatment are 'method-ideology' and 'therapeutic nihilism.' Define each and state the alternative principle that avoids both.",
    "answer": "Method-ideology: forcing every client into one favorite modality (e.g., only 12-step, or only abstinence). Therapeutic nihilism: believing 'nothing works with addicts.' Both are false. The alternative: stage-matched and problem-matched, often combined care — MI to build motivation, CBT/relapse prevention for skills, medication where proven (methadone/buprenorphine for opioids; naltrexone/acamprosate for alcohol), contingency management where it's best (stimulants), mutual-help for durable support, and harm reduction to keep the person alive long enough for any of it to work.",
    "type": "explain",
    "source_page": "wiki/concept-treatment-and-recovery.md",
    "topic": "matching-treatment",
    "cluster": "addiction-treatments",
    "bloom_level": "analyze"
  }
]
```
