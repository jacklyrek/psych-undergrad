# Elective module items — Psychological First Aid & Acute Grief Support

Source of truth for this **elective/ad-hoc module** (off-spine; `aux-` namespace). Each fenced
`json` block is a JSON array merged by `apps/build_items.py` into `build/items.json`. Items span
Bloom levels and lean toward **application + stance** (the acute-helper's restraint), per the
generate rules in [`../CLAUDE.md`](../CLAUDE.md). Clusters: `pfa-frameworks`, `grief-models`,
`bereavement-support`. Item id prefix: `ax-pfa-`.

## Cluster: pfa-frameworks

```json
[
  {
    "id": "ax-pfa-lll-cloze-01",
    "prompt": "WHO's three action principles of Psychological First Aid are Look, Listen, and {{Link}}.",
    "answer": "Link",
    "type": "cloze",
    "source_page": "wiki/concept-pfa-core-actions.md",
    "topic": "look-listen-link",
    "cluster": "pfa-frameworks",
    "bloom_level": "remember"
  },
  {
    "id": "ax-pfa-objectives-recall-01",
    "prompt": "What are the two stated objectives of PFA, and who is qualified to deliver it?",
    "answer": "Objectives: (1) reduce initial distress in the immediate aftermath of a crisis, and (2) foster short- and long-term adaptive functioning. It is NOT therapy. It can be delivered by trained lay helpers and responders, not only mental-health professionals.",
    "type": "recall",
    "source_page": "wiki/concept-pfa-core-actions.md",
    "topic": "pfa-objectives",
    "cluster": "pfa-frameworks",
    "bloom_level": "remember"
  },
  {
    "id": "ax-pfa-debrief-understand-01",
    "prompt": "Why does PFA deliberately NOT require a survivor to talk through what happened? Cite the evidence.",
    "answer": "Because structured single-session psychological debriefing (CISD) was found ineffective at preventing PTSD and possibly harmful — a Cochrane review found it equivalent to or worse than control and that it may increase PTSD/depression risk, and NICE recommends not offering it. So PFA accompanies and stabilizes rather than extracting a trauma narrative; if the person chooses to talk you listen, but you never push.",
    "type": "explain",
    "source_page": "wiki/concept-pfa-core-actions.md",
    "topic": "debriefing",
    "cluster": "pfa-frameworks",
    "bloom_level": "understand"
  },
  {
    "id": "ax-pfa-coreactions-recall-01",
    "prompt": "List the eight NCTSN Core Actions of PFA in order.",
    "answer": "1) Contact and Engagement, 2) Safety and Comfort, 3) Stabilization, 4) Information Gathering (current needs and concerns), 5) Practical Assistance, 6) Connection with Social Supports, 7) Information on Coping, 8) Linkage with Collaborative Services. They are flexible modules, not a rigid sequence.",
    "type": "recall",
    "source_page": "wiki/concept-pfa-core-actions.md",
    "topic": "core-actions",
    "cluster": "pfa-frameworks",
    "bloom_level": "understand"
  },
  {
    "id": "ax-pfa-lll-apply-01",
    "prompt": "You arrive at a scene after a fatal accident. A bystander is standing in a dangerous spot, shaking, saying nothing. Walk through what 'Look, Listen, Link' has you do first, second, third.",
    "answer": "LOOK: scan for safety and serious reactions — first move the person out of the dangerous spot and check for urgent basic needs. LISTEN: approach calmly, make contact, ask about their needs/concerns and help them feel calm, without pressing them to recount the accident. LINK: connect them to practical support — loved ones, basic needs, services/information. The order is triage-first, talk-second, connect-onward.",
    "type": "vignette",
    "source_page": "wiki/concept-pfa-core-actions.md",
    "topic": "look-listen-link",
    "cluster": "pfa-frameworks",
    "bloom_level": "apply"
  },
  {
    "id": "ax-pfa-debrief-apply-01",
    "prompt": "A colleague says: 'Let's get the survivors in a room tonight and have each describe exactly what they saw, so it doesn't fester.' What is the problem, and what would you propose instead?",
    "answer": "That is critical incident stress debriefing, which the evidence does not support — single-session debriefing doesn't prevent PTSD and may worsen outcomes (Cochrane; NICE says don't offer it). Forcing fresh recounting can re-distress people. Instead provide PFA: ensure safety/comfort, meet practical needs, offer information on normal stress reactions and coping, and connect people to social support and follow-up services — letting anyone who wants to talk do so voluntarily.",
    "type": "vignette",
    "source_page": "wiki/concept-pfa-core-actions.md",
    "topic": "debriefing",
    "cluster": "pfa-frameworks",
    "bloom_level": "apply"
  },
  {
    "id": "ax-pfa-coreactions-analyze-01",
    "prompt": "A flooded survivor is disoriented, can't track what you're saying, and is hyperventilating. Which NCTSN Core Action is specifically called for, and is it always used?",
    "answer": "Stabilization (Core Action 3) — calming and orienting a survivor who is emotionally overwhelmed or disoriented. It is NOT always needed: it's the one core action used only for survivors who are overwhelmed/disoriented; most people receiving PFA don't require it.",
    "type": "vignette",
    "source_page": "wiki/concept-pfa-core-actions.md",
    "topic": "core-actions",
    "cluster": "pfa-frameworks",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-pfa-evidence-evaluate-01",
    "prompt": "PFA is described as 'evidence-informed,' not 'evidence-based.' What is the honest claim to make for it, and what would overstate it?",
    "answer": "Honest claim: PFA is supported by expert consensus, is low-risk, humane, and reflects what's known about acute crisis response — and notably it avoids the harms of debriefing. Overstating it: claiming PFA is proven to prevent PTSD or proven effective in rigorous outcome trials — that evidence is limited. Claim its reasonableness and safety, not demonstrated efficacy.",
    "type": "explain",
    "source_page": "wiki/concept-pfa-core-actions.md",
    "topic": "pfa-evidence",
    "cluster": "pfa-frameworks",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: grief-models

```json
[
  {
    "id": "ax-pfa-dpm-cloze-01",
    "prompt": "Stroebe & Schut's Dual Process Model says grievers oscillate between loss-oriented coping and {{restoration-oriented}} coping.",
    "answer": "restoration-oriented",
    "type": "cloze",
    "source_page": "wiki/concept-grief-models.md",
    "topic": "dual-process-model",
    "cluster": "grief-models",
    "bloom_level": "remember"
  },
  {
    "id": "ax-pfa-worden-recall-01",
    "prompt": "Name Worden's four tasks of mourning.",
    "answer": "1) Accept the reality of the loss; 2) Process the pain of grief; 3) Adjust to a world without the deceased (external, internal, spiritual); 4) Find an enduring connection with the deceased while embarking on a new life. They are active tasks, not ordered stages.",
    "type": "recall",
    "source_page": "wiki/concept-grief-models.md",
    "topic": "worden-tasks",
    "cluster": "grief-models",
    "bloom_level": "understand"
  },
  {
    "id": "ax-pfa-kublerross-evaluate-01",
    "prompt": "Give two reasons clinicians have largely retired the Kübler-Ross five stages as a guide to bereavement.",
    "answer": "(1) The stages were derived from terminally ill patients facing their own death, not from bereaved people, so generalizing them to mourning was never well-founded. (2) Grief doesn't follow a fixed order, and presenting the stages as an itinerary makes grieving people feel they're 'doing it wrong' when their experience doesn't fit. Keep them only as a vocabulary for reactions that can occur, not a path.",
    "type": "explain",
    "source_page": "wiki/concept-grief-models.md",
    "topic": "kubler-ross",
    "cluster": "grief-models",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-pfa-dpm-apply-01",
    "prompt": "A grieving father sobs while looking at photos in the morning, then spends the afternoon calmly sorting insurance paperwork and even laughs at a memory. A relative whispers that he's 'in denial.' Using the dual process model, what's actually happening?",
    "answer": "Normal oscillation. The morning is loss-oriented coping (confronting the loss); the afternoon is restoration-oriented coping (dealing with the changed world). Healthy grieving moves back and forth between the two, with breaks from the pain. The functional, even light moments are not denial or 'being strong' — they are a normal half of grieving, and taking a break from grief is not avoidance.",
    "type": "vignette",
    "source_page": "wiki/concept-grief-models.md",
    "topic": "dual-process-model",
    "cluster": "grief-models",
    "bloom_level": "apply"
  },
  {
    "id": "ax-pfa-pgd-analyze-01",
    "prompt": "Six weeks after her child's death a mother is devastated, barely sleeping, and crying daily. A well-meaning friend wonders aloud if she has 'prolonged grief disorder.' Is that the right call? Why or why not?",
    "answer": "No. Prolonged Grief Disorder requires the death to have been at least 12 months ago for adults (6 months for children/adolescents), plus persistent intense yearning/preoccupation and impairment exceeding cultural norms. At six weeks, intense daily grief is expected and normal. Pathologizing acute grief is a clinical error. Because child loss IS a top PGD risk factor, the right move is to stay connected and watch over time — not to diagnose now.",
    "type": "vignette",
    "source_page": "wiki/concept-grief-models.md",
    "topic": "prolonged-grief-disorder",
    "cluster": "grief-models",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-pfa-pgd-cloze-01",
    "prompt": "DSM-5-TR sets the time threshold for Prolonged Grief Disorder at {{12}} months for adults (and 6 months for children/adolescents).",
    "answer": "12",
    "type": "cloze",
    "source_page": "wiki/concept-grief-models.md",
    "topic": "prolonged-grief-disorder",
    "cluster": "grief-models",
    "bloom_level": "remember"
  },
  {
    "id": "ax-pfa-grief-compare-01",
    "prompt": "Compare the Kübler-Ross stage model with the dual process model as guides for a helper: what does each imply about how a grieving person 'should' look, and which is the safer default?",
    "answer": "Kübler-Ross implies an ordered sequence (denial→...→acceptance), which tempts a helper to judge whether the person is 'progressing' and can make them feel they're grieving wrong. The dual process model implies no path at all — only a back-and-forth between confronting the loss and handling the changed world — so it predicts and normalizes both devastation and functional moments. The dual process model is the safer default: it stops you imposing a shape on someone's grief.",
    "type": "compare",
    "source_page": "wiki/concept-grief-models.md",
    "topic": "grief-model-comparison",
    "cluster": "grief-models",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-pfa-pgd-risk-mcq-01",
    "prompt": "Which bereavement carries the HIGHEST risk of developing prolonged grief disorder?",
    "answer": "Sudden, violent death of one's child",
    "options": [
      "An elderly grandparent's expected death after a long illness",
      "Sudden, violent death of one's child",
      "A distant cousin's death the person rarely saw",
      "A pet's death from old age"
    ],
    "correct": "Sudden, violent death of one's child",
    "type": "mcq",
    "source_page": "wiki/concept-grief-models.md",
    "topic": "prolonged-grief-disorder",
    "cluster": "grief-models",
    "bloom_level": "understand"
  }
]
```

## Cluster: bereavement-support

```json
[
  {
    "id": "ax-pfa-ring-cloze-01",
    "prompt": "Ring Theory's rule for grief support is: comfort {{in}}, dump out.",
    "answer": "in",
    "type": "cloze",
    "source_page": "wiki/concept-supporting-the-bereaved.md",
    "topic": "ring-theory",
    "cluster": "bereavement-support",
    "bloom_level": "remember"
  },
  {
    "id": "ax-pfa-ring-apply-01",
    "prompt": "At a wake, you (a friend) feel overwhelmed by the death and start telling the bereaved mother how devastated YOU are and how you can't stop crying. Using Ring Theory, what's the error and what's the rule?",
    "answer": "Error: you're dumping inward — directing your own distress at the person closest to the loss. Ring Theory: the bereaved parent is at the center; comfort flows IN toward the center, while your own needs/complaints go OUT to someone further from the loss than you. You can grieve too, but process it with your own outer ring, not with the mother.",
    "type": "vignette",
    "source_page": "wiki/concept-supporting-the-bereaved.md",
    "topic": "ring-theory",
    "cluster": "bereavement-support",
    "bloom_level": "apply"
  },
  {
    "id": "ax-pfa-condolence-analyze-01",
    "prompt": "A coworker whose child just died is back at work. You want to say something. Why are 'everything happens for a reason,' 'he's in a better place,' and 'I know how you feel' all poor choices — and what's a better move?",
    "answer": "Each minimizes or redirects: 'everything happens for a reason' demands meaning in the unbearable; 'a better place' denies the parent's reality that nowhere is better than their child alive; 'I know how you feel' centers you and is almost never true. Better: acknowledge the loss plainly, say the child's NAME, and offer presence or a concrete help ('I'm so sorry. I think about [name]. I'm bringing dinner Tuesday') — don't explain, rank, or hurry the grief.",
    "type": "vignette",
    "source_page": "wiki/concept-supporting-the-bereaved.md",
    "topic": "condolence",
    "cluster": "bereavement-support",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-pfa-name-understand-01",
    "prompt": "Many people avoid mentioning a dead child for fear of 'reminding' the parent. Why do bereaved parents usually want the opposite?",
    "answer": "The parent hasn't forgotten — the avoidance doesn't spare them pain, it makes the child feel erased. Parents overwhelmingly want their child acknowledged, by name, soon after and for years. Speaking the child's name and sharing memories is consoling, not harmful.",
    "type": "explain",
    "source_page": "wiki/concept-supporting-the-bereaved.md",
    "topic": "say-the-name",
    "cluster": "bereavement-support",
    "bloom_level": "understand"
  },
  {
    "id": "ax-pfa-help-apply-01",
    "prompt": "STANCE DRILL. You want to help a bereaved family. Why is 'let me know if you need anything' weak, and what's the stronger version?",
    "answer": "A grieving family can't project-manage their own support or make requests, so an open offer quietly puts the work on them and usually yields nothing. Stronger: do a specific, concrete thing — drop off a meal, take the other kids to school, handle the laundry, drive them to an appointment — and keep doing it past the funeral, including on birthdays and the anniversary, when most support has vanished.",
    "type": "vignette",
    "source_page": "wiki/concept-supporting-the-bereaved.md",
    "topic": "concrete-help",
    "cluster": "bereavement-support",
    "bloom_level": "apply"
  },
  {
    "id": "ax-pfa-refer-analyze-01",
    "prompt": "You've been supporting a bereaved father for a month. Which of his statements would shift this from 'normal grief I can accompany' to 'refer to clinical/crisis care now,' and what do you do?",
    "answer": "A statement of suicidal ideation/intent or a wish to die to 'be with' the child is the clear escalation — that's a risk situation, not ordinary grief. Don't manage it alone: stay with him, take it seriously, and link him to crisis/clinical care immediately (PFA's Linkage; see Unit 8 risk assessment). Other escalation signs: total non-functioning that never oscillates toward restoration, escalating substance use, psychosis, or self-neglect endangering health. Ferocious sadness by itself is not a referral trigger.",
    "type": "vignette",
    "source_page": "wiki/concept-supporting-the-bereaved.md",
    "topic": "when-to-refer",
    "cluster": "bereavement-support",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-pfa-selfcare-evaluate-01",
    "prompt": "Why is a helper's own self-care treated as part of competently supporting the bereaved, not a separate indulgence?",
    "answer": "Sitting with profound loss has a real cost (vicarious/secondary stress). A depleted helper withdraws — and disappearing is precisely what grieving parents report hurt most. Using your own support (your outer ring, not the bereaved person) and protecting your capacity is what lets you keep showing up over the long haul, which is the most valuable thing you offer.",
    "type": "explain",
    "source_page": "wiki/concept-supporting-the-bereaved.md",
    "topic": "helper-self-care",
    "cluster": "bereavement-support",
    "bloom_level": "evaluate"
  }
]
```
