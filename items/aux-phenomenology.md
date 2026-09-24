# Elective module items: Phenomenology

Source of truth for this **elective/ad-hoc module** (off-spine; `aux-` namespace). Each fenced `json` block is a JSON array merged by `apps/build_items.py` into `build/items.json`. Items span all five Bloom levels and lean toward **discrimination** (confusable thinkers, concepts, and methods), **application** (vignettes), and **stance** (describe-before-explain; not over-claiming evidence), per the generate rules in [`../CLAUDE.md`](../CLAUDE.md) and [`../learning-science-for-self-study.md`](../learning-science-for-self-study.md). Item id prefix: `ax-phe-`.

Clusters: `phen-method` · `phen-founders` · `heidegger-concepts` · `embodiment-ecology` · `daseinsanalysis` · `phen-psychopathology` · `phen-stance` · `phen-research`. Each cluster has at least one dedicated compare item.

## Cluster: phen-method (Husserl's method, intentionality, lifeworld)

```json
[
  {
    "id": "ax-phe-def-cloze-01",
    "prompt": "Phenomenology is the study of structures of experience as experienced from the {{first-person}} point of view.",
    "answer": "first-person",
    "type": "cloze",
    "source_page": "wiki/concept-husserl-phenomenology.md",
    "topic": "definition",
    "cluster": "phen-method",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-slogan-cloze-01",
    "prompt": "Husserl's rallying cry for phenomenology was 'back to the {{things themselves}}' (zu den Sachen selbst).",
    "answer": "things themselves",
    "type": "cloze",
    "source_page": "wiki/concept-husserl-phenomenology.md",
    "topic": "husserl-method",
    "cluster": "phen-method",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-natatt-recall-01",
    "prompt": "What is the 'natural attitude,' and what does it hide?",
    "answer": "The everyday, unreflective stance that takes for granted an independent world 'out there' full of objects, with minds as things in it receiving impressions. It works and science is built on it, but it hides HOW the world comes to have the meaning it has for us: we look straight through experience to its objects and never notice the experience itself.",
    "type": "recall",
    "source_page": "wiki/concept-husserl-phenomenology.md",
    "topic": "natural-attitude",
    "cluster": "phen-method",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-epoche-explain-01",
    "prompt": "Explain the epoché (bracketing). What does it suspend, and what does it NOT do?",
    "answer": "It suspends (puts 'in brackets') the natural attitude's assumption about the world's independent existence and nature: you stop USING that assumption so attention can turn to the world as experienced. It does NOT doubt or deny the world (unlike Descartes), and it is not 'having no opinions'. It is a deliberate, repeatable shift of attention from what things are to how they are given.",
    "type": "explain",
    "source_page": "wiki/concept-husserl-phenomenology.md",
    "topic": "epoche",
    "cluster": "phen-method",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-eidetic-apply-01",
    "prompt": "You want to know what is ESSENTIAL to the experience of shame. Using eidetic (imaginative) variation, describe how you would proceed, with one example of a feature that survives and one that doesn't.",
    "answer": "Imaginatively vary the experience, removing or changing features one at a time, and ask whether it would still be shame. E.g., remove 'being seen/exposed to an evaluating other (real or imagined)': it collapses into something else (guilt? regret?), so that feature is essential. Remove 'blushing': it is still shame, so blushing is not essential. What survives every variation is the eidos (essential structure).",
    "type": "vignette",
    "source_page": "wiki/concept-husserl-phenomenology.md",
    "topic": "eidetic-variation",
    "cluster": "phen-method",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-reductions-compare-01",
    "prompt": "Compare the phenomenological (transcendental) reduction with the eidetic reduction: what question does each ask?",
    "answer": "Phenomenological reduction: leads attention back from objects to the consciousness-world correlation in which they are constituted as meaningful. It asks 'how does this come to show up as what it is, for me?' Eidetic reduction: uses imaginative variation to find invariant essences. It asks 'what is invariant in every possible case of this kind of experience?' One is about givenness, the other about essence.",
    "type": "compare",
    "source_page": "wiki/concept-husserl-phenomenology.md",
    "topic": "reductions",
    "cluster": "phen-method",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-psychologism-understand-01",
    "prompt": "What is psychologism, why did Husserl attack it, and what follows for the claim that 'phenomenology is a kind of psychology'?",
    "answer": "Psychologism is the view that logic is a branch of psychology describing how people happen to think. In the Logical Investigations (1900-01) Husserl argued that logical truths are ideal and timeless, not facts about mental processes. So he insisted phenomenology is not empirical psychology: it seeks essential structures of any possible experience, not statistics about actual people. Counseling's 'phenomenological approach' is a looser borrowing of his attitude, not his project.",
    "type": "explain",
    "source_page": "wiki/concept-husserl-phenomenology.md",
    "topic": "anti-psychologism",
    "cluster": "phen-method",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-intent-cloze-01",
    "prompt": "In phenomenology, the directedness of every experience toward something beyond itself (every fear is fear OF something) is called {{intentionality}}.",
    "answer": "intentionality",
    "type": "cloze",
    "source_page": "wiki/concept-intentionality.md",
    "topic": "intentionality",
    "cluster": "phen-method",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-intent-mcq-01",
    "prompt": "Which statement best captures 'intentionality' in the phenomenological sense?",
    "options": [
      "Experiences are always directed at or about something, as something.",
      "People act on purpose rather than by reflex.",
      "The unconscious aims behavior at hidden goals.",
      "Therapists should set explicit intentions for each session."
    ],
    "correct": "Experiences are always directed at or about something, as something.",
    "answer": "Intentionality comes from Latin 'intendere' (to aim toward): every perception, belief, emotion, or daydream is ABOUT something. It has nothing special to do with intending to act. Brentano made it the mark of the mental; Husserl made it the core of phenomenology.",
    "type": "mcq",
    "source_page": "wiki/concept-intentionality.md",
    "topic": "intentionality",
    "cluster": "phen-method",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-noesis-noema-compare-01",
    "prompt": "Distinguish noesis from noema, using a client's memory of their childhood home.",
    "answer": "Noesis = the act side, the mode of directedness (here: remembering, as opposed to imagining, dreading, perceiving). Noema = the object-as-intended, the home as it is meant in this act (e.g., 'a place I was never safe' vs. 'a warm refuge'). The same home can carry different noemata. How it is meant is part of the experience, which is exactly what a reflection of meaning tries to capture.",
    "type": "compare",
    "source_page": "wiki/concept-intentionality.md",
    "topic": "noesis-noema",
    "cluster": "phen-method",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-intent-apply-01",
    "prompt": "A client says only, 'I'm just anxious all the time.' Using the idea of intentionality, what two questions would a phenomenologically minded counselor pursue, and why?",
    "answer": "(1) What is the anxiety directed at or about: the future, the body, other people's judgment, a specific situation? (2) How is that thing given: as looming, as uncontrollable, as watching me? Intentionality says experiences are not free-floating states but ways the world shows up. So clarifying the 'of what' and the 'as what' makes the experience describable and reflectable, before any explanation.",
    "type": "vignette",
    "source_page": "wiki/concept-intentionality.md",
    "topic": "intentionality",
    "cluster": "phen-method",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-lifeworld-recall-01",
    "prompt": "What did Husserl mean by the lifeworld (Lebenswelt), in which work did he develop it, and what 'crisis' was it meant to address?",
    "answer": "The pre-scientific, taken-for-granted world of everyday experience: shared, cultural, historical, the ground of meaning that science abstracts from. Developed in The Crisis of European Sciences (1936). The crisis: modern science (from Galileo's mathematization of nature) forgot it was an abstraction from the lifeworld and mistook its measurable abstractions for the whole of reality, leaving it unable to address meaning and value.",
    "type": "recall",
    "source_page": "wiki/concept-lifeworld.md",
    "topic": "lifeworld",
    "cluster": "phen-method",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-lifeworld-evaluate-01",
    "prompt": "A classmate argues: 'If a treatment's RCT evidence is strong, the client's account of what their depression means is just noise.' Evaluate this using the lifeworld concept.",
    "answer": "The claim confuses two kinds of knowledge. RCT evidence is abstracted from the lifeworld: indispensable for knowing what works on average, but silent about what depression is like for this person and what recovery would mean to them. Husserl's point is that such abstractions grow out of the lifeworld and can't replace it. Evidence-based practice itself includes client values and preferences for this reason. The client's account isn't noise; it's a different, necessary kind of data.",
    "type": "explain",
    "source_page": "wiki/concept-lifeworld.md",
    "topic": "lifeworld",
    "cluster": "phen-method",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-worldconcepts-compare-01",
    "prompt": "Four 'world' concepts: Husserl's lifeworld, Rogers' phenomenal field, Lewin's life space, Binswanger's Umwelt/Mitwelt/Eigenwelt. For each, say whose world it is and its key feature.",
    "answer": "Lifeworld: shared and intersubjective; the taken-for-granted background of meaning that science abstracts from. Phenomenal field: individual; everything this person experiences, the only reality that matters for understanding them. Life space: individual at a moment; person plus psychological environment, used to predict and explain behavior now. Umwelt/Mitwelt/Eigenwelt: individual, structured into three regions (surroundings/body, others, self) that are always co-present.",
    "type": "compare",
    "source_page": "wiki/concept-lifeworld.md",
    "topic": "world-concepts",
    "cluster": "phen-method",
    "bloom_level": "analyze"
  }
]
```

## Cluster: phen-founders (who's who)

```json
[
  {
    "id": "ax-phe-founders-mcq-01",
    "prompt": "Which phenomenologist made the LIVED BODY the center of phenomenology, drew heavily on Gestalt psychology and neurology, and analyzed the Schneider case?",
    "options": [
      "Maurice Merleau-Ponty",
      "Edmund Husserl",
      "Martin Heidegger",
      "Karl Jaspers"
    ],
    "correct": "Maurice Merleau-Ponty",
    "answer": "Merleau-Ponty: Phenomenology of Perception (1945); lived body, body schema, motor intentionality, habit, Schneider and the phantom limb. Husserl = consciousness and bracketing; Heidegger = being-in-the-world; Jaspers = phenomenological psychiatry.",
    "type": "mcq",
    "source_page": "wiki/person-maurice-merleau-ponty.md",
    "topic": "founders",
    "cluster": "phen-founders",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-founders-mcq-02",
    "prompt": "Which figure trained as a psychiatrist, wrote General Psychopathology (1913), and distinguished understanding (Verstehen) from explanation (Erklären)?",
    "options": [
      "Karl Jaspers",
      "Ludwig Binswanger",
      "Eugène Minkowski",
      "Edmund Husserl"
    ],
    "correct": "Karl Jaspers",
    "answer": "Jaspers, at Heidelberg, before he became an existential philosopher. Binswanger = Daseinsanalysis and Ellen West; Minkowski = lived time and loss of vital contact; Husserl = the founding philosopher, not a psychiatrist.",
    "type": "mcq",
    "source_page": "wiki/person-karl-jaspers.md",
    "topic": "founders",
    "cluster": "phen-founders",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-founders-compare-01",
    "prompt": "Contrast Husserl and Heidegger on the STARTING POINT of phenomenology and on whether bracketing is possible.",
    "answer": "Husserl starts from consciousness, reached by bracketing the natural attitude (the epoché), and pursues transcendental phenomenology. Heidegger starts from existence (Dasein) as being-in-the-world: we are always already in a world of involvements and understanding runs through prior understanding, so the world can't be bracketed away. This gives existential/hermeneutic phenomenology and, later, interpretive research methods.",
    "type": "compare",
    "source_page": "wiki/person-martin-heidegger.md",
    "topic": "husserl-vs-heidegger",
    "cluster": "phen-founders",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-founders-table-recall-01",
    "prompt": "Name the 'type' of phenomenology associated with each: Husserl, Heidegger, Merleau-Ponty.",
    "answer": "Husserl: transcendental phenomenology (consciousness, epoché, essences). Heidegger: existential/hermeneutic phenomenology (Dasein, being-in-the-world, interpretation). Merleau-Ponty: embodied phenomenology (the lived body, perception).",
    "type": "recall",
    "source_page": "wiki/aux-phenomenology.md",
    "topic": "founders",
    "cluster": "phen-founders",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-brentano-cloze-01",
    "prompt": "Husserl took the concept of intentionality from his teacher {{Franz Brentano}}, who proposed it as the mark of the mental.",
    "answer": "Franz Brentano",
    "type": "cloze",
    "source_page": "wiki/person-edmund-husserl.md",
    "topic": "brentano",
    "cluster": "phen-founders",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-heidegger-nazi-evaluate-01",
    "prompt": "A classmate says: 'Heidegger's Nazism is irrelevant; ideas stand or fall on their own.' Another says: 'Nothing he wrote should be used.' Evaluate both positions as the wiki presents the issue.",
    "answer": "Both are overconfident. The record is real: party membership in 1933, the Freiburg rectorship, antisemitic passages in the Black Notebooks. Scholars genuinely disagree about how far it infects the philosophy (from separable to essentially entangled). A defensible middle: you can use concepts like being-in-the-world without endorsing the man, but don't present him as a neutral sage, and recognize that refusing to build on him is also a defensible position. The point is to engage the record, not ignore it or treat it as settled.",
    "type": "explain",
    "source_page": "wiki/person-martin-heidegger.md",
    "topic": "heidegger-nazism",
    "cluster": "phen-founders",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-stein-recall-01",
    "prompt": "Who was Edith Stein and what was her contribution to phenomenology?",
    "answer": "Husserl's assistant, who wrote the dissertation On the Problem of Empathy (1917). She described empathy as a sui generis experience in which another's experience is given to me directly, in the present, but as NOT mine. She distinguished it from emotional contagion and sympathy, and traced it from bodily/sensual to emotional levels.",
    "type": "recall",
    "source_page": "wiki/concept-phenomenology-of-empathy.md",
    "topic": "stein",
    "cluster": "phen-founders",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-gibson-lewin-analyze-01",
    "prompt": "Why is it a mistake to call Gibson or Lewin 'phenomenologists,' even though both appear in the phenomenology module?",
    "answer": "Both were experimental psychologists (Gibson in perception, Lewin a Gestalt-trained social psychologist), working with empirical methods to predict and explain, not describing structures of experience from the first-person point of view. They appear because they reached convergent conclusions: affordances as organism-environment complementarity, and B = f(P, E) with the life space. Convergence is not membership.",
    "type": "explain",
    "source_page": "wiki/concept-affordances.md",
    "topic": "founders",
    "cluster": "phen-founders",
    "bloom_level": "analyze"
  }
]
```

## Cluster: heidegger-concepts

```json
[
  {
    "id": "ax-phe-dasein-cloze-01",
    "prompt": "Heidegger's term for the human being, literally 'being-there,' is {{Dasein}}.",
    "answer": "Dasein",
    "type": "cloze",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "dasein",
    "cluster": "heidegger-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-bitw-explain-01",
    "prompt": "Why does Heidegger insist being-in-the-world is a UNITARY phenomenon, and what traditional picture is he rejecting?",
    "answer": "Because world, self, and 'being-in' are inseparable aspects of one structure, not a self plus a world glued together. He rejects the picture of a mind or subject inside a skull, facing a separate world of objects and puzzling over how the two connect. On his view we are always already absorbed in a meaningful world of tasks, tools, and people. The subject-object split is derivative, not basic.",
    "type": "explain",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "being-in-the-world",
    "cluster": "heidegger-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-hammer-compare-01",
    "prompt": "Using Heidegger's hammer, contrast ready-to-hand with present-at-hand, and say which he thinks is basic.",
    "answer": "Ready-to-hand (zuhanden): the hammer in use, encountered as for-hammering within a web of purposes, almost transparent while I'm absorbed in the job. Present-at-hand (vorhanden): the hammer as a mere object with properties (400 g, cracked handle), which shows up when it breaks or goes missing, or when I take a detached theoretical stance. Ready-to-hand is basic; detached observation is a derivative mode.",
    "type": "compare",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "ready-vs-present-at-hand",
    "cluster": "heidegger-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-hammer-apply-01",
    "prompt": "A client's marriage has been 'just there' for years, unnoticed like the air. After discovering an affair, they say, 'Suddenly I'm looking at my whole life like a stranger's.' Which Heidegger idea does this illustrate, and what is the clinical implication?",
    "answer": "Breakdown turning the ready-to-hand into the present-at-hand: a structure that was lived through transparently becomes conspicuous as an object when it fails, like the broken hammer. Implication: crises are painful but make the background structure of a life visible, and so available for examination and choice. The counselor can help the client look at what was previously invisible rather than rushing to restore the old transparency.",
    "type": "vignette",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "ready-vs-present-at-hand",
    "cluster": "heidegger-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-thrown-cloze-01",
    "prompt": "Heidegger's term for always already finding ourselves in circumstances we didn't choose (body, family, language, era) is {{thrownness}} (Geworfenheit).",
    "answer": "thrownness",
    "type": "cloze",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "thrownness",
    "cluster": "heidegger-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-dasman-apply-01",
    "prompt": "A 30-year-old describes her life: 'I did the degree one does, took the job one takes, I'm dating the way everyone dates, and I have no idea what I actually want.' Name the Heideggerian concept and explain it without moralizing.",
    "answer": "Das Man (the They, the Anyone) and 'falling': living as 'one' lives, by anonymous public norms of what one does and thinks. Heidegger treats this as a structural feature of everyday existence, not simply a moral failing: we all mostly live this way. But it lets us dodge ownership of our own lives. The clinical move is to explore which choices are hers, not to shame her for conforming.",
    "type": "vignette",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "das-man",
    "cluster": "heidegger-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-angst-fear-compare-01",
    "prompt": "Contrast fear and anxiety (Angst) in Heidegger's sense.",
    "answer": "Fear is of a specific threat in the world (the dog, the exam). Anxiety has no object: the whole web of everyday meanings goes flat and 'of no consequence', and what remains is the bare fact that one is, and has to be, one's own life. Anxiety discloses care (Sorge) and makes authenticity possible. Note this differs from DSM anxiety disorders; it is an existential-structural concept, not a diagnosis.",
    "type": "compare",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "anxiety-vs-fear",
    "cluster": "heidegger-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-care-recall-01",
    "prompt": "What does Heidegger mean by 'care' (Sorge), and by 'understanding as projection'?",
    "answer": "Care: the overarching structure of being-in-the-world. We are always already concerned with how our existence goes; our own being is an issue for us. Understanding as projection: to understand anything is to grasp it in terms of what it makes possible. We are always projecting ourselves onto possibilities (becoming a counselor, being a parent).",
    "type": "recall",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "care",
    "cluster": "heidegger-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-mood-explain-01",
    "prompt": "In Heidegger's account, why are moods 'world-disclosing' rather than inner feelings added to a neutral world?",
    "answer": "Because we are always in some mood (Befindlichkeit), and only through attunement does anything show up as mattering at all: threatening, inviting, boring. A mood-less world wouldn't be neutral, it would be unintelligible. Moods are neither in me (like a stomachache) nor in the room (like its temperature); they arise from being-in-the-world itself and shape which possibilities the whole world seems to offer.",
    "type": "explain",
    "source_page": "wiki/concept-mood-attunement.md",
    "topic": "befindlichkeit",
    "cluster": "heidegger-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-affect-levels-compare-01",
    "prompt": "Distinguish emotion, mood (attunement), and existential feeling (Ratcliffe) by what each is directed at, with an example of each.",
    "answer": "Emotion: a specific object, e.g., afraid of the dog. Mood/attunement: the world as a whole, e.g., everything seems menacing today. Existential feeling: one's overall sense of belonging to the world and of what possibilities it contains, e.g., feeling unreal, cut off, as if nothing could ever matter again. Existential feelings sit beneath emotions and shape the field in which things can be encountered at all.",
    "type": "compare",
    "source_page": "wiki/concept-mood-attunement.md",
    "topic": "mood-levels",
    "cluster": "heidegger-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-mood-mse-analyze-01",
    "prompt": "A student writes in an MSE: 'Mood: the client's Befindlichkeit is closed off to possibility.' What's wrong with that, and how should the two senses of 'mood' be kept apart?",
    "answer": "It conflates the MSE's technical 'mood' (the client's self-reported emotional state, in their own words, paired with observed affect) with Heidegger's philosophical 'mood' (the attunement through which a whole world shows up as mattering). The MSE should record e.g. 'Mood: \"empty, like nothing matters\"' and describe affect. The phenomenological sense is useful for listening and reflecting, not as MSE terminology.",
    "type": "explain",
    "source_page": "wiki/concept-mood-attunement.md",
    "topic": "mood-vs-mse",
    "cluster": "heidegger-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-mood-reflect-apply-01",
    "prompt": "A client says: 'It's like the whole world has gone cardboard. I can see everything, it just doesn't reach me.' Write a reflection that captures the attunement rather than just the feeling-label.",
    "answer": "Example: 'It sounds like the world is all still there, but it's gone flat and distant, as if nothing in it can touch you anymore.' This reflects the shape of the lived world (flat, distant, unreachable) rather than labeling it 'depressed' or 'sad'. It shows you grasp the experience from inside, which often lands more accurately than the label.",
    "type": "vignette",
    "source_page": "wiki/concept-mood-attunement.md",
    "topic": "reflecting-attunement",
    "cluster": "heidegger-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-bitw-environment-evaluate-01",
    "prompt": "Evaluate the claim 'Heidegger shows that a client's environment is just one factor influencing their inner self.'",
    "answer": "It gets Heidegger backwards. For him there is no self first and environment second: being-in-the-world is unitary, so home, relationships, work, and culture are part of the structure of the person's existence, not external 'factors' acting on a separate inner self. The 'factors' framing is the subject-object picture he rejects. This converges with systems thinking, Lewin's life space, and 4E cognition.",
    "type": "explain",
    "source_page": "wiki/concept-being-in-the-world.md",
    "topic": "being-in-the-world",
    "cluster": "heidegger-concepts",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: embodiment-ecology (lived body, affordances, 4E, Lewin)

```json
[
  {
    "id": "ax-phe-leib-korper-compare-01",
    "prompt": "Contrast the lived body (Leib, corps propre) with the physical body (Körper).",
    "answer": "Lived body: the body as I live it from inside, the zero-point from which things are near/far, reachable or not; usually transparent (I don't notice my hand while writing). Physical body: the body as an object, anatomy, measurable, visible from outside, showing up when something goes wrong (pain, illness, being stared at). Depression can turn the lived body into a heavy Körper: Fuchs's 'corporealization'.",
    "type": "compare",
    "source_page": "wiki/concept-embodiment.md",
    "topic": "leib-vs-korper",
    "cluster": "embodiment-ecology",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-schema-image-compare-01",
    "prompt": "Distinguish body schema from body image, and name a clinical condition that centrally disturbs each.",
    "answer": "Body schema: the pre-conscious, practical system of bodily capacities and spatial know-how that lets you move without monitoring yourself (disrupted by stroke, amputation, the Schneider case). Body image: perceptions, beliefs, and attitudes ABOUT your body, the conceptual/evaluative picture (centrally disturbed in eating disorders). Confusing them muddles case conceptualization.",
    "type": "compare",
    "source_page": "wiki/concept-embodiment.md",
    "topic": "schema-vs-image",
    "cluster": "embodiment-ecology",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-motorint-cloze-01",
    "prompt": "Merleau-Ponty described the body's basic relation to the world as an 'I {{can}}' rather than an 'I think': motor intentionality.",
    "answer": "can",
    "type": "cloze",
    "source_page": "wiki/concept-embodiment.md",
    "topic": "motor-intentionality",
    "cluster": "embodiment-ecology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-schneider-understand-01",
    "prompt": "What could Schneider (Gelb & Goldstein's brain-injured patient) do and not do, and what did Merleau-Ponty conclude?",
    "answer": "He could perform concrete, habitual movements (take out a handkerchief and blow his nose) but not abstract ones on command (point to his nose, trace a shape in the air). Merleau-Ponty read this as loss of the 'intentional arc', the capacity to project into virtual, merely possible space. Normal bodily life therefore involves an openness to possibility that is neither pure reflex nor pure thought. (Treat as illustration; the original reports have been questioned.)",
    "type": "explain",
    "source_page": "wiki/concept-embodiment.md",
    "topic": "schneider",
    "cluster": "embodiment-ecology",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-habit-apply-01",
    "prompt": "A client says, 'I understand exactly why I freeze up with my boss. I've understood it for two years. Why can't I stop?' Use Merleau-Ponty's account of habit to explain why insight alone may not be enough.",
    "answer": "For Merleau-Ponty, ways of engaging the world sediment into the 'habit body': acquired bodily understanding that runs below explicit thought. If the freeze is sedimented bodily know-how, conceptual insight addresses the wrong level. Change also requires re-habituation through repeated new bodily practice (e.g., graded exposure, rehearsed assertive behavior), not only understanding. (This is an interpretive bridge from phenomenology to why practice-based methods help.)",
    "type": "vignette",
    "source_page": "wiki/concept-embodiment.md",
    "topic": "habit",
    "cluster": "embodiment-ecology",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-affordance-cloze-01",
    "prompt": "Gibson: 'The {{affordances}} of the environment are what it offers the animal, what it provides or furnishes, either for good or ill.'",
    "answer": "affordances",
    "type": "cloze",
    "source_page": "wiki/concept-affordances.md",
    "topic": "affordances",
    "cluster": "embodiment-ecology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-affordance-relational-explain-01",
    "prompt": "Why are affordances called 'relational,' and what view of perception did Gibson reject?",
    "answer": "An affordance belongs neither to the environment alone nor to the animal alone but to their fit: a knee-high surface affords sitting for an adult human, not for an ant (Gibson: animal and environment are 'complementary'). He rejected the inferential view (Helmholtz, Gregory, Rock) that the brain builds a picture from impoverished data by unconscious inference. He held instead that an actively moving observer directly picks up rich information about action possibilities.",
    "type": "explain",
    "source_page": "wiki/concept-affordances.md",
    "topic": "affordances",
    "cluster": "embodiment-ecology",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-affordance-depression-apply-01",
    "prompt": "A depressed client: 'The guitar is right there. I love playing. It just sits there like furniture.' Describe this in terms of affordances and suggest what follows for intervention.",
    "answer": "The field of affordances has flattened: the guitar is still perceived but no longer invites action, which is a precise description of anhedonia and amotivation rather than a willpower failure. Since affordances are relational, one route is to change the relation from the action side: very small, scheduled engagements (pick it up for two minutes) can reopen contact before motivation returns, which is the behavioral-activation logic. Also check hopelessness and risk as usual.",
    "type": "vignette",
    "source_page": "wiki/concept-affordances.md",
    "topic": "affordances-depression",
    "cluster": "embodiment-ecology",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-affordance-means-analyze-01",
    "prompt": "Explain how the relational nature of affordances gives a conceptual rationale for means reduction in suicide prevention, and state the limit of that rationale.",
    "answer": "If what the environment offers is part of what a person can do in a moment, then removing a lethal means removes an affordance: it changes the person-environment system during a crisis rather than only trying to change the person's mind. Limit: this is an interpretive bridge. The evidence for means reduction comes from its own epidemiological literature (on its own page), not from Gibson.",
    "type": "explain",
    "source_page": "wiki/concept-affordances.md",
    "topic": "affordances-means",
    "cluster": "embodiment-ecology",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-4e-recall-01",
    "prompt": "Name the four Es of 4E cognition, with one-line claims, from weakest to strongest.",
    "answer": "Embedded: cognition leans on a well-organized environment that reduces internal load (environment as support). Embodied: the body's form and sensorimotor capacities shape and partly constitute cognition (the umbrella). Enactive: cognition IS skilled sensorimotor interaction; mind emerges from living activity (Varela, Thompson & Rosch). Extended: parts of the environment can literally be constituents of cognitive processes (Clark & Chalmers). Extended is the most disputed.",
    "type": "recall",
    "source_page": "wiki/concept-4e-cognition.md",
    "topic": "4e",
    "cluster": "embodiment-ecology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-otto-explain-01",
    "prompt": "Summarize the Otto/Inga thought experiment and the parity principle.",
    "answer": "Inga recalls from biological memory that the museum is on 53rd Street; Otto (Alzheimer's) looks it up in a notebook he always carries, trusts, and updates. The notebook plays the same functional role for Otto that memory plays for Inga, so Otto believed the address before looking, as Inga did before recalling. Parity principle: if a part of the world functions as a process which, were it done in the head, we'd call cognitive, then it IS part of the cognitive process.",
    "type": "explain",
    "source_page": "wiki/concept-4e-cognition.md",
    "topic": "extended-mind",
    "cluster": "embodiment-ecology",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-embedded-extended-compare-01",
    "prompt": "Contrast the embedded and extended theses using a smartphone calendar. Then state Adams & Aizawa's objection to the stronger one.",
    "answer": "Embedded: the calendar HELPS the mind (a support that reduces memory load). Extended: the calendar is PART OF the mind (a constituent of the person's memory system, if it is reliably available, trusted, and used). Adams & Aizawa's coupling-constitution fallacy: being causally coupled to something doesn't make it part of you, just as a bowling ball's spin doesn't extend into the lane. Clark replies that only tight, reliable, reciprocal loops count.",
    "type": "compare",
    "source_page": "wiki/concept-4e-cognition.md",
    "topic": "embedded-vs-extended",
    "cluster": "embodiment-ecology",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-scaffold-apply-01",
    "prompt": "A widowed client, 78, moved into her daughter's house after her husband's death. She is disoriented, forgetful, and can't settle, even though 'everything is taken care of.' Use the idea of affective scaffolding to reframe what she has lost.",
    "answer": "Beyond her husband, she has lost the scaffolds that were holding up her memory, mood regulation, and identity: her home's layout, routines, objects, neighbors, and the shared habits of the marriage (Colombetti & Krueger: affect is supported by material culture, other people, and their interplay). If those scaffolds partly constituted how she functioned, the disorientation is intelligible as a loss of self-supporting structure, not just grief or decline. Work includes grief support plus deliberately rebuilding scaffolds (familiar objects, routines, relationships) while screening appropriately for depression and cognitive change.",
    "type": "vignette",
    "source_page": "wiki/concept-4e-cognition.md",
    "topic": "affective-scaffolding",
    "cluster": "embodiment-ecology",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-4e-evaluate-01",
    "prompt": "A workshop flyer advertises '4E Therapy: the evidence-based treatment that proves your environment is your mind.' Evaluate it.",
    "answer": "It over-claims on two counts. (1) The extended-mind (constitution) thesis is a live, disputed philosophical claim, not a proven finding; embedded and embodied claims are much better accepted. (2) Clinical applications of 4E are mostly conceptual; there is no established evidence-based '4E therapy'. The ideas are useful lenses (re-scaffolding, environmental intervention, a justice lens) but shouldn't be marketed as proven treatment.",
    "type": "explain",
    "source_page": "wiki/concept-4e-cognition.md",
    "topic": "4e-limits",
    "cluster": "embodiment-ecology",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-lewin-cloze-01",
    "prompt": "Lewin's heuristic equation states that behavior is a function of the person and the environment: B = {{f(P, E)}}.",
    "answer": "f(P, E)",
    "type": "cloze",
    "source_page": "wiki/concept-lewin-field-theory.md",
    "topic": "lewin-equation",
    "cluster": "embodiment-ecology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-lifespace-understand-01",
    "prompt": "What is Lewin's 'life space,' and why is a locked door the person doesn't know about NOT in it?",
    "answer": "The totality of psychological facts (needs, goals, perceived barriers and paths, others as they matter) that determine behavior at a given moment: person plus psychological environment. The environment that counts is the environment as perceived and as it matters now. An unknown locked door plays no role in the person's field, while an imagined rejection that will never happen does.",
    "type": "explain",
    "source_page": "wiki/concept-lewin-field-theory.md",
    "topic": "life-space",
    "cluster": "embodiment-ecology",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-lewin-lineage-recall-01",
    "prompt": "Trace two lines of influence from Lewin's field theory into counseling.",
    "answer": "Any two: (1) Bronfenbrenner recast B = f(P, E) as development = f(P, E) and elaborated E into nested micro/meso/exo/macro systems, the root of counseling's socioecological models (e.g., MSJCC advocacy levels). (2) Group dynamics: Lewin/Lippitt/White leadership styles, T-groups, here-and-now group focus. (3) Gestalt therapy's 'field' language and person-in-environment. (4) Force-field analysis (a simplified descendant).",
    "type": "recall",
    "source_page": "wiki/concept-lewin-field-theory.md",
    "topic": "lewin-lineage",
    "cluster": "embodiment-ecology",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-envpart-compare-01",
    "prompt": "'Your environment is part of you.' Give the distinct sense in which each says yes: Heidegger, Lewin, Clark & Chalmers, Colombetti & Krueger.",
    "answer": "Heidegger: ontologically. Person and world are one phenomenon (being-in-the-world); there's no self first and world second. Lewin: explanatorily. Behavior is a function of person and psychological environment together (the life space), so neither alone predicts it. Clark & Chalmers: cognitively. Parts of the environment can literally be constituents of cognitive processes (Otto's notebook). Colombetti & Krueger: affectively. Emotions and moods are scaffolded and regulated by things, people, and their interplay.",
    "type": "compare",
    "source_page": "wiki/aux-phenomenology.md",
    "topic": "environment-as-self",
    "cluster": "embodiment-ecology",
    "bloom_level": "analyze"
  }
]
```

## Cluster: daseinsanalysis (Binswanger, Boss, Ellen West)

```json
[
  {
    "id": "ax-phe-worlds-recall-01",
    "prompt": "Name and define Binswanger's three 'worlds.'",
    "answer": "Umwelt ('around-world'): the natural/physical environment, including body, biology, needs, and surroundings. Mitwelt ('with-world'): the world of relationships with others. Eigenwelt ('own-world'): one's relationship to oneself, self-awareness and self-relatedness. They are three aspects of one being-in-the-world, always co-present, not three separate places.",
    "type": "recall",
    "source_page": "wiki/theory-daseinsanalysis.md",
    "topic": "three-worlds",
    "cluster": "daseinsanalysis",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-worlds-mcq-01",
    "prompt": "A client experiences other people only as critics waiting to catch her out; her relationship with her body and her solitude feel comparatively intact. Which of Binswanger's worlds is most constricted?",
    "options": [
      "Mitwelt",
      "Umwelt",
      "Eigenwelt",
      "Lebenswelt"
    ],
    "correct": "Mitwelt",
    "answer": "Mitwelt, the with-world of relationships with others. Umwelt = physical/bodily surroundings; Eigenwelt = relation to self; Lebenswelt is Husserl's lifeworld, not one of Binswanger's three.",
    "type": "mcq",
    "source_page": "wiki/theory-daseinsanalysis.md",
    "topic": "three-worlds",
    "cluster": "daseinsanalysis",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-worlds-apply-01",
    "prompt": "Map a client onto the three worlds: a 45-year-old man with chronic pain, estranged from his adult children, who says 'I don't even know who I am if I can't work.'",
    "answer": "Umwelt: the body as an enemy (chronic pain), and possibly a shrunken physical world if pain limits movement. Mitwelt: estrangement from his children, and likely lost work relationships. Eigenwelt: identity collapse ('I don't know who I am'); self-relation was carried by the worker role. All three are constricted and interlocked: the pain-limited body cost the work that held his identity, which strains relations. Daseinsanalysis would explore how his world-design has narrowed, not rank one 'cause'.",
    "type": "vignette",
    "source_page": "wiki/theory-daseinsanalysis.md",
    "topic": "three-worlds",
    "cluster": "daseinsanalysis",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-binswanger-boss-compare-01",
    "prompt": "Binswanger vs. Boss: give three differences between the two founders of Daseinsanalysis.",
    "answer": "Any three: (1) Binswanger was a psychiatric anthropologist with long case studies (Ellen West) and world-design; Boss built Daseinsanalysis as a therapy. (2) Heidegger rejected Binswanger's reading as conflating the ontological with everyday psychology; Boss worked with Heidegger directly and hosted the Zollikon Seminars (1959-1969). (3) Binswanger's signature is Umwelt/Mitwelt/Eigenwelt; Boss's is phenomenological dream work and the existentials. (4) After the 1957 split Binswanger turned back to Husserl; Boss's lineage became today's Zurich school.",
    "type": "compare",
    "source_page": "wiki/person-binswanger-boss.md",
    "topic": "binswanger-vs-boss",
    "cluster": "daseinsanalysis",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-zollikon-cloze-01",
    "prompt": "From 1959 to 1969 Heidegger taught psychiatrists at Medard Boss's home in the {{Zollikon}} Seminars.",
    "answer": "Zollikon",
    "type": "cloze",
    "source_page": "wiki/theory-daseinsanalysis.md",
    "topic": "zollikon",
    "cluster": "daseinsanalysis",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-boss-dreams-compare-01",
    "prompt": "A client dreams of being locked in a glass room while friends talk outside without noticing her. Contrast a classical Freudian approach to this dream with Boss's daseinsanalytic approach.",
    "answer": "Freudian: the manifest content is a disguise; decode the latent wish or conflict behind it via symbolism and associations. Boss: take the dream as it shows itself, as a way she exists in that moment: visible yet cut off, present yet unable to reach or be reached. Then ask whether and how that mode of being is also true of her waking life. No hidden mechanism is posited. (Critique: Gendlin argued Boss imports Heideggerian concepts in place of Freudian ones.)",
    "type": "compare",
    "source_page": "wiki/theory-daseinsanalysis.md",
    "topic": "dreams",
    "cluster": "daseinsanalysis",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-dasein-stuck-recall-01",
    "prompt": "In Daseinsanalysis, how is a person 'stuck,' and how do they get better?",
    "answer": "Stuck: their way of being-in-the-world has narrowed or rigidified. Only a few possibilities still show up as open, and surroundings, relationships, and self are all lived through one constricted world-design. Better by: therapist and patient carefully seeing together how that world is structured, without reducing it to hidden causes, so that more of the patient's own possibilities can open up.",
    "type": "recall",
    "source_page": "wiki/theory-daseinsanalysis.md",
    "topic": "stuck-better",
    "cluster": "daseinsanalysis",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-dasein-evidence-evaluate-01",
    "prompt": "A clinic wants to list Daseinsanalysis as an 'evidence-based treatment for depression' on its website. Evaluate.",
    "answer": "Not supportable. There is little controlled outcome research on Daseinsanalysis specifically, and the existential therapies as a group have a modest, uneven evidence base. It is better described as a phenomenological lens or orientation. The clinic could honestly say it offers existential-phenomenological therapy and separately list evidence-based treatments (e.g., BA, CBT) where it provides them.",
    "type": "explain",
    "source_page": "wiki/theory-daseinsanalysis.md",
    "topic": "evidence",
    "cluster": "daseinsanalysis",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-ew-recall-01",
    "prompt": "Summarize the basic facts of the Ellen West case: setting, diagnosis given, the discharge decision, and the outcome.",
    "answer": "Treated at Binswanger's Bellevue sanatorium in Kreuzlingen, January-March 1921, after two prior psychoanalyses. Binswanger diagnosed schizophrenia, with Bleuler concurring and Hoche also consulted. The consultants judged no treatment promising, suspended therapy, and discharged her home with her husband's consent despite her explicit suicidal intentions. She died by poison three days later. Binswanger published the case in 1944-45; its English translation appeared in May, Angel & Ellenberger's Existence (1958).",
    "type": "recall",
    "source_page": "wiki/study-ellen-west.md",
    "topic": "ellen-west-facts",
    "cluster": "daseinsanalysis",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-ew-worlds-understand-01",
    "prompt": "How did Binswanger interpret Ellen West's existence, and what was his most controversial claim?",
    "answer": "Her world-design was split between a light, airy 'ethereal world' of spirit and thinness she longed for, and a dark, heavy 'tomb-world' of body, earth, and appetite she felt trapped in. Eating became a daily confrontation with that split, and her world constricted until death seemed the only way out. Most controversially, he framed her suicide as the moment her existence finally became authentically her own.",
    "type": "explain",
    "source_page": "wiki/study-ellen-west.md",
    "topic": "ellen-west-interpretation",
    "cluster": "daseinsanalysis",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-ew-critique-analyze-01",
    "prompt": "List four major critiques of how Ellen West was diagnosed, treated, and written up.",
    "answer": "(1) Misdiagnosis: the documented presentation fits anorexia nervosa, binge-eating/purging type, far better than schizophrenia (Hirschmüller's archival edition). (2) A foreseeable suicide: a patient with an announced plan was discharged, and the archive suggests the outcome was effectively arranged. Hoche, a public 'euthanasia' advocate, was among the consultants. (3) Romanticizing death as authentic self-realization. (4) Rogers: she was treated as an object by a series of experts and never met in a real relationship ('Ellen West, and loneliness'). Also: Akavia shows how the published case constructs its subject.",
    "type": "explain",
    "source_page": "wiki/study-ellen-west.md",
    "topic": "ellen-west-critique",
    "cluster": "daseinsanalysis",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-ew-stance-evaluate-01",
    "prompt": "A client with a severe eating disorder says death feels like 'finally being free.' Drawing on the Ellen West case, what is the right stance, and what is the trap?",
    "answer": "Right stance: take seriously and explore what death MEANS to her (freedom, escape, relief) with genuine phenomenological curiosity and relationship, AND act fully on safety: suicide risk assessment, safety planning, medical monitoring, and specialist eating-disorder referral. Understanding a wish to die is not endorsing it. The trap, Binswanger's, is letting an elegant existential interpretation or a pessimistic 'incurable' label turn into therapeutic nihilism that frames death as authentic fulfillment.",
    "type": "vignette",
    "source_page": "wiki/study-ellen-west.md",
    "topic": "ellen-west-stance",
    "cluster": "daseinsanalysis",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: phen-psychopathology (Jaspers, lived time, self-disorder, depression)

```json
[
  {
    "id": "ax-phe-jaspers-cloze-01",
    "prompt": "Jaspers distinguished understanding meaningful connections from the inside ({{Verstehen}}) from identifying causes from the outside (Erklären).",
    "answer": "Verstehen",
    "type": "cloze",
    "source_page": "wiki/concept-understanding-vs-explanation.md",
    "topic": "verstehen-erklaren",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-jaspers-levels-recall-01",
    "prompt": "Name and define Jaspers' three levels: static understanding, genetic understanding, causal explanation.",
    "answer": "Static understanding (his 'phenomenology'): precise description of WHAT the patient experiences, from their own account and the clinician's empathic re-presentation, before any connection-making. Genetic understanding: HOW one experience meaningfully follows from another (betrayed, so furious). Causal explanation: what CAUSES it, via natural-science regularities and mechanisms, used where meaningful connection runs out.",
    "type": "recall",
    "source_page": "wiki/concept-understanding-vs-explanation.md",
    "topic": "jaspers-levels",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-verstehen-mcq-01",
    "prompt": "Which statement is an EXPLANATION (Erklären) claim rather than an UNDERSTANDING (Verstehen) claim?",
    "options": [
      "Her irritability and weight loss follow from an overactive thyroid.",
      "His rage at home makes sense given the humiliation he suffers at work.",
      "Her withdrawal follows from feeling she let her family down.",
      "His hopelessness grew as each job application was rejected."
    ],
    "correct": "Her irritability and weight loss follow from an overactive thyroid.",
    "answer": "The thyroid statement is causal-mechanistic (explanation). The others trace meaningful, motive-based connections from the inside (genetic understanding). A good formulation uses both and labels which is which.",
    "type": "mcq",
    "source_page": "wiki/concept-understanding-vs-explanation.md",
    "topic": "verstehen-erklaren",
    "cluster": "phen-psychopathology",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-verstehen-evaluate-01",
    "prompt": "A counselor builds a compelling narrative linking a 58-year-old client's new-onset confusion and personality change to unresolved grief, and plans grief work. Evaluate using Jaspers' distinction.",
    "answer": "Risky. An understandable story can be told about almost anything, and its existence does not rule out a causal explanation that needs a physician. New-onset confusion and personality change in midlife raise medical/neurological possibilities (delirium, dementia, tumor, substances, endocrine). The counselor should refer for medical evaluation within scope of practice while continuing supportive work. Understanding and explanation are complementary, and mistaking one for the other is the classic error.",
    "type": "vignette",
    "source_page": "wiki/concept-understanding-vs-explanation.md",
    "topic": "verstehen-erklaren",
    "cluster": "phen-psychopathology",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-formcontent-apply-01",
    "prompt": "A client insists neighbors are broadcasting his thoughts through the Wi-Fi. Using Jaspers' form/content distinction, what should your assessment focus on, and what should you avoid?",
    "answer": "Focus on FORM: how the experience is lived. Is it a delusion or an overvalued idea, sudden certainty or gradual suspicion, thought broadcasting as a passivity experience, preceded by uncanny delusional mood? Form matters most for psychopathological classification. Avoid getting pulled into arguing about the CONTENT (whether Wi-Fi could do this). Content is shaped by biography and culture, and debating it damages rapport without clarifying the clinical picture.",
    "type": "vignette",
    "source_page": "wiki/theory-phenomenological-psychopathology.md",
    "topic": "form-content",
    "cluster": "phen-psychopathology",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-primary-delusion-explain-01",
    "prompt": "What is a primary delusion for Jaspers, what makes it 'un-understandable,' and what is the main criticism of that criterion?",
    "answer": "A delusion that cannot be meaningfully derived from prior mood, experiences, or beliefs: it arrives as an immediate, perception-like 'awareness of meaning' (delusional perception: 'the light turned red and I knew I was chosen'). It is un-understandable because genetic understanding finds no meaningful connection, so Jaspers switched to causal explanation. Criticism: 'un-understandable' may reflect the clinician's limits, and it risks placing psychotic people beyond empathy. The modern tradition keeps the description and rejects the closure.",
    "type": "explain",
    "source_page": "wiki/concept-understanding-vs-explanation.md",
    "topic": "primary-delusion",
    "cluster": "phen-psychopathology",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-delusional-mood-understand-01",
    "prompt": "How has Jaspers' 'delusional mood' been linked to contemporary neuroscience of psychosis onset?",
    "answer": "Delusional mood, the uncanny sense that everything has become significant before any specific delusion forms, has been linked to the aberrant-salience account (dysregulated dopamine assigning significance to neutral stimuli), e.g., Mishara & Fusar-Poli (2013). It is an example of phenomenological description and neurobiology informing each other rather than competing.",
    "type": "explain",
    "source_page": "wiki/theory-phenomenological-psychopathology.md",
    "topic": "delusional-mood",
    "cluster": "phen-psychopathology",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-timephases-cloze-01",
    "prompt": "Husserl's three phases of time-consciousness are retention, primal impression, and {{protention}}.",
    "answer": "protention",
    "type": "cloze",
    "source_page": "wiki/concept-lived-time.md",
    "topic": "time-consciousness",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-retention-memory-compare-01",
    "prompt": "Distinguish retention from memory, and protention from planning.",
    "answer": "Retention: the just-elapsed still held within the present moment, automatic and pre-reflective (why you hear a melody, not isolated notes). Memory/recollection: a separate, deliberate act that re-presents a past that is no longer held. Protention: the automatic, implicit anticipation of the just-about-to-come (why a wrong note jars). Planning/expectation: a deliberate act that re-presents a future. Retention and protention are built into every now.",
    "type": "compare",
    "source_page": "wiki/concept-lived-time.md",
    "topic": "retention-vs-memory",
    "cluster": "phen-psychopathology",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-minkowski-recall-01",
    "prompt": "What did Eugène Minkowski propose was the core ('generative disorder') of schizophrenia, and on what influences did he draw?",
    "answer": "A 'loss of vital contact with reality': a change in the temporo-spatial structure of experience, from dynamic, time-flowing engagement toward rigid, static, spatial forms (e.g., 'morbid rationalism'). He drew on Bergson's vitalism and on the phenomenologists Husserl and Scheler, and characterized many disorders as distortions of lived time and space.",
    "type": "recall",
    "source_page": "wiki/concept-lived-time.md",
    "topic": "minkowski",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-closedfuture-apply-01",
    "prompt": "A client says, 'There's no future. It's not that it's bad, it's just not there. Time has stopped.' Give a phenomenologically informed response AND the non-negotiable clinical action.",
    "answer": "Response: meet the experience before contesting it. Reflect that time feels stopped and the future blank, and explore what that is like, rather than arguing 'things will get better', which addresses a belief when the problem is a changed structure of experience. Non-negotiable: a lost lived future is close to hopelessness, a well-established correlate of suicidal thinking, so conduct a standard suicide risk assessment now. Phenomenological description is not itself a risk instrument.",
    "type": "vignette",
    "source_page": "wiki/concept-lived-time.md",
    "topic": "closed-future",
    "cluster": "phen-psychopathology",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-ipseity-cloze-01",
    "prompt": "Sass and Parnas (2003) proposed that schizophrenia is fundamentally a disturbance of {{ipseity}}, the basic, pre-reflective sense of being a self.",
    "answer": "ipseity",
    "type": "cloze",
    "source_page": "wiki/study-ipseity-disturbance.md",
    "topic": "ipseity",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-ipseity-compare-01",
    "prompt": "Contrast hyperreflexivity with diminished self-affection, with a first-person example of each. What third component did the 2025 update add?",
    "answer": "Hyperreflexivity: exaggerated self-consciousness in which normally tacit processes (sensations, thoughts, perceiving) become objects of explicit, alienated attention ('I have to watch myself think'). Diminished self-affection: a weakened sense of existing as the subject of one's experience ('I'm not really here'; 'my thoughts feel anonymous'). The 2025 update adds a disturbed grip or hold on the world: unstable immersion and loss of the implicit sense of what is relevant and obvious.",
    "type": "compare",
    "source_page": "wiki/study-ipseity-disturbance.md",
    "topic": "ipseity-components",
    "cluster": "phen-psychopathology",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-ease-recall-01",
    "prompt": "What is the EASE, and what three kinds of evidence do its proponents cite for self-disorders?",
    "answer": "The Examination of Anomalous Self-Experience (Parnas et al., 2005): a semi-structured, phenomenologically oriented interview rating self-disorders that standard symptom interviews miss. Evidence: (1) specificity, as self-disorders hyper-aggregate in the schizophrenia spectrum (including subclinical) and not in other disorders; (2) temporal priority and stability, as they precede diagnosable psychosis and persist; (3) prediction, as they predict transition to psychosis in help-seeking youth. Caveat: summarized by the model's proponents.",
    "type": "recall",
    "source_page": "wiki/study-ipseity-disturbance.md",
    "topic": "ease",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-selfdisorder-apply-01",
    "prompt": "A 19-year-old college student tells a campus counselor: 'I feel like I'm watching myself from behind my eyes. My thoughts don't feel like mine exactly. Everyone else just gets what's obvious and I have to work it all out.' No hallucinations or delusions. What should the counselor do?",
    "answer": "Take it seriously. These resemble self-disorders (diminished self-affection, hyperreflexivity, loss of natural self-evidence), which can precede psychosis. Describe the experiences carefully in the student's own words without diagnosing or dismissing them as 'just anxiety' or 'normal stress'. Refer for specialist early-psychosis assessment, especially if they persist or cluster. In session, favor grounding and concrete here-and-now contact over relentless introspective questioning, which may feed hyperreflexivity. Screen for risk and functioning as usual.",
    "type": "vignette",
    "source_page": "wiki/study-ipseity-disturbance.md",
    "topic": "self-disorder-response",
    "cluster": "phen-psychopathology",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-ipseity-evaluate-01",
    "prompt": "Evaluate the claim: 'Self-disorders are now an established diagnostic criterion for schizophrenia.'",
    "answer": "False. DSM-5-TR schizophrenia is defined by the five symptom domains and duration criteria. The ipseity model is a proposal about the experiential core beneath those criteria. Its evidence (specificity, temporal priority, prediction) is encouraging but mainly summarized by its proponents, and open challenges remain: specificity, independence from interpersonal and contextual factors, and neural correlates. It is best described as a promising, well-researched construct, not a criterion.",
    "type": "explain",
    "source_page": "wiki/study-ipseity-disturbance.md",
    "topic": "ipseity-status",
    "cluster": "phen-psychopathology",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-blankenburg-recall-01",
    "prompt": "What did Blankenburg's patient Anne Rau say she had lost, and how did Blankenburg interpret it?",
    "answer": "'Natural self-evidence': the taken-for-granted, unspoken grasp of the obvious that lets everyone else move through ordinary life without effort. Blankenburg read her schizophrenia simplex as a disturbance of common sense in the deep sense, the shared, lifeworld background of obviousness, which is intersubjective at root. (Tatossian offered a more intrasubjective reading.)",
    "type": "recall",
    "source_page": "wiki/theory-phenomenological-psychopathology.md",
    "topic": "blankenburg",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-corporealization-compare-01",
    "prompt": "Contrast Fuchs's 'corporealization' in melancholic depression with 'disembodiment' in schizophrenia.",
    "answer": "Corporealization (depression): the lived body loses its transparency and becomes too much a thing, heavy, opaque, resistant, an obstacle to engagement (leaden fatigue, psychomotor retardation, feeling imprisoned in the body). Disembodiment (schizophrenia): the self becomes detached from the bodily processes that normally carry it, so experience feels unreal, mechanical, 'not here' (linked to diminished self-affection).",
    "type": "compare",
    "source_page": "wiki/concept-phenomenology-of-depression.md",
    "topic": "corporealization-vs-disembodiment",
    "cluster": "phen-psychopathology",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-dep-dimensions-recall-01",
    "prompt": "Name the four dimensions of the phenomenological model of depression (Frohn & Martiny, 2023), with the key concept in each.",
    "answer": "Body: corporealization, the body turned opaque and heavy (Fuchs). Time: desynchronization and the closed future, slowed or stalled lived time (Fuchs; Minkowski, Straus, von Gebsattel). Possibility: existential feeling, the space of possibilities collapsing and a flattened field of affordances (Ratcliffe). Others: detunement, cut off from shared life and hypersensitive to obligation.",
    "type": "recall",
    "source_page": "wiki/concept-phenomenology-of-depression.md",
    "topic": "depression-dimensions",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-ratcliffe-hope-understand-01",
    "prompt": "What distinction does Ratcliffe draw about hope in severe depression, and why does it matter for how you respond to hopelessness?",
    "answer": "It's not merely that the depressed person lacks particular hopes. They have lost the capacity to experience anything as hopeable, because the world no longer offers significant possibilities (a change in existential feeling). So reassurance ('look at the good things ahead') addresses the wrong level: it offers contents to hope for when the structure that makes hoping possible is altered. Validate the experience first; action-based approaches may reopen possibility from the outside in.",
    "type": "explain",
    "source_page": "wiki/concept-phenomenology-of-depression.md",
    "topic": "ratcliffe-hope",
    "cluster": "phen-psychopathology",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-typus-recall-01",
    "prompt": "What is Tellenbach's 'typus melancholicus,' and what triggers collapse in this type?",
    "answer": "A pre-depressive personality type: orderly, over-conscientious, hyper-identified with social roles and norms. When a role destabilizes (retirement, a move, a failure, a loss), their world 'literally collapses' into melancholia. It is historically influential; treat it as a clinical type, not a validated risk scale.",
    "type": "recall",
    "source_page": "wiki/concept-phenomenology-of-depression.md",
    "topic": "typus-melancholicus",
    "cluster": "phen-psychopathology",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-dep-limits-evaluate-01",
    "prompt": "What is the 'patho-description' problem, and what other limitations should temper confidence in the phenomenological model of depression?",
    "answer": "Patho-description: depression distorts the very capacities (memory, language, reflection) used to describe it, so first-person reports are an imperfect window. Other limits: heavy reliance on autobiographical and literary accounts rather than systematic sampling; the fit is best for severe or melancholic depression, not everyone meeting MDD criteria; and core concepts are disputed (existential feeling vs. de-situatedness, per Fernandez). It is illuminating description, not validated measurement.",
    "type": "explain",
    "source_page": "wiki/concept-phenomenology-of-depression.md",
    "topic": "depression-limits",
    "cluster": "phen-psychopathology",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-psychopath-mcq-01",
    "prompt": "Which figure is correctly matched with their core idea?",
    "options": [
      "Blankenburg: loss of natural self-evidence",
      "Minkowski: ipseity disturbance and the EASE",
      "Fuchs: typus melancholicus",
      "Tellenbach: loss of vital contact with reality"
    ],
    "correct": "Blankenburg: loss of natural self-evidence",
    "answer": "Correct pairings: Blankenburg = loss of natural self-evidence (Anne Rau); Minkowski = loss of vital contact with reality; Sass & Parnas = ipseity disturbance and the EASE; Tellenbach = typus melancholicus; Fuchs = corporealization and disembodiment.",
    "type": "mcq",
    "source_page": "wiki/theory-phenomenological-psychopathology.md",
    "topic": "lineage",
    "cluster": "phen-psychopathology",
    "bloom_level": "analyze"
  }
]
```

## Cluster: phen-stance (the stance in the room, and empathy)

```json
[
  {
    "id": "ax-phe-spinelli-recall-01",
    "prompt": "Name and define Spinelli's three rules of the phenomenological method in therapy.",
    "answer": "(1) Rule of epoché: set aside, as far as possible, initial biases, theories, and expectations so what the client presents can show itself on its own terms. (2) Rule of description: describe rather than explain; stay with what and how the client experiences before why. (3) Rule of horizontalization: treat every item of description as initially of equal significance; don't rank what the client says by your theory of importance.",
    "type": "recall",
    "source_page": "wiki/concept-phenomenological-stance.md",
    "topic": "spinelli-rules",
    "cluster": "phen-stance",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-horizontal-apply-01",
    "prompt": "Late in a session about work stress, a client says, 'Anyway, my sister moved to Australia last month, but that's not really important.' Which rule applies, and what do you do?",
    "answer": "Horizontalization: give the throwaway remark the same careful attention as the 'main' problem rather than ranking it low because the client (or your theory) did. For example: 'You mentioned your sister moving to Australia. I'd like to hear a bit about that.' Often the offhand detail turns out to be central.",
    "type": "vignette",
    "source_page": "wiki/concept-phenomenological-stance.md",
    "topic": "horizontalization",
    "cluster": "phen-stance",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-describe-apply-01",
    "prompt": "Rewrite this counselor response to follow the rule of description: 'Why do you think you have panic attacks in the grocery store? Could it be connected to your mother's illness?'",
    "answer": "Example: 'Take me through the last time it happened in the grocery store. What did you notice first? Where in your body? What happened next?' This shifts from why and interpretation (a premature explanation that may be the counselor's, not the client's) to what and how: detailed, first-person description before any explanation.",
    "type": "vignette",
    "source_page": "wiki/concept-phenomenological-stance.md",
    "topic": "description",
    "cluster": "phen-stance",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-epoche-apply-01",
    "prompt": "Ten minutes into an intake, the thought 'textbook avoidant attachment' fires in your head. What does the rule of epoché ask you to do with it, and what does it NOT ask?",
    "answer": "Notice the label and hold it lightly, as a hypothesis in brackets, while you keep listening to how this client describes their experience in their own terms; check later whether it survived. It does NOT ask you to have no clinical judgment or to suppress knowledge. The stance governs the order (understand first) and the grip (hold explanations loosely), not whether you think.",
    "type": "vignette",
    "source_page": "wiki/concept-phenomenological-stance.md",
    "topic": "epoche-clinical",
    "cluster": "phen-stance",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-stance-schools-compare-01",
    "prompt": "Show how the same phenomenological stance appears in person-centered, Gestalt, and existential therapy, and in Jaspers' psychiatric assessment.",
    "answer": "Person-centered: Rogers called his theory 'basically phenomenological'; understand the client from their internal frame of reference and phenomenal field. Gestalt: the phenomenological method of awareness, what and how over why, here-and-now, dialogic inclusion without judging or interpreting (Yontef). Existential: Spinelli's three rules (epoché, description, horizontalization), with the therapist as fellow explorer. Jaspers: static understanding, precise description of the patient's experience in their own terms before explanation.",
    "type": "compare",
    "source_page": "wiki/concept-phenomenological-stance.md",
    "topic": "stance-across-schools",
    "cluster": "phen-stance",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-gestalt-cloze-01",
    "prompt": "Gestalt therapy's phenomenological method favors exploring 'what' and '{{how}}' over 'why.'",
    "answer": "how",
    "type": "cloze",
    "source_page": "wiki/concept-phenomenological-stance.md",
    "topic": "gestalt",
    "cluster": "phen-stance",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-bracket-limits-evaluate-01",
    "prompt": "A trainee says: 'I practice total bracketing. I come in with no assumptions at all, so I don't do risk screens until the client brings it up.' Evaluate.",
    "answer": "Two errors. (1) Complete bracketing is impossible: Heidegger and the hermeneutic tradition, and even Merleau-Ponty, hold that understanding runs through prior understanding. The realistic aim is reflexivity or 'bridling': noticing and holding assumptions lightly. (2) Bracketing is not the absence of clinical judgment, and risk assessment is never bracketed. Waiting for the client to raise suicide risk is unsafe. The stance governs order and grip, not whether you assess.",
    "type": "explain",
    "source_page": "wiki/concept-phenomenological-stance.md",
    "topic": "bracketing-limits",
    "cluster": "phen-stance",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-explain-reflex-analyze-01",
    "prompt": "Why does the wiki call the 'explain-it reflex' the same as the 'fix-it reflex,' and what does premature explanation do to a client?",
    "answer": "Both manage the helper's own discomfort with not knowing: jumping to a label or explanation closes the uncertainty, just as jumping to advice closes the helplessness. Premature explanation teaches the client that their details don't matter (their experience gets slotted into your theory), so they stop offering them. It also skips description, which is often itself relieving and produces better data for later formulation.",
    "type": "explain",
    "source_page": "wiki/concept-phenomenological-stance.md",
    "topic": "explain-reflex",
    "cluster": "phen-stance",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-empathy-phen-explain-01",
    "prompt": "What is empathy on the phenomenological account (Husserl, Stein, Zahavi)?",
    "answer": "A direct, perception-like experience of another person's experience, given through their embodied expression, and given as THEIRS, with its otherness intact (asymmetrically: I never live it as I live mine). Stein called it sui generis. Zahavi stresses it does not require simulating or sharing the feeling.",
    "type": "explain",
    "source_page": "wiki/concept-phenomenology-of-empathy.md",
    "topic": "empathy-phenomenological",
    "cluster": "phen-stance",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-empathy-types-compare-01",
    "prompt": "Distinguish empathy, emotional contagion, sympathy, and simulation (perspective-taking): whose feeling is it in each, and what's the counseling risk of each non-empathy form?",
    "answer": "Empathy: I grasp YOUR experience as yours; the target. Contagion: I catch your feeling and it becomes mine, often without knowing its source; risk of burnout and enmeshment (vicarious trauma). Sympathy: I feel FOR you (concern, pity), a feeling of mine about you; risk of centering the helper. Simulation: I imagine what I'd feel in your position, an imagined version of me; risk of projecting my reaction onto you.",
    "type": "compare",
    "source_page": "wiki/concept-phenomenology-of-empathy.md",
    "topic": "empathy-vs-contagion",
    "cluster": "phen-stance",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-empathy-mcq-01",
    "prompt": "After sessions with an enraged client, a counselor notices she feels calm but clearly grasps how furious and humiliated he feels. By the phenomenological account, this is:",
    "options": [
      "Empathy: grasping his experience as his without sharing it",
      "A failure of empathy, because she doesn't feel the anger herself",
      "Emotional contagion",
      "Sympathy"
    ],
    "correct": "Empathy: grasping his experience as his without sharing it",
    "answer": "Zahavi: seeing someone's anger may make me afraid, or leave me calm, and yet I grasp their anger perfectly well. Empathy doesn't require matching the feeling, and not matching is what keeps it useful and sustainable. Contagion would be catching his rage; sympathy would be feeling sorry for him.",
    "type": "mcq",
    "source_page": "wiki/concept-phenomenology-of-empathy.md",
    "topic": "empathy-without-matching",
    "cluster": "phen-stance",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-asif-analyze-01",
    "prompt": "How does Rogers' 'as if' clause line up with the phenomenological account of empathy, and what caution do Stein and Zahavi add to 'putting yourself in their shoes'?",
    "answer": "Rogers: sense the client's world as if it were your own without losing the 'as if'. That does the same work as Husserl's and Stein's insistence that the other's experience is given as other: no merging. The caution: if 'putting yourself in their shoes' means imagining what YOU would feel, you may be simulating yourself rather than perceiving them. They push toward attending to the other as they actually express themselves, which is what accurate reflection needs. (Interpretive bridge; neither literature cites the other.)",
    "type": "explain",
    "source_page": "wiki/concept-phenomenology-of-empathy.md",
    "topic": "as-if",
    "cluster": "phen-stance",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-contagion-apply-01",
    "prompt": "A trainee says proudly, 'I'm so empathic that I go home feeling everything my clients feel.' Respond as a supervisor using the phenomenology of empathy.",
    "answer": "What's described sounds more like emotional contagion than empathy: taking the client's feelings on as your own, often without distinguishing whose they are. Empathy grasps the client's experience as theirs, with the 'as if' intact. Contagion isn't deeper empathy; it's a self-care and boundary signal and a risk path toward vicarious trauma and burnout. Explore self-care, supervision, and ways to stay attuned without merging.",
    "type": "vignette",
    "source_page": "wiki/concept-phenomenology-of-empathy.md",
    "topic": "contagion",
    "cluster": "phen-stance",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-ew-relationship-evaluate-01",
    "prompt": "The Ellen West case contains one of the most detailed phenomenological descriptions of a patient ever written. Why is that not the same as a phenomenological stance of care, and whose critique makes the point?",
    "answer": "Because describing someone's world is not meeting them in it. Binswanger's analysis was brilliant but was conducted about her, with her treated as an object of diagnosis by a series of experts; no one entered her experience in a real relationship. Carl Rogers made this critique ('Ellen West, and loneliness'): she died of loneliness as much as illness, and a relationship offering the core conditions might have mattered. Description without relationship can become detachment.",
    "type": "explain",
    "source_page": "wiki/study-ellen-west.md",
    "topic": "description-vs-relationship",
    "cluster": "phen-stance",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: phen-research (qualitative methods)

```json
[
  {
    "id": "ax-phe-research-split-compare-01",
    "prompt": "Contrast descriptive and interpretive (hermeneutic) phenomenological research on aim, bracketing, output, and example methods.",
    "answer": "Descriptive (Husserl-inspired): aims at the essential structure of an experience; the researcher brackets prior assumptions; outputs a general structure or essence; methods are Giorgi and Moustakas. Interpretive (Heidegger/Gadamer-inspired): aims to interpret meaning in context; full bracketing is impossible, so pre-understanding is made explicit and used reflexively; outputs an interpretive account, a 'fusion of horizons'; methods are van Manen and IPA.",
    "type": "compare",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "descriptive-vs-interpretive",
    "cluster": "phen-research",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-giorgi-recall-01",
    "prompt": "List the steps of Giorgi's descriptive phenomenological psychological method.",
    "answer": "(1) Adopt the phenomenological attitude (a scientific epoché). (2) Read the whole description for a sense of the whole. (3) Divide it into meaning units. (4) Transform each unit into psychologically sensitive language that makes its lived meaning explicit. (5) Use imaginative variation to synthesize a general psychological structure of the experience.",
    "type": "recall",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "giorgi",
    "cluster": "phen-research",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-moustakas-recall-01",
    "prompt": "Outline Moustakas's transcendental phenomenology analysis sequence, the version most counseling dissertations follow.",
    "answer": "Epoché (the researcher writes out and sets aside their own experience of the phenomenon) → horizontalization (list every significant statement as equally weighted) → clusters of meaning (themes) → textural description (WHAT participants experienced) → structural description (HOW: context and conditions) → a composite essence. It is popularized in counseling via Creswell & Poth.",
    "type": "recall",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "moustakas",
    "cluster": "phen-research",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-textural-structural-cloze-01",
    "prompt": "In Moustakas's method, the {{textural}} description captures WHAT participants experienced, and the structural description captures HOW they experienced it.",
    "answer": "textural",
    "type": "cloze",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "moustakas",
    "cluster": "phen-research",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-double-hermeneutic-cloze-01",
    "prompt": "IPA's '{{double hermeneutic}}': the researcher is trying to make sense of the participant trying to make sense of their experience.",
    "answer": "double hermeneutic",
    "type": "cloze",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "ipa",
    "cluster": "phen-research",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-ipa-recall-01",
    "prompt": "Name IPA's three theoretical touchstones and its typical sampling approach.",
    "answer": "Phenomenology (focus on lived experience), hermeneutics (interpretation is unavoidable, hence the double hermeneutic), and idiography (commitment to the particular case, with each case analyzed in depth before cross-case work). Sampling: small, homogeneous, purposive samples, commonly about 3-10, and single-case IPA is legitimate (vs. roughly 5-25 in Polkinghorne's guidance for descriptive phenomenology).",
    "type": "recall",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "ipa",
    "cluster": "phen-research",
    "bloom_level": "remember"
  },
  {
    "id": "ax-phe-method-mcq-01",
    "prompt": "A study of 6 bereaved fathers analyzes each father's interview in depth before comparing cases, foregrounds the researcher's interpretation of how the fathers make sense of their loss, and does not claim to bracket. Which method is it most likely using?",
    "options": [
      "Interpretative Phenomenological Analysis (IPA)",
      "Giorgi's descriptive phenomenological method",
      "Moustakas's transcendental phenomenology",
      "A randomized controlled trial"
    ],
    "correct": "Interpretative Phenomenological Analysis (IPA)",
    "answer": "Small homogeneous sample, idiographic case-by-case analysis, a double hermeneutic, and no bracketing claim are all IPA signatures. Giorgi and Moustakas are descriptive and use bracketing or epoché; Moustakas also uses horizontalization and textural/structural descriptions.",
    "type": "mcq",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "method-identification",
    "cluster": "phen-research",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-horizontal-double-analyze-01",
    "prompt": "'Horizontalization' appears both in Spinelli's therapy method and Moustakas's research method. Compare the two uses.",
    "answer": "Same root idea (treat everything as initially of equal weight), two different jobs. In therapy (Spinelli) it is a LISTENING rule: don't rank what the client says by your theory of importance. In research (Moustakas) it is a DATA-ANALYSIS step: list every significant statement from the transcripts as equally weighted before clustering them into themes.",
    "type": "compare",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "horizontalization-two-uses",
    "cluster": "phen-research",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-phe-research-fit-apply-01",
    "prompt": "For each research question, is phenomenology a good fit? (a) 'What is it like to be a first-generation college student in counseling?' (b) 'Does a 6-week mindfulness group reduce PHQ-9 scores more than waitlist?' (c) 'How do counselors experience a client's suicide?'",
    "answer": "(a) Good fit: a lived-experience question about what it is like. (b) Poor fit: an efficacy question needing an experimental design (RCT) with quantitative outcomes; phenomenology can't establish that X works. (c) Good fit: a lived-experience question; IPA with a small, homogeneous sample would be typical, with strong IRB and wellbeing protections because of the sensitive topic.",
    "type": "vignette",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "method-fit",
    "cluster": "phen-research",
    "bloom_level": "apply"
  },
  {
    "id": "ax-phe-generalize-evaluate-01",
    "prompt": "A counseling article's discussion section says: 'Our IPA study of 8 participants shows that most Latina immigrant mothers experience therapy as culturally alienating.' Evaluate the claim.",
    "answer": "It over-generalizes. IPA uses small, homogeneous, purposive samples for idiographic, in-depth understanding of how these participants make sense of their experience. It supports no statistical generalization to 'most' of a population. A defensible claim would be that these participants described therapy as culturally alienating, which offers insight into how this can be experienced and generates hypotheses for further research. Also check for reflexivity and a clear philosophy-procedure fit.",
    "type": "explain",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "generalization",
    "cluster": "phen-research",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-phe-zahavi-critique-understand-01",
    "prompt": "What was Dan Zahavi's 2019 critique of applied phenomenological research, and what middle position on bracketing did LeVasseur offer?",
    "answer": "Zahavi ('Getting it quite wrong', Qualitative Health Research, 2019) argued that both van Manen and Smith (IPA) promote confusions about what phenomenology is, including the role of the epoché and reduction, and pointed researchers to other resources. The 'is applied phenomenology really phenomenology?' debate is ongoing. LeVasseur's middle position is 'bridling': restrain and reflect on preconceptions rather than claim to remove them (between strict bracketing and none).",
    "type": "explain",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "zahavi-critique",
    "cluster": "phen-research",
    "bloom_level": "understand"
  },
  {
    "id": "ax-phe-vanmanen-recall-01",
    "prompt": "What characterizes van Manen's hermeneutic phenomenology as a research approach?",
    "answer": "From Researching Lived Experience (1990): research as reflective writing, interpreting lived experience through attention to lived body, lived time, lived space, and lived relations. It follows Heidegger and Gadamer in holding that pre-understanding cannot be fully bracketed and must instead be made explicit.",
    "type": "recall",
    "source_page": "wiki/theory-phenomenological-research.md",
    "topic": "van-manen",
    "cluster": "phen-research",
    "bloom_level": "remember"
  }
]
```
