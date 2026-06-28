# Unit 2 items — Counseling Theories: The Major Schools

Source of truth for Unit 2 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This unit's signature item is the syllabus practice
rep — **"stuck because ___, better by ___"** — applied to each family, plus heavy
**compare-and-contrast** and **differential vignette** items, because telling the six families apart
*is* the skill. Everything is in one cluster — `theory-families` — which is the interleaving target;
the `topic` tag names the specific school. See generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## Per-family core (remember → understand → apply)

```json
[
  {
    "id": "u2-psychodynamic-cloze-01",
    "prompt": "The three pillars of psychodynamic theory are the unconscious, {{defense mechanisms}}, and transference.",
    "answer": "defense mechanisms",
    "type": "cloze",
    "source_page": "wiki/theory-psychodynamic.md",
    "topic": "psychodynamic",
    "cluster": "theory-families",
    "bloom_level": "remember"
  },
  {
    "id": "u2-psychodynamic-stuckbetter-01",
    "prompt": "Fill in the psychodynamic frame: 'People get stuck because ___, and they get better by ___.'",
    "answer": "Stuck because of unconscious, unresolved conflicts (often from early childhood) that drive behavior outside awareness, kept hidden by defense mechanisms. Better by making the unconscious conscious — insight — plus emotional processing and working through patterns as they replay in the therapy relationship (transference).",
    "type": "explain",
    "source_page": "wiki/theory-psychodynamic.md",
    "topic": "psychodynamic",
    "cluster": "theory-families",
    "bloom_level": "understand"
  },
  {
    "id": "u2-psychodynamic-apply-01",
    "prompt": "A client keeps choosing emotionally unavailable partners and, a few sessions in, starts reacting to you as if you'll abandon her like her father did. Name the psychodynamic concept this in-session reaction illustrates, and why a psychodynamic therapist treats it as useful rather than a problem.",
    "answer": "Transference — she is redirecting feelings/relational patterns from an early relationship onto the therapist. It's useful because the very pattern that causes trouble in her life is now happening live in the room, where it can be observed and worked through.",
    "type": "vignette",
    "source_page": "wiki/theory-psychodynamic.md",
    "topic": "psychodynamic",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-personcentered-cloze-01",
    "prompt": "In person-centered theory, the built-in drive toward growth that therapy aims to free is called the {{actualizing tendency}}.",
    "answer": "actualizing tendency",
    "type": "cloze",
    "source_page": "wiki/theory-person-centered.md",
    "topic": "person-centered",
    "cluster": "theory-families",
    "bloom_level": "remember"
  },
  {
    "id": "u2-personcentered-stuckbetter-01",
    "prompt": "Fill in the person-centered frame: 'People get stuck because ___, and they get better by ___.'",
    "answer": "Stuck because the actualizing tendency got blocked by conditions of worth, creating incongruence between the real self and the self-image they feel they must maintain. Better by a genuine relationship offering the core conditions (empathy, unconditional positive regard, congruence), which frees the person to re-own denied experience and resume growing.",
    "type": "explain",
    "source_page": "wiki/theory-person-centered.md",
    "topic": "person-centered",
    "cluster": "theory-families",
    "bloom_level": "understand"
  },
  {
    "id": "u2-personcentered-apply-01",
    "prompt": "A client asks, 'Just tell me what I should do.' The counselor instead reflects the client's feeling and stays with their experience, declining to advise. Which theory's stance is this, and what is the term for that stance?",
    "answer": "Person-centered / humanistic theory. The stance is non-directive: the client is the expert on their own life and leads the direction; the counselor creates conditions for growth rather than giving advice or interpretations.",
    "type": "vignette",
    "source_page": "wiki/theory-person-centered.md",
    "topic": "person-centered",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-existential-cloze-01",
    "prompt": "Yalom's four ultimate concerns (givens of existence) are death, freedom, {{isolation}}, and meaninglessness.",
    "answer": "isolation",
    "type": "cloze",
    "source_page": "wiki/theory-existential.md",
    "topic": "existential",
    "cluster": "theory-families",
    "bloom_level": "remember"
  },
  {
    "id": "u2-existential-frankl-recall-01",
    "prompt": "Name Frankl's three sources of meaning in logotherapy.",
    "answer": "(1) Creating or achieving something through work or a deed; (2) experiencing something or encountering someone, especially through love; (3) the attitude one takes toward unavoidable suffering ('the last of the human freedoms').",
    "type": "recall",
    "source_page": "wiki/theory-existential.md",
    "topic": "existential",
    "cluster": "theory-families",
    "bloom_level": "understand"
  },
  {
    "id": "u2-existential-apply-01",
    "prompt": "A recently retired client says, 'I had a title and a schedule and now I'm nobody — what's the point of any of it?' Identify which of Yalom's givens are most active here, and what an existential therapist would help him do.",
    "answer": "Meaninglessness (an existential vacuum) and freedom/responsibility (he must now author a life without an externally given role). The therapist helps him face this honestly and actively choose/create meaning — e.g., through new deeds, relationships, or the stance he takes — rather than waiting for meaning to be handed back to him.",
    "type": "vignette",
    "source_page": "wiki/theory-existential.md",
    "topic": "existential",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-cbt-cloze-01",
    "prompt": "In Ellis's REBT, the ABC model holds that emotional consequences (C) are caused not by the activating event (A) but by the person's {{beliefs}} (B) about it.",
    "answer": "beliefs",
    "type": "cloze",
    "source_page": "wiki/theory-cbt.md",
    "topic": "cbt",
    "cluster": "theory-families",
    "bloom_level": "remember"
  },
  {
    "id": "u2-cbt-stuckbetter-01",
    "prompt": "Fill in the CBT frame: 'People get stuck because ___, and they get better by ___.'",
    "answer": "Stuck because of distorted/inaccurate automatic thoughts and maladaptive learned behavior that maintain distress in the present. Better by identifying and testing those thoughts against evidence (cognitive restructuring) and changing the behavior (e.g., exposure, behavioral activation) — structured, directive, present-focused work.",
    "type": "explain",
    "source_page": "wiki/theory-cbt.md",
    "topic": "cbt",
    "cluster": "theory-families",
    "bloom_level": "understand"
  },
  {
    "id": "u2-cbt-apply-01",
    "prompt": "Client: 'My friend didn't text back. I knew it — nobody actually likes me, I always end up alone.' Name the cognitive distortion(s) and what a CBT therapist would do next with this thought.",
    "answer": "Mind reading (assuming she knows why he didn't text), overgeneralization/catastrophizing ('always end up alone'), and an activated core belief ('nobody likes me / I am unlovable'). The CBT therapist would treat the thought as a hypothesis to test — examine the evidence for and against, generate alternative explanations (he's busy), and check the conclusion against reality.",
    "type": "vignette",
    "source_page": "wiki/theory-cbt.md",
    "topic": "cbt",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-familysystems-cloze-01",
    "prompt": "In family systems theory, the family member who carries the visible symptom but is reframed as expressing tension in the whole system is called the {{identified patient}}.",
    "answer": "identified patient",
    "type": "cloze",
    "source_page": "wiki/theory-family-systems.md",
    "topic": "family-systems",
    "cluster": "theory-families",
    "bloom_level": "remember"
  },
  {
    "id": "u2-familysystems-stuckbetter-01",
    "prompt": "Fill in the family-systems frame: 'People get stuck because ___, and they get better by ___.'",
    "answer": "Stuck because the problem lives in the relationship system — dysfunctional patterns, roles, boundaries, and emotional reactivity — not inside one individual. Better by changing those patterns: increasing differentiation of self and de-triangling (Bowen), or restructuring boundaries and subsystems (Minuchin), so the symptom in the identified patient eases.",
    "type": "explain",
    "source_page": "wiki/theory-family-systems.md",
    "topic": "family-systems",
    "cluster": "theory-families",
    "bloom_level": "understand"
  },
  {
    "id": "u2-familysystems-apply-01",
    "prompt": "Parents bring in their 14-year-old 'problem child' for acting out, while barely speaking to each other. A systems-oriented counselor suspects the teen's behavior may be stabilizing the parents' conflict. Name the concept describing a two-person tension pulling in a third, and how the counselor reframes who the 'patient' is.",
    "answer": "Triangulation — the marital tension is routed through the child to stabilize the dyad. The counselor reframes the teen as the identified patient (symptom-bearer) rather than the source of pathology, and treats the family system — the parents' relationship and patterns — as the actual focus of change.",
    "type": "vignette",
    "source_page": "wiki/theory-family-systems.md",
    "topic": "family-systems",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-postmodern-cloze-01",
    "prompt": "Narrative therapy's defining premise is summarized as: 'The person is not the problem; {{the problem}} is the problem.'",
    "answer": "the problem",
    "type": "cloze",
    "source_page": "wiki/theory-postmodern.md",
    "topic": "postmodern",
    "cluster": "theory-families",
    "bloom_level": "remember"
  },
  {
    "id": "u2-postmodern-stuckbetter-01",
    "prompt": "Fill in the postmodern frame: 'People get stuck because ___, and they get better by ___.'",
    "answer": "Stuck because they are trapped inside a problem-saturated dominant story about themselves, built from language and culture, that hides their resources and exceptions — with no single objective truth to uncover. Better by collaboratively re-authoring that story and building on exceptions/strengths (solution-focused and narrative methods), with the counselor in a non-expert stance.",
    "type": "explain",
    "source_page": "wiki/theory-postmodern.md",
    "topic": "postmodern",
    "cluster": "theory-families",
    "bloom_level": "understand"
  },
  {
    "id": "u2-postmodern-apply-01",
    "prompt": "A counselor asks: 'Suppose tonight while you sleep a miracle happens and this problem is solved, but you don't know it happened. What's the first thing you'd notice tomorrow that tells you?' Name the technique, the approach it belongs to, and what it is designed to elicit.",
    "answer": "The miracle question, from Solution-Focused Brief Therapy (de Shazer & Berg). It is designed to elicit a concrete, vivid picture of the client's desired future/solution — bypassing problem analysis and orienting toward what change would look like.",
    "type": "vignette",
    "source_page": "wiki/theory-postmodern.md",
    "topic": "postmodern",
    "cluster": "theory-families",
    "bloom_level": "apply"
  }
]
```

## Compare-and-contrast (analyze) — interleaving baked into the item

```json
[
  {
    "id": "u2-psychodynamic-vs-cbt-compare-01",
    "prompt": "Contrast psychodynamic therapy and CBT on three axes: time focus, what they target, and therapist stance.",
    "answer": "Time focus: psychodynamic looks to the PAST (early unresolved conflict); CBT is PRESENT-focused. Target: psychodynamic targets unconscious conflict/defenses via insight; CBT targets distorted automatic thoughts and maladaptive behavior via testing/restructuring. Stance: psychodynamic is interpretive (therapist reads unconscious meaning); CBT is directive-collaborative (therapist teaches skills, tests thoughts as hypotheses).",
    "type": "compare",
    "source_page": "wiki/unit02-theories.md",
    "topic": "psychodynamic-vs-cbt",
    "cluster": "theory-families",
    "bloom_level": "analyze"
  },
  {
    "id": "u2-personcentered-vs-existential-compare-01",
    "prompt": "Person-centered and existential therapies are both humanistic and anti-deterministic. What is the key difference in their starting assumptions about human nature?",
    "answer": "Person-centered theory starts optimistically: there's an actualizing tendency that, once freed by the core conditions, naturally drives growth. Existential theory starts from the hard givens of existence (death, freedom, isolation, meaninglessness) and the anxiety they provoke — growth comes from facing those givens and choosing responsibly, not from releasing an innate growth drive.",
    "type": "compare",
    "source_page": "wiki/theory-existential.md",
    "topic": "person-centered-vs-existential",
    "cluster": "theory-families",
    "bloom_level": "analyze"
  },
  {
    "id": "u2-ellis-vs-beck-compare-01",
    "prompt": "Within CBT, distinguish Ellis's REBT from Beck's Cognitive Therapy in both core concept and therapeutic style.",
    "answer": "Ellis (REBT) frames it as the ABC model and targets IRRATIONAL BELIEFS, disputing them directly in a more CONFRONTATIONAL style. Beck (CT) targets AUTOMATIC THOUGHTS and cognitive distortions, treating them as HYPOTHESES TO TEST in a more COLLABORATIVE, empirical style ('collaborative empiricism'). Hook: Ellis disputes, Beck tests.",
    "type": "compare",
    "source_page": "wiki/theory-cbt.md",
    "topic": "ellis-vs-beck",
    "cluster": "theory-families",
    "bloom_level": "analyze"
  },
  {
    "id": "u2-bowen-vs-minuchin-compare-01",
    "prompt": "Contrast Bowen's and Minuchin's models of family systems therapy.",
    "answer": "Bowen (Bowen Family Systems): multigenerational and emotion-focused — central construct is differentiation of self, plus triangulation, multigenerational transmission, and emotional cutoff; looks back and inward. Minuchin (Structural Family Therapy): here-and-now and structure-focused — subsystems and boundaries (rigid/disengaged vs. diffuse/enmeshed), actively restructured through enactments in the session.",
    "type": "compare",
    "source_page": "wiki/theory-family-systems.md",
    "topic": "bowen-vs-minuchin",
    "cluster": "theory-families",
    "bloom_level": "analyze"
  },
  {
    "id": "u2-sfbt-vs-narrative-compare-01",
    "prompt": "Both SFBT and narrative therapy are postmodern. Contrast their central question/method.",
    "answer": "SFBT (de Shazer & Berg): future- and solution-focused — 'what does the solution look like, and when does it already happen?' — using the miracle question, exception questions, and scaling. Narrative (White & Epston): story- and identity-focused — 'whose story is running your life, and what story would you rather live?' — using externalizing, dominant vs. alternative stories, unique outcomes, and re-authoring.",
    "type": "compare",
    "source_page": "wiki/theory-postmodern.md",
    "topic": "sfbt-vs-narrative",
    "cluster": "theory-families",
    "bloom_level": "analyze"
  },
  {
    "id": "u2-cbt-vs-postmodern-compare-01",
    "prompt": "CBT and postmodern therapies are both present/future-focused. What is the deep philosophical difference between them about a client's thoughts?",
    "answer": "CBT assumes there is a reality against which a thought can be judged distorted or inaccurate, and works to correct it toward that reality. Postmodern therapy denies a single objective truth — a thought/story isn't 'distorted', it's just one construction — so it co-authors a more livable story rather than correcting an error, and the counselor drops the expert stance.",
    "type": "compare",
    "source_page": "wiki/unit02-theories.md",
    "topic": "cbt-vs-postmodern",
    "cluster": "theory-families",
    "bloom_level": "analyze"
  },
  {
    "id": "u2-unitofanalysis-analyze-01",
    "prompt": "Family systems theory and the individual therapies (psychodynamic, CBT, person-centered) differ most fundamentally in one thing. What is it, and why does it change who/what gets treated?",
    "answer": "The unit of analysis. Individual therapies locate the problem inside the person (unconscious conflict, distorted cognition, blocked growth) and treat the individual. Family systems locates the problem in the relationship system and treats the patterns/structure — so the 'identified patient' is reframed as the symptom-bearer of the whole system, and change targets the relationships, not just the person.",
    "type": "explain",
    "source_page": "wiki/theory-family-systems.md",
    "topic": "unit-of-analysis",
    "cluster": "theory-families",
    "bloom_level": "analyze"
  }
]
```

## Differential vignettes (mcq) — match the theory to the case

```json
[
  {
    "id": "u2-differential-mcq-01",
    "prompt": "A counselor spends the session asking when the client's depression is even slightly less intense, and what is different in those moments — deliberately not exploring causes or childhood. Which theory is this?",
    "answer": "Postmodern (Solution-Focused Brief Therapy) — exception questions, future/resource focus, no interest in problem origins.",
    "type": "mcq",
    "options": ["Psychodynamic", "Cognitive-Behavioral (CBT)", "Postmodern (Solution-Focused)", "Family systems"],
    "source_page": "wiki/theory-postmodern.md",
    "topic": "differential",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-differential-mcq-02",
    "prompt": "A counselor helps a client confront the fact that no one can give her life meaning but herself, and that her anxiety is partly the cost of her freedom to choose. Which theory is this?",
    "answer": "Existential — working with the givens of existence (freedom/responsibility, meaninglessness) rather than symptoms or cognitions.",
    "type": "mcq",
    "options": ["Person-centered", "Existential", "CBT", "Psychodynamic"],
    "source_page": "wiki/theory-existential.md",
    "topic": "differential",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-differential-mcq-03",
    "prompt": "A counselor maps how a couple's unspoken conflict gets routed through their symptomatic child, and works to change that pattern rather than treating the child alone. Which theory is this?",
    "answer": "Family systems — triangulation and the identified patient; the problem is in the relationship system.",
    "type": "mcq",
    "options": ["Family systems", "Psychodynamic", "CBT", "Postmodern (Narrative)"],
    "source_page": "wiki/theory-family-systems.md",
    "topic": "differential",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-differential-mcq-04",
    "prompt": "A client says 'the Anxiety has been bossing me around all week.' The counselor leans into that phrasing and asks about a time the client stood up to it. Which theory/technique is this?",
    "answer": "Postmodern (Narrative therapy) — externalizing language ('the Anxiety') plus a unique outcome (a time the problem didn't dominate).",
    "type": "mcq",
    "options": ["CBT (cognitive restructuring)", "Narrative therapy (externalizing)", "Psychodynamic (transference)", "Existential (paradoxical intention)"],
    "source_page": "wiki/theory-postmodern.md",
    "topic": "differential",
    "cluster": "theory-families",
    "bloom_level": "analyze"
  },
  {
    "id": "u2-differential-mcq-05",
    "prompt": "A client notices he reacts to his new female supervisor with the same resentment he felt toward his controlling mother, and the counselor explores this pattern as it's now showing up toward the counselor too. Which theory is this?",
    "answer": "Psychodynamic — transference of an early relational pattern onto present figures, including the therapist.",
    "type": "mcq",
    "options": ["CBT", "Psychodynamic", "Solution-focused", "Family systems"],
    "source_page": "wiki/theory-psychodynamic.md",
    "topic": "differential",
    "cluster": "theory-families",
    "bloom_level": "apply"
  }
]
```

## Evaluate & stance (the integrative move + the CS fix-it caution)

```json
[
  {
    "id": "u2-integrative-evaluate-01",
    "prompt": "Surveys show most experienced clinicians describe themselves as integrative/eclectic rather than purist. Make the case for learning each pure theory anyway, and name the failure mode of doing integration badly.",
    "answer": "Each theory is a distinct lens that directs attention and suggests next moves; knowing them well lets you choose deliberately and combine them coherently for a given client. The failure mode is undisciplined eclecticism — grabbing techniques at random with no organizing rationale ('grab-bag' therapy), which loses the coherence that makes any single theory useful. Principled integration requires first understanding what each lens assumes.",
    "type": "explain",
    "source_page": "wiki/unit02-theories.md",
    "topic": "integrative",
    "cluster": "theory-families",
    "bloom_level": "evaluate"
  },
  {
    "id": "u2-psychodynamic-evaluate-01",
    "prompt": "What is the main scientific criticism of psychodynamic theory's core constructs, and how strong is its evidence base?",
    "answer": "Core constructs (the unconscious, defenses, transference) are hard to operationalize and falsify, so they resist clean empirical testing. The outcome evidence is reasonably supportive for depression and anxiety but limited/less robust for OCD, PTSD, and psychosis; treatment can also be long and costly.",
    "type": "explain",
    "source_page": "wiki/theory-psychodynamic.md",
    "topic": "psychodynamic",
    "cluster": "theory-families",
    "bloom_level": "evaluate"
  },
  {
    "id": "u2-postmodern-evaluate-01",
    "prompt": "Postmodern therapy holds there is 'no single objective truth.' Why is that philosophically contested, and how do most clinicians reconcile it with evidence-based practice and risk assessment?",
    "answer": "Taken literally it conflicts with the existence of clinical facts (a real suicide risk, a real diagnosis) and with evidence-based practice, which assumes some interventions objectively outperform others. Most clinicians apply constructionism as a stance toward the client's MEANING — honoring their story and dropping the all-knowing-expert posture — without denying clinical reality, so they still assess risk and use evidence objectively.",
    "type": "explain",
    "source_page": "wiki/theory-postmodern.md",
    "topic": "postmodern",
    "cluster": "theory-families",
    "bloom_level": "evaluate"
  },
  {
    "id": "u2-stance-evaluate-01",
    "prompt": "STANCE DRILL (for a CS background). You feel most drawn to CBT because it resembles a debuggable algorithm. Why is it worth deliberately mastering person-centered and existential theory too?",
    "answer": "Because the 'find the bug and fix it' reflex actively backfires in the relational and meaning-based schools — person-centered and existential therapy work precisely BECAUSE the counselor resists solving and instead offers relationship or honest encounter. Treating theory as an identity/algorithm to optimize also misses the point: theory is a tool for attention, held loosely. Over-relying on the most protocol-like school would leave you unable to help clients whose problem isn't a faulty cognition to correct.",
    "type": "explain",
    "source_page": "wiki/unit02-theories.md",
    "topic": "stance",
    "cluster": "theory-families",
    "bloom_level": "evaluate"
  },
  {
    "id": "u2-existential-vs-personcentered-apply-01",
    "prompt": "A client is grieving a terminal diagnosis and asks how to live with the time she has. Briefly contrast how a person-centered vs. an existential counselor would primarily respond.",
    "answer": "Person-centered: provide empathy, unconditional positive regard, and congruence — a relationship in which she feels deeply understood, trusting her own process to find her way. Existential: gently help her face the given of death directly and use it to clarify what makes her remaining time meaningful — choosing how to live in light of finitude. Both are humanistic; existential leans into the death/meaning content, person-centered into the relationship itself.",
    "type": "compare",
    "source_page": "wiki/theory-existential.md",
    "topic": "person-centered-vs-existential",
    "cluster": "theory-families",
    "bloom_level": "apply"
  },
  {
    "id": "u2-defense-apply-01",
    "prompt": "A man furious at his boss goes home and snaps at his kids over nothing. Name the defense mechanism, and one that would instead channel the anger into something socially productive (e.g., a hard workout or a project).",
    "answer": "Displacement (redirecting the feeling onto a safer target — the kids instead of the boss). Channeling it into something productive is sublimation (redirecting an unacceptable impulse into a valued activity).",
    "type": "vignette",
    "source_page": "wiki/theory-psychodynamic.md",
    "topic": "psychodynamic",
    "cluster": "theory-families",
    "bloom_level": "apply"
  }
]
```
