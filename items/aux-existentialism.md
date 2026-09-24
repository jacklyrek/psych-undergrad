# Elective module items — Existentialism, In Depth

Source of truth for this **elective/ad-hoc module** (off-spine; `aux-` namespace). Each fenced
`json` block is a JSON array merged by `apps/build_items.py` into `build/items.json`. Items span
Bloom levels and lean toward **application, evidence appraisal, and stance** (the givens as a lens
for listening, not content to teach; what the trials do and don't show), per the generate rules in
[`../CLAUDE.md`](../CLAUDE.md). Clusters: `existential-thinkers`, `existential-givens`,
`existential-schools`, `existential-evidence`, `existential-practice`. Item id prefix: `ax-exi-`.

## Cluster: existential-thinkers

```json
[
  {
    "id": "ax-exi-label-recall-01",
    "prompt": "Of the major figures usually grouped as 'existentialists,' which two explicitly accepted the label? Name one major figure who explicitly rejected it.",
    "answer": "Sartre and Beauvoir were the only ones who explicitly self-identified as existentialists. Camus rejected the label, and so did Heidegger. Kierkegaard and Nietzsche died before the word existed (Marcel coined it in 1943). Existentialism is a retrospective family resemblance, not a school with members.",
    "type": "recall",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "what-existentialism-is",
    "cluster": "existential-thinkers",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-existence-essence-cloze-01",
    "prompt": "Sartre's slogan for the claim that humans have no pre-given nature, and become what they are through their choices: existence {{precedes essence}}.",
    "answer": "precedes essence",
    "type": "cloze",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "existence-precedes-essence",
    "cluster": "existential-thinkers",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-facticity-explain-01",
    "prompt": "Explain the facticity ↔ transcendence tension and why existentialists say bad faith can run in EITHER direction.",
    "answer": "Facticity is what we are already stuck with: body, history, social position, past choices. Transcendence is our capacity to interpret, respond to, and go beyond those facts. Existence is the tension between the two. Bad faith denies one pole: collapsing into facticity ('that's just who I am, I have no choice') denies freedom, and collapsing into transcendence (pretending the past, body, or situation doesn't constrain you) denies facticity. Both are self-deception.",
    "type": "explain",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "facticity-transcendence",
    "cluster": "existential-thinkers",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-kierkegaard-cloze-01",
    "prompt": "Kierkegaard described anxiety as 'the {{dizziness of freedom}}', the feeling of looking down into one's own possibilities.",
    "answer": "dizziness of freedom",
    "type": "cloze",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "kierkegaard-anxiety",
    "cluster": "existential-thinkers",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-kierkegaard-despair-vignette-01",
    "prompt": "Client A has spent eight years 'keeping options open': three half-finished degrees, several near-engagements, endless plans, no commitments. Client B says, 'I'm 50, this is my life, nothing can change now.' Using Kierkegaard's two forms of despair, name each.",
    "answer": "A: despair of POSSIBILITY, lost in imagined options and never committing to actuality. B: despair of NECESSITY, fatalism and loss of possibility. For Kierkegaard both are failures to become a self, which requires holding possibility and necessity together.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "kierkegaard-despair",
    "cluster": "existential-thinkers",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-waiter-apply-01",
    "prompt": "Sartre's café waiter moves a little too precisely, a little too eagerly, playing at BEING a waiter. What concept does he illustrate, and what exactly is the self-deception?",
    "answer": "Bad faith (mauvaise foi). He treats 'waiter' as a fixed essence he simply IS, the way an inkwell is an inkwell, rather than a role he keeps choosing and could stop choosing. He is a waiter 'in the mode of being what I am not.' He collapses into facticity to escape the anguish of his freedom.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "bad-faith",
    "cluster": "existential-thinkers",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-camus-responses-recall-01",
    "prompt": "Camus names three possible responses to the absurd. List them and say which he endorses.",
    "answer": "1) Physical suicide; 2) Philosophical suicide, meaning a leap into a hope or system (religion, ideology) that explains the absurd away; 3) Revolt, living lucidly with the absurd without false comfort and without surrender. He endorses revolt: 'One must imagine Sisyphus happy.'",
    "type": "recall",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "camus-absurd",
    "cluster": "existential-thinkers",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-absurd-understand-01",
    "prompt": "A student says, 'For Camus, the absurd just means life is meaningless.' Correct the claim.",
    "answer": "For Camus the absurd isn't the world's meaninglessness by itself. It is the CLASH between the human demand for meaning and the world's silence. It exists only in the confrontation. If humans didn't demand meaning, or if the world supplied it, there would be no absurd.",
    "type": "explain",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "camus-absurd",
    "cluster": "existential-thinkers",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-beauvoir-explain-01",
    "prompt": "How does Beauvoir's account of oppression correct the 'radical freedom' reading of early Sartre? Why does it matter for counseling?",
    "answer": "Beauvoir holds that oppression doesn't abolish freedom but blocks its EXERCISE by withholding the material conditions it needs (security, education, leisure), and that affirming my freedom requires affirming others'. Freedom is situated and social. For counseling, 'you are responsible for your choices' can't be applied the same way to someone whose options are constrained by poverty, racism, disability, or abuse. Existentialism itself supplies the correction to its most victim-blaming form.",
    "type": "explain",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "beauvoir-situated-freedom",
    "cluster": "existential-thinkers",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-tillich-recall-01",
    "prompt": "Name Tillich's three types of existential anxiety (The Courage to Be), each with its relative and absolute form.",
    "answer": "Ontic anxiety: fate (relative) / death (absolute). Moral anxiety: guilt / condemnation. Spiritual anxiety: emptiness / meaninglessness. The 'courage to be' takes this anxiety into itself rather than eliminating it.",
    "type": "recall",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "tillich-anxieties",
    "cluster": "existential-thinkers",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-thinkers-compare-01",
    "prompt": "Compare Kierkegaard, Sartre, and Camus: for each, what is the core problem, the failed response, and the recommended response?",
    "answer": "Kierkegaard: problem = the dizziness of freedom; failure = despair (of possibility or of necessity); response = becoming a self through committed choice, ultimately faith. Sartre: problem = radical freedom with no given essence; failure = bad faith; response = owning the choice and its responsibility. Camus: problem = the absurd (demand for meaning vs. a silent world); failure = physical or philosophical suicide; response = revolt, lucid living without appeal. Only Kierkegaard's answer is religious, and Camus would call that leap 'philosophical suicide.'",
    "type": "compare",
    "source_page": "wiki/concept-existential-philosophy-roots.md",
    "topic": "thinkers-compared",
    "cluster": "existential-thinkers",
    "bloom_level": "analyze"
  }
]
```

## Cluster: existential-givens

```json
[
  {
    "id": "ax-exi-givens-recall-01",
    "prompt": "Name Yalom's four ultimate concerns (the 'givens of existence').",
    "answer": "Death, freedom, isolation, meaninglessness.",
    "type": "recall",
    "source_page": "wiki/aux-existentialism.md",
    "topic": "four-givens",
    "cluster": "existential-givens",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-death-defenses-recall-01",
    "prompt": "Yalom organized clinical material around two primary defenses against death anxiety. Name and briefly define each.",
    "answer": "Specialness: the belief that I am personally exempt from the rules of mortality (inviolability). The ultimate rescuer: the belief that someone or something beyond me will protect me. They are opposite-seeming and interchangeable; most people use both.",
    "type": "recall",
    "source_page": "wiki/concept-death-anxiety.md",
    "topic": "death-defenses",
    "cluster": "existential-givens",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-death-defenses-vignette-01",
    "prompt": "Client 1, a 52-year-old surgeon, works 90-hour weeks, never sees a doctor ('I don't get sick'), and falls apart after a minor heart attack. Client 2 has stayed 20 years in a demeaning marriage and says, 'without him I'd be nothing, he takes care of everything.' Which of Yalom's death-anxiety defenses is each client relying on?",
    "answer": "Client 1: SPECIALNESS, personal inviolability expressed as compulsive heroism and work. It collapses when illness disproves it, which is a classic point of decompensation. Client 2: the ULTIMATE RESCUER, fusing with a protector at the cost of self (passivity, dependency). The rescuer defense also guards against isolation.",
    "type": "vignette",
    "source_page": "wiki/concept-death-anxiety.md",
    "topic": "death-defenses",
    "cluster": "existential-givens",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-transdiagnostic-explain-01",
    "prompt": "What does it mean to call death anxiety a 'transdiagnostic construct,' which disorders were highlighted, and how strong is that claim currently?",
    "answer": "It means death anxiety may be a basic fear underlying many different disorders, so treating it could help across diagnoses. Iverach et al. (2014) highlighted illness anxiety/hypochondriasis, panic disorder, and anxiety and depressive disorders. Status: promising, not established. The authors themselves call for large controlled trials, and TMT's lab effect, often cited as support, failed to replicate.",
    "type": "explain",
    "source_page": "wiki/concept-death-anxiety.md",
    "topic": "death-anxiety-transdiagnostic",
    "cluster": "existential-givens",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-death-treatment-mcq-01",
    "prompt": "In the 2018 meta-analysis of randomized trials of interventions targeting death anxiety, which approach produced the largest reduction?",
    "answer": "CBT, especially with exposure to death-related stimuli (g ≈ 1.7). Other therapies did not separate from control (g ≈ .20). Studies were few and mostly low quality, but for fear of dying as a symptom, exposure-based CBT has the best current evidence.",
    "options": [
      "Open-ended existential psychotherapy",
      "Cognitive-behavioral therapy with exposure",
      "Death education courses",
      "Psychodynamic therapy"
    ],
    "correct": "Cognitive-behavioral therapy with exposure",
    "type": "mcq",
    "source_page": "wiki/concept-death-anxiety.md",
    "topic": "death-anxiety-treatment",
    "cluster": "existential-givens",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-awakening-evaluate-01",
    "prompt": "Two days after a stage-3 diagnosis, a client is tearful and frightened. A trainee, who has just read Yalom's Staring at the Sun, says: 'Sometimes a diagnosis like this can be a real wake-up call to live more fully.' Evaluate the response.",
    "answer": "Poorly timed. The 'awakening experience' is a possibility Yalom describes, not a script, and offering it two days in feels like a silver lining that minimizes the fear and moves the client to where the counselor would like them to be. It belongs in the counselor's understanding. If it ever reaches the client, it should come in the client's own words, at their pace. For now: stay with the fear.",
    "type": "vignette",
    "source_page": "wiki/concept-death-anxiety.md",
    "topic": "awakening-experience",
    "cluster": "existential-givens",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-exi-authenticity-understand-01",
    "prompt": "How does EXISTENTIAL authenticity differ from the pop idea of 'finding your true self'?",
    "answer": "Existential authenticity is a WAY of choosing: owning one's existence and its limits instead of living by default ('what one does,' das Man). The pop idea assumes a hidden, pre-existing true self waiting to be discovered and expressed, which is closer to person-centered actualization. Existentialism denies there is a pre-given essence (existence precedes essence), so there is nothing buried to find.",
    "type": "explain",
    "source_page": "wiki/concept-existential-freedom.md",
    "topic": "authenticity",
    "cluster": "existential-givens",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-guilt-compare-01",
    "prompt": "Distinguish neurotic guilt from existential guilt, and say what the clinical response to each should be.",
    "answer": "Neurotic guilt: about imagined or trivial transgressions, often against internalized parental rules. It punishes and keeps the person small, so examine it, reduce it, and treat it as a symptom. Existential guilt: about failing one's own potential, the unlived life. It SIGNALS what one is not yet living, so listen to it rather than reassuring it away. Mistake to avoid: saying 'you shouldn't feel guilty' when the guilt is accurate information.",
    "type": "compare",
    "source_page": "wiki/concept-existential-freedom.md",
    "topic": "existential-guilt",
    "cluster": "existential-givens",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-freedom-evaluate-01",
    "prompt": "A counselor tells a client who is undocumented and working two exploitative jobs: 'Ultimately, you're choosing to stay in this situation. You're responsible for your life.' Evaluate this from within existentialism.",
    "answer": "It is poor existential practice and poor existential philosophy. Later Sartre recast freedom as freedom-in-situation, and Beauvoir argued that oppression blocks the EXERCISE of freedom by withholding its conditions. Facticity is half of existence, not an excuse. The statement also carries the individualist bias multicultural critics identify, and it blames the client. Better: name the real constraints honestly first, then explore the zone of choice inside them, including the choice of attitude and of who the client wants to be within it.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-freedom.md",
    "topic": "situated-freedom",
    "cluster": "existential-givens",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-exi-isolation-types-vignette-01",
    "prompt": "Three clients: (a) moved to a new city and knows no one; (b) 'I just don't feel anything about my father's death, it's like that part of me is switched off'; (c) a bereaved mother with a supportive husband and friends who says 'no one, not even my husband, can know what this is like.' Match each to interpersonal, intrapersonal, or existential isolation.",
    "answer": "(a) Interpersonal: few relationships, which more connection can fix. (b) Intrapersonal: cut off from a part of oneself (disowned feeling), a target for integration. (c) Existential: the unbridgeable gap between selves, which persists even amid love. It can be faced and shared, not solved, and 'join a support group' misses it.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-isolation.md",
    "topic": "isolation-types",
    "cluster": "existential-givens",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-eis-grief-explain-01",
    "prompt": "What does the Existential Isolation Scale measure, and what did Zhou et al. (2023) find about it in bereaved people?",
    "answer": "It measures the felt sense that others do not share or understand one's experience (Pinel et al., 2017), which is distinct from having few relationships or from loneliness. In bereaved Chinese and German-speaking adults, higher existential isolation was associated with more prolonged-grief symptoms, with culture moderating the strength of the link. Levels themselves did not differ by culture or gender. It is also higher among people with non-normative experiences, such as racial and sexual minorities.",
    "type": "explain",
    "source_page": "wiki/concept-existential-isolation.md",
    "topic": "existential-isolation-scale",
    "cluster": "existential-givens",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-fusion-analyze-01",
    "prompt": "Why is FUSION (merging into a partner, group, or cause) considered a defense against existential isolation rather than a solution to it, and what is the existential alternative?",
    "answer": "Fusion removes the felt gap by dissolving the boundary between self and other, so it evades isolation by giving up the self. It is the relational form of the ultimate-rescuer defense. The alternative is relationship between two people who stay separate: isolation can't be eliminated, but it can be SHARED. Buber's I–Thou requires the other to remain other, not merged.",
    "type": "explain",
    "source_page": "wiki/concept-existential-isolation.md",
    "topic": "fusion",
    "cluster": "existential-givens",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-mlq-cloze-01",
    "prompt": "The Meaning in Life Questionnaire (Steger et al., 2006) measures two distinct factors: presence of meaning and {{search for meaning}}.",
    "answer": "search for meaning",
    "type": "cloze",
    "source_page": "wiki/concept-meaning-in-life.md",
    "topic": "mlq",
    "cluster": "existential-givens",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-park-apply-01",
    "prompt": "A father whose core belief was 'if you do things right, your family will be safe' loses his daughter to a drunk driver. Using Park's meaning-making model, describe what is causing the distress and the two broad ways it could resolve.",
    "answer": "Distress comes from a DISCREPANCY between global meaning ('doing right keeps family safe') and situational meaning (the death violates it). Meaning-making efforts try to close the gap, either by reappraising the event's meaning or by revising the global belief, for example toward 'the world isn't controllable, but love still matters.' Caveat: effort isn't the same as meaning MADE. Endless 'why?' rumination is effort without resolution, and Park found quality matters more than quantity.",
    "type": "vignette",
    "source_page": "wiki/concept-meaning-in-life.md",
    "topic": "meaning-making-model",
    "cluster": "existential-givens",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-byproduct-understand-01",
    "prompt": "Why do both Yalom and Frankl say meaning should not be pursued directly?",
    "answer": "Meaning is a BYPRODUCT of engagement. It comes through turning outward (work, love, a cause, creativity), what Frankl calls self-transcendence. Chasing meaning or happiness directly through introspection tends to make it recede, because it 'ensues' rather than being attained. Clinically, help clients engage with something rather than hunt for the meaning of life.",
    "type": "explain",
    "source_page": "wiki/concept-meaning-in-life.md",
    "topic": "meaning-byproduct",
    "cluster": "existential-givens",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-givens-compare-01",
    "prompt": "For each of Yalom's four givens, name the characteristic DEFENSE or evasion described in this module.",
    "answer": "Death → specialness and the ultimate rescuer. Freedom → bad faith, meaning disowning responsibility ('I have no choice') and avoiding decisions (staying stuck at wishing). Isolation → fusion (merging with a partner, group, or cause). Meaninglessness → frantic busyness or chasing meaning directly, the existential vacuum masked until a 'Sunday neurosis' exposes it. In each case the defense evades the given rather than facing it.",
    "type": "compare",
    "source_page": "wiki/aux-existentialism.md",
    "topic": "givens-defenses",
    "cluster": "existential-givens",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-givens-lens-evaluate-01",
    "prompt": "Critique the claim: 'Yalom showed that all psychopathology stems from four ultimate concerns.'",
    "answer": "Overstated twice. First, Yalom offered the four givens as a clinical LENS for organizing listening, not an empirically validated taxonomy, and no study has shown they are THE four or that they drive symptoms as claimed. Other thinkers divide the same ground differently (Tillich's three anxieties include guilt; van Deurzen has four dimensions). Second, he didn't claim they explain ALL pathology. Use them to listen, not as proof.",
    "type": "explain",
    "source_page": "wiki/aux-existentialism.md",
    "topic": "givens-status",
    "cluster": "existential-givens",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: existential-schools

```json
[
  {
    "id": "ax-exi-will-meaning-cloze-01",
    "prompt": "Frankl held that the primary human motive is the will to {{meaning}}, in contrast to Freud's will to pleasure and Adler's will to power.",
    "answer": "meaning",
    "type": "cloze",
    "source_page": "wiki/theory-logotherapy.md",
    "topic": "will-to-meaning",
    "cluster": "existential-schools",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-frankl-sources-recall-01",
    "prompt": "Name Frankl's three routes to meaning, and the fourth source that Meaning-Centered Psychotherapy adds.",
    "answer": "Creative values (what we give: a work or deed); experiential values (what we receive: beauty, truth, encountering someone in love); attitudinal values (the stance we take toward unavoidable suffering). MCP adds historical meaning: life narrative, roles, legacy.",
    "type": "recall",
    "source_page": "wiki/theory-logotherapy.md",
    "topic": "sources-of-meaning",
    "cluster": "existential-schools",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-attitudinal-condition-understand-01",
    "prompt": "What condition must hold before Frankl's ATTITUDINAL value applies, and why is that caveat clinically important?",
    "answer": "The suffering must be UNAVOIDABLE. Frankl: 'to suffer unnecessarily is masochistic rather than heroic.' Suffering that can be relieved should be relieved. Clinically, 'find meaning in your suffering' must never replace addressing a changeable problem (leaving an abusive situation, treating depression, getting pain managed).",
    "type": "explain",
    "source_page": "wiki/theory-logotherapy.md",
    "topic": "attitudinal-values",
    "cluster": "existential-schools",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-vacuum-noogenic-compare-01",
    "prompt": "Distinguish Frankl's existential vacuum, existential frustration, and noogenic neurosis. Is concern about life's meaning itself a disorder, for Frankl?",
    "answer": "Existential vacuum: pervasive emptiness and boredom, a private form of nihilism ('Sunday neurosis' is when it surfaces after the busy week). Existential frustration: the will to meaning is blocked. Noogenic neurosis: neurotic SYMPTOMS arising from that meaning problem rather than from psychosexual conflict or trauma. No, concern over life's worthwhileness is 'a spiritual distress but by no means a mental disease.' It becomes neurosis only when it produces symptoms.",
    "type": "compare",
    "source_page": "wiki/theory-logotherapy.md",
    "topic": "existential-vacuum",
    "cluster": "existential-schools",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-pi-derefl-vignette-01",
    "prompt": "Client A lies awake each night straining to fall asleep, dreading another sleepless night. Client B, preoccupied with monitoring his own sexual performance, has developed erectile difficulties. Which logotherapy technique fits each, and what is the mechanism?",
    "answer": "A: PARADOXICAL INTENTION, deliberately trying to stay awake. This breaks the fear-of-fear / effort-to-sleep loop, and it is supported by a 2022 meta-analysis (large vs. passive, moderate vs. active comparators). B: DEREFLECTION, shifting attention away from self-monitoring toward the partner and the experience. The symptom is fed by hyper-reflection, and attention elsewhere lets natural function return.",
    "type": "vignette",
    "source_page": "wiki/theory-logotherapy.md",
    "topic": "logotherapy-techniques",
    "cluster": "existential-schools",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-frankl-misuse-evaluate-01",
    "prompt": "A counselor tells a client going through a painful divorce: 'Frankl found meaning in Auschwitz. Surely you can find meaning in this.' Evaluate.",
    "answer": "A misuse of logotherapy. It turns another person's survival into a standard the client has failed to meet, which shames rather than helps. It shuts down the client's actual suffering and imposes the counselor's frame, the directiveness risk May warned about. Frankl wrote about his own response to his own suffering. Meaning has to be found by the client, for example through Socratic dialogue, not prescribed by comparison.",
    "type": "vignette",
    "source_page": "wiki/theory-logotherapy.md",
    "topic": "logotherapy-misuse",
    "cluster": "existential-schools",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-exi-tragic-optimism-recall-01",
    "prompt": "What are the three elements of Frankl's 'tragic triad,' and what is 'tragic optimism'?",
    "answer": "Pain, guilt, and death. Tragic optimism is saying 'yes' to life in spite of all three: turning suffering into achievement, guilt into change, and transience into a spur to responsible action. From the 1984 postscript to Man's Search for Meaning.",
    "type": "recall",
    "source_page": "wiki/theory-logotherapy.md",
    "topic": "tragic-optimism",
    "cluster": "existential-schools",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-may-anxiety-compare-01",
    "prompt": "Distinguish Rollo May's normal anxiety from neurotic anxiety on three dimensions.",
    "answer": "1) Proportion: normal anxiety is proportionate to the real threat; neurotic anxiety is disproportionate. 2) Mechanism: normal anxiety needs no repression; neurotic anxiety relies on repression and defense. 3) Outcome: normal anxiety can be used constructively (courage, creativity, growth); neurotic anxiety produces symptoms. For May, the goal is not to eliminate anxiety but to move from neurotic to normal anxiety.",
    "type": "compare",
    "source_page": "wiki/theory-existential-therapy-schools.md",
    "topic": "may-anxiety",
    "cluster": "existential-schools",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-van-deurzen-recall-01",
    "prompt": "Name van Deurzen's four dimensions of existence (with their German terms) and say which one she added to Binswanger's original three.",
    "answer": "Physical (Umwelt), social (Mitwelt), personal/psychological (Eigenwelt), spiritual (Überwelt). She added the spiritual dimension (Überwelt): values, beliefs, meaning.",
    "type": "recall",
    "source_page": "wiki/theory-existential-therapy-schools.md",
    "topic": "four-dimensions",
    "cluster": "existential-schools",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-schools-mcq-01",
    "prompt": "A therapist's signature concept is 'presence,' the therapist's full in-the-moment availability, and she works with how clients protect themselves against their own vitality in the session. Which branch of existential therapy is this?",
    "answer": "Existential-humanistic therapy (Bugental, Schneider; American, with May). Presence is Bugental's central term, and Schneider's approach attends to clients' in-the-moment 'protections.'",
    "options": [
      "Logotherapy",
      "Existential-humanistic therapy",
      "Daseinsanalysis",
      "Meaning-centered group psychotherapy"
    ],
    "correct": "Existential-humanistic therapy",
    "type": "mcq",
    "source_page": "wiki/theory-existential-therapy-schools.md",
    "topic": "schools-discrimination",
    "cluster": "existential-schools",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-schools-compare-01",
    "prompt": "Compare logotherapy, Yalom's existential psychotherapy, and the British existential-phenomenological school on how directive they are and what status they give to meaning.",
    "answer": "Logotherapy is the most directive (named techniques, Socratic dialogue) and treats meaning as quasi-objective, discovered in each situation and ultimately a 'super-meaning.' Yalom's approach is less directive, psychodynamic in structure (conflict → anxiety → defense), uses the here-and-now relationship, and treats meaning as created and a byproduct of engagement. The British school (van Deurzen, Spinelli) is the least technique-driven: it describes the client's lived world through the phenomenological method and treats meaning as something to explore descriptively, not to supply.",
    "type": "compare",
    "source_page": "wiki/theory-existential-therapy-schools.md",
    "topic": "schools-compared",
    "cluster": "existential-schools",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-yalom-structure-understand-01",
    "prompt": "In what sense is Yalom's existential psychotherapy 'psychodynamic in structure'?",
    "answer": "It keeps the psychodynamic model of unconscious conflict → anxiety → defenses → symptoms, but replaces Freud's instinctual drives with the four ultimate concerns (death, freedom, isolation, meaninglessness) as the source of the conflict. His defenses (specialness, ultimate rescuer, fusion) play the role that classic defense mechanisms play in psychoanalysis.",
    "type": "explain",
    "source_page": "wiki/theory-existential-therapy-schools.md",
    "topic": "yalom-structure",
    "cluster": "existential-schools",
    "bloom_level": "understand"
  }
]
```

## Cluster: existential-evidence

```json
[
  {
    "id": "ax-exi-ms-hypothesis-explain-01",
    "prompt": "State terror management theory's mortality-salience hypothesis and describe the classic paradigm used to test it.",
    "answer": "TMT: cultural worldviews and self-esteem buffer death anxiety. So the hypothesis is that reminding people of their death should increase worldview defense and self-esteem striving. Classic paradigm: write about your own death (vs. a control topic like dental pain), do a delay task, then rate pro-US vs. anti-US essay authors. The prediction is stronger preference for the pro-US author under mortality salience.",
    "type": "explain",
    "source_page": "wiki/study-terror-management-theory.md",
    "topic": "tmt-hypothesis",
    "cluster": "existential-evidence",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-ml4-recall-01",
    "prompt": "What did Many Labs 4 (2022) find about the mortality-salience effect, and what feature of its design ruled out the objection 'the replicators didn't know how to run it'?",
    "answer": "No mortality-salience effect on the classic worldview-defense measure. The design compared protocols developed WITH vs. WITHOUT the original TMT authors' involvement, and the effect failed to appear in either. So expertise was not the missing ingredient. Conclusion: a false positive, or conditions no one currently understands. (Re-analyses split: one found a small effect in well-powered sites, a Bayesian multiverse favored the null.)",
    "type": "recall",
    "source_page": "wiki/study-terror-management-theory.md",
    "topic": "many-labs-4",
    "cluster": "existential-evidence",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-tmt-analyze-01",
    "prompt": "A 2010 meta-analysis of 277 experiments found a moderate mortality-salience effect (r = .35), yet a 2022 preregistered multi-lab study found none. Explain how both can be true, naming at least two mechanisms.",
    "answer": "A meta-analysis inherits the biases of the studies it pools. (1) PUBLICATION BIAS: null results go unpublished, so the published record overstates the effect. (2) RESEARCHER DEGREES OF FREEDOM: flexible analyses and choice of outcomes produce false positives. (3) Moderator patterns (stronger in US college students, with longer delays) may reflect flexibility rather than real boundary conditions. Bias-corrected meta-analyses shrank the effect toward zero (Schindler et al., 2023, co-authored by a 2010 meta-analyst). One high-powered preregistered study can outweigh hundreds of small biased ones.",
    "type": "explain",
    "source_page": "wiki/study-terror-management-theory.md",
    "topic": "replication-lessons",
    "cluster": "existential-evidence",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-tmt-evaluate-01",
    "prompt": "Does the TMT replication failure refute Yalom's clinical claim that death anxiety shapes psychopathology? Evaluate.",
    "answer": "No, but it weakens it. Yalom's thesis came from clinical observation and philosophy, not from the mortality-salience paradigm, so the replication failure doesn't refute it directly. It does remove what was often cited as its EXPERIMENTAL support. Death anxiety as a clinical phenomenon has separate support: it appears across anxiety disorders and responds to exposure-based CBT. Fair stance: the clinical construct is plausible and partly supported; the specific lab claim that death reminders drive worldview defense is currently unsupported.",
    "type": "explain",
    "source_page": "wiki/study-terror-management-theory.md",
    "topic": "tmt-implications",
    "cluster": "existential-evidence",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-exi-vos-recall-01",
    "prompt": "In Vos, Craig & Cooper's (2015) meta-analysis of existential therapies, which TYPE had the strongest effects, and on what population was support concentrated?",
    "answer": "Meaning therapies (6 studies): large effects on meaning in life (d ≈ 0.65 post, 0.57 follow-up) and moderate effects on psychopathology (d ≈ 0.47) and self-efficacy. Support concentrated on STRUCTURED interventions (psychoeducation, exercises, direct positive discussion of meaning) with PHYSICALLY ILL patients. Experiential-existential and cognitive-existential therapies showed no significant effects, but on only 2 and 1 studies.",
    "type": "recall",
    "source_page": "wiki/study-existential-therapy-outcomes.md",
    "topic": "vos-meta-analysis",
    "cluster": "existential-evidence",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-vos-critique-evaluate-01",
    "prompt": "Name three reasons to read Vos et al.'s (2015) meta-analysis cautiously, and state what the null result for experiential-existential therapy does and does not mean.",
    "answer": "(1) Few and low-quality studies (the authors say so). (2) A FIXED-effect model, which assumes one true effect across very different therapies and populations; random-effects would be more cautious. (3) Researcher allegiance: the authors are existential-therapy researchers. The experiential-existential null rests on 2 studies. It is ABSENCE of evidence, not evidence that the therapy doesn't work. Honest summary: open-ended existential therapy is untested rather than disproven.",
    "type": "explain",
    "source_page": "wiki/study-existential-therapy-outcomes.md",
    "topic": "vos-critique",
    "cluster": "existential-evidence",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-exi-mcgp-analyze-01",
    "prompt": "The MCGP trial compared meaning-centered group psychotherapy with SUPPORTIVE group psychotherapy rather than a waitlist. Why does that design choice matter for interpreting the result, and what did the stricter intent-to-treat analysis show?",
    "answer": "An ACTIVE control shares the nonspecific ingredients of being in a supportive group (belonging, attention, universality). Beating it suggests the MEANING content adds something specific. Intent-to-treat (everyone randomized, no covariates): advantages held for quality of life, depression, and hopelessness only. Completer analyses (≥3 sessions) showed broader gains, including desire for hastened death and spiritual well-being. Anxiety did not differ in either.",
    "type": "explain",
    "source_page": "wiki/study-existential-therapy-outcomes.md",
    "topic": "mcgp-trial",
    "cluster": "existential-evidence",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-trials-compare-01",
    "prompt": "Compare MCGP (Breitbart 2015), CALM (Rodin 2018), and dignity therapy (Chochinov 2011) on comparator type and what they showed about distress or depression.",
    "answer": "MCGP: active comparator (supportive group). Beat it on QoL, depression, and hopelessness in ITT (and more among completers); no difference on anxiety. CALM: passive comparator (usual care). Small reductions in depression (d ≈ 0.23 at 3 months, 0.29 at 6 months) and better end-of-life preparation. Dignity therapy: three arms. NO significant difference in distress (depression, desire for death, suicidality), but patients rated it more helpful and better for dignity and family. Lesson: 'patients value it' and 'it reduces symptoms' are separate claims.",
    "type": "compare",
    "source_page": "wiki/study-existential-therapy-outcomes.md",
    "topic": "palliative-trials",
    "cluster": "existential-evidence",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-dignity-mcq-01",
    "prompt": "Which statement best describes the main result of the 2011 dignity therapy RCT in terminally ill patients?",
    "answer": "No significant reduction in measured distress, but patients rated it more helpful and valuable for their families. This is the classic case of an intervention that patients value without it moving the primary symptom outcomes.",
    "options": [
      "It significantly reduced depression and desire for death compared with standard care",
      "No significant reduction in distress, but patients rated it more helpful and valuable for their families",
      "It performed worse than client-centred care on every measure",
      "It was stopped early for harm"
    ],
    "correct": "No significant reduction in distress, but patients rated it more helpful and valuable for their families",
    "type": "mcq",
    "source_page": "wiki/study-existential-therapy-outcomes.md",
    "topic": "dignity-therapy",
    "cluster": "existential-evidence",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-match-tool-apply-01",
    "prompt": "Match each presentation to the intervention with the best current evidence: (a) a healthy 30-year-old with intrusive fear of dying, avoiding hospitals and funerals; (b) a patient with advanced cancer saying life has lost its meaning; (c) chronic sleep-onset insomnia driven by effort to sleep.",
    "answer": "(a) Exposure-based CBT (death-anxiety meta-analysis: CBT g ≈ 1.7; other therapies n.s.). (b) A structured meaning-centered intervention such as MCGP or CALM, the best-supported corner of existential therapy. (c) Paradoxical intention, Frankl's technique, now part of CBT for insomnia (2022 meta-analysis). The existential lens informs all three, but the evidence points to different tools.",
    "type": "vignette",
    "source_page": "wiki/study-existential-therapy-outcomes.md",
    "topic": "matching-evidence",
    "cluster": "existential-evidence",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-structure-evidence-analyze-01",
    "prompt": "Across the existential family, the most structured interventions have the strongest RCT support. Give two different explanations for this pattern.",
    "answer": "(1) TESTABILITY: manualized, time-limited protocols are easy to run and replicate in RCTs; open-ended relational therapy is hard to manualize, so it is under-tested rather than shown to fail. (2) Real EFFICACY difference: structure (psychoeducation, exercises, explicit focus on meaning) may add active ingredients, which Vos et al. suggest. The data can't yet separate the two, so 'untested' is the honest label for the open-ended branches.",
    "type": "explain",
    "source_page": "wiki/theory-existential-therapy-schools.md",
    "topic": "structure-evidence",
    "cluster": "existential-evidence",
    "bloom_level": "analyze"
  }
]
```

## Cluster: existential-practice

```json
[
  {
    "id": "ax-exi-spinelli-recall-01",
    "prompt": "Name Spinelli's three rules of the phenomenological method in therapy and give a one-line gloss of each.",
    "answer": "Epoché: bracket your assumptions, a stance of 'un-knowing.' Description: describe the experience rather than explain it. Horizontalization: don't pre-rank what matters; treat each detail as potentially significant.",
    "type": "recall",
    "source_page": "wiki/concept-existential-practice.md",
    "topic": "phenomenological-method",
    "cluster": "existential-practice",
    "bloom_level": "remember"
  },
  {
    "id": "ax-exi-no-choice-apply-01",
    "prompt": "Client: 'I have no choice, I HAVE to stay in this job.' Write an existential response and name two opposite mistakes to avoid.",
    "answer": "Response: curiosity about the 'have to,' e.g. 'What would happen if you didn't?' or 'What makes it feel like there's no choice?' Hold open both the real constraints and the zone of choice inside them, including attitude. Mistake 1: accepting the statement wholesale as fact, which closes the exploration. Mistake 2: confronting it as bad faith ('you're choosing this'), which is one-up, often wrong, and ignores real constraints like money, visas, or family obligations.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-practice.md",
    "topic": "working-with-freedom",
    "cluster": "existential-practice",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-meaningless-risk-apply-01",
    "prompt": "A client who has been quoting Camus says quietly, 'Honestly, what's the point of any of it anymore?' What is your FIRST move, and why doesn't the philosophical framing change it?",
    "answer": "Assess suicide risk directly: ask about thoughts of death or suicide, intent, plan, means, and protective factors, and safety-plan if needed. 'What's the point' can be philosophy, depression, and suicidal ideation all at once, and sounding philosophical doesn't make it safe. (Camus answered his own question with revolt, not death.) Only after safety is addressed does existential exploration of the despair belong, and it can then be really valuable.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-practice.md",
    "topic": "existential-despair-risk",
    "cluster": "existential-practice",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-here-now-apply-01",
    "prompt": "A client says for the third session running that 'everyone eventually gets tired of me and leaves.' She has started arriving late and apologizing a lot. How would Yalom's here-and-now approach use this?",
    "answer": "Bring the pattern into the room, tentatively: 'I notice you've been apologizing a lot here. I wonder whether you're expecting me to get tired of you too?' The relationship becomes live material where the pattern can be examined and a different experience had, rather than only talked about as history. This is Yalom's signature move in individual and group work.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-practice.md",
    "topic": "here-and-now",
    "cluster": "existential-practice",
    "bloom_level": "apply"
  },
  {
    "id": "ax-exi-lecturing-evaluate-01",
    "prompt": "Session excerpt. Client: 'Since Mom died I just feel so alone, even with my husband.' Counselor: 'That's existential isolation. Yalom says we're all fundamentally alone; it's one of the four givens. Facing it can actually be freeing.' Evaluate the counselor's response.",
    "answer": "It delivers philosophy AT the client. The givens are a lens for the counselor's listening, not content to teach. The response intellectualizes, moves the client from feeling to theory, adds a premature silver lining ('freeing'), and puts the counselor in the expert role instead of fellow traveler. Better: stay with the experience, e.g. 'Even with him there, it's like no one can reach where you are right now,' and let the client describe it. Sharing isolation is done through presence, not explanation.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-practice.md",
    "topic": "lecturing-trap",
    "cluster": "existential-practice",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-exi-presence-understand-01",
    "prompt": "Why does the existential tradition treat the counselor's own reckoning with death, freedom, isolation, and meaning as part of clinical competence?",
    "answer": "The material is frightening for the counselor too, who is also mortal, free, alone, and unsure about meaning. A counselor who hasn't faced their own death anxiety tends to hurry clients past theirs by reassuring, changing the subject, or problem-solving. That breaks presence, which is the core of existential work. Being able to stay with the unfixable depends on having stopped running from it oneself.",
    "type": "explain",
    "source_page": "wiki/concept-existential-practice.md",
    "topic": "presence",
    "cluster": "existential-practice",
    "bloom_level": "understand"
  },
  {
    "id": "ax-exi-stance-fix-evaluate-01",
    "prompt": "Why is existential work described as the place where the counselor's urge to 'fix' does the most damage? Give one concrete example of fixing and what it costs the client.",
    "answer": "The givens can't be fixed. No one can remove a client's mortality, fundamental aloneness, freedom, or the absence of ready-made meaning. So fixing moves (reassurance, silver linings, supplying meaning, problem-solving) don't solve anything. They signal that the counselor can't bear to be with it. Example: 'I'm sure the scan will be fine' leaves the client alone with the fear and teaches them not to bring it up again. The alternative is presence: staying with what can't be solved.",
    "type": "explain",
    "source_page": "wiki/aux-existentialism.md",
    "topic": "stance-no-fixing",
    "cluster": "existential-practice",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-exi-practice-compare-01",
    "prompt": "Compare how a CBT counselor and an existential counselor would each approach a client whose central complaint is 'I'm terrified of dying.' Where do the two approaches converge?",
    "answer": "CBT: treat the fear as an anxiety symptom. Assess avoidance and safety behaviors, then run graded EXPOSURE to death-related stimuli; this has the strongest RCT support (g ≈ 1.7). Existential: explore what death means to this person, the defenses it has driven (specialness, rescuer), and how finitude bears on how they are living, with the goal of facing rather than eliminating the fear. Convergence: both reject reassurance and avoidance, and both have the client FACE what they've been fleeing. Exposure is the behavioral form of 'staring at the sun.' They can be integrated.",
    "type": "compare",
    "source_page": "wiki/concept-death-anxiety.md",
    "topic": "cbt-vs-existential-death",
    "cluster": "existential-practice",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-exi-dying-client-apply-01",
    "prompt": "You're working with a man in hospice care who says he's 'wasted his life' and has nothing to leave his grandchildren. Drawing on meaning-centered and dignity approaches, name two concrete directions the work could take.",
    "answer": "(1) HISTORICAL meaning: review his life story, roles, and what he has given, which often uncovers more than he currently sees. (2) Legacy / generativity: something like dignity therapy's recorded, edited document of what mattered most, what he learned, and what he hopes for his grandchildren. Also attitudinal meaning in how he faces this. Keep his 'wasted' claim open rather than arguing it away: existential guilt may be accurate and worth hearing. Presence and structure, not cheerfulness.",
    "type": "vignette",
    "source_page": "wiki/concept-existential-practice.md",
    "topic": "dying-client",
    "cluster": "existential-practice",
    "bloom_level": "apply"
  }
]
```
