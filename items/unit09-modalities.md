# Unit 9 items — Evidence-Based Modalities (a practical toolkit)

Source of truth for Unit 9 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This is the "toolkit" unit — the concrete, structured
methods a counselor reaches for. Items lean hard on **application and discrimination** ("which tool
fits this client, and why?") because that is the real skill, and on the unit's **stance thread**: these
are the fixing tools, and two of them (MI's held **righting reflex**, the third wave's **acceptance**)
make *not* fixing the central move. Item ids use the `u9-` prefix. Clusters: `ebt-modalities`
(the cross-modality differential — the big interleaving target), `cbt-techniques`, `mi-processes`,
`oars-skills`, `sfbt-techniques`, `third-wave-skills`. See generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## Choosing among the modalities (cluster: ebt-modalities)

```json
[
  {
    "id": "u9-modalities-compare-01",
    "prompt": "For the five main modalities in this unit — CBT (cognitive restructuring), Behavioral Activation, Motivational Interviewing, Solution-Focused Brief Therapy, and the third-wave (ACT/DBT) — give the 'stuck because / better by' one-liner for each.",
    "answer": "CBT/restructuring: stuck because of distorted, inaccurate thinking → better by testing thoughts against evidence and building accurate alternatives. Behavioral Activation: stuck because avoidance/withdrawal has cut off reward → better by scheduling values-based activity (act first, mood follows). Motivational Interviewing: stuck because of unresolved ambivalence about change → better by evoking the client's OWN arguments for change (holding the righting reflex). Solution-Focused: stuck in a problem-saturated story → better by building on exceptions and a described preferred future, ignoring problem origins. ACT: stuck because the struggle to control/eliminate inner experience has taken over → better by acceptance + defusion + committed action toward values. DBT: stuck in pervasive emotion dysregulation → better by learning skills while holding acceptance AND change together.",
    "type": "compare",
    "source_page": "wiki/unit09-modalities.md",
    "topic": "modality-map",
    "cluster": "ebt-modalities",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-modality-ambivalence-mcq-01",
    "prompt": "A client court-referred for a DUI says, 'Honestly I don't think my drinking is a problem — I'm only here because I have to be.' Which approach best fits this moment?",
    "options": [
      "Motivational Interviewing — meet the ambivalence, evoke the client's own reasons, hold the righting reflex",
      "Behavioral Activation — schedule sober activities immediately",
      "Cognitive restructuring — challenge the distorted belief that drinking isn't a problem",
      "A detailed relapse-prevention plan starting today"
    ],
    "correct": "Motivational Interviewing — meet the ambivalence, evoke the client's own reasons, hold the righting reflex",
    "answer": "This is textbook ambivalence/pre-contemplation, and the other three options all trip the righting reflex — arguing for change or handing over a plan the client hasn't bought into will make them defend the drinking (sustain talk). MI is the tool for exactly this: engage, evoke change talk, let the client voice the case. The change-plan tools (BA, restructuring, relapse prevention) come AFTER motivation is engaged.",
    "type": "mcq",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "modality-fit-ambivalence",
    "cluster": "ebt-modalities",
    "bloom_level": "apply"
  },
  {
    "id": "u9-modality-depression-mcq-01",
    "prompt": "A depressed client has stopped seeing friends, quit the gym, and spends most of the day in bed; they say they'll 'do things again once I feel up to it.' Which intervention most directly targets this pattern?",
    "options": [
      "Behavioral Activation — schedule small values-based activities now, since motivation follows action",
      "Cognitive defusion — help them see their thoughts as just thoughts",
      "The miracle question",
      "Distress tolerance skills (TIPP)"
    ],
    "correct": "Behavioral Activation — schedule small values-based activities now, since motivation follows action",
    "answer": "The 'once I feel up to it' framing IS the depressive avoidance trap (TRAP): waiting for motivation that only comes downstream of action. BA inverts it — schedule small, graded, rewarding activity now (outside-in), which restores reinforcement and lifts mood. Defusion (ACT) and the miracle question (SFBT) target other problems; distress tolerance (DBT) is for crisis survival, not depressive withdrawal.",
    "type": "mcq",
    "source_page": "wiki/concept-behavioral-activation.md",
    "topic": "modality-fit-depression",
    "cluster": "ebt-modalities",
    "bloom_level": "apply"
  },
  {
    "id": "u9-modality-bpd-mcq-01",
    "prompt": "A client with borderline personality disorder presents with recurrent self-harm and intense, rapidly shifting emotions. Which modality has the strongest evidence base for this presentation?",
    "options": [
      "Dialectical Behavior Therapy (DBT)",
      "Solution-Focused Brief Therapy",
      "Classical (second-wave) cognitive restructuring alone",
      "Motivational Interviewing as a standalone treatment"
    ],
    "correct": "Dialectical Behavior Therapy (DBT)",
    "answer": "DBT was built by Linehan specifically for chronically suicidal / BPD clients and has the strongest RCT evidence for reducing suicide attempts and self-harm in this population (Linehan 1991 vs. TAU; 2006 vs. expert therapy). Restructuring-alone can read as invalidating for these clients; SFBT and MI aren't built for pervasive emotion dysregulation and self-harm.",
    "type": "mcq",
    "source_page": "wiki/concept-dbt-skills.md",
    "topic": "modality-fit-bpd",
    "cluster": "ebt-modalities",
    "bloom_level": "apply"
  },
  {
    "id": "u9-modality-chronicpain-mcq-01",
    "prompt": "A client with chronic pain has spent years trying to eliminate the pain and the anxious thoughts about it, and the struggle itself now dominates their life. Which approach fits best?",
    "options": [
      "ACT — accept the experience that can't be controlled, defuse from the thoughts, and act toward values",
      "Cognitive restructuring — prove the pain-related thoughts are false",
      "Behavioral Activation delivered as 'just push through and ignore it'",
      "A no-suicide contract"
    ],
    "correct": "ACT — accept the experience that can't be controlled, defuse from the thoughts, and act toward values",
    "answer": "When the control agenda has already failed on something that genuinely can't be eliminated (chronic pain, persistent intrusive thoughts), ACT's move fits: stop the unwinnable war, change your relationship to the experience (acceptance, defusion), and pour energy into valued action. Trying to prove the thoughts false (restructuring) keeps fighting the content; the other options misfit.",
    "type": "mcq",
    "source_page": "wiki/concept-act.md",
    "topic": "modality-fit-act",
    "cluster": "ebt-modalities",
    "bloom_level": "apply"
  },
  {
    "id": "u9-three-waves-recall-01",
    "prompt": "Name the three 'waves' of CBT-family therapy, what each targets, and one example from this unit of each.",
    "answer": "First wave — BEHAVIORAL: targets observable behavior via conditioning/reinforcement/avoidance (example: Behavioral Activation). Second wave — COGNITIVE: targets the CONTENT of thought — is it accurate? (example: CBT cognitive restructuring / the thought record). Third wave — CONTEXTUAL: targets your RELATIONSHIP to thought — acceptance over control (examples: ACT and DBT).",
    "type": "recall",
    "source_page": "wiki/unit09-modalities.md",
    "topic": "three-waves",
    "cluster": "ebt-modalities",
    "bloom_level": "remember"
  },
  {
    "id": "u9-ebp-definition-explain-01",
    "prompt": "'Evidence-based practice' does NOT simply mean 'use the treatment with the biggest effect size.' State the three components of the APA definition and why the distinction matters.",
    "answer": "APA evidence-based practice = integrating (1) the best available RESEARCH, (2) clinical EXPERTISE, and (3) the client's CHARACTERISTICS, culture, and preferences. It matters because a high-research-support method the client won't engage with, or that ignores their culture (Unit 4) or readiness to change, is NOT evidence-based practice for THAT person. You're choosing from a toolkit to fit the client, not always grabbing the #1-ranked technique.",
    "type": "explain",
    "source_page": "wiki/unit09-modalities.md",
    "topic": "evidence-based-practice",
    "cluster": "ebt-modalities",
    "bloom_level": "understand"
  },
  {
    "id": "u9-ebp-common-factors-evaluate-01",
    "prompt": "A trainee argues: 'Since we have evidence-based modalities now, technique choice is what really determines outcome — the relationship is secondary.' Evaluate this against the common-factors evidence.",
    "answer": "It overstates technique. The common-factors / dodo-bird evidence (Unit 1) shows that between bona-fide therapies, specific-technique differences are typically SMALL, and the alliance carries a large share of outcome variance. This doesn't make technique pointless — it means technique works THROUGH the relationship, not instead of it, and modality choice matters most for FIT and ENGAGEMENT rather than as a horse race. The trainee has the emphasis backwards: the relationship isn't secondary; it's the medium the technique runs on.",
    "type": "explain",
    "source_page": "wiki/unit09-modalities.md",
    "topic": "common-factors-caveat",
    "cluster": "ebt-modalities",
    "bloom_level": "evaluate"
  },
  {
    "id": "u9-modality-styles-analyze-01",
    "prompt": "Two of this unit's tools — Motivational Interviewing and Solution-Focused Brief Therapy — are described as sitting outside the CBT 'wave' scheme. In what sense are they different in KIND from CBT/BA/ACT/DBT?",
    "answer": "CBT, BA, ACT, and DBT are content/change MODELS — each has a theory of what maintains distress and a mechanism for changing it. MI is a STYLE or STANCE (a way of talking that resolves ambivalence) rather than a treatment of a disorder; it's what you use before a change model will land. SFBT is a postmodern TOOLKIT that deliberately refuses to theorize the problem at all, building instead on exceptions and a described future. So both are more about HOW you engage a client's own resources than about a specific change mechanism applied to specific pathology.",
    "type": "explain",
    "source_page": "wiki/unit09-modalities.md",
    "topic": "styles-vs-models",
    "cluster": "ebt-modalities",
    "bloom_level": "analyze"
  }
]
```

## CBT in practice: cognitive triangle & behavioral activation (cluster: cbt-techniques)

```json
[
  {
    "id": "u9-cognitive-model-cloze-01",
    "prompt": "Fill in the founding claim of the cognitive model: events don't directly cause feelings — our {{interpretation}} of events does.",
    "answer": "interpretation (i.e., the automatic thought / appraisal). Same event, different thought, different feeling — which locates the point of leverage.",
    "type": "cloze",
    "source_page": "wiki/concept-cognitive-triangle.md",
    "topic": "cognitive-model",
    "cluster": "cbt-techniques",
    "bloom_level": "remember"
  },
  {
    "id": "u9-hallway-apply-01",
    "prompt": "Using the cognitive triangle, walk the same situation — a friend walks past you in a hallway without saying hello — down two different paths to show why the feeling depends on the thought.",
    "answer": "Path A: thought 'he hates me / I did something wrong' → feeling hurt/anxious → behavior withdraw and ruminate. Path B: thought 'he's in a hurry / didn't see me' → feeling neutral → behavior text him later. Same event, different automatic thought, different emotion and behavior — the event didn't change, the interpretation did. That gap is where CBT intervenes.",
    "type": "explain",
    "source_page": "wiki/concept-cognitive-triangle.md",
    "topic": "cognitive-triangle-apply",
    "cluster": "cbt-techniques",
    "bloom_level": "apply"
  },
  {
    "id": "u9-thought-record-rep-01",
    "prompt": "PRACTICE REP (syllabus): Run a thought record on one of your own recent frustrations. Name the columns you move through in order, then fill them for a real example.",
    "answer": "Columns in order: (1) Situation — what happened, factually. (2) Automatic thought — what went through your mind. (3) Emotion, rated 0-100. (4) Evidence FOR the thought. (5) Evidence AGAINST it. (6) Balanced alternative thought. (7) Re-rate the emotion. The point of the rep is to notice that generating the balanced alternative YOURSELF (Socratic/guided discovery) shifts the feeling more than being told a reframe — and to feel how the emotion re-rating usually drops once the thought is tested.",
    "type": "recall",
    "source_page": "wiki/concept-cognitive-triangle.md",
    "topic": "thought-record-rep",
    "cluster": "cbt-techniques",
    "bloom_level": "apply"
  },
  {
    "id": "u9-three-levels-cognition-recall-01",
    "prompt": "Name the three levels of cognition in Beck's model, from most to least accessible, with an example of each.",
    "answer": "(1) Automatic thoughts — immediate, surface, situation-specific ('I'm going to fail this'). (2) Intermediate beliefs — conditional rules/assumptions ('If I'm not perfect, I'm a failure'). (3) Core beliefs / schemas — global, absolute self-judgments formed early ('I am inadequate' / 'I'm unlovable'). Beginning CBT works at the automatic-thought level; schemas are reached over time, not opened with.",
    "type": "recall",
    "source_page": "wiki/concept-cognitive-triangle.md",
    "topic": "levels-of-cognition",
    "cluster": "cbt-techniques",
    "bloom_level": "remember"
  },
  {
    "id": "u9-distortion-mcq-01",
    "prompt": "A client says: 'I bombed one interview question, so the whole interview was a disaster and I'll never get hired anywhere.' Which cognitive distortions are most clearly present?",
    "options": [
      "All-or-nothing thinking and overgeneralization (with catastrophizing)",
      "Emotional reasoning and mind reading",
      "Personalization and 'should' statements",
      "No distortion — this is an accurate appraisal"
    ],
    "correct": "All-or-nothing thinking and overgeneralization (with catastrophizing)",
    "answer": "'The whole interview was a disaster' from one bad question is all-or-nothing/dichotomous thinking; 'never get hired anywhere' generalizes one event into always/never/everywhere (overgeneralization) and leaps to the worst case (catastrophizing). Naming the pattern isn't dismissing the thought — it flags it as a hypothesis to test against evidence.",
    "type": "mcq",
    "source_page": "wiki/concept-cognitive-triangle.md",
    "topic": "cognitive-distortions",
    "cluster": "cbt-techniques",
    "bloom_level": "apply"
  },
  {
    "id": "u9-collaborative-empiricism-explain-01",
    "prompt": "Why is 'collaborative empiricism' the stance that keeps CBT from becoming the fix-it reflex — i.e., why isn't CBT 'telling clients their thoughts are wrong'?",
    "answer": "Collaborative empiricism means counselor and client work TOGETHER (collaborative) to treat automatic thoughts as HYPOTHESES to test against evidence (empiricism), not as errors the expert corrects. You don't overrule the client's reality; you co-investigate it ('what's the evidence? another way to see it? what would you tell a friend?'). This is why Beck TESTS thoughts rather than Ellis's more confrontational DISPUTING — and why CBT done well is collaborative rather than the corrective, fix-it stance the curriculum warns against, even though it looks the most procedural.",
    "type": "explain",
    "source_page": "wiki/theory-cbt-practice.md",
    "topic": "collaborative-empiricism",
    "cluster": "cbt-techniques",
    "bloom_level": "understand"
  },
  {
    "id": "u9-socratic-evaluate-01",
    "prompt": "In cognitive restructuring, why guide the client to GENERATE the balanced alternative thought (Socratic questioning) rather than just tell them a better thought?",
    "answer": "Because a client who produces their own reframe believes it more and remembers it longer than one who is handed it — the generation effect from the learning-science rulebook. Supplying the alternative also re-enacts the expert-corrects-the-patient stance and invites the client to argue back. Guided discovery ('what's the evidence on the other side? what would you tell a friend?') makes the insight the client's own, which is both more convincing and more durable.",
    "type": "explain",
    "source_page": "wiki/theory-cbt-practice.md",
    "topic": "socratic-questioning",
    "cluster": "cbt-techniques",
    "bloom_level": "evaluate"
  },
  {
    "id": "u9-restructuring-vs-ba-compare-01",
    "prompt": "Contrast cognitive restructuring and behavioral activation — the two engines inside CBT — by what each changes and the direction of causation each assumes.",
    "answer": "Cognitive restructuring changes the THOUGHT: identify a distorted automatic thought, test it against evidence, build a balanced alternative (thought → feeling). It assumes changing the interpretation shifts the emotion. Behavioral activation changes the BEHAVIOR: schedule rewarding, values-based, graded activity to break the avoidance/withdrawal cycle (behavior → feeling). It assumes you act your way into feeling (outside-in), not feel your way into acting. They're the second-wave (cognitive) vs. first-wave (behavioral) handles on the same triangle — and dismantling studies suggest the behavioral handle may do much of the work on its own.",
    "type": "compare",
    "source_page": "wiki/concept-behavioral-activation.md",
    "topic": "restructuring-vs-activation",
    "cluster": "cbt-techniques",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-ba-outside-in-cloze-01",
    "prompt": "Behavioral activation's core, counterintuitive slogan: you {{act}} your way into feeling better, not feel your way into acting.",
    "answer": "act (the 'outside-in' logic — motivation and mood follow action in depression, rather than preceding it).",
    "type": "cloze",
    "source_page": "wiki/concept-behavioral-activation.md",
    "topic": "outside-in",
    "cluster": "cbt-techniques",
    "bloom_level": "understand"
  },
  {
    "id": "u9-trap-trac-cloze-01",
    "prompt": "Behavioral activation's signature heuristic: get out of the {{TRAP}} (Trigger-Response-Avoidance Pattern) and back on TRAC (Trigger-Response-Alternative Coping).",
    "answer": "TRAP (Trigger → Response → Avoidance Pattern). The escape is TRAC — same trigger and feeling, but an approach/alternative-coping behavior instead of avoidance.",
    "type": "cloze",
    "source_page": "wiki/concept-behavioral-activation.md",
    "topic": "trap-trac",
    "cluster": "cbt-techniques",
    "bloom_level": "remember"
  },
  {
    "id": "u9-ba-avoidance-vignette-01",
    "prompt": "A depressed client got a critical email (trigger), felt shame (response), and hasn't opened their laptop for two days (avoidance) — now facing overdue work that deepens the low mood. Map this onto TRAP and describe the BA move.",
    "answer": "TRAP: Trigger = the critical email; Response = shame; Avoidance Pattern = not opening the laptop, which brings brief relief but piles up secondary problems (overdue work) and deepens depression. The BA move is TRAC: same trigger and feeling, but an Alternative Coping action — e.g., a tiny graded step like opening the laptop and drafting a two-line reply — done WITH the shame still present, not after it lifts. Small approach behavior restores reinforcement and breaks the downward spiral.",
    "type": "vignette",
    "source_page": "wiki/concept-behavioral-activation.md",
    "topic": "avoidance-cycle-apply",
    "cluster": "cbt-techniques",
    "bloom_level": "apply"
  },
  {
    "id": "u9-ba-dismantling-evaluate-01",
    "prompt": "Jacobson's 1996 dismantling study (n=150) compared behavioral activation alone, BA plus cognitive restructuring, and full CBT — all three worked equally well. Dimidjian 2006 (N=241) found BA matched medication and beat cognitive therapy for severe depression. Evaluate what this implies about the 'cognitive' part of CBT.",
    "answer": "It genuinely complicates the intuitive 'you must fix the distorted thoughts' story. If adding cognitive restructuring didn't improve on BA alone, and BA alone matched meds and beat cognitive therapy for severe depression, then much of CBT's benefit for depression may come from the BEHAVIORAL component, not from changing thought content. The honest reading: CBT works, but the cognitive-triangle mechanism is a useful map, not a proven active ingredient — hold it loosely. (Caveat: these are specific trials/populations; it doesn't mean cognition never matters, e.g., for anxiety/OCD.)",
    "type": "explain",
    "source_page": "wiki/concept-behavioral-activation.md",
    "topic": "dismantling-evidence",
    "cluster": "cbt-techniques",
    "bloom_level": "evaluate"
  },
  {
    "id": "u9-ba-prescribe-stance-01",
    "prompt": "A supervisor overhears a trainee tell a depressed, withdrawn client, 'You just need to get out more and exercise.' Why is this NOT behavioral activation, and what's the difference?",
    "answer": "'Just get out more' is advice-giving/the fix-it reflex: it bounces off anhedonia, shames the client for not already doing it, and hands over a goal they haven't bought into. Real BA is COLLABORATIVE and graded — you start from the client's own valued activities, break them into steps small enough to actually succeed at, monitor pleasure/mastery, and schedule specific tiny actions ('walk 15 min at 8am Tuesday'). The content ('do more activity') overlaps; the stance (with the client, small and specific, values-based) is what makes it a treatment rather than a platitude.",
    "type": "explain",
    "source_page": "wiki/concept-behavioral-activation.md",
    "topic": "ba-stance",
    "cluster": "cbt-techniques",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-exposure-analyze-01",
    "prompt": "How is exposure (for anxiety) the same underlying logic as behavioral activation (for depression), and how do they differ in target?",
    "answer": "Both are approach-not-avoid: they break a maladaptive avoidance cycle by having the client APPROACH what they've been avoiding, allowing new learning to occur while the difficult feeling is present. BA targets depressive WITHDRAWAL (approach rewarding/valued activity to restore reinforcement); exposure targets anxious AVOIDANCE of feared situations (graded, repeated approach so the fear response extinguishes and the catastrophic prediction is disconfirmed). Same behavioral engine — approach dissolves avoidance — pointed at different emotions. (DBT's 'opposite action' is the same idea again.)",
    "type": "explain",
    "source_page": "wiki/theory-cbt-practice.md",
    "topic": "exposure-vs-activation",
    "cluster": "cbt-techniques",
    "bloom_level": "analyze"
  }
]
```

## Motivational Interviewing (cluster: mi-processes)

```json
[
  {
    "id": "u9-mi-definition-cloze-01",
    "prompt": "Motivational Interviewing is best understood not as a treatment but as a person-centered counseling STYLE for addressing the common problem of {{ambivalence}} about change.",
    "answer": "ambivalence (holding two conflicting feelings about change at once — the normal condition of being stuck, not a deficit of knowledge or willpower).",
    "type": "cloze",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "mi-definition",
    "cluster": "mi-processes",
    "bloom_level": "remember"
  },
  {
    "id": "u9-righting-reflex-explain-01",
    "prompt": "Define the 'righting reflex' in MI and explain why acting on it backfires.",
    "answer": "The righting reflex is the helper's natural urge to jump in, warn, correct, and steer the client toward the healthy choice — it feels like caring. It backfires because when YOU voice the arguments FOR change, an ambivalent client stays balanced by voicing the arguments AGAINST it — and people talk themselves into their own positions. So pushing 'you should quit' evokes and strengthens the client's sustain talk. MI's discipline is to HOLD the righting reflex and arrange the conversation so the client makes the case for change. It's this curriculum's fix-it stance, named as a technical hazard.",
    "type": "explain",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "righting-reflex",
    "cluster": "mi-processes",
    "bloom_level": "understand"
  },
  {
    "id": "u9-righting-reflex-vignette-01",
    "prompt": "A counselor tells a client, 'Look, the smoking is clearly killing you — you have to quit for your kids.' The client replies, 'It's the only thing that keeps me sane, and plenty of people smoke and live to ninety.' Name what just happened in MI terms and the better move.",
    "answer": "The counselor acted on the RIGHTING REFLEX (arguing for change), which evoked SUSTAIN TALK — the client defended the status quo to restore balance. This is discord, a signal about the counselor's stance, not a defect in the client. The better move is to STOP arguing, roll with it, and evoke the client's own change talk instead — e.g., an open question ('What worries YOU about the smoking?') and reflections of any change talk that follows.",
    "type": "vignette",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "righting-reflex-apply",
    "cluster": "mi-processes",
    "bloom_level": "apply"
  },
  {
    "id": "u9-pace-recall-01",
    "prompt": "The 'spirit' of MI is captured by PACE. Name the four elements.",
    "answer": "Partnership (a collaboration of experts — you on change, the client on their life), Acceptance (absolute worth, accurate empathy, autonomy support, affirmation), Compassion (actively prioritizing the client's welfare), and Evocation (drawing out the motivation and resources already in the client). Run the techniques without the spirit and MI becomes manipulation.",
    "type": "recall",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "mi-spirit-pace",
    "cluster": "mi-processes",
    "bloom_level": "remember"
  },
  {
    "id": "u9-four-processes-recall-01",
    "prompt": "Name the four processes of MI in order, and say which one is the distinctive heart of the method.",
    "answer": "Engaging → Focusing → Evoking → Planning. EVOKING is the distinctive heart — eliciting the client's OWN motivations so they voice the arguments for change (drawing out change talk). The processes are sequential but recursive; moving to Planning too early trips the righting reflex.",
    "type": "recall",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "four-processes",
    "cluster": "mi-processes",
    "bloom_level": "remember"
  },
  {
    "id": "u9-processes-mcq-01",
    "prompt": "A client is clearly motivated and says, 'I'm done drinking — I just don't know how to start.' In the four-processes model, where are you, and what's the task?",
    "options": [
      "Planning — collaboratively develop a change plan the client owns and drives",
      "Engaging — you still need to build the relationship first",
      "Focusing — you haven't identified a target behavior yet",
      "Evoking — keep eliciting reasons to change"
    ],
    "correct": "Planning — collaboratively develop a change plan the client owns and drives",
    "answer": "The client has moved to mobilizing change talk ('I'm done… I just don't know how to start') — commitment plus a request for help executing. That's the signal to move into PLANNING: build an acceptable, client-driven plan. Staying in Evoking here (piling on more reasons) would be tone-deaf; the earlier processes are already done.",
    "type": "mcq",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "processes-apply",
    "cluster": "mi-processes",
    "bloom_level": "apply"
  },
  {
    "id": "u9-change-sustain-compare-01",
    "prompt": "Contrast change talk and sustain talk, give the DARN-CAT breakdown of change talk, and say what the counselor does with each.",
    "answer": "Change talk = any client speech favoring change; sustain talk = client speech favoring the status quo. More change talk (and less sustain talk) predicts actual behavior change, so the counselor SELECTIVELY evokes, reflects, and reinforces change talk and lets sustain talk pass without amplifying it. DARN-CAT: preparatory change talk = Desire ('I want to'), Ability ('I could'), Reasons ('I'd sleep better'), Need ('I have to'); mobilizing change talk = Commitment ('I will'), Activation ('I'm ready'), Taking steps ('I already started'). The shift from DARN to CAT signals readiness to move to Planning.",
    "type": "compare",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "change-vs-sustain-talk",
    "cluster": "mi-processes",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-darn-cat-mcq-01",
    "prompt": "A client says, 'I already threw out the cigarettes I had at home.' Which kind of change talk is this?",
    "options": [
      "Mobilizing change talk — Taking steps (the 'T' in CAT)",
      "Preparatory change talk — Desire (the 'D' in DARN)",
      "Sustain talk",
      "Preparatory change talk — Reasons (the 'R' in DARN)"
    ],
    "correct": "Mobilizing change talk — Taking steps (the 'T' in CAT)",
    "answer": "Reporting an action already taken toward change is 'Taking steps' — mobilizing change talk (CAT), the strongest signal of readiness. Desire/Ability/Reasons/Need are PREPARATORY (still weighing it); this client has moved past weighing into doing, which points toward Planning.",
    "type": "mcq",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "darn-cat",
    "cluster": "mi-processes",
    "bloom_level": "apply"
  },
  {
    "id": "u9-discord-evaluate-01",
    "prompt": "MI deliberately retired the word 'resistance' as a client trait, reframing it as 'discord.' Evaluate why this reframe changes what the counselor does.",
    "answer": "Calling it 'resistance' locates the problem IN the client (a trait to overcome), which licenses pushing harder — and pushing evokes more sustain talk. Reframing it as DISCORD locates it in the RELATIONSHIP: it's a two-way street, usually a signal the counselor got ahead of the client or tripped the righting reflex. That changes the response from 'push through resistance' to 'change direction or listen more carefully' (double-sided/amplified reflection, reframing, emphasizing autonomy). The reframe is powerful because it makes the counselor's own stance the adjustable variable rather than blaming the client.",
    "type": "explain",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "discord-vs-resistance",
    "cluster": "mi-processes",
    "bloom_level": "evaluate"
  },
  {
    "id": "u9-mi-planning-too-early-vignette-01",
    "prompt": "A client is still openly ambivalent ('part of me wants to cut back, part of me really doesn't'). The counselor responds by outlining a detailed week-by-week reduction schedule. What's the error, and what does it predict?",
    "answer": "The counselor jumped to PLANNING while the client is still in the EVOKING stage (unresolved ambivalence). Planning before the client has voiced and resolved their ambivalence trips the righting reflex — imposing a plan the client hasn't bought into — and predicts sustain talk, discord, and a plan that won't stick. The move is to stay with evoking: draw out and reflect the client's own change talk until they, not the counselor, start proposing steps.",
    "type": "vignette",
    "source_page": "wiki/theory-motivational-interviewing.md",
    "topic": "premature-planning",
    "cluster": "mi-processes",
    "bloom_level": "apply"
  }
]
```

## OARS — the core MI skills (cluster: oars-skills)

```json
[
  {
    "id": "u9-oars-recall-01",
    "prompt": "OARS names the four core MI skills. What does each letter stand for?",
    "answer": "O = Open questions (can't be answered in a word; invite elaboration). A = Affirmations (genuine recognition of strengths/effort/worth). R = Reflective listening (say back a hypothesis about the client's meaning as a statement — the key to expressing empathy). S = Summaries (gather what the client said into a fuller picture, and hand back the change talk).",
    "type": "recall",
    "source_page": "wiki/concept-oars.md",
    "topic": "oars-recall",
    "cluster": "oars-skills",
    "bloom_level": "remember"
  },
  {
    "id": "u9-oars-microskills-explain-01",
    "prompt": "The course-map flags a cross-unit thread: 'Microskills ↔ OARS.' Explain how OARS relates to Unit 1's microskills, and what MI adds.",
    "answer": "OARS IS essentially the Unit 1 microskills set (open questions, reflection, summarizing — the attending/listening/reflecting skills) reused. What MI adds is a DIRECTION: in plain listening you reflect to understand; in MI you deploy the same skills SELECTIVELY to draw out and strengthen change talk. Same relational engine, aimed at ambivalence. Naming the link is the point — you already know the engine from Unit 1.",
    "type": "explain",
    "source_page": "wiki/concept-oars.md",
    "topic": "oars-microskills-link",
    "cluster": "oars-skills",
    "bloom_level": "understand"
  },
  {
    "id": "u9-reflection-vs-question-compare-01",
    "prompt": "Beginners over-question. Contrast reflections and questions as MI moves, and explain the guidance to keep a high reflection-to-question ratio.",
    "answer": "A question DEMANDS more disclosure and, stacked, turns the session into an interrogation with the counselor driving. A reflection DEMONSTRATES understanding — you state back a hypothesis about the client's meaning ('That sounds exhausting'), which often does more than a follow-up question ('How does that make you feel?'). A higher reflection-to-question ratio predicts better outcomes, so the guidance is: when in doubt, reflect. Reflection also lets you selectively amplify change talk by having the client hear it again. The single most common OARS error to catch in yourself is question-stacking.",
    "type": "compare",
    "source_page": "wiki/concept-oars.md",
    "topic": "reflection-vs-question",
    "cluster": "oars-skills",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-affirmation-vs-approval-analyze-01",
    "prompt": "Distinguish an MI 'affirmation' from the counselor's approval or praise, and connect it to a Unit 1 concept.",
    "answer": "An affirmation names something REAL and specific about the client's strength, effort, or worth ('It took real effort to come in today when part of you didn't want to'). Approval/praise ('Good job! You're doing amazing!') is the counselor's evaluation, which makes worth CONTINGENT on doing what the counselor wants — the opposite of unconditional positive regard (Unit 1). Affirmations build the alliance and counter shame (which fuels sustain talk) precisely because they aren't contingent judgments.",
    "type": "explain",
    "source_page": "wiki/concept-oars.md",
    "topic": "affirmation-vs-approval",
    "cluster": "oars-skills",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-complex-reflection-apply-01",
    "prompt": "A client says: 'I keep saying I'll deal with the debt but then I just avoid the mail for weeks.' Give a simple reflection and a complex reflection, and say why the complex one can do more.",
    "answer": "Simple reflection (restates content/feeling): 'So you intend to deal with it, but you end up avoiding it.' Complex reflection (adds meaning / continues the paragraph): 'Part of you really wants to face this — and the avoidance might be about how overwhelming or shameful opening that mail feels.' The complex reflection can do more because it names the unspoken (the avoidance's function, the ambivalence) and, if it lands, invites the client to elaborate their own change talk — while still being offered as a hypothesis, not a pronouncement.",
    "type": "vignette",
    "source_page": "wiki/concept-oars.md",
    "topic": "complex-reflection",
    "cluster": "oars-skills",
    "bloom_level": "apply"
  },
  {
    "id": "u9-oars-produces-change-talk-analyze-01",
    "prompt": "Explain how the four OARS skills work together as a delivery system for MI's mechanism (change talk).",
    "answer": "OARS isn't neutral listening; it's engineered to make the CLIENT voice the arguments for change. You ASK an evocative open question ('What would be some good reasons to cut back?'); the client answers with change talk; you REFLECT it back (they hear it twice); you AFFIRM the strength it reveals; and you SUMMARIZE a cluster of change talk (they hear their own case assembled in one place). Every argument for change is spoken by the client, not the counselor — which is exactly why it sticks (the generation effect) and why the righting reflex stays disarmed.",
    "type": "explain",
    "source_page": "wiki/concept-oars.md",
    "topic": "oars-mechanism",
    "cluster": "oars-skills",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-question-stacking-evaluate-01",
    "prompt": "A trainee's transcript shows nine questions and one reflection in ten minutes, all open-ended and warm. Evaluate the trainee's OARS use.",
    "answer": "Warm and open-ended isn't enough — the reflection-to-question RATIO is badly skewed toward questions, which is the classic beginner error. Even open questions, when stacked, put the counselor in the driver's seat and make the session feel like an interrogation, evoking less change talk than reflections would. The corrective: cut the questions roughly in half and convert many into reflections, aiming for more reflections than questions. Good intentions and open format don't rescue an interrogation.",
    "type": "explain",
    "source_page": "wiki/concept-oars.md",
    "topic": "question-stacking",
    "cluster": "oars-skills",
    "bloom_level": "evaluate"
  }
]
```

## Solution-Focused Brief Therapy (cluster: sfbt-techniques)

```json
[
  {
    "id": "u9-miracle-question-recall-01",
    "prompt": "What is the 'miracle question' in SFBT, and what job does it do?",
    "answer": "A classic wording: 'Suppose tonight while you sleep a miracle happens and the problem that brought you here is solved — but you were asleep, so you don't know it happened. When you wake up, what's the first small sign that tells you things are different? What else? Who else would notice?' Its job is to bypass problem analysis and elicit a concrete, vivid, BEHAVIORAL picture of the client's preferred future — which becomes the goal, described in the client's own detail. Experimentally it also reduces negative affect more than problem-focused questions.",
    "type": "recall",
    "source_page": "wiki/theory-solution-focused.md",
    "topic": "miracle-question",
    "cluster": "sfbt-techniques",
    "bloom_level": "remember"
  },
  {
    "id": "u9-sfbt-assumptions-cloze-01",
    "prompt": "Fill in SFBT's rule of thumb about what to change: 'If it works, {{do more of it}}. If it doesn't work, do something different.'",
    "answer": "do more of it. (Paired with 'do something different' when it isn't working — reflecting the premise that you don't need to understand a problem's origins to build a solution.)",
    "type": "cloze",
    "source_page": "wiki/theory-solution-focused.md",
    "topic": "sfbt-assumptions",
    "cluster": "sfbt-techniques",
    "bloom_level": "remember"
  },
  {
    "id": "u9-scaling-apply-01",
    "prompt": "A client rates themselves a 4 out of 10 on coping today. Give the two SFBT scaling follow-up questions that do the therapeutic work, and say what each accomplishes.",
    "answer": "(1) 'What makes you a 4 and not a 2?' — surfaces the strengths and resources ALREADY present (what's keeping them off the floor). (2) 'What would a 5 look like — one small thing that would tell you you'd moved up half a point?' — defines the next tiny, concrete, observable step. Together they turn a vague felt-sense into something measurable and generate an action step, without any analysis of why the problem exists.",
    "type": "explain",
    "source_page": "wiki/theory-solution-focused.md",
    "topic": "scaling-questions",
    "cluster": "sfbt-techniques",
    "bloom_level": "apply"
  },
  {
    "id": "u9-exception-explain-01",
    "prompt": "What is an 'exception question' in SFBT, and why does the approach treat exceptions as important?",
    "answer": "An exception question asks about times the problem could have happened but didn't, or was less severe: 'Tell me about a recent time this was a little better — what was different, what were you doing?' Exceptions matter because SFBT assumes solutions are already present, in miniature, in the client's life — the exception is a seed of the solution to be noticed and amplified ('do more of what works'). Exception (and scaling) questions are the SFBT techniques with the most empirical support.",
    "type": "explain",
    "source_page": "wiki/theory-solution-focused.md",
    "topic": "exception-questions",
    "cluster": "sfbt-techniques",
    "bloom_level": "understand"
  },
  {
    "id": "u9-sfbt-techniques-compare-01",
    "prompt": "Compare the miracle question, exception questions, and scaling questions by the distinct job each does in SFBT.",
    "answer": "Miracle question: builds the GOAL — a vivid, concrete picture of the preferred future, bypassing problem analysis (and it reduces negative affect). Exception questions: find EXISTING solutions — times the problem was absent or milder, to amplify what already works. Scaling questions: MEASURE and mobilize — locate the client on a 0-10, surface the strengths keeping them above the bottom ('why a 4 not a 2?'), and define the next small step ('what's a 5?'), which produces concrete action steps. Future / past / present-and-next, respectively — three tools for three jobs, all strengths-first.",
    "type": "compare",
    "source_page": "wiki/theory-solution-focused.md",
    "topic": "sfbt-techniques-compare",
    "cluster": "sfbt-techniques",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-coping-question-vignette-01",
    "prompt": "A client is so overwhelmed that the miracle question falls flat — they can't imagine anything being different. Which SFBT move fits, and what does it accomplish?",
    "answer": "Use a COPING question: 'Things sound really hard right now. How have you managed to keep going? How do you get through a day like that?' It meets a too-stuck client where they are, reframes bare survival as active coping, and finds resources hidden inside the despair — a foothold to build on when future-focused questions are too big a leap. (In genuine crisis, the Unit 8 stance takes priority over solution-forcing.)",
    "type": "vignette",
    "source_page": "wiki/theory-solution-focused.md",
    "topic": "coping-questions",
    "cluster": "sfbt-techniques",
    "bloom_level": "apply"
  },
  {
    "id": "u9-sfbt-evidence-evaluate-01",
    "prompt": "A brochure claims SFBT produces a couples effect size of g ≈ 3.02 and is 'effective in 86% of studies.' Evaluate how much weight to put on these numbers.",
    "answer": "Treat the giant figures skeptically. Some of the largest reported SFBT effect sizes come from PROPONENT sources and are almost certainly inflated by allegiance and publication bias — a g ≈ 3.02 is implausibly large for a psychotherapy. The more trustworthy peer-reviewed meta-analytic estimate is more modest (e.g., g ≈ 1.17 on psychosocial functioning in community RCTs), and even that shows SFBT MATCHING established treatments in fewer sessions rather than beating them. SFBT's real strength is that it 'began as evidence-based' (empirically derived from observed sessions) and is brief/portable — not that it's dramatically superior.",
    "type": "explain",
    "source_page": "wiki/theory-solution-focused.md",
    "topic": "sfbt-evidence-caution",
    "cluster": "sfbt-techniques",
    "bloom_level": "evaluate"
  }
]
```

## Third-wave: ACT & DBT (cluster: third-wave-skills)

```json
[
  {
    "id": "u9-psych-flexibility-cloze-01",
    "prompt": "The single goal of ACT is {{psychological flexibility}} — contacting the present moment fully and changing or persisting in behavior in the service of chosen values.",
    "answer": "psychological flexibility. Its opposite, psychological inflexibility, is driven by experiential avoidance and cognitive fusion.",
    "type": "cloze",
    "source_page": "wiki/concept-act.md",
    "topic": "psychological-flexibility",
    "cluster": "third-wave-skills",
    "bloom_level": "remember"
  },
  {
    "id": "u9-hexaflex-recall-01",
    "prompt": "Name the six core processes of ACT (the hexaflex) and the two halves they group into.",
    "answer": "Mindfulness & acceptance half: (1) Acceptance, (2) Cognitive defusion, (3) Contact with the present moment, (4) Self as context. Commitment & behavior-change half: (5) Values, (6) Committed action (plus present-moment and self-as-context, which bridge both halves). All six serve one goal: psychological flexibility.",
    "type": "recall",
    "source_page": "wiki/concept-act.md",
    "topic": "hexaflex",
    "cluster": "third-wave-skills",
    "bloom_level": "remember"
  },
  {
    "id": "u9-defusion-vs-restructuring-analyze-01",
    "prompt": "Both CBT and ACT deal with a distressing thought like 'I'm a failure.' Contrast cognitive restructuring (CBT) with cognitive defusion (ACT) in how each handles it.",
    "answer": "Cognitive restructuring (2nd-wave CBT) engages the thought's CONTENT: is it accurate? Examine the evidence for/against and build a more balanced alternative ('I failed at this, but I've succeeded at many things'). Cognitive defusion (3rd-wave ACT) leaves the content ALONE and changes your RELATIONSHIP to the thought — seeing it as just a thought, not literal truth ('I'm having the thought that I'm a failure'; repeating the word until it's noise). CBT asks 'is it true?'; ACT asks 'is fighting/believing this workable, and can I hold it lightly and act on my values anyway?'",
    "type": "compare",
    "source_page": "wiki/concept-act.md",
    "topic": "defusion-vs-restructuring",
    "cluster": "third-wave-skills",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-acceptance-not-resignation-evaluate-01",
    "prompt": "A client hears 'acceptance' in ACT and objects: 'So you're telling me to give up and just tolerate feeling this way?' Evaluate the objection.",
    "answer": "The objection misreads acceptance. In ACT, acceptance is NOT liking the pain, giving up, or passively tolerating a bad situation — it's stopping the UNWINNABLE WAR against your own inner experience so your energy goes into valued action instead. You accept the anxiety in order to DO the thing that matters anyway; acceptance is in the service of committed action, not instead of it. That's precisely why it isn't resignation or quietism — it's what frees you to move. (And for changeable external situations, ACT still supports action to change them.)",
    "type": "explain",
    "source_page": "wiki/concept-act.md",
    "topic": "acceptance-not-resignation",
    "cluster": "third-wave-skills",
    "bloom_level": "evaluate"
  },
  {
    "id": "u9-dbt-modules-recall-01",
    "prompt": "Name the four DBT skills modules and say which are acceptance-oriented and which are change-oriented.",
    "answer": "Acceptance-oriented: (1) Mindfulness (the core module, taught first) and (2) Distress Tolerance (get through a crisis without making it worse — TIPP, radical acceptance). Change-oriented: (3) Emotion Regulation (label emotions, reduce vulnerability, opposite action) and (4) Interpersonal Effectiveness (ask/refuse while keeping the relationship and self-respect — DEAR MAN, GIVE, FAST). The two-and-two split is the dialectic (acceptance AND change) built into the curriculum.",
    "type": "recall",
    "source_page": "wiki/concept-dbt-skills.md",
    "topic": "dbt-modules",
    "cluster": "third-wave-skills",
    "bloom_level": "remember"
  },
  {
    "id": "u9-dbt-dialectic-explain-01",
    "prompt": "What is the central 'dialectic' in DBT, and why is it especially important for the clients DBT was built for?",
    "answer": "The central dialectic is ACCEPTANCE and CHANGE held together at once: 'You are doing the best you can, AND you need to do better.' It matters for chronically dysregulated / BPD clients because a purely change-focused therapy tells them their reactions are wrong and must be fixed — which they experience as the same INVALIDATION that helped create the problem — while a purely acceptance-focused therapy leaves them stuck. DBT validates first (taking their pain and effort seriously) and only then pushes for change, resolving the fix-it paradox for exactly the clients where fixing-without-accepting backfires most.",
    "type": "explain",
    "source_page": "wiki/concept-dbt-skills.md",
    "topic": "dbt-dialectic",
    "cluster": "third-wave-skills",
    "bloom_level": "understand"
  },
  {
    "id": "u9-act-vs-dbt-compare-01",
    "prompt": "ACT and DBT are both third-wave, acceptance-and-mindfulness-based therapies. Contrast them by their target, structure, and strongest evidence base.",
    "answer": "TARGET: ACT aims broadly at psychological flexibility (acceptance + defusion + values-based action) for a wide range of problems, especially where control has failed (chronic pain, rumination); DBT targets pervasive EMOTION DYSREGULATION specifically. STRUCTURE: ACT is a model/set of processes (the hexaflex) applied flexibly; DBT is a structured SKILLS program (four modules) usually within a four-component treatment (individual therapy, skills group, phone coaching, consultation team). EVIDENCE: ACT is evidence-based across anxiety/depression/pain but not shown superior to CBT; DBT has the strongest RCT evidence for reducing suicide attempts/self-harm in BPD and is the gold standard there. Shared DNA (mindfulness, acceptance); different scope and build.",
    "type": "compare",
    "source_page": "wiki/concept-dbt-skills.md",
    "topic": "act-vs-dbt",
    "cluster": "third-wave-skills",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-dbt-scope-analyze-01",
    "prompt": "A newly licensed counselor took a weekend workshop on DBT distress-tolerance skills and now advertises 'DBT therapy.' What's the scope-of-practice problem?",
    "answer": "Borrowing individual DBT skills (distress tolerance, mindfulness) into general practice is fine and useful. But 'doing DBT' means the full, structured program — individual therapy PLUS skills group PLUS phone coaching PLUS a therapist consultation team, delivered with fidelity and training. Advertising 'DBT therapy' after a weekend workshop misrepresents competence and scope (Unit 3): it's 'DBT-informed' skills-borrowing, not DBT. Claiming the brand without the training and structure is a competence/scope-of-practice violation.",
    "type": "explain",
    "source_page": "wiki/concept-dbt-skills.md",
    "topic": "dbt-scope",
    "cluster": "third-wave-skills",
    "bloom_level": "analyze"
  },
  {
    "id": "u9-opposite-action-apply-01",
    "prompt": "A client's depression urges them to cancel a lunch with a friend and stay home. Their DBT skills coach suggests they go anyway. Name the DBT skill, and connect it to two other techniques in this unit.",
    "answer": "This is OPPOSITE ACTION (from the Emotion Regulation module): when an emotion's urge is unjustified or unhelpful, act against it (the urge says withdraw → you approach). It's the same approach-not-avoid logic as behavioral activation (act toward value while the low mood is present) and as exposure (approach the avoided thing so new learning occurs) — one behavioral engine appearing in three modalities.",
    "type": "vignette",
    "source_page": "wiki/concept-dbt-skills.md",
    "topic": "opposite-action",
    "cluster": "third-wave-skills",
    "bloom_level": "apply"
  },
  {
    "id": "u9-act-when-vignette-01",
    "prompt": "A client with recurring intrusive thoughts says, 'I've tried everything to get rid of these thoughts and nothing works — I spend all day fighting them.' Why might an ACT frame fit better here than trying harder to eliminate the thoughts?",
    "answer": "The client's whole problem is now the STRUGGLE to control an experience that won't be controlled — the control agenda has failed and become the main event (experiential avoidance, cognitive fusion). ACT stops trying to eliminate the thoughts and instead builds acceptance and defusion (hold the thoughts lightly, as thoughts) so the client can redirect energy into valued action. Trying harder to get rid of them just feeds the war. (Note: for OCD specifically, exposure with response prevention is also first-line — see Unit 6.)",
    "type": "vignette",
    "source_page": "wiki/concept-act.md",
    "topic": "act-fit",
    "cluster": "third-wave-skills",
    "bloom_level": "apply"
  }
]
```
