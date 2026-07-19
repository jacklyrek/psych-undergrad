# Unit 8 items — Crisis, Risk Assessment & Trauma-Informed Care

Source of truth for Unit 8 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This is the syllabus's highest-stakes, emotionally
heaviest unit — items are kept **clinical and precise, no sensationalism** (per CLAUDE.md). Signature
reps: the **ask-directly / don't-freeze** stance and the syllabus practice rep (a memorized structure
for asking about suicidal ideation), the **ideation-vs-behavior** and **warning-sign-vs-risk-factor**
discriminations, the **safety-plan-vs-no-suicide-contract** contrast, the **trauma-informed-vs-
trauma-treatment** distinction and its **don't-dig** restraint, the **trauma-brain** working model,
and the **counselor-cost** confusable cluster (VT/STS/compassion-fatigue/burnout/countertransference)
with self-care as an **ethical** duty. Item ids use the `u8-` prefix. Clusters: `suicide-risk-concepts`,
`crisis-response-models`, `trauma-informed-vs-treatment`, `trauma-brain`, `counselor-distress-types`.
See generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## Suicide risk assessment (cluster: suicide-risk-concepts)

```json
[
  {
    "id": "u8-ask-directly-evaluate-01",
    "prompt": "A trainee says: 'I don't ask clients about suicide directly because I'm afraid I'll put the idea in their head.' Evaluate this reasoning against the evidence, and give the actual danger.",
    "answer": "The reasoning is wrong and, in practice, dangerous. Reviews across community, adolescent, adult, and at-risk samples find that asking about suicide does NOT induce or increase ideation — and may reduce distress by letting the person talk about it. The real danger is the opposite: NOT asking, or asking so vaguely ('thinking of doing something silly?') that you never learn what you needed to. The corrective is to ask plainly and non-anxiously — 'Are you thinking about killing yourself?' — and then tolerate the answer instead of deflecting or reassuring.",
    "type": "explain",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "asking-directly",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-sra-rep-01",
    "prompt": "PRACTICE REP (syllabus): Out loud, in a plain non-anxious voice, run a basic structure for asking about suicidal ideation. Name the sequence you'd move through, then check it against the model. (The syllabus point is to practice saying the words until the awkwardness fades.)",
    "answer": "Model sequence: (1) IDEATION — ask directly: 'Are you thinking about killing yourself / ending your life?' (2) PLAN — 'Have you thought about how?' (3) INTENT — 'Do you think you might act on these thoughts?' (4) MEANS / ACCESS — 'Do you have access to [the method]?' (e.g., a firearm, pills). (5) PREPARATION — 'Have you done anything to prepare — gotten the means, written a note, given things away?' (6) PAST ATTEMPTS — 'Have you ever tried before?' (a past attempt is the strongest long-term risk factor). Say the words aloud; the goal of the rep is fluency and calm, not a script you read.",
    "type": "recall",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "asking-structure-rep",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "u8-ideation-behavior-compare-01",
    "prompt": "The C-SSRS is built on separating suicidal IDEATION from suicidal BEHAVIOR. Contrast the two and say why grading them separately matters clinically.",
    "answer": "IDEATION = thoughts about suicide, graded on a severity ladder from passive ('wish I were dead') up through active thoughts with methods, intent, and a specific plan. BEHAVIOR = acts: actual attempts, interrupted attempts (stopped by an outside circumstance), aborted/self-interrupted attempts (stopped by the person), and preparatory acts (acquiring means, writing a note, giving things away). Why separate: they're distinct dimensions of risk — someone can have intense ideation with no behavior, or minimal stated ideation but serious preparatory behavior — and the ideation-to-action framework says the causes of thinking about suicide differ from the causes of acting. Collapsing them into one 'how suicidal' score loses exactly the information that guides disposition.",
    "type": "compare",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "ideation-vs-behavior",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-ideation-ladder-recall-01",
    "prompt": "Name the five rungs of the C-SSRS suicidal-ideation severity ladder, in order of increasing seriousness.",
    "answer": "(1) Wish to be dead (passive). (2) Nonspecific active suicidal thoughts (no method). (3) Active ideation with methods considered (but no plan/intent). (4) Active ideation with some intent to act. (5) Active ideation with a specific plan AND intent. The passive-to-active jump (rung 1 to 2) is a meaningful line — but passive ideation is the start of the conversation, not a safe finding.",
    "type": "recall",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "ideation-ladder",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "u8-passive-active-mcq-01",
    "prompt": "A client says, 'Most mornings I wish I just wouldn't wake up, but I'd never actually do anything — I haven't thought about how or anything like that.' On the ideation ladder, this is best characterized as:",
    "options": [
      "Passive ideation (wish to be dead) — real and worth assessing further, not a 'safe' finding",
      "Active ideation with a specific plan and intent",
      "A suicide attempt that was self-aborted",
      "No suicidal ideation, since the client denies intent"
    ],
    "correct": "Passive ideation (wish to be dead) — real and worth assessing further, not a 'safe' finding",
    "answer": "'Wish I wouldn't wake up,' with no method/plan, is PASSIVE ideation (rung 1). It is not 'no ideation' just because intent is denied, and it's nowhere near plan+intent. Passive ideation is where the assessment begins — you still ask about methods, access, and past attempts — not where it ends.",
    "type": "mcq",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "passive-vs-active",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "u8-warningsign-riskfactor-compare-01",
    "prompt": "Distinguish a suicide RISK FACTOR, a WARNING SIGN, and a PROTECTIVE FACTOR — by what each is and its time frame — and give one example of each.",
    "answer": "RISK FACTOR = a standing characteristic that raises baseline, LONGER-TERM likelihood (chronic/distal): e.g., a prior attempt, psychiatric disorder, substance use, firearm access. WARNING SIGN = an observable indicator that risk is elevated RIGHT NOW (acute/proximal): e.g., giving possessions away, saying goodbye, seeking means, a sudden calm after despair. PROTECTIVE FACTOR = a characteristic that LOWERS likelihood (buffering): e.g., reasons for living, connectedness, engaged treatment. The key axis is time: risk factors are the background over years; warning signs are the foreground over hours-to-days; and protective factors buffer but do NOT cancel acute risk.",
    "type": "compare",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "warning-sign-vs-risk-factor",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-acute-chronic-mcq-01",
    "prompt": "A client with a years-long history of depression and one attempt in college now, this week, has begun giving away his guitars and texting old friends to 'thank them for everything.' Which element is the ACUTE WARNING SIGN (as opposed to a chronic risk factor)?",
    "options": [
      "Giving away his possessions and saying goodbye this week",
      "His years-long history of depression",
      "His single suicide attempt in college",
      "His diagnosis of a psychiatric disorder"
    ],
    "correct": "Giving away his possessions and saying goodbye this week",
    "answer": "Giving away valued possessions and saying goodbye NOW is an acute/proximal WARNING SIGN — it signals elevated risk in the near term. The depression, the past attempt, and the diagnosis are chronic/distal RISK FACTORS: real, and important context, but they've been stable for years. The clinical alarm is the acute change layered on top of the standing risk.",
    "type": "mcq",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "acute-vs-chronic",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "u8-ispathwarm-cloze-01",
    "prompt": "The American Association of Suicidology warning-sign mnemonic is IS PATH WARM: Ideation, Substance abuse, Purposelessness, Anxiety, Trapped, Hopelessness, Withdrawal, Anger, {{Recklessness}}, and Mood change.",
    "answer": "Recklessness",
    "type": "cloze",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "is-path-warm",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "u8-priorattempt-cloze-01",
    "prompt": "The single strongest LONG-TERM risk factor for death by suicide is a {{prior attempt}} — which is why 'have you ever tried before?' belongs in every risk assessment.",
    "answer": "prior attempt",
    "type": "cloze",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "prior-attempt",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "u8-ideation-to-action-explain-01",
    "prompt": "Explain the core claim of the 'ideation-to-action' framework and why it reorganizes a suicide risk assessment.",
    "answer": "The core claim: the causes of suicidal IDEATION are DISTINCT from the causes of the PROGRESSION from ideation to an attempt — so the factors that explain who thinks about suicide differ from those that explain who acts. It reorganizes assessment because you stop asking one lumped question ('how suicidal are they?') and ask two: (1) what's driving the ideation (in the theories: pain + hopelessness; thwarted belongingness + perceived burdensomeness), and (2) what would move them from thought to act (CAPABILITY — habituation to fear/pain, plus practical access to means). It tells you where to intervene: you can raise connectedness and lower practical capability (means reduction) tonight even if you can't quickly change the pain.",
    "type": "explain",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "ideation-to-action",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "u8-acquired-capability-mcq-01",
    "prompt": "Two clients report equally intense suicidal ideation. In the ideation-to-action framework, which additional detail most raises concern that a client could PROGRESS from ideation to an attempt?",
    "options": [
      "The client has a history of repeated self-injury and access to a firearm at home",
      "The client feels intense psychological pain and hopelessness",
      "The client reports feeling like a burden to their family",
      "The client feels disconnected and lonely"
    ],
    "correct": "The client has a history of repeated self-injury and access to a firearm at home",
    "answer": "Ideation-to-action theories say the leap from thinking to acting is governed by CAPABILITY — habituation to pain/fear/death (e.g., repeated self-injury) plus PRACTICAL capability (access to lethal means). The other three (pain+hopelessness, burdensomeness, disconnection) are drivers of IDEATION itself — they explain why the person is suicidal, not what would move them to an attempt. This is exactly why means reduction targets the modifiable practical-capability piece.",
    "type": "mcq",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "acquired-capability",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-predict-vs-manage-evaluate-01",
    "prompt": "A supervisor asks, 'Based on your assessment, will this client attempt suicide or not?' Evaluate the question, and reframe what a risk assessment is actually for. Name the earlier unit whose critique this echoes.",
    "answer": "The question asks for a PREDICTION the science can't deliver: individual suicide is not reliably predictable, and instruments/risk-factor lists identify elevated-risk POPULATIONS, not who will act and when. Treating assessment as prophecy produces false confidence and defensive practice. Reframe: a risk assessment exists to MANAGE risk — to choose disposition (how closely to monitor, what to remove, where they spend tonight) and to build a safety plan — not to forecast. This echoes the Tarasoff PREDICTION CRITIQUE from Unit 3 (clinicians can't reliably predict dangerousness/violence either). Assess to intervene, not to predict.",
    "type": "explain",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "assess-to-manage-not-predict",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-case-approach-recall-01",
    "prompt": "Shea's CASE Approach walks the interview through four chronological regions. Name them in order, and state what 'reflected intent' means.",
    "answer": "Four regions: (1) PRESENTING ideation/events (today's crisis), (2) RECENT ideation/events (past ~8 weeks), (3) PAST ideation/events (lifetime), (4) IMMEDIATE ideation (safety right now + disposition). REFLECTED INTENT = how much thinking, planning, and action the client DESCRIBES — which often reveals more real intent than their STATED intent ('not really'). A client who denies intent but describes researching methods, acquiring means, and writing letters is showing reflected intent that outweighs the denial; the interview's job is to maximize reflected intent and minimize withheld intent.",
    "type": "recall",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "case-approach",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "u8-reflected-intent-vignette-01",
    "prompt": "You ask a client directly about suicide and he says, 'No, not really, I'd never do that.' But over the session he mentions he recently bought a gun 'for no reason,' gave his dog to his sister, and updated his will. How do you weigh his stated denial against the rest, and what's the concept?",
    "answer": "You weight the BEHAVIOR over the verbal denial. This is the gap between STATED intent ('I'd never') and REFLECTED intent — the thinking, planning, and preparatory ACTION he's describing (acquiring means, giving away a pet, putting affairs in order). Reflected intent here is high and contradicts the denial, so the assessment is NOT reassured by 'not really.' The move: name what you're noticing without accusation ('I hear you say you wouldn't — and I also notice some things that worry me: the gun, giving away your dog...'), and treat this as elevated risk requiring safety planning, means reduction, and likely a higher level of care.",
    "type": "vignette",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "reflected-intent",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "u8-disposition-mcq-01",
    "prompt": "A client reports persistent active ideation with a specific plan and intent, has acquired the means, and is in acute distress. Which disposition fits, per standard risk stratification?",
    "options": [
      "High risk: do not leave the person alone, remove means immediately, and arrange hospitalization / emergency evaluation",
      "Low risk: outpatient follow-up with a safety plan in two weeks",
      "Moderate risk: keep the next routine appointment and monitor",
      "No action needed as long as the client verbally agrees to stay safe"
    ],
    "correct": "High risk: do not leave the person alone, remove means immediately, and arrange hospitalization / emergency evaluation",
    "answer": "Plan + intent + acquired means + acute distress = HIGH risk: don't leave them alone, remove means now, and arrange hospitalization or emergency evaluation. Low/moderate dispositions under-respond to plan-plus-intent-plus-means. And a verbal promise to 'stay safe' (a no-suicide contract) is not a disposition and has no evidence of protecting anyone — this is precisely where you act on the danger-to-self limit of confidentiality (Unit 3).",
    "type": "mcq",
    "source_page": "wiki/concept-suicide-risk-assessment.md",
    "topic": "risk-stratification-disposition",
    "cluster": "suicide-risk-concepts",
    "bloom_level": "apply"
  }
]
```

## Safety planning & means reduction (cluster: crisis-response-models)

```json
[
  {
    "id": "u8-spi-steps-recall-01",
    "prompt": "List the six steps of the Stanley-Brown Safety Planning Intervention in order.",
    "answer": "(1) Warning signs (personal cues a crisis is building). (2) Internal coping strategies (things to do ALONE, no contact needed). (3) Social contacts and settings for distraction (people/places, without disclosing the crisis). (4) People to ask for help (family/friends the client WILL tell). (5) Professionals and agencies to contact (clinician, ED, 988 Suicide & Crisis Lifeline). (6) Making the environment safe (means reduction). The order runs from what the client can do alone toward external and professional help.",
    "type": "recall",
    "source_page": "wiki/concept-safety-planning.md",
    "topic": "spi-six-steps",
    "cluster": "crisis-response-models",
    "bloom_level": "remember"
  },
  {
    "id": "u8-spi-order-understand-01",
    "prompt": "Why are the six safety-plan steps ordered from internal coping toward professional help, rather than the reverse?",
    "answer": "Because the earliest steps must be the ones ALWAYS available — even at 2 a.m. with no one reachable. Starting with warning signs and internal coping builds the client's sense that 'I can get through a wave myself,' then escalates to distraction with others, then to disclosing the crisis to trusted people, then to professionals/988, and finally to making the environment safe. Ordering self-reliance first means the plan doesn't collapse if a support is unreachable, and it restores agency rather than teaching immediate dependence on a hotline.",
    "type": "explain",
    "source_page": "wiki/concept-safety-planning.md",
    "topic": "spi-ordering",
    "cluster": "crisis-response-models",
    "bloom_level": "understand"
  },
  {
    "id": "u8-spi-contract-compare-01",
    "prompt": "Contrast a collaborative SAFETY PLAN with a NO-SUICIDE CONTRACT on: what it asks of the client, who it serves, and the evidence.",
    "answer": "NO-SUICIDE CONTRACT asks for a PROMISE ('I won't kill myself'); it primarily serves the CLINICIAN's anxiety/liability; and it has NO evidence of reducing suicide or attempts — it can create false reassurance and gives the client nothing to DO in a crisis. SAFETY PLAN asks for a PLAN ('here's what I'll do, and whom I'll contact, when the warning signs start'); it serves the CLIENT's survival; and it has cohort/RCT support (SPI + follow-up ~45% fewer suicidal behaviors). A promise is not a plan — the deliverable is the concrete, prioritized list of actions and contacts.",
    "type": "compare",
    "source_page": "wiki/concept-safety-planning.md",
    "topic": "safety-plan-vs-contract",
    "cluster": "crisis-response-models",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-nosuicide-evaluate-01",
    "prompt": "A clinic still uses signed 'no-suicide contracts' and a supervisor says they 'keep clients safe and cover us legally.' Evaluate both claims.",
    "answer": "Both claims are weak. CLINICALLY: no study shows no-suicide contracts reduce suicide or attempts; they can create FALSE REASSURANCE (the clinician feels the work is done) and give the client nothing actionable when the urge hits. LEGALLY: they don't confer real protection and reflect defensive rather than therapeutic practice — a plan the client couldn't use is not a defense. The evidence-based replacement is collaborative SAFETY PLANNING (with means reduction), which gives the client concrete steps and is what current guidelines (Joint Commission, VA/DoD, Zero Suicide) endorse. Replace the contract with a plan.",
    "type": "explain",
    "source_page": "wiki/concept-safety-planning.md",
    "topic": "no-suicide-contract-critique",
    "cluster": "crisis-response-models",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-spi-collaborative-vignette-01",
    "prompt": "A busy clinician prints a blank safety-plan form, hands it to an at-risk client, and says 'fill this out at home.' What did they miss about how the intervention works?",
    "answer": "They skipped the intervention itself. The SPI's value is the COLLABORATIVE conversation — eliciting the client's OWN warning signs, testing whether each coping strategy is realistic ('would you actually call your brother, or not want to worry him?'), and troubleshooting barriers. A plan the client didn't help build is one they won't use in crisis. The move: build it together, in the room, in the client's own words, and treat it as a living document to revisit — not a form handed over.",
    "type": "vignette",
    "source_page": "wiki/concept-safety-planning.md",
    "topic": "spi-collaborative",
    "cluster": "crisis-response-models",
    "bloom_level": "apply"
  },
  {
    "id": "u8-spi-988-cloze-01",
    "prompt": "Step 5 of the safety plan lists professionals and crisis services to contact, including the U.S. {{988}} Suicide & Crisis Lifeline (call or text), written down because a person in crisis won't go looking for the number.",
    "answer": "988",
    "type": "cloze",
    "source_page": "wiki/concept-safety-planning.md",
    "topic": "988-lifeline",
    "cluster": "crisis-response-models",
    "bloom_level": "remember"
  },
  {
    "id": "u8-means-why-recall-01",
    "prompt": "Means reduction rests on four facts that make access to method decisive. Name them.",
    "answer": "(1) CASE FATALITY varies enormously by method — ~85-90% of firearm attempts are fatal vs. a few percent for overdose/cutting — so what's within reach largely determines survival. (2) Suicidal crises are often BRIEF AND IMPULSIVE — often minutes to an hour between deciding and acting. (3) Method SUBSTITUTION is incomplete — many people don't simply switch to an equally lethal method. (4) Most attempt survivors DON'T later die by suicide (~9 in 10). Together: because crises are transient and lethality is method-dependent, reducing access to the most lethal means buys time and saves lives.",
    "type": "recall",
    "source_page": "wiki/concept-means-reduction.md",
    "topic": "means-rationale",
    "cluster": "crisis-response-models",
    "bloom_level": "understand"
  },
  {
    "id": "u8-means-casefatality-cloze-01",
    "prompt": "Case fatality is why firearms are the highest-priority means: roughly {{85-90}} percent of firearm suicide attempts are fatal, versus a few percent for overdose or cutting.",
    "answer": "85-90",
    "type": "cloze",
    "source_page": "wiki/concept-means-reduction.md",
    "topic": "case-fatality",
    "cluster": "crisis-response-models",
    "bloom_level": "remember"
  },
  {
    "id": "u8-means-substitution-evaluate-01",
    "prompt": "A colleague dismisses means reduction: 'If someone really wants to die, they'll just find another way — so removing the gun is pointless.' Evaluate this.",
    "answer": "It's a common but mistaken objection. Three facts rebut it: (1) SUBSTITUTION IS INCOMPLETE — many people do not switch to an equally lethal method when the first is unavailable. (2) Crises are TRANSIENT/IMPULSIVE — often minutes to an hour — so removing the most lethal method during that window often means the acute urge passes. (3) CASE FATALITY differs so much by method that even partial substitution to a less lethal method raises survival. And ~9 in 10 attempt survivors don't later die by suicide. So at the population level, reducing access to the most lethal means demonstrably saves lives — the objection assumes a fixed, method-indifferent intent that the evidence doesn't support.",
    "type": "explain",
    "source_page": "wiki/concept-means-reduction.md",
    "topic": "substitution-objection",
    "cluster": "crisis-response-models",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-means-firearm-mcq-01",
    "prompt": "A suicidal client keeps a firearm at home. Which option best reflects lethal-means safety counseling?",
    "options": [
      "Collaboratively arrange temporary OFF-SITE storage with a trusted person or facility while the client is at risk",
      "Tell the client they must permanently get rid of all their firearms",
      "Note that the client has firearm access in the chart and take no further action",
      "Advise keeping the firearm loaded but hidden in a different room"
    ],
    "correct": "Collaboratively arrange temporary OFF-SITE storage with a trusted person or facility while the client is at risk",
    "answer": "Best practice is temporary OFF-SITE storage (trusted person, gun shop, range, police department) while at risk — collaborative and time-limited, not confiscation. Demanding permanent removal invites a fight; noting access without acting is the most common and consequential miss (78% of EDs assess access but only ~35% counsel); and 'loaded but hidden' does nothing about case fatality. If off-site is impossible, the fallback is locked, unloaded, ammunition stored separately, key held by someone else.",
    "type": "mcq",
    "source_page": "wiki/concept-means-reduction.md",
    "topic": "firearm-storage",
    "cluster": "crisis-response-models",
    "bloom_level": "apply"
  },
  {
    "id": "u8-means-gap-analyze-01",
    "prompt": "Surveys find ~78% of EDs ask whether a suicidal patient has access to lethal means, but only ~35% actually provide means counseling. Analyze what's being dropped, and name the stance trap.",
    "answer": "What's dropped is the COUNSELING — the harder half. Asking 'do you have a gun?' is easy; helping the person and family actually reduce that access (arranging off-site storage, locking meds) is what gets skipped. The stance trap is that the omission is driven by the CLINICIAN'S discomfort, not the client's — clinicians fear raising firearms will rupture the alliance, though a collaborative, concerned tone generally doesn't. It's the same avoidance reflex that keeps clinicians from asking about suicide directly: skipping the conversation to spare your own discomfort is the failure mode, and here it's the highest-yield step you skipped.",
    "type": "explain",
    "source_page": "wiki/concept-means-reduction.md",
    "topic": "means-counseling-gap",
    "cluster": "crisis-response-models",
    "bloom_level": "analyze"
  }
]
```

## Crisis intervention & de-escalation models (cluster: crisis-response-models)

```json
[
  {
    "id": "u8-crisis-def-cloze-01",
    "prompt": "A crisis is defined not by the event but by the person's {{perception}} of it as an intolerable difficulty that overwhelms their current resources and coping — which is why two people can face the same event and only one is in crisis.",
    "answer": "perception",
    "type": "cloze",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "crisis-definition",
    "cluster": "crisis-response-models",
    "bloom_level": "remember"
  },
  {
    "id": "u8-sixstep-recall-01",
    "prompt": "Name the six steps of James & Gilliland's crisis-intervention model, and say which three are 'listening' and which three are 'acting.'",
    "answer": "LISTENING: (1) Define the problem (from the client's viewpoint), (2) Ensure client safety, (3) Provide support. ACTING: (4) Examine alternatives, (5) Make plans, (6) Obtain commitment. The listening steps use core microskills; the acting steps are collaborative but more directive than ordinary therapy (a crisis isn't the time for pure non-directiveness). Ensuring safety is written as step 2 but functions as a continuous priority through all six.",
    "type": "recall",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "six-step-model",
    "cluster": "crisis-response-models",
    "bloom_level": "remember"
  },
  {
    "id": "u8-safety-thread-understand-01",
    "prompt": "In the crisis-intervention models, client safety is listed as a step but is described as 'the thread, not a step.' Explain what that means and why it matters.",
    "answer": "It means safety isn't something you assess once at step 2 and check off — it's re-evaluated continuously through every step, because in a crisis danger can change in seconds. Reading a step model as strictly sequential ('handle safety, then move on') is the error: you can be in the middle of 'examine alternatives' when acute risk spikes and you're back to safety instantly. Treating safety as the continuous through-line, not a completed box, is what keeps the model from lulling you into a false sense that the danger has been dealt with.",
    "type": "explain",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "safety-continuous",
    "cluster": "crisis-response-models",
    "bloom_level": "understand"
  },
  {
    "id": "u8-sixstep-roberts-compare-01",
    "prompt": "Compare James & Gilliland's six-step model with Roberts' seven-stage model. What's the shared spine, and how do they differ?",
    "answer": "SHARED SPINE: assess/ensure safety first → establish rapport and define the problem from the client's view → deal with feelings / provide support → generate and examine alternatives → make a concrete collaborative plan → (Roberts adds explicit) follow-up. Both are assessment-and-safety-first, relationship-based, and end in a doable plan. DIFFERENCE: mostly granularity — Roberts splits the work into seven stages (with a distinct lethality-assessment stage and an explicit follow-up stage), while James & Gilliland compress it into six (three listening + three acting). They differ in how finely they slice the same sequence, not in what they tell you to do.",
    "type": "compare",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "six-step-vs-roberts",
    "cluster": "crisis-response-models",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-beta-domains-recall-01",
    "prompt": "Project BETA frames verbal de-escalation as three moves and ten domains. Name the three moves and at least five of the ten domains.",
    "answer": "THREE MOVES: verbally engage the person → build a collaborative relationship → verbally de-escalate them out of agitation. TEN DOMAINS (any five): respect personal space (≥2 arms' lengths); don't be provocative (calm posture, hands visible); establish verbal contact (only ONE person speaks); be concise (short, simple, repeat); identify wants and feelings; listen closely (active listening; restate it back); agree or agree to disagree; set clear limits (matter-of-factly, no threats); offer choices and optimism; debrief patient and staff afterward.",
    "type": "recall",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "beta-ten-domains",
    "cluster": "crisis-response-models",
    "bloom_level": "remember"
  },
  {
    "id": "u8-beta-onevoice-mcq-01",
    "prompt": "An agitated client is escalating in a waiting area while three staff members simultaneously talk to him, each telling him to calm down. Per Project BETA, what's the first correction?",
    "options": [
      "Have ONE person establish verbal contact and speak with him; the others step back",
      "Have all three continue so he knows the team is united",
      "Move immediately to physical restraint since he's escalating",
      "Everyone stops talking and ignores him until he settles on his own"
    ],
    "correct": "Have ONE person establish verbal contact and speak with him; the others step back",
    "answer": "BETA domain: only ONE person verbally interacts with the agitated patient — multiple voices confuse and escalate. The others step back (respecting personal space, keeping exits clear). Restraint is a LAST resort, not a response to escalation itself; and ignoring him abandons the engagement the model is built on. Establish one calm line of contact first.",
    "type": "mcq",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "beta-one-voice",
    "cluster": "crisis-response-models",
    "bloom_level": "apply"
  },
  {
    "id": "u8-beta-agree-vignette-01",
    "prompt": "An agitated man is shouting that the intake wait was 'a total disgrace' and 'nobody here respects anyone.' You feel pulled to defend the clinic and correct him. Per verbal de-escalation, what's the better move and why?",
    "answer": "Don't defend or correct — find something TRUE to agree with ('You're right that the wait has been way too long, and that's frustrating'). This is 'agree or agree to disagree': you don't have to win the argument or endorse every claim, you have to lower arousal. Defending the clinic makes you an adversary and escalates; partial, genuine agreement makes you an ally and de-escalates. Getting to calm — not being proven right — is the goal; problem-solving comes AFTER arousal drops.",
    "type": "vignette",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "beta-agree",
    "cluster": "crisis-response-models",
    "bloom_level": "apply"
  },
  {
    "id": "u8-restraint-evaluate-01",
    "prompt": "Why is coercion / physical restraint framed as a LAST resort in de-escalation rather than an efficient way to end an agitated episode?",
    "answer": "Because beyond the direct injury risk, restraint tends to REINFORCE the idea that violence is how conflict gets resolved, is associated with worse outcomes (longer stays, higher admission), and ruptures the therapeutic relationship that makes future help possible. It also contradicts the whole logic of the unit: the counselor's job is to RESTORE the person's agency and control, not override it. Successful verbal de-escalation preserves dignity and returns control to the person, which is both more humane and more effective — so coercion is the fallback when safety can't be secured any other way, not the shortcut.",
    "type": "explain",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "restraint-last-resort",
    "cluster": "crisis-response-models",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-deescalate-calm-mcq-01",
    "prompt": "As a client gets louder and more agitated, which counselor adjustment best fits verbal de-escalation principles?",
    "options": [
      "Get calmer and physically smaller — lower your voice, relax posture, keep hands visible, give space",
      "Match their volume so they know you're taking them seriously",
      "Step closer and make firm eye contact to assert control",
      "Deliver a detailed logical explanation of why they shouldn't be upset"
    ],
    "correct": "Get calmer and physically smaller — lower your voice, relax posture, keep hands visible, give space",
    "answer": "The skill is to get CALMER and smaller as they get bigger: lower voice, relaxed non-provocative posture, hands visible, respect personal space. Matching volume and stepping in are provocative and escalate; a long logical explanation fails because an agitated brain processes language poorly (be concise instead). Your regulated nervous system is the tool — de-escalate first, problem-solve later.",
    "type": "mcq",
    "source_page": "wiki/concept-de-escalation.md",
    "topic": "get-calmer",
    "cluster": "crisis-response-models",
    "bloom_level": "apply"
  }
]
```

## The neurobiology of trauma (cluster: trauma-brain)

```json
[
  {
    "id": "u8-brain-three-compare-01",
    "prompt": "In the working model of the traumatized brain, contrast the roles of the amygdala, hippocampus, and prefrontal cortex — normally and in trauma.",
    "answer": "AMYGDALA = threat detector (the smoke alarm); in trauma it's HYPERACTIVE and over-generalizes, firing at cues that aren't dangerous. HIPPOCAMPUS = memory + CONTEXT; it time-stamps events as 'past'; in trauma it shows reduced volume/function and FAILS to mark the memory as over, so it intrudes as if happening NOW. PREFRONTAL CORTEX (medial) = top-down brake on the amygdala; in trauma its regulatory activity is REDUCED, so it can't dampen the alarm. Net: alarm stuck on (amygdala up), context lost and memory feels present (hippocampus down), brake failing (PFC down) — the picture of hypervigilance and flashbacks.",
    "type": "compare",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "three-structures",
    "cluster": "trauma-brain",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-hippocampus-mcq-01",
    "prompt": "A veteran describes that a car backfiring doesn't just remind him of combat — it feels like he is BACK there, in danger, right now. Which structure's trauma-related dysfunction best explains the 'happening now' quality?",
    "options": [
      "The hippocampus failing to time-stamp the memory as past/contextualized",
      "The amygdala being underactive and missing the threat",
      "The prefrontal cortex over-regulating the fear response",
      "The adrenal glands failing to release cortisol"
    ],
    "correct": "The hippocampus failing to time-stamp the memory as past/contextualized",
    "answer": "The HIPPOCAMPUS normally contextualizes memory and stamps it as 'past'; when its function is reduced by trauma, the memory intrudes without a time/context tag — so it feels PRESENT, not remembered. The amygdala is OVER-active (not under), the PFC is UNDER-regulating (not over), and cortisol timing isn't what produces the 'happening now' quality. The lost time-stamp is the tell.",
    "type": "mcq",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "hippocampus-context",
    "cluster": "trauma-brain",
    "bloom_level": "apply"
  },
  {
    "id": "u8-hpa-axis-recall-01",
    "prompt": "Trace the HPA axis stress-hormone loop and name what normally shuts it off.",
    "answer": "Hypothalamus releases CRH → pituitary releases ACTH → adrenal glands release CORTISOL, which mobilizes energy for threat. What shuts it off: NEGATIVE FEEDBACK — cortisol and hippocampal output feed back to inhibit further CRH release, returning the system to baseline. Chronic/early trauma dysregulates this loop (findings are inconsistent — sometimes elevated, sometimes blunted cortisol), which is why 'dysregulation of the stress axis' is the accurate takeaway rather than a clean 'high cortisol = trauma.'",
    "type": "recall",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "hpa-axis",
    "cluster": "trauma-brain",
    "bloom_level": "remember"
  },
  {
    "id": "u8-cortisol-evaluate-01",
    "prompt": "A workshop claims 'trauma shows up as high cortisol, so a cortisol test can confirm a trauma history.' Evaluate this against the actual evidence.",
    "answer": "Overstated and wrong as a diagnostic claim. The HPA/cortisol findings in trauma are INCONSISTENT — some studies show elevated baseline cortisol, others show reduced morning cortisol or blunted reactivity — and dysregulated cortisol responses are NOT consistently associated with psychopathology. So there is no clean 'high cortisol = trauma' biomarker, and a cortisol test cannot confirm or rule out a trauma history. The defensible statement is that trauma is associated with DYSREGULATION of the stress axis, read as direction, not a decimal — a caution against over-reading the neurobiology.",
    "type": "explain",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "cortisol-inconsistent",
    "cluster": "trauma-brain",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-explicit-implicit-compare-01",
    "prompt": "Distinguish EXPLICIT from IMPLICIT memory and explain how their trauma-related split produces a fragmented, non-verbal trauma memory.",
    "answer": "EXPLICIT memory (hippocampus-dependent) = conscious, verbal, NARRATIVE, time-stamped ('this happened last year'). IMPLICIT memory (amygdala-dependent) = non-conscious, SENSORY/emotional/bodily (a smell, a posture, a surge of dread). Under extreme trauma arousal, explicit encoding is DISRUPTED while implicit encoding is STRENGTHENED — so a survivor may carry vivid sensory/somatic fragments and intense reactions WITHOUT a coherent story, and a trigger can launch the body into full alarm before any conscious memory arrives. This is the defensible core of 'the body keeps the score': the body reacts before the narrative catches up.",
    "type": "compare",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "explicit-vs-implicit-memory",
    "cluster": "trauma-brain",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-freeze-vignette-01",
    "prompt": "An assault survivor says, 'It must have been partly my fault — I just froze, I didn't fight or scream.' Using the trauma-response model, how do you respond?",
    "answer": "Name FREEZE / tonic immobility as an INVOLUNTARY, hardwired defensive response — not a choice, not consent, and not weakness. The threat response isn't only fight-or-flight; freeze is an automatic shutdown mediated below conscious control, and it's extremely common during assault. So 'I froze' is the body doing what bodies do under overwhelming threat, not a failure of will or a sign of complicity. Reframing the freeze this way — as physiology, not fault — is often itself therapeutic and directly counters the self-blame.",
    "type": "vignette",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "freeze-not-a-choice",
    "cluster": "trauma-brain",
    "bloom_level": "apply"
  },
  {
    "id": "u8-window-tolerance-recall-01",
    "prompt": "Define the 'window of tolerance' and name the two states outside it.",
    "answer": "The WINDOW OF TOLERANCE (Siegel) is the arousal band in which a person stays regulated — able to think, feel, and stay present without being overwhelmed. ABOVE it = HYPERAROUSAL (fight/flight: panic, rage, racing thoughts, hypervigilance). BELOW it = HYPOAROUSAL (freeze/shutdown: numbness, dissociation, flatness, collapse). Trauma NARROWS and destabilizes the window, so small triggers push a survivor out of it. It's a clinical heuristic — a map for what you observe — not a measured brain state.",
    "type": "recall",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "window-of-tolerance",
    "cluster": "trauma-brain",
    "bloom_level": "understand"
  },
  {
    "id": "u8-window-hypo-mcq-01",
    "prompt": "Mid-session, a client recounting a trauma goes silent, stares blankly, stops responding, and seems 'checked out' and numb. In window-of-tolerance terms, this is best read as:",
    "options": [
      "Hypoarousal (dissociative shutdown) — help them re-orient/re-engage before any content work",
      "Hyperarousal — apply grounding to bring arousal down further",
      "Normal within-window processing — continue exploring the trauma detail",
      "Resistance to treatment that should be interpreted and confronted"
    ],
    "correct": "Hypoarousal (dissociative shutdown) — help them re-orient/re-engage before any content work",
    "answer": "Blank, numb, checked-out, non-responsive = HYPOAROUSAL (below the window: freeze/dissociation). The move is to help them back INTO the window by re-orienting/re-engaging (grounding to the present, gentle sensory contact), NOT to keep pushing trauma content — and not grounding-to-lower-arousal, which is for HYPERarousal (they're already too low). It isn't 'resistance' to interpret; it's the nervous system leaving the window, and content work waits until they're back in it.",
    "type": "mcq",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "hypoarousal",
    "cluster": "trauma-brain",
    "bloom_level": "apply"
  },
  {
    "id": "u8-bodykeepsscore-evaluate-01",
    "prompt": "A peer treats van der Kolk's 'The Body Keeps the Score' as settled neuroscience and cites it for the claim that trauma memories are perfectly stored in the body and can be recovered intact. Evaluate what to keep and what to flag.",
    "answer": "KEEP (corroborated): the explicit/implicit memory split, limbic hyperarousal, and the idea that the body reacts (somatically, physiologically) before the narrative — these are supported by peer-reviewed work. FLAG (contested/overstated): the book is POPULAR-PRESS, not peer-reviewed; the strong 'trauma is literally STORED in the body' metaphor is overstated; and claims of perfectly stored, recoverable-intact traumatic memory contradict memory science — trauma memory is RECONSTRUCTIVE and SUGGESTIBLE, not a sealed videotape. Also flag its reliance on POLYVAGAL THEORY, whose specific neurophysiological claims are scientifically contested. Use the book for orientation and empathy; corroborate the mechanisms elsewhere.",
    "type": "explain",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "body-keeps-score-contested",
    "cluster": "trauma-brain",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-body-remembers-cloze-01",
    "prompt": "Because trauma strengthens {{implicit}} memory (amygdala-based, sensory/bodily) while disrupting explicit narrative memory, a survivor can have somatic and emotional reactions to a trigger before any conscious story of the event arrives.",
    "answer": "implicit",
    "type": "cloze",
    "source_page": "wiki/concept-neurobiology-of-trauma.md",
    "topic": "implicit-memory",
    "cluster": "trauma-brain",
    "bloom_level": "understand"
  }
]
```

## Trauma-informed care vs. trauma treatment (cluster: trauma-informed-vs-treatment)

```json
[
  {
    "id": "u8-tic-treatment-compare-01",
    "prompt": "Distinguish TRAUMA-INFORMED CARE from TRAUMA TREATMENT on: what it is, who does it, whether the client must disclose, and the goal.",
    "answer": "TRAUMA-INFORMED CARE = a universal STANCE any counselor adopts in any setting; it does NOT require the client to disclose or process the trauma; its goal is to create safety and AVOID RE-TRAUMATIZATION. TRAUMA TREATMENT (trauma-focused) = a specific, TRAINED modality (PE, CPT, TF-CBT, EMDR); it DOES involve processing the trauma; its goal is to REDUCE trauma symptoms; only clinicians trained in the protocol should deliver it. One is 'first, do no harm' for everyone; the other is the specialized 'surgery' for those ready and with a trained clinician. Conflating them is what makes a beginner dig for the trauma story.",
    "type": "compare",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "informed-vs-treatment",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-three-es-recall-01",
    "prompt": "State SAMHSA's 'three E's' definition of trauma, and say which E is load-bearing and why.",
    "answer": "Trauma results from an EVENT (or series of events) that is EXPERIENCED as harmful or life-threatening and has lasting adverse EFFECTS on functioning and well-being. The load-bearing E is EXPERIENCE: the same event traumatizes one person and not another because what makes it traumatic is the person's subjective experience of it (appraisal, meaning, resources), not a checklist of 'bad enough' events. This is why you can't tell from the event alone who carries trauma — and why trauma-informed care has to be a UNIVERSAL stance.",
    "type": "recall",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "three-es",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "understand"
  },
  {
    "id": "u8-four-rs-recall-01",
    "prompt": "Name SAMHSA's 'four R's' of a trauma-informed approach, and state the approach's primary goal.",
    "answer": "REALIZE the widespread impact of trauma and paths to recovery; RECOGNIZE the signs and symptoms (in clients, families, staff, self); RESPOND by integrating trauma knowledge into policies, procedures, and practices; and RESIST RE-TRAUMATIZATION. The primary goal of the whole approach is to AVOID RE-TRAUMATIZATION — everything else serves that.",
    "type": "recall",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "four-rs",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "remember"
  },
  {
    "id": "u8-six-principles-cloze-01",
    "prompt": "Among SAMHSA's six principles of a trauma-informed approach — safety; trustworthiness and transparency; peer support; collaboration and mutuality; cultural/historical/gender issues — the principle about restoring the agency trauma took away is {{empowerment, voice, and choice}}.",
    "answer": "empowerment, voice, and choice",
    "type": "cloze",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "six-principles",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "remember"
  },
  {
    "id": "u8-dont-dig-vignette-01",
    "prompt": "A new client hints at 'some stuff that happened as a kid' and goes quiet. The trainee, wanting to 'be thorough and understand the root,' presses for the full account at intake. Why is this a trauma-informed-care error, and what's the move?",
    "answer": "It's an error because trauma-informed care does NOT require the client to disclose or process the trauma, and pressing for the narrative before safety and trust exist RE-ENACTS the powerlessness of the trauma — the 'be thorough' reflex serves the counselor's need to understand, not the client's safety. The move: assume the client MAY be a survivor, make it safe, screen gently ('has something happened that still affects you?'), accept the answer, and let the story come — or not — at their pace. Deep processing belongs in trauma TREATMENT with a trained clinician when the client is ready, not extracted at intake by a well-meaning probe.",
    "type": "vignette",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "dont-dig",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "apply"
  },
  {
    "id": "u8-tic-disclosure-mcq-01",
    "prompt": "Which statement correctly describes the relationship between trauma-informed care and client disclosure of trauma?",
    "options": [
      "Trauma-informed care does NOT require the client to disclose or process the trauma; it's a safety-creating stance",
      "Trauma-informed care requires taking a detailed trauma history at intake to be done properly",
      "Trauma-informed care means the counselor must deliver EMDR or exposure therapy",
      "Trauma-informed care applies only to clients with a diagnosed trauma disorder"
    ],
    "correct": "Trauma-informed care does NOT require the client to disclose or process the trauma; it's a safety-creating stance",
    "answer": "Trauma-informed care is a UNIVERSAL stance to create safety and avoid re-traumatization; it assumes any client MAY be a survivor and specifically does NOT require disclosure or processing. It is not a detailed-history mandate (that risks re-traumatizing), not a specific modality like EMDR (that's trauma TREATMENT), and not limited to diagnosed clients (its universality is the point).",
    "type": "mcq",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "tic-no-disclosure",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "understand"
  },
  {
    "id": "u8-treatments-mcq-01",
    "prompt": "Which set lists FIRST-LINE trauma TREATMENTS (trauma-focused psychotherapies), as opposed to elements of trauma-informed care?",
    "options": [
      "Prolonged Exposure (PE), Cognitive Processing Therapy (CPT), TF-CBT, and EMDR",
      "Offering choices, explaining procedures before doing them, and not probing for details",
      "Safety, trustworthiness, peer support, and empowerment",
      "Realize, Recognize, Respond, and Resist re-traumatization"
    ],
    "correct": "Prolonged Exposure (PE), Cognitive Processing Therapy (CPT), TF-CBT, and EMDR",
    "answer": "PE, CPT, TF-CBT, and EMDR are the first-line trauma-focused TREATMENTS in the APA and VA/DoD guidelines — structured, symptom-reducing modalities delivered by trained clinicians. The other options are trauma-INFORMED CARE: the stance (offering choice, explaining, not probing), the six principles, and the four R's. As a foundations counselor you recognize and REFER to the treatments, not deliver them untrained.",
    "type": "mcq",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "trauma-treatments",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "remember"
  },
  {
    "id": "u8-retraumatization-evaluate-01",
    "prompt": "SAMHSA says the primary goal of a trauma-informed approach is to avoid re-traumatization. Evaluate why a coercive, rushed, no-explanation intake can itself be re-traumatizing, using the six principles.",
    "answer": "A trauma-informed approach exists above all to AVOID RE-TRAUMATIZATION, and a coercive/rushed/opaque intake re-creates the very dynamics of trauma — powerlessness, unpredictability, being unheard, having control taken. Mapped to the principles: it violates SAFETY (feels unsafe), TRUSTWORTHINESS/TRANSPARENCY (surprises, no explanation), COLLABORATION/MUTUALITY (clinician holds all the power), and EMPOWERMENT/VOICE/CHOICE (no choices offered). For a survivor whose nervous system is primed for threat, that intake can trigger the same shutdown or hyperarousal the original trauma did — meaning the process meant to help instead reinjures. The corrective is to build safety, predictability, and choice into the process itself.",
    "type": "explain",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "avoid-retraumatization",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-experience-explain-01",
    "prompt": "Two people go through the same car accident; one develops trauma symptoms and one doesn't. Using SAMHSA's definition, explain how the same event can be traumatic for one person and not the other.",
    "answer": "Because trauma lives in the EXPERIENCE, not the event. SAMHSA's definition has three parts — Event, Experience, Effect — and the middle one is decisive: an event becomes traumatic through how the person subjectively EXPERIENCES it (their appraisal, sense of threat, meaning, and available resources at the time), which then determines the lasting Effects. The same crash can be experienced by one person as a survivable scare and by another as a life-threatening, helpless horror — differing prior history, meaning, and support produce different experiences and thus different outcomes. This is why you can't judge 'how traumatic' something 'should' be from the outside, and why the stance must be universal.",
    "type": "explain",
    "source_page": "wiki/concept-trauma-informed-care.md",
    "topic": "experience-is-subjective",
    "cluster": "trauma-informed-vs-treatment",
    "bloom_level": "understand"
  }
]
```

## The cost of the work: vicarious trauma & self-care (cluster: counselor-distress-types)

```json
[
  {
    "id": "u8-vt-def-recall-01",
    "prompt": "Define vicarious trauma (VT), including its mechanism and what specifically it changes in the counselor.",
    "answer": "VT (McCann & Pearlman, 1990) is the transformation of the COUNSELOR'S inner world — a disruption of their own cognitive SCHEMAS (beliefs about safety, trust, esteem, intimacy, and control) — that builds up from EMPATHIC EXPOSURE to clients' trauma material. Mechanism matters: it comes THROUGH empathy, not despite it, so the counselors most present with clients are the most exposed. It's framed by Constructivist Self-Development Theory (we construct reality through schemas, and bearing witness reshapes the helper's schemas), and it's cumulative and potentially lasting if unaddressed — a normal cost of caring, not a weakness.",
    "type": "recall",
    "source_page": "wiki/concept-vicarious-trauma.md",
    "topic": "vt-definition",
    "cluster": "counselor-distress-types",
    "bloom_level": "understand"
  },
  {
    "id": "u8-vt-schemas-cloze-01",
    "prompt": "Vicarious trauma disrupts five schema areas of the counselor's belief system: safety, {{trust}}, esteem, intimacy, and control.",
    "answer": "trust",
    "type": "cloze",
    "source_page": "wiki/concept-vicarious-trauma.md",
    "topic": "vt-schemas",
    "cluster": "counselor-distress-types",
    "bloom_level": "remember"
  },
  {
    "id": "u8-vt-burnout-compare-01",
    "prompt": "Contrast vicarious trauma with burnout on: what causes it, where it occurs, onset, and whether beliefs/imagery change.",
    "answer": "VT: caused by the specific TRAUMATIC CONTENT of clients' material; occurs ONLY in those working with trauma survivors; onset can be sudden/abrupt; and it DOES change the belief system (schema disruption in safety/trust/esteem/intimacy/control) plus intrusive imagery. BURNOUT: caused by general OVERLOAD/exhaustion (caseload, hours, workplace stress); occurs in ANY profession; onset is GRADUAL via emotional exhaustion; and it does NOT involve schema/imagery change. Short version: burnout is about volume, VT is about content — and many trauma counselors have both.",
    "type": "compare",
    "source_page": "wiki/concept-vicarious-trauma.md",
    "topic": "vt-vs-burnout",
    "cluster": "counselor-distress-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-distress-types-mcq-01",
    "prompt": "A counselor who works ONLY with sexual-assault survivors begins, after one especially graphic case, having nightmares featuring the assault and intrusive images of it during the day. Which term best fits?",
    "options": [
      "Secondary traumatic stress / vicarious trauma — PTSD-like symptoms and intrusive imagery from indirect exposure to a client's trauma",
      "Burnout — gradual emotional exhaustion from workload and hours",
      "Countertransference — a reaction rooted in the counselor's own past experiences",
      "Compassion satisfaction — the positive reward of helping"
    ],
    "correct": "Secondary traumatic stress / vicarious trauma — PTSD-like symptoms and intrusive imagery from indirect exposure to a client's trauma",
    "answer": "PTSD-like symptoms (nightmares, intrusive imagery) with SUDDEN onset after exposure to a specific client's trauma = secondary traumatic stress / vicarious trauma (STS emphasizes the PTSD-symptom picture; VT emphasizes the schema disruption — they overlap heavily). It's not burnout (that's gradual overload, no trauma-specific imagery), not countertransference (that stems from the counselor's OWN history, not the client's material), and certainly not compassion satisfaction.",
    "type": "mcq",
    "source_page": "wiki/concept-vicarious-trauma.md",
    "topic": "distress-discrimination",
    "cluster": "counselor-distress-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-countertransference-mcq-01",
    "prompt": "A counselor notices he becomes irritated and dismissive specifically with clients who remind him of his critical father, and this reaction fades when the session ends. This is best described as:",
    "options": [
      "Countertransference — a reaction rooted in the counselor's OWN past, tied to the session",
      "Vicarious trauma — schema disruption from clients' traumatic material that transcends the session",
      "Secondary traumatic stress — PTSD-like symptoms from indirect trauma exposure",
      "Burnout — general exhaustion from an overloaded caseload"
    ],
    "correct": "Countertransference — a reaction rooted in the counselor's OWN past, tied to the session",
    "answer": "A reaction driven by the counselor's OWN history (the critical father), directed at a specific client, and BOUND to the session = countertransference. Vicarious trauma comes from the CLIENT'S trauma material and TRANSCENDS the session (spilling into the counselor's whole life); STS is the PTSD-symptom picture from indirect exposure; burnout is general overload. The tells here: source = counselor's past, and it stays in the room.",
    "type": "mcq",
    "source_page": "wiki/concept-vicarious-trauma.md",
    "topic": "countertransference-vs-vt",
    "cluster": "counselor-distress-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-vt-normal-vignette-01",
    "prompt": "A supervisee confides, half-ashamed, that trauma cases have left her more fearful for her kids and less trusting of people, and she wonders if she's 'too weak for this work.' How do you reframe it without minimizing?",
    "answer": "Normalize WITHOUT minimizing. Name it as vicarious trauma — a NORMAL, expectable adaptation to sustained empathic contact with others' trauma (CSDT explicitly frames the counselor's reactions as normal and adaptive), specifically the schema shifts in SAFETY and TRUST she's describing. It is NOT a sign she's too weak or too soft; treating it as a personal failing is exactly what drives it underground and lets it become cumulative and lasting. Then don't stop at reassurance: pair the normalizing with action — peer supervision, caseload balance, self-care — because it's real and it needs tending, not just acceptance.",
    "type": "vignette",
    "source_page": "wiki/concept-vicarious-trauma.md",
    "topic": "vt-normalize",
    "cluster": "counselor-distress-types",
    "bloom_level": "apply"
  },
  {
    "id": "u8-proqol-cloze-01",
    "prompt": "The {{ProQOL}} (Professional Quality of Life scale) captures both sides of the work by measuring compassion satisfaction alongside burnout and secondary traumatic stress.",
    "answer": "ProQOL",
    "type": "cloze",
    "source_page": "wiki/concept-vicarious-trauma.md",
    "topic": "proqol",
    "cluster": "counselor-distress-types",
    "bloom_level": "remember"
  },
  {
    "id": "u8-vt-ethical-explain-01",
    "prompt": "Explain why unaddressed vicarious trauma is a CLINICAL and ETHICAL problem, not just the counselor's private burden. Link it to a specific stance from the trauma-informed-care page.",
    "answer": "Because as VT destabilizes the counselor's schemas, it degrades CLIENT care: boundary lapses (missed appointments, over-involvement), clinical errors and misdiagnosis, loss of sight of client strengths, 'rescuing,' and swinging between avoiding and intrusively PROBING trauma material. That last one directly violates the trauma-informed-care DON'T-DIG stance — a vicariously traumatized counselor is MORE likely to push for the trauma narrative and re-traumatize. Because it harms clients and can compromise fitness to practice, addressing VT is an ethical duty (ACA C.2.g impairment), which is why self-care is framed as an ethical competency rather than a personal luxury.",
    "type": "explain",
    "source_page": "wiki/concept-vicarious-trauma.md",
    "topic": "vt-ethical-problem",
    "cluster": "counselor-distress-types",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-selfcare-ethics-evaluate-01",
    "prompt": "The syllabus calls counselor self-care 'not optional — an ethical competency.' Build the argument that connects self-care to the ethics code.",
    "answer": "The chain: vicarious trauma / STS / burnout IMPAIR judgment and boundaries → an impaired counselor HARMS clients (boundary lapses, errors, misdiagnosis) → the ACA Code, standard C.2.g (Impairment), requires counselors to monitor for impairment, REFRAIN from practicing while impaired, seek help, and if needed limit/suspend/terminate their duties → therefore preventing and addressing one's own distress is an ETHICAL DUTY, not a personal luxury. It's the same fitness-to-practice thread as competence in Unit 3: staying within your competence includes staying FIT to practice it. An exhausted, boundary-slipping counselor who keeps a full trauma caseload is committing a slow ethical breach.",
    "type": "explain",
    "source_page": "wiki/concept-counselor-self-care.md",
    "topic": "self-care-ethics",
    "cluster": "counselor-distress-types",
    "bloom_level": "evaluate"
  },
  {
    "id": "u8-c2g-cloze-01",
    "prompt": "The ACA Code standard that makes self-care an ethical duty is C.2.g ({{Impairment}}): counselors monitor themselves for it, refrain from practicing when it's present, seek assistance, and if necessary limit, suspend, or terminate their duties.",
    "answer": "Impairment",
    "type": "cloze",
    "source_page": "wiki/concept-counselor-self-care.md",
    "topic": "aca-c2g",
    "cluster": "counselor-distress-types",
    "bloom_level": "remember"
  },
  {
    "id": "u8-organizational-analyze-01",
    "prompt": "Why is 'just do more self-care' an incomplete — even counterproductive — response to vicarious trauma? Name the levels prevention actually operates on.",
    "answer": "Because placing the whole burden on individual willpower ignores that VT dose is driven by the WORK, and it can shame counselors for a structural problem. Prevention is a SHARED responsibility across levels: ORGANIZATIONAL (caseload management — limiting trauma clients per week; funded supervision; traumatology training; adequate pay, paid vacation, coverage for personal counseling), SUPERVISORY (peer supervision/consultation — the most-used coping method and an ethical way to debrief given confidentiality limits), and PERSONAL (work/play/rest balance, social support, meaning/spirituality). Personal self-care sits ON TOP of a workplace that shares the load — 'self-care' around thirty trauma intakes a week will lose.",
    "type": "explain",
    "source_page": "wiki/concept-counselor-self-care.md",
    "topic": "organizational-prevention",
    "cluster": "counselor-distress-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u8-peer-supervision-vignette-01",
    "prompt": "After a harrowing trauma session, a counselor wants to unload the details to her spouse that night to cope. What's the problem, and what's the ethical alternative — and why is that alternative especially suited to the job?",
    "answer": "The problem: venting the session's details to a spouse BREAKS client confidentiality (Unit 3). The ethical alternative is PEER SUPERVISION / CONSULTATION — a setting where she CAN process the material without violating privacy. It's especially suited because it does several jobs at once: it NORMALIZES the reaction (lessening the shame that keeps VT hidden and cumulative), gives an outside perspective that REPAIRS the distorted schemas VT installs, and is the counselor's ethical release valve precisely because confidentiality limits prevent debriefing with friends and family. It was the single most-used coping method among trauma counselors for a reason.",
    "type": "vignette",
    "source_page": "wiki/concept-counselor-self-care.md",
    "topic": "peer-supervision",
    "cluster": "counselor-distress-types",
    "bloom_level": "apply"
  },
  {
    "id": "u8-selfcare-martyr-mcq-01",
    "prompt": "A counselor believes that a truly dedicated helper should be able to absorb unlimited client pain without needing time off or support. Best assessment of this belief?",
    "options": [
      "It's the martyr reflex — the very belief that produces impaired, boundary-slipping counselors who then help no one",
      "It's the professional ideal counselors should aspire to",
      "It's realistic as long as the counselor has strong enough willpower",
      "It only applies to counselors who haven't had their own therapy"
    ],
    "correct": "It's the martyr reflex — the very belief that produces impaired, boundary-slipping counselors who then help no one",
    "answer": "This is the MARTYR REFLEX, and it's self-defeating: the belief that a good counselor absorbs unlimited pain is exactly what produces vicarious trauma, impairment, and boundary lapses — an 'engulfed in anguish' counselor helps no one. Self-care isn't a willpower test or a lesser ideal; it's an ethical obligation (C.2.g) and an organizational responsibility. Sustainability IS competence, not a compromise of it.",
    "type": "mcq",
    "source_page": "wiki/concept-counselor-self-care.md",
    "topic": "martyr-reflex",
    "cluster": "counselor-distress-types",
    "bloom_level": "apply"
  }
]
```
