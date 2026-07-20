# Unit 10 items — Group Counseling

Source of truth for Unit 10 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This unit's one idea is that **groups heal differently**
— through mechanisms a dyad cannot supply — so the items lean on **discrimination** (which therapeutic
factor / which stage / which group type / which difficult member?) and on the unit's **stance thread**:
*decenter yourself and trust the group.* The beginner's trap here is running individual therapy in
front of an audience; the skill is activating the group as the therapist. Item ids use the `u10-`
prefix. Clusters: `yalom-factors` (the prime interleaving set), `group-stages`, `leadership-functions`,
`group-types`, `difficult-members`, `group-formation`. See generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## Yalom's therapeutic factors (cluster: yalom-factors)

```json
[
  {
    "id": "u10-eleven-factors-recall-01",
    "prompt": "Name as many of Yalom's eleven therapeutic factors as you can, and say which two Yalom considered most important.",
    "answer": "The eleven: (1) instillation of hope, (2) universality, (3) imparting information, (4) altruism, (5) corrective recapitulation of the primary family group, (6) development of socializing techniques, (7) imitative behavior, (8) interpersonal learning, (9) group cohesiveness, (10) catharsis, (11) existential factors. The two Yalom weighted most heavily: GROUP COHESIVENESS (the precondition — the group analog of the individual alliance) and INTERPERSONAL LEARNING (the factor that most distinctively cannot be replicated in individual therapy).",
    "type": "recall",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "eleven-factors",
    "cluster": "yalom-factors",
    "bloom_level": "remember"
  },
  {
    "id": "u10-universality-cloze-01",
    "prompt": "The therapeutic factor that dissolves shame and isolation by disconfirming a member's sense of being uniquely broken — 'I'm not the only one' — is {{universality}}.",
    "answer": "universality. You can assert it in individual therapy, but only a group lets the client actually experience it (hear their own secret in someone else's mouth).",
    "type": "cloze",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "universality",
    "cluster": "yalom-factors",
    "bloom_level": "remember"
  },
  {
    "id": "u10-altruism-apply-01",
    "prompt": "A member who has described himself for weeks as 'a burden to everyone' spends a session gently helping a newer member feel less alone, and afterward seems visibly lighter. Name the therapeutic factor at work and why a group can supply it that individual therapy cannot.",
    "answer": "ALTRUISM — being genuinely useful to another person. It counters the 'I only take, I have nothing to give' self-image that fuels his depression. Individual therapy structurally casts the client as a permanent RECIPIENT of help; a group lets him be a GIVER, and helping others is one of the most reliable routes out of self-absorption. The lift is the point: he discovered he has something to offer.",
    "type": "vignette",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "altruism",
    "cluster": "yalom-factors",
    "bloom_level": "apply"
  },
  {
    "id": "u10-social-microcosm-explain-01",
    "prompt": "Explain Yalom's concept of the 'social microcosm' and why it is the engine of interpersonal learning.",
    "answer": "Given enough time and freedom, each member unconsciously recreates their CHARACTERISTIC interpersonal world inside the group — the chronically-rejected person behaves in ways that get them overlooked; the caretaker exhausts themselves tending everyone; the one braced for rejection subtly provokes it. So the group becomes a live, low-stakes REPLICA of the member's outside relationships. That's what makes interpersonal learning possible: unlike the outside world, the group can be helped to tell the member what it's actually like to be on the receiving end of them — honest feedback that becomes a corrective emotional experience.",
    "type": "explain",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "social-microcosm",
    "cluster": "yalom-factors",
    "bloom_level": "understand"
  },
  {
    "id": "u10-interpersonal-learning-analyze-01",
    "prompt": "Why does Yalom argue that interpersonal learning is the therapeutic factor that most clearly 'cannot be replicated in individual therapy'?",
    "answer": "Because its ingredients require OTHER PEERS. In a dyad, the only other person is a paid professional being deliberately careful and accepting with you — so you can't get honest, spontaneous feedback from a range of equals, and your habitual patterns don't fully play out against real relational stakes. A group supplies a whole social microcosm: multiple people who will react to you authentically, enact and receive your patterns, and (with the leader's help) reflect back what it's like to relate to you. That multi-person feedback loop, and the corrective emotional experience it produces, is the thing a one-on-one room can't manufacture.",
    "type": "explain",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "interpersonal-learning",
    "cluster": "yalom-factors",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-cohesion-alliance-explain-01",
    "prompt": "Group cohesiveness is described as 'the group therapy analog of the therapeutic alliance.' Explain what that means and why Yalom treats cohesion as a precondition rather than just one factor among eleven.",
    "answer": "Cohesion is the members' sense of belonging, acceptance, and being valued BY the group — StatPearls calls it 'a client-client equivalent to the client-therapist therapeutic alliance' (Unit 1's Bordin bond, at the group level). Yalom treats it as a PRECONDITION because members will only take the risks the other factors require — self-disclosure, honest feedback, catharsis — inside a group they feel held by. So cohesion isn't parallel to the others; it's the ground they stand on. This is the direct import of Unit 1: the relationship (here a web of relationships) comes first, and the work runs on it.",
    "type": "explain",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "cohesion-as-alliance",
    "cluster": "yalom-factors",
    "bloom_level": "understand"
  },
  {
    "id": "u10-cohesion-vs-il-compare-01",
    "prompt": "Contrast the two therapeutic factors Yalom weighted most heavily — group cohesiveness and interpersonal learning — by the distinct job each does.",
    "answer": "COHESIVENESS is the CONDITION: the bond, belonging, and acceptance that make the group safe enough to work — the precondition for every other factor and the group analog of the individual alliance. INTERPERSONAL LEARNING is the WORK that the condition makes possible: members enact their patterns in the social microcosm, receive honest feedback about how they come across, and have a corrective emotional experience. Roughly: cohesion is the container, interpersonal learning is what happens inside it. You need cohesion first (nobody risks feedback in an unsafe group), but cohesion without the interpersonal work is just a pleasant support group, not change.",
    "type": "compare",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "cohesion-vs-interpersonal-learning",
    "cluster": "yalom-factors",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-catharsis-evaluate-01",
    "prompt": "A trainee believes group therapy works mainly by getting members to 'let it all out' — that catharsis is the active ingredient. Evaluate this against Yalom's account.",
    "answer": "It's a half-truth that misfires in practice. Catharsis (open expression of strong affect) IS one of the eleven factors, but Yalom is clear it heals only when PAIRED with cohesiveness and then UNDERSTOOD — the here-and-now processing that follows the feeling. Raw ventilation in a group that isn't yet bonded does little and can even re-traumatize a member (or the group). So the trainee has isolated a real factor and stripped it of the two things that make it therapeutic: a cohesive container and subsequent meaning-making. Emotion plus a bonded group that helps make sense of it heals; emotion alone doesn't.",
    "type": "explain",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "catharsis-needs-cohesion",
    "cluster": "yalom-factors",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-which-factor-mcq-01",
    "prompt": "A group member in her first month says, 'Watching Devon — he was where I am a year ago and now he's actually doing okay — that's the first time I've believed I might get better.' Which therapeutic factor is most directly at work?",
    "options": [
      "Instillation of hope",
      "Altruism",
      "Universality",
      "Imparting information"
    ],
    "correct": "Instillation of hope",
    "answer": "This is INSTILLATION OF HOPE — seeing others, especially those further along, improve, which makes her own recovery feel possible. (It's why some programs deliberately mix newer and more-recovered members.) Universality is 'I'm not the only one'; altruism is being useful to others; imparting information is advice/psychoeducation — none of which is what's driving her here.",
    "type": "mcq",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "which-factor-hope",
    "cluster": "yalom-factors",
    "bloom_level": "apply"
  },
  {
    "id": "u10-which-factor-mcq-02",
    "prompt": "Over several sessions, other members tell a man that his habit of interrupting with advice leaves them feeling unseen — and he realizes, with a jolt, that his wife and coworkers have hinted at the same thing for years. Which therapeutic factor does this best illustrate?",
    "options": [
      "Interpersonal learning (via the social microcosm)",
      "Catharsis",
      "Imitative behavior",
      "Instillation of hope"
    ],
    "correct": "Interpersonal learning (via the social microcosm)",
    "answer": "This is INTERPERSONAL LEARNING through the social microcosm: he enacted his habitual pattern in the group, the group gave him honest feedback about how it lands, and it connected to his outside relationships — a corrective emotional experience no dyad could supply. Catharsis is affect release; imitative behavior is learning by watching others; instillation of hope is seeing others improve. The tell is feedback-about-a-pattern that generalizes to his life.",
    "type": "mcq",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "which-factor-il",
    "cluster": "yalom-factors",
    "bloom_level": "apply"
  },
  {
    "id": "u10-member-clinician-rankings-evaluate-01",
    "prompt": "Research repeatedly finds that group members and their therapists rank the therapeutic factors DIFFERENTLY. What is the pattern, and what does it teach?",
    "answer": "Members tend to rank interpersonal INPUT (honest feedback), catharsis, cohesiveness, and self-understanding at the top — and rate the leader's clever INTERPRETATIONS lower than the leader would like; universality and existential factors also rank higher for members than clinicians expect. The lesson mirrors Unit 1's common-factors finding: what clients actually experience as helpful (feeling understood, belonging, honest feedback among peers, facing real existential concerns) outweighs the technical moves the counselor is most proud of. It's a humility check on over-valuing your own interpretations.",
    "type": "explain",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "member-vs-clinician-rankings",
    "cluster": "yalom-factors",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-factors-contested-evaluate-01",
    "prompt": "Yalom's eleven factors are sometimes taught as if they were a validated, measured mechanism of group change. Evaluate how much confidence that framing deserves.",
    "answer": "Hold them as a clinical LENS, not a measured mechanism. The eleven are a clinically derived taxonomy — enormously useful for SEEING what's happening in a group — but they overlap, they weren't derived by factor analysis, and their relative importance shifts by group type, population, and stage (which is also why different lists count 11–14 factors). Even cohesion, called 'the core mechanism of action,' has thinner efficacy evidence than its billing implies — the firmer empirical support attaches to interpersonal feedback and the alliance. So: excellent vocabulary for what's going on, weak as a claim about proven quantities.",
    "type": "explain",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "factors-contested",
    "cluster": "yalom-factors",
    "bloom_level": "evaluate"
  }
]
```

## Stages of group development (cluster: group-stages)

```json
[
  {
    "id": "u10-tuckman-recall-01",
    "prompt": "Name Tuckman's five stages of group development in order, and note which was added in the 1977 revision.",
    "answer": "Forming → Storming → Norming → Performing (Tuckman, 1965), plus ADJOURNING (added by Tuckman & Jensen, 1977). Forming = orientation/anxiety/dependence; Storming = conflict and challenges to authority; Norming = cohesion and shared norms; Performing = productive working; Adjourning = termination and mourning.",
    "type": "recall",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "tuckman-stages",
    "cluster": "group-stages",
    "bloom_level": "remember"
  },
  {
    "id": "u10-pregroup-cloze-01",
    "prompt": "Corey adds a stage before the group even meets — the {{pre-group}} stage — where screening, selection, preparation, and informed consent happen; Yalom's research shows this stage strongly predicts who stays and who drops out.",
    "answer": "pre-group (formation). Often skipped by beginners, but the group's fate is partly decided before it convenes — prepared, well-screened members drop out less and engage sooner.",
    "type": "cloze",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "pre-group-stage",
    "cluster": "group-stages",
    "bloom_level": "remember"
  },
  {
    "id": "u10-corey-transition-explain-01",
    "prompt": "Describe Corey's 'transition' stage and what the leader's core task is during it.",
    "answer": "Transition is the counseling name for Tuckman's STORMING: anxiety, defensiveness, resistance, and the struggle for control surface, and members may challenge the leader or each other. The leader's core task is to help the group work THROUGH the conflict, not around it — to contain and make the tension examinable, modeling that the group can survive disagreement. Mishandled (suppressed or fled), the stage stalls the group; handled well, it produces the real trust the working stage runs on.",
    "type": "explain",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "transition-stage",
    "cluster": "group-stages",
    "bloom_level": "understand"
  },
  {
    "id": "u10-storming-normal-evaluate-01",
    "prompt": "In week three, a previously polite group erupts into open disagreement and two members question whether the leader knows what she's doing. A new co-leader whispers, 'This group is falling apart.' Evaluate that reading.",
    "answer": "It's almost certainly wrong — and acting on it would do harm. Conflict and challenges to the leader's authority in week three are the STORMING / transition stage, which is developmentally ON SCHEDULE, not a sign of failure. The costly beginner error the stage model prevents is exactly this: reading normal transition-stage conflict as breakdown and reflexively suppressing it, which robs the group of the trust that only comes from surviving conflict together. The move is to tolerate and contain the conflict, make it examinable, and let the group work through it — not to smooth it over or rescue the group from its own tension.",
    "type": "explain",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "storming-is-normal",
    "cluster": "group-stages",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-tuckman-corey-compare-01",
    "prompt": "Map Tuckman's stages onto Corey's counseling stages, and note the one thing Corey adds that Tuckman doesn't.",
    "answer": "Tuckman Forming ≈ Corey Initial (orientation, trust, norms); Tuckman Storming ≈ Corey Transition (anxiety, conflict, struggle for control); Tuckman Norming + Performing ≈ Corey Working (cohesion consolidates, then real risk-taking and feedback); Tuckman Adjourning ≈ Corey Final (consolidation, termination, transfer of learning). The thing Corey adds up front is the PRE-GROUP stage — screening, selection, preparation, and consent BEFORE the group convenes — which Tuckman's generic model doesn't include but which is decisive for a therapy group.",
    "type": "compare",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "tuckman-vs-corey",
    "cluster": "group-stages",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-which-stage-mcq-01",
    "prompt": "A group has been meeting for two months. Members take real risks, give each other honest feedback that lands as supportive rather than attacking, and hold one another accountable. Which stage is this?",
    "options": [
      "Working (Corey) / Performing (Tuckman)",
      "Initial (Corey) / Forming (Tuckman)",
      "Transition (Corey) / Storming (Tuckman)",
      "Final (Corey) / Adjourning (Tuckman)"
    ],
    "correct": "Working (Corey) / Performing (Tuckman)",
    "answer": "High trust, real risk-taking, and supportive-but-honest accountability are the hallmarks of the WORKING / performing stage, where the therapeutic factors do their heaviest lifting. Initial/forming is tentative and polite; transition/storming is conflictual; final/adjourning is about closure and transfer.",
    "type": "mcq",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "which-stage-working",
    "cluster": "group-stages",
    "bloom_level": "apply"
  },
  {
    "id": "u10-leader-by-stage-analyze-01",
    "prompt": "Explain how the leader's level of structure and involvement should change from the initial stage to the working stage, and why.",
    "answer": "EARLY (initial/forming), the leader supplies high structure and executive function — setting norms, protecting members, reducing anxiety, modeling inclusion — because the group can't yet self-regulate. As the group matures into the WORKING stage, the leader deliberately STEPS BACK and lets members do the therapeutic work on one another. The reason is the unit's core stance: an over-involved leader in a mature group STARVES it, killing universality, altruism, and interpersonal learning by hogging the helping role. So leadership is a dial turned down over time — decentering as the group can carry its own process.",
    "type": "explain",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "leader-by-stage",
    "cluster": "group-stages",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-stages-recycle-evaluate-01",
    "prompt": "A leader treats the stage model as a fixed timetable and is alarmed when her 'working' group suddenly returns to conflict after a new member joins. Evaluate her use of the model.",
    "answer": "She's over-applying a heuristic. Stages are a lens for READING a group, not a one-way timetable to grade it against. Real groups RECYCLE — a new member, a crisis, or a rupture can throw a working group back into storming/transition, and open-ended groups never sit still in one stage at all. A group re-storming after a new member is normal and expectable, not a regression to be alarmed by; the move is to help the reconfigured group re-establish safety and norms, not to conclude something has gone wrong. (Tuckman's evidence was also mostly non-clinical, another reason to hold it loosely.)",
    "type": "explain",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "stages-recycle",
    "cluster": "group-stages",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-final-stage-apply-01",
    "prompt": "A time-limited group has two sessions left. A member says, 'Let's not make it weird — we can just keep going as normal until it's over.' Why should the leader resist this, and what is the final stage's therapeutic task?",
    "answer": "Because 'just keep going as normal' skips the FINAL stage and wastes the ending's therapeutic potential. The task of the final/adjourning stage is consolidation and closure: reviewing progress, saying what still needs saying between members, grieving the group's ending, and — crucially — planning how to TRANSFER the learning to life outside the group. Endings also re-evoke members' other losses and attachment patterns, making them rich material. The leader should surface the ending, not collude in avoiding it.",
    "type": "vignette",
    "source_page": "wiki/concept-group-development-stages.md",
    "topic": "final-stage",
    "cluster": "group-stages",
    "bloom_level": "apply"
  }
]
```

## Group leadership (cluster: leadership-functions)

```json
[
  {
    "id": "u10-four-functions-recall-01",
    "prompt": "Name the four basic leadership functions from Lieberman, Yalom & Miles (1973), with a one-line gloss of each.",
    "answer": "(1) Emotional stimulation — challenging, confronting, self-disclosing, drawing out feeling (the leader as activator). (2) Caring — support, warmth, acceptance, protection (the holder). (3) Meaning-attribution — explaining, clarifying, interpreting, giving cognitive frameworks (the translator). (4) Executive function — setting limits, rules, norms, goals; managing time and structure (the manager).",
    "type": "recall",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "four-functions",
    "cluster": "leadership-functions",
    "bloom_level": "remember"
  },
  {
    "id": "u10-linear-curvilinear-compare-01",
    "prompt": "The key finding of Lieberman, Yalom & Miles is not the four functions but the SHAPE of each function's relationship to outcome. Contrast the two functions that are 'linear' with the two that are 'curvilinear,' and give the best-supported leader profile.",
    "answer": "CARING and MEANING-ATTRIBUTION have a LINEAR relationship with outcome — more is better; you essentially can't over-supply warmth or over-supply sense-making. EMOTIONAL STIMULATION and EXECUTIVE FUNCTION have a CURVILINEAR (inverted-U) relationship — a MODERATE amount is best, and too much OR too little produces worse outcomes (too little stimulation = flat/inert; too much = flooded; too little executive = chaotic/unsafe; too much = a traffic cop running dyads). Best-supported profile: MODERATE emotional stimulation, MODERATE executive function, HIGH caring, HIGH meaning-attribution.",
    "type": "compare",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "linear-vs-curvilinear",
    "cluster": "leadership-functions",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-best-leader-profile-mcq-01",
    "prompt": "Based on the Lieberman, Yalom & Miles findings, which leader is likely to produce the best member outcomes?",
    "options": [
      "Moderate stimulation and executive control, high warmth, high meaning-making",
      "High stimulation and confrontation, low warmth, charismatic and dominating",
      "Very low stimulation and very hands-off structure, high warmth",
      "Maximum executive control and structure at every stage"
    ],
    "correct": "Moderate stimulation and executive control, high warmth, high meaning-making",
    "answer": "The best-supported profile is MODERATE emotional stimulation and executive function (both curvilinear — moderate beats extreme) plus HIGH caring and HIGH meaning-attribution (both linear — more is better). Option 2 is the 'aggressive stimulator' who produced the most CASUALTIES; option 3 is under-stimulating and rudderless; option 4 over-does the curvilinear executive function and suffocates the group's own process.",
    "type": "mcq",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "best-leader-profile",
    "cluster": "leadership-functions",
    "bloom_level": "apply"
  },
  {
    "id": "u10-aggressive-stimulator-evaluate-01",
    "prompt": "The Lieberman, Yalom & Miles study is often cited as the field's key evidence that group leadership can HARM. What did it find, and what practical lesson follows?",
    "answer": "The study found real CASUALTIES — members who left worse off — and the damage clustered under one leader profile: the 'aggressive stimulator,' high in emotional stimulation, intrusive, charismatic-authoritarian, and low in caring. The practical lesson is a direct argument for humility and warmth over charisma: a leader whose personality dominates the group and who confronts hard while caring little is not merely ineffective but dangerous. It's the empirical backbone of the unit's stance warning and of the ethical duties to SCREEN members and PROTECT them, and to keep stimulation moderate rather than maximal.",
    "type": "explain",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "casualties-aggressive-stimulator",
    "cluster": "leadership-functions",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-here-and-now-explain-01",
    "prompt": "Explain the 'here-and-now' as the leader's central technical focus, including its two tiers.",
    "answer": "The here-and-now is the group's immediate, present-moment interactions — as opposed to the 'there-and-then' of members' outside lives. It has TWO tiers, both required: (1) ACTIVATION — steering attention into the present, e.g., looking for the live echo in the room of an outside story ('you said your wife dismisses you — did you feel dismissed by the group just now?'); and (2) PROCESS ILLUMINATION / the self-reflective loop — after the group EXPERIENCES an interaction, helping it REFLECT on the interaction itself ('every time Maria opens up, someone rushes to fix it — what's that about in here?'). Experience without reflection is just events; reflection without experience is dry intellectualizing. The loop is the engine.",
    "type": "explain",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "here-and-now",
    "cluster": "leadership-functions",
    "bloom_level": "understand"
  },
  {
    "id": "u10-process-vs-content-compare-01",
    "prompt": "Distinguish 'content' from 'process' in a group, and explain why Yalom says the leader's leverage is in the process.",
    "answer": "CONTENT is the topic — what the members are literally talking about (a job, a spouse, last week's argument). PROCESS is the relationship-level meaning of HOW they're talking about it — what the interaction reveals about how members relate to each other and to the leader right now. Yalom locates the leverage in process because the group's unique power is the social microcosm: members enact their interpersonal patterns live, and it's by commenting on the process ('I notice you agree with everyone and then go quiet') — not by solving the content — that those patterns become examinable and changeable. Content is the cover story; process is the data.",
    "type": "compare",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "process-vs-content",
    "cluster": "leadership-functions",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-process-illumination-vignette-01",
    "prompt": "A member spends ten minutes describing a fight with his brother (there-and-then). Give a here-and-now / process move the leader could make, and say what it accomplishes.",
    "answer": "Look for the live echo in the room: 'You felt your brother talked over you and didn't take you seriously — I'm wondering if anything like that happens for you in here, with us.' Or, if it's visible: 'I notice as you tell this, you keep checking my face — what are you watching for?' It accomplishes the shift from an unverifiable outside story into examinable present-moment DATA about how the member relates, which the group can then reflect on (the social microcosm made usable). Staying only with the brother story keeps the work in the there-and-then, where the group can't do its distinctive work.",
    "type": "vignette",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "activating-here-and-now",
    "cluster": "leadership-functions",
    "bloom_level": "apply"
  },
  {
    "id": "u10-styles-mcq-01",
    "prompt": "A leader adopts a fully hands-off, minimally directive (laissez-faire) style from the very first session of a brand-new, anxious group. What's the most likely problem?",
    "options": [
      "In an early/anxious group, a laissez-faire absence leaves members feeling unsafe and rudderless",
      "Laissez-faire is the ideal style for every stage, so there is no problem",
      "It provides too much structure and fosters dependence",
      "It is identical to a democratic style and equally effective"
    ],
    "correct": "In an early/anxious group, a laissez-faire absence leaves members feeling unsafe and rudderless",
    "answer": "Style should FLEX with the stage: an early group needs more structure (executive function) because it can't yet self-direct. A laissez-faire, hands-off leader in that moment reads as absence and leaves anxious members without safety or direction. Laissez-faire can free a MATURE working group, but it misfits an initial one. (Autocratic fosters dependence; democratic is generally the default aim — laissez-faire is not identical to it.)",
    "type": "mcq",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "leadership-styles",
    "cluster": "leadership-functions",
    "bloom_level": "apply"
  },
  {
    "id": "u10-decenter-stance-evaluate-01",
    "prompt": "A skilled individual therapist moves to co-leading a group and finds himself responding thoughtfully to every member's disclosure, one after another. His supervisor calls this a problem, not a strength. Evaluate.",
    "answer": "The supervisor is right. Responding personally to every disclosure is the INDIVIDUAL-THERAPY reflex, and in a group it's counterproductive: it turns the session into serial one-on-one therapy with an audience and STARVES the members of the chance to help each other — killing universality, altruism, and interpersonal learning in one move. The high-skill move is to DECENTER — to turn the work back to the group ('does anyone else recognize that feeling?') rather than being the one who helps. Over-functioning as a leader isn't generosity; it's theft of the group's own therapeutic power. His individual-therapy strength is exactly what he has to unlearn here.",
    "type": "explain",
    "source_page": "wiki/concept-group-leadership.md",
    "topic": "decenter-stance",
    "cluster": "leadership-functions",
    "bloom_level": "evaluate"
  }
]
```

## Types of group work — ASGW (cluster: group-types)

```json
[
  {
    "id": "u10-asgw-four-types-recall-01",
    "prompt": "Name the ASGW's four types of group work and the primary aim of each.",
    "answer": "(1) TASK/WORK groups — accomplish a work goal external to the members (committees, teams). (2) PSYCHOEDUCATIONAL (guidance) groups — prevent and educate; teach information/skills to relatively well-functioning members (e.g., a stress-management class). (3) COUNSELING groups — interpersonal problem-solving and growth around conscious 'problems of living'; NOT aimed at major personality change. (4) PSYCHOTHERAPY groups — remediation and reconstruction of deeper, more severe/enduring dysfunction, including personality change. They're distinguished mainly by FOCUS and DEPTH of aim.",
    "type": "recall",
    "source_page": "wiki/concept-group-types.md",
    "topic": "asgw-four-types",
    "cluster": "group-types",
    "bloom_level": "remember"
  },
  {
    "id": "u10-task-group-cloze-01",
    "prompt": "In the ASGW taxonomy, the group type whose focus is accomplishing a work goal {{external}} to the members — committees, task forces, teams — is the task/work group.",
    "answer": "external. A skilled task-group leader still attends to dynamics (a committee can tear itself apart on process), but the POINT is the product, not the members' personal growth.",
    "type": "cloze",
    "source_page": "wiki/concept-group-types.md",
    "topic": "task-group",
    "cluster": "group-types",
    "bloom_level": "remember"
  },
  {
    "id": "u10-counseling-vs-psychotherapy-compare-01",
    "prompt": "Counseling groups and psychotherapy groups share a lot of method. Contrast them on aim, depth, membership, and whether personality change is a goal.",
    "answer": "AIM: counseling = growth, prevention, interpersonal problem-solving; psychotherapy = remediation and reconstruction. DEPTH: counseling deals with CONSCIOUS, situational 'problems of living'; psychotherapy works with deeper, more ENDURING dysfunction and may engage the unconscious/developmental history. MEMBERS: counseling = relatively well-functioning people with developmental concerns; psychotherapy = more severe/entrenched problems. PERSONALITY CHANGE: NOT a goal in counseling groups; CAN be a goal in psychotherapy groups. In practice they sit on a continuum of depth rather than in sealed boxes — which is exactly why the distinction matters for competence/scope: the deeper the aim, the more training and careful screening it requires.",
    "type": "compare",
    "source_page": "wiki/concept-group-types.md",
    "topic": "counseling-vs-psychotherapy-group",
    "cluster": "group-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-which-type-mcq-01",
    "prompt": "A community agency runs an eight-week, curriculum-based group that teaches coping skills and information to parents newly navigating a child's ADHD diagnosis. The members are functioning well and want knowledge and skills. Which ASGW type is this?",
    "options": [
      "Psychoeducational (guidance) group",
      "Psychotherapy group",
      "Task/work group",
      "Counseling group"
    ],
    "correct": "Psychoeducational (guidance) group",
    "answer": "Curriculum-based, skill/information teaching, prevention-oriented, for relatively well-functioning members around a specific life role = a PSYCHOEDUCATIONAL (guidance) group, with the leader as teacher/facilitator. It's not a task group (no external work product), not a counseling group (the focus is education/skills, not here-and-now interpersonal problem-solving), and not psychotherapy (no reconstruction of deep dysfunction).",
    "type": "mcq",
    "source_page": "wiki/concept-group-types.md",
    "topic": "which-type-psychoeducational",
    "cluster": "group-types",
    "bloom_level": "apply"
  },
  {
    "id": "u10-psychoeducational-apply-01",
    "prompt": "Why does a psychoeducational group borrow so heavily from Unit 9's structured methods (e.g., a DBT skills group), and how does its leader's role differ from a psychotherapy-group leader's?",
    "answer": "Because psychoeducational groups are about teaching information and building specific skills for relatively well-functioning members — which maps directly onto structured, curriculum-based interventions like DBT skills training, social-skills training, or stress-management protocols. The leader functions more as a TEACHER/facilitator delivering content, with the group as a supportive learning context. A psychotherapy-group leader, by contrast, is a PROCESS facilitator — working the here-and-now, cohesion, and interpersonal learning to remediate deeper dysfunction, with far less reliance on curriculum.",
    "type": "explain",
    "source_page": "wiki/concept-group-types.md",
    "topic": "psychoeducational-role",
    "cluster": "group-types",
    "bloom_level": "apply"
  },
  {
    "id": "u10-type-drives-screening-analyze-01",
    "prompt": "Explain why the group TYPE you choose drives how intensively you must screen members and how you lead.",
    "answer": "Because screening intensity and leadership style scale with the DEPTH of the group's aim. A psychoeducational stress-management class needs only light screening and a teaching stance — members are well-functioning and the risk of harm is low. A reconstructive psychotherapy group needs careful, clinical selection (so members won't be harmed or won't derail the group) and a process-facilitation stance working the here-and-now. The deeper and more emotionally intense the work, the more a wrong-fit member can be hurt or can hurt the group — so type isn't just a label; it sets the screening, the leadership, and even what counts as a 'difficult member.'",
    "type": "explain",
    "source_page": "wiki/concept-group-types.md",
    "topic": "type-drives-screening",
    "cluster": "group-types",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-scope-type-mcq-01",
    "prompt": "A newly licensed counselor trained only in running psychoeducational skills groups decides to start an open-ended reconstructive psychotherapy group for clients with severe personality disorders. What's the primary problem?",
    "options": [
      "Competence / scope of practice — reconstructive group psychotherapy requires training she doesn't have",
      "Nothing — all group work uses the same skills, so any group leader can run any type",
      "Psychotherapy groups don't require screening, so it's simpler than a skills group",
      "Personality disorders can't be treated in groups at all"
    ],
    "correct": "Competence / scope of practice — reconstructive group psychotherapy requires training she doesn't have",
    "answer": "This is a COMPETENCE / scope-of-practice problem (Unit 3): the depth of a reconstructive psychotherapy group — often engaging unconscious/developmental material with severely impaired members — requires training and supervision a psychoeducational-group leader may not have. The deeper the aim, the more careful the screening AND the more advanced the competence required; running a group type you aren't trained for risks harming members. (Personality disorders CAN be treated in groups — DBT groups are a prime example — but by adequately trained leaders.)",
    "type": "mcq",
    "source_page": "wiki/concept-group-types.md",
    "topic": "type-scope-of-practice",
    "cluster": "group-types",
    "bloom_level": "apply"
  }
]
```

## Managing difficult group members (cluster: difficult-members)

```json
[
  {
    "id": "u10-prototypes-recall-01",
    "prompt": "Name several of Yalom's 'problem group member' prototypes and the single reframe that governs how a skilled leader handles all of them.",
    "answer": "Prototypes: the monopolist, the silent member, the boring patient, the help-rejecting complainer ('yes, but'), the scapegoat/group deviant, and characterologically difficult members (borderline, narcissistic, schizoid). The governing reframe: a 'difficult' member is NOT a nuisance to manage out of the way — their difficult behavior IS the work. It's usually a live re-enactment of the very interpersonal pattern that hurts them outside (the social microcosm), so the group is the one place it can be seen, named, and revised.",
    "type": "recall",
    "source_page": "wiki/concept-difficult-group-members.md",
    "topic": "problem-member-prototypes",
    "cluster": "difficult-members",
    "bloom_level": "remember"
  },
  {
    "id": "u10-monopolist-apply-01",
    "prompt": "A member talks compulsively, fills every silence, and gives everyone advice; other members are visibly disengaging. Describe the therapeutic move — and why simply cutting him off is not it.",
    "answer": "Simply cutting him off shames the monopolist and teaches the group the leader will police airtime (so members stop self-regulating). The therapeutic move works on TWO levels at once: (1) help the GROUP look at why it has allowed one person to carry all the talking ('I'm curious what it's like for the rest of you to be so quiet while Tom does all the work') — surfacing the group's collusion; and (2) help the MONOPOLIST examine what the compulsive talking protects him from (usually anxiety — silence feels dangerous). Both the behavior and the group's response to it become examinable here-and-now material, rather than a nuisance to suppress.",
    "type": "vignette",
    "source_page": "wiki/concept-difficult-group-members.md",
    "topic": "monopolist",
    "cluster": "difficult-members",
    "bloom_level": "apply"
  },
  {
    "id": "u10-silent-member-apply-01",
    "prompt": "A member has said almost nothing across four sessions. A co-leader wants to put her on the spot next week to 'make her participate.' What's the better approach and why?",
    "answer": "Understand BEFORE you push. Silence has many possible meanings — fear of self-disclosure, feeling one's contributions don't matter, cultural norms about speaking in a group, shame, or a trauma history — and pressuring a silent member to perform usually deepens the withdrawal. The better move is gentle invitation and here-and-now curiosity ('I notice you take a lot in — I'd be interested in what stirs for you when others share') WITHOUT coercion, aiming to make participation safe rather than mandatory. It also matters because silent members tend to gain little, so re-engaging her serves her — but on her terms, not by force.",
    "type": "vignette",
    "source_page": "wiki/concept-difficult-group-members.md",
    "topic": "silent-member",
    "cluster": "difficult-members",
    "bloom_level": "apply"
  },
  {
    "id": "u10-help-rejecting-complainer-analyze-01",
    "prompt": "A member repeatedly presents problems, asks the group for help, and rejects every suggestion with 'yes, but that won't work because…' The group is getting frustrated and starting to withdraw. Name the prototype and explain why this is the unit's purest case for 'resist the urge to fix.'",
    "answer": "This is the HELP-REJECTING COMPLAINER ('yes, but' member). It's the purest 'resist the urge to fix' case because the whole pattern is baited to PULL the fix reflex out of the group: the member simultaneously demands and defeats help, and every new suggestion just feeds the doomed cycle and deepens everyone's frustration. The way out is to DECLINE the bait — stop the content-level rescue attempts and shift to PROCESS, gently naming the dynamic itself ('I notice we keep offering ideas and they keep not fitting — I wonder if what happens in here happens in your life too'). The pattern is the material; the enacted relationship (needing yet defeating help) is what surely operates outside the group and what the group can actually make examinable.",
    "type": "explain",
    "source_page": "wiki/concept-difficult-group-members.md",
    "topic": "help-rejecting-complainer",
    "cluster": "difficult-members",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-which-member-mcq-01",
    "prompt": "Which vignette best illustrates a help-rejecting complainer rather than a monopolist?",
    "options": [
      "A member keeps raising problems and asking for help, then rejects each suggestion with a reason it can't work",
      "A member talks nonstop, fills every silence, and steers every topic back to himself",
      "A member says almost nothing and avoids eye contact for several sessions",
      "A member becomes the target the group blames whenever it feels stuck"
    ],
    "correct": "A member keeps raising problems and asking for help, then rejects each suggestion with a reason it can't work",
    "answer": "The defining signature of the help-rejecting complainer is the SOLICIT-then-REJECT cycle ('yes, but'): demanding help and defeating it. Option 2 is the monopolist (compulsive talking/dominating airtime); option 3 is the silent member; option 4 is the scapegoat/group deviant. The discrimination is the pattern, not the volume of talk.",
    "type": "mcq",
    "source_page": "wiki/concept-difficult-group-members.md",
    "topic": "which-difficult-member",
    "cluster": "difficult-members",
    "bloom_level": "apply"
  },
  {
    "id": "u10-monopolist-vs-silent-compare-01",
    "prompt": "The monopolist and the silent member look like opposites. Contrast them, then state the single principle that governs the leader's response to both.",
    "answer": "They're opposite POLES of participation: the monopolist over-participates (compulsive talking, dominating airtime, often to manage anxiety), draining the group's energy and disengaging others; the silent member under-participates (withdrawn, minimally engaged), gains little, and risks being over-protected or scapegoated. But the SAME principle governs both: work the PROCESS, not just the behavior, and USE the group rather than handling it as a private transaction — make the participation pattern (and the group's response to it) examinable here-and-now material, with curiosity about what the pattern protects or expresses, rather than simply policing the airtime up or down.",
    "type": "compare",
    "source_page": "wiki/concept-difficult-group-members.md",
    "topic": "monopolist-vs-silent",
    "cluster": "difficult-members",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-difficult-opportunity-evaluate-01",
    "prompt": "Evaluate the claim: 'The goal with a difficult group member is to manage their behavior so it stops disrupting the group and the real work can proceed.'",
    "answer": "It has the priority backwards. Managing the behavior out of the way to 'get to the real work' protects the group's COMFORT at the cost of its therapeutic POWER — because the difficult behavior IS the real work. In the social microcosm, the member is enacting, live, the very interpersonal pattern that causes them trouble outside the group, which makes the group the one place that pattern can be seen, named, and revised. So the difficult member is an OPPORTUNITY, not an obstacle. (The genuine limit: making a pattern examinable never licenses letting a member be attacked or humiliated — the leader's protective duty is the floor beneath all of it.)",
    "type": "explain",
    "source_page": "wiki/concept-difficult-group-members.md",
    "topic": "difficult-is-opportunity",
    "cluster": "difficult-members",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-difficult-is-leadership-signal-evaluate-01",
    "prompt": "A leader complains that his group is full of 'resistant,' silent members. Before labeling the members, what two things should he consider?",
    "answer": "First, that a whole group of 'resistant'/silent members is often a signal about LEADERSHIP, not the members — an over-controlling or over-stimulating leader can manufacture the very difficulty they then complain about (the same 'discord, not resistance' reframe as MI in Unit 9: check your own contribution first). Second, a CULTURE check: norms about self-disclosure, deference, and speaking up in a group vary widely, so members read as 'silent' or 'resistant' may be behaving exactly as their cultural context prescribes (Unit 4 cultural humility). Both caution against reifying a prototype — 'resistant' is a role partly created by the group and the leader, not a fixed trait carried in by the member.",
    "type": "explain",
    "source_page": "wiki/concept-difficult-group-members.md",
    "topic": "difficult-as-leadership-signal",
    "cluster": "difficult-members",
    "bloom_level": "evaluate"
  }
]
```

## Group ethics & formation (cluster: group-formation)

```json
[
  {
    "id": "u10-group-confidentiality-cloze-01",
    "prompt": "ACA Code B.4.a, on group work: 'In group work, counselors clearly explain the importance and {{parameters}} of confidentiality for the specific group being entered.'",
    "answer": "parameters. The counselor's duty is to EXPLAIN confidentiality's importance and set it as an explicit group norm — describing its parameters and the consequences of breaching it — because they can only promise their OWN confidentiality, not the other members'.",
    "type": "cloze",
    "source_page": "wiki/concept-group-ethics-and-formation.md",
    "topic": "aca-b4a-confidentiality",
    "cluster": "group-formation",
    "bloom_level": "remember"
  },
  {
    "id": "u10-privilege-cloze-01",
    "prompt": "A legal wrinkle unique to groups: privilege — the protection that can keep therapy communications out of court — generally does {{not}} apply to group treatment, because the presence of third parties can waive it, unless a specific state statute preserves it.",
    "answer": "not. So members should be told that group disclosures may not carry the legal protection that one-on-one therapy communications do.",
    "type": "cloze",
    "source_page": "wiki/concept-group-ethics-and-formation.md",
    "topic": "group-privilege",
    "cluster": "group-formation",
    "bloom_level": "remember"
  },
  {
    "id": "u10-cant-guarantee-confidentiality-evaluate-01",
    "prompt": "A group leader tells new members, 'Everything said in this room is completely confidential — I guarantee it.' Evaluate this statement.",
    "answer": "It's an ethical overreach and it's false. In a group, the OTHER MEMBERS are not bound by the counselor's ethics code, so the leader CANNOT guarantee they'll keep what they hear private. Per ACA B.4.a, the honest duty is to EXPLAIN confidentiality's importance and parameters, set it as a firm group norm, describe the consequences of breaching it, and often have members agree to it — while being clear the leader promises only their OWN confidentiality, not the members'. Guaranteeing it misleads members into disclosures they might not make if they understood the real limit (and privilege may not even protect group communications legally). Honesty about the limit is itself part of informed consent.",
    "type": "explain",
    "source_page": "wiki/concept-group-ethics-and-formation.md",
    "topic": "cannot-guarantee-confidentiality",
    "cluster": "group-formation",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-group-vs-individual-confidentiality-compare-01",
    "prompt": "Contrast confidentiality in individual therapy with confidentiality in group work. What is the key structural difference?",
    "answer": "In INDIVIDUAL therapy the counselor CONTROLS confidentiality (within its legal limits — duty to warn, mandated reporting, etc. from Unit 3): it's the counselor's promise to keep. In a GROUP, the counselor can promise only their own confidentiality, because the OTHER MEMBERS in the room aren't bound by the counselor's ethics code and can't be guaranteed to keep what they hear private. So the structural difference is the presence of third parties: it turns confidentiality from something the counselor can assure into something the counselor can only explain, norm, and request — and it may also strip the LEGAL privilege that protects one-on-one therapy. Group confidentiality is a shared expectation, not a professional guarantee.",
    "type": "compare",
    "source_page": "wiki/concept-group-ethics-and-formation.md",
    "topic": "group-vs-individual-confidentiality",
    "cluster": "group-formation",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-screening-explain-01",
    "prompt": "Both ACA and ASGW require screening prospective group members. What is the standard the counselor is applying, and whom does screening protect?",
    "answer": "The standard: select members whose NEEDS and GOALS are compatible with the group's purpose, who will NOT impede the group process, and whose WELL-BEING will not be jeopardized by the group experience. It's a two-way fit judgment that protects BOTH parties: the candidate (a fragile or acutely-in-crisis person may be harmed by, or unable to use, a particular group) AND the group (a radically mismatched member can derail it, and the wrong mix breeds the 'difficult member' dynamics). Screening intensity scales with the group's depth of aim — light for a psychoeducational class, careful and clinical for a psychotherapy group.",
    "type": "explain",
    "source_page": "wiki/concept-group-ethics-and-formation.md",
    "topic": "screening-standard",
    "cluster": "group-formation",
    "bloom_level": "understand"
  },
  {
    "id": "u10-preparation-apply-01",
    "prompt": "Yalom stresses pre-group preparation. What does it involve, and what is the evidence-based payoff for spending a session on it before the group starts?",
    "answer": "Pre-group preparation means meeting with members before the group starts to demystify the process: explain how group works, set realistic expectations (including that early sessions feel awkward and that conflict is normal), correct misconceptions ('I'll just be talked at' / 'I'll be forced to bare my soul'), and establish norms. The payoff, per Yalom's research: prepared members DROP OUT LESS and engage SOONER. It's why formation counts as the first therapeutic act, not paperwork — a large share of a group's outcome is decided before session one.",
    "type": "explain",
    "source_page": "wiki/concept-group-ethics-and-formation.md",
    "topic": "pre-group-preparation",
    "cluster": "group-formation",
    "bloom_level": "apply"
  },
  {
    "id": "u10-mandated-member-vignette-01",
    "prompt": "A court orders a client into a domestic-violence group; attendance is not optional. Can informed consent still be meaningful, and what must the leader clarify?",
    "answer": "Yes — consent is still meaningful even when ATTENDANCE isn't optional; what's voluntary is what and how much the member discloses and engages. The leader must clarify, up front: what is and isn't required of him, WHAT WILL BE REPORTED to the referring court (and what won't), the limits of confidentiality in this setting, and what genuine CHOICES he still has within the group. Being honest about the mandated frame — rather than pretending it's a fully voluntary therapy relationship — is itself part of ethical consent and, done respectfully, models the same non-coercive stance that lets an involuntary member actually use the group.",
    "type": "vignette",
    "source_page": "wiki/concept-group-ethics-and-formation.md",
    "topic": "mandated-member-consent",
    "cluster": "group-formation",
    "bloom_level": "apply"
  },
  {
    "id": "u10-protective-duty-mcq-01",
    "prompt": "Midway through a session, several members begin piling criticism onto one quiet member who has become the group's scapegoat. What does the leader's ethical duty (ACA A.8) most require here?",
    "options": [
      "Intervene to protect the member from harm, then illuminate what the group is doing",
      "Stay out of it — conflict is part of the storming stage and should never be interrupted",
      "Let the scapegoating continue because catharsis is therapeutic for the group",
      "Immediately remove the scapegoated member from the group to end the conflict"
    ],
    "correct": "Intervene to protect the member from harm, then illuminate what the group is doing",
    "answer": "ACA A.8 charges the counselor to take reasonable precautions to PROTECT members from physical, emotional, or psychological trauma — so the leader must intervene to stop the pile-on, THEN work the process ('what is the group doing by putting everything on one person?'), since scapegoating is a group-level phenomenon that usually says the target is carrying something for the whole group. Protection is the floor; it never licenses letting a member be attacked (not all conflict is therapeutic), and abruptly removing the scapegoat abandons him and leaves the group's dynamic unexamined.",
    "type": "mcq",
    "source_page": "wiki/concept-group-ethics-and-formation.md",
    "topic": "protective-duty-scapegoat",
    "cluster": "group-formation",
    "bloom_level": "apply"
  }
]
```

## Why groups heal differently — the unit's throughline (unclustered)

```json
[
  {
    "id": "u10-why-group-heals-analyze-01",
    "prompt": "The syllabus objective for this unit is to understand why groups heal DIFFERENTLY than individual work — not just additionally or more cheaply. Name the therapeutic factors a dyad structurally cannot supply, and explain the common thread.",
    "answer": "Factors a one-on-one room can't produce: UNIVERSALITY (you can tell a client others struggle too, but only a group lets them WITNESS it), ALTRUISM (being genuinely useful to a peer — a dyad casts the client as a permanent recipient), and INTERPERSONAL LEARNING in a SOCIAL MICROCOSM (habitual patterns enacted against real peers, with honest multi-person feedback — a corrective emotional experience). The common thread: all three require OTHER PEERS, not a paid professional being careful with you. That's what makes group its own modality rather than individual therapy in bulk — the members are agents of change for each other.",
    "type": "explain",
    "source_page": "wiki/unit10-group.md",
    "topic": "why-groups-heal-differently",
    "bloom_level": "analyze"
  },
  {
    "id": "u10-group-vs-individual-efficacy-evaluate-01",
    "prompt": "A clinic director assumes group therapy is 'the budget option — cheaper but not as good as individual.' Evaluate this against the outcome evidence.",
    "answer": "The 'cheaper-but-worse' assumption is wrong on the evidence. Burlingame's meta-analysis of 46 randomized trials found ZERO outcome difference between group and individual therapy across multiple disorders when the treatment, patients, and dose are matched. So group is EQUIVALENT and cheaper — not equivalent-minus. Group also lets one therapist treat several clients at once, works across ages and ethnic groups, and offers benefits (universality, altruism, interpersonal learning) individual therapy can't. If anything the evidence indicts the opposite bias: group is badly UNDERUSED relative to its support — only about a quarter of psychology trainees get group training. The correct read is 'equally effective and more efficient,' not 'a lesser substitute.'",
    "type": "explain",
    "source_page": "wiki/unit10-group.md",
    "topic": "group-vs-individual-efficacy",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-audience-trap-evaluate-01",
    "prompt": "Describe the classic beginner error of 'doing individual therapy in front of an audience,' and explain why it squanders the group modality.",
    "answer": "It's the leader taking turns doing one-on-one work with each member in sequence while everyone else watches — the individual-therapy reflex transplanted into a group. It squanders the modality because it makes the LEADER the sole agent of change and reduces the other members to spectators, which starves the group of its distinctive engines: universality, altruism, and interpersonal learning all require members interacting WITH EACH OTHER, not queuing for the leader's attention. The whole apparatus of the group — the social microcosm, member-to-member feedback, cohesion — goes unused. The corrective is the unit's core stance: decenter yourself and activate the group as the therapist (turn disclosures back to the group rather than answering them all yourself).",
    "type": "explain",
    "source_page": "wiki/unit10-group.md",
    "topic": "individual-in-front-of-audience",
    "bloom_level": "evaluate"
  },
  {
    "id": "u10-cohesion-efficacy-caveat-evaluate-01",
    "prompt": "Cohesion is routinely called 'the core mechanism of action' in group therapy. What is the honest caveat about that claim?",
    "answer": "Its clinical centrality outruns its efficacy evidence. Cohesion is genuinely important — it's the precondition members need to take risks, and it's the group analog of the individual alliance — but the FIRMER empirical support in group outcome research attaches to INTERPERSONAL FEEDBACK and the ALLIANCE more than to cohesion or 'emotional climate' per se. So 'cohesion is everything' is best held as a strong clinical HEURISTIC, not a settled, measured finding. This is the same posture the whole unit takes toward the therapeutic factors: a superb lens for seeing what's happening, weaker as proven mechanism.",
    "type": "explain",
    "source_page": "wiki/theory-yalom-factors.md",
    "topic": "cohesion-efficacy-caveat",
    "bloom_level": "evaluate"
  }
]
```
