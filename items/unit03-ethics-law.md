# Unit 3 items — Ethics, Law & Professional Identity

Source of truth for Unit 3 practice items. Each fenced `json` block is a JSON array merged by
`apps/build_items.py` into `build/items.json`. This unit's signature reps: **the confidentiality
speech** (the syllabus practice rep, as a production item), heavy **which-exception-applies
vignettes** (cluster `confidentiality-exceptions` — the unit's main interleaving target), the
**warn-vs-protect / legal-vs-ethical** distinctions (cluster `duty-concepts`), the six **ethical
principles** as a confusable set (cluster `ethics-principles`), boundary **crossing vs. violation**
(cluster `boundary-concepts`), and **who-does-what/who-prescribes** discrimination (cluster
`the-helping-professions`). Several items are stance probes — ethics under relational pressure, not
just rule recall. See generate rules in [`../CLAUDE.md`](../CLAUDE.md).

## The Code, its principles, and ethics vs. law

```json
[
  {
    "id": "u3-code-structure-cloze-01",
    "prompt": "The 2014 ACA Code of Ethics has nine sections. Section A is The Counseling Relationship; Section B is {{Confidentiality and Privacy}}.",
    "answer": "Confidentiality and Privacy",
    "type": "cloze",
    "source_page": "wiki/unit03-ethics-law.md",
    "topic": "aca-code",
    "cluster": "ethics-principles",
    "bloom_level": "remember"
  },
  {
    "id": "u3-code-newsection-mcq-01",
    "prompt": "A standard about maintaining professional boundaries with clients on social media would live in which section of the 2014 ACA Code — and that section was itself the headline addition of the 2014 revision?",
    "options": [
      "Section H: Distance Counseling, Technology, and Social Media",
      "Section B: Confidentiality and Privacy",
      "Section I: Resolving Ethical Issues",
      "Section C: Professional Responsibility"
    ],
    "correct": "Section H: Distance Counseling, Technology, and Social Media",
    "answer": "Section H — new in 2014, covering distance counseling, technology, and social media. (Note: the *no personal virtual relationships with current clients* rule also appears as A.5.e, but the technology section as a whole is H.)",
    "type": "mcq",
    "source_page": "wiki/unit03-ethics-law.md",
    "topic": "aca-code",
    "cluster": "ethics-principles",
    "bloom_level": "remember"
  },
  {
    "id": "u3-principles-recall-01",
    "prompt": "Name the six ethical principles of the ACA Code and give a three-to-five-word gloss of each.",
    "answer": "Autonomy — client controls their own life's direction. Nonmaleficence — avoid causing harm. Beneficence — actively work for the client's/society's good. Justice — treat people equitably and fairly. Fidelity — honor commitments; keep the relationship's trust. Veracity — deal truthfully.",
    "type": "recall",
    "source_page": "wiki/unit03-ethics-law.md",
    "topic": "ethics-principles",
    "cluster": "ethics-principles",
    "bloom_level": "remember"
  },
  {
    "id": "u3-principles-compare-01",
    "prompt": "Fidelity and veracity are the two most-confused ACA principles. Distinguish them, with an example of violating each without violating the other.",
    "answer": "Fidelity = keeping promises/commitments and honoring the trust of the relationship (e.g., abandoning a client mid-treatment violates fidelity even if you were honest about it). Veracity = truthfulness (e.g., inflating your credentials violates veracity even while you faithfully keep every appointment). Fidelity is about loyalty to commitments; veracity is about honesty of statements.",
    "type": "compare",
    "source_page": "wiki/unit03-ethics-law.md",
    "topic": "ethics-principles",
    "cluster": "ethics-principles",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-principles-apply-01",
    "prompt": "You break confidentiality to hospitalize an acutely suicidal client against her stated wishes. Frame this as a conflict between ACA principles: which principles are you overriding, and which are you serving?",
    "answer": "Overriding autonomy (her right to direct her own life) and, arguably, fidelity (the confidentiality promise). Serving nonmaleficence and beneficence (preventing serious harm; acting for her good). Ethical dilemmas are typically principle-vs-principle conflicts, not rule lookups — and this one is the canonical example.",
    "type": "vignette",
    "source_page": "wiki/unit03-ethics-law.md",
    "topic": "ethics-principles",
    "cluster": "ethics-principles",
    "bloom_level": "apply"
  },
  {
    "id": "u3-ethicslaw-compare-01",
    "prompt": "Distinguish a legal duty from an ethical duty for a counselor: source, enforcer, and consequence of breach. Give one example of conduct that is legal but unethical.",
    "answer": "Legal duty: from statute/regulation/case law, enforced by courts and the state; breach brings criminal/civil liability. Ethical duty: from the professional code (ACA), enforced by the association and licensing board; breach brings complaints, sanctions, license loss. The Code itself notes breaching it 'does not necessarily constitute legal liability.' Legal-but-unethical example: dating a former client six months after termination — legal in many states, but prohibited by the ACA 5-year rule.",
    "type": "compare",
    "source_page": "wiki/unit03-ethics-law.md",
    "topic": "ethics-vs-law",
    "cluster": "duty-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-ethicslaw-conflict-recall-01",
    "prompt": "Per ACA Standard I.1.c, what should a counselor do when ethical responsibilities conflict with the law — and what is the permitted last resort?",
    "answer": "Make known their commitment to the ACA Code and take steps to resolve the conflict. If it cannot be resolved that way, the counselor — acting in the client's best interest — MAY adhere to the law. (Note: 'may follow the law,' not 'must defy it' and not 'ethics always wins.')",
    "type": "recall",
    "source_page": "wiki/unit03-ethics-law.md",
    "topic": "ethics-vs-law",
    "cluster": "duty-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "u3-decision-model-explain-01",
    "prompt": "A classmate says: 'Just tell me the correct ethical decision-making algorithm and I'll apply it.' What does the ACA Code actually say about decision-making models, and what does it expect instead?",
    "answer": "The Code says no specific ethical decision-making model is always most effective. It expects counselors to use *a* credible model that can bear public scrutiny — identify the problem, consult the Code/law/colleagues, weigh the principles, involve the client where possible, document the reasoning. The deliverable is a defensible process, not a provably-correct output. (Stance note: this is exactly the anti-algorithm adjustment the CS reflex resists.)",
    "type": "explain",
    "source_page": "wiki/unit03-ethics-law.md",
    "topic": "ethics-vs-law",
    "cluster": "duty-concepts",
    "bloom_level": "evaluate"
  }
]
```

## Informed consent

```json
[
  {
    "id": "u3-consent-cloze-01",
    "prompt": "Per ACA A.2.a, informed consent is reviewed in writing and verbally, and is an {{ongoing}} part of the counseling process — not a one-time signature.",
    "answer": "ongoing",
    "type": "cloze",
    "source_page": "wiki/concept-informed-consent.md",
    "topic": "informed-consent",
    "bloom_level": "remember"
  },
  {
    "id": "u3-consent-elements-recall-01",
    "prompt": "List at least six things ACA A.2.b requires counselors to explain to clients as part of informed consent.",
    "answer": "Any six of: purposes/goals of services; techniques and procedures; limitations; potential risks; benefits; the counselor's qualifications, credentials, and experience; approach to counseling; continuation of services if the counselor is incapacitated or dies; the role of technology; fees/billing; confidentiality and its limits; the right to refuse services and consequences of refusal.",
    "type": "recall",
    "source_page": "wiki/concept-informed-consent.md",
    "topic": "informed-consent",
    "bloom_level": "remember"
  },
  {
    "id": "u3-consent-trainee-apply-01",
    "prompt": "A counseling intern, worried clients will leave if they find out she's a student, introduces herself only as 'a therapist here at the clinic' and never mentions that a supervisor reviews her cases. Which consent element(s) does this violate, and why does it matter beyond rule-compliance?",
    "answer": "A.2.b requires disclosing qualifications, credentials, and relevant experience — trainee status and supervision (which also affects who hears case material) must be disclosed. Beyond compliance: consent hides a person the client is entitled to know about; discovering it later damages the alliance far more than the disclosure would have. Honest limits are alliance-builders.",
    "type": "vignette",
    "source_page": "wiki/concept-informed-consent.md",
    "topic": "informed-consent",
    "bloom_level": "apply"
  },
  {
    "id": "u3-consent-assent-compare-01",
    "prompt": "For a 10-year-old client, distinguish consent from assent: who gives which, and what does the ACA Code expect the counselor to do with the child's view?",
    "answer": "The legal guardian gives informed CONSENT (the child lacks legal capacity). The child gives ASSENT — agreement sought in developmentally appropriate terms. A.2.d expects counselors to seek assent and include clients in decisions to the extent possible; the child is a participant, not a package. (State law varies on when minors can consent to their own outpatient care.)",
    "type": "compare",
    "source_page": "wiki/concept-informed-consent.md",
    "topic": "informed-consent",
    "bloom_level": "understand"
  },
  {
    "id": "u3-consent-ongoing-why-01",
    "prompt": "Give the empirical argument for treating informed consent as an ongoing process rather than an intake formality.",
    "answer": "Clients demonstrably don't retain consent information — studies find patients and surrogates unable to remember relevant information weeks later (Darby & Weinstock 2018). And exhaustive up-front warnings would be time-prohibitive and needlessly frightening for rare scenarios. So the load-bearing move is a clear plain-language summary at intake plus revisiting the relevant limit when a situation makes it live (e.g., re-explaining the harm exception before detailed risk questioning).",
    "type": "explain",
    "source_page": "wiki/concept-informed-consent.md",
    "topic": "informed-consent",
    "bloom_level": "understand"
  },
  {
    "id": "u3-consent-mandated-apply-01",
    "prompt": "A client is court-ordered to counseling after a DUI. Before starting, what must the counselor explain under A.2.e — and what right does the client keep?",
    "answer": "Exactly what information will be shared with whom (the court, probation), before services begin. The client retains the right to refuse services — knowing the consequences of refusing (e.g., what gets reported back to the court). Mandated referral doesn't erase consent; it changes what consent must cover.",
    "type": "vignette",
    "source_page": "wiki/concept-informed-consent.md",
    "topic": "informed-consent",
    "bloom_level": "apply"
  }
]
```

## Confidentiality, privacy, privilege — and the exceptions

```json
[
  {
    "id": "u3-conf-triad-compare-01",
    "prompt": "Distinguish privacy, confidentiality, and privileged communication — and say who 'holds' the privilege.",
    "answer": "Privacy = the client's underlying right to control access to themselves/their information. Confidentiality = the counselor's ETHICAL duty not to disclose what the client reveals (ACA B.1.c). Privilege = the LEGAL protection against compelled disclosure in court, created by statute/case law. The CLIENT holds the privilege — the client can waive it; the counselor cannot.",
    "type": "compare",
    "source_page": "wiki/concept-confidentiality-limits.md",
    "topic": "confidentiality",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-jaffee-recall-01",
    "prompt": "What did Jaffee v. Redmond (1996) establish, and which profession's inclusion made the holding notably broad?",
    "answer": "The U.S. Supreme Court recognized a psychotherapist–patient privilege in FEDERAL courts (under Federal Rule of Evidence 501) — confidential therapy communications are protected from compelled disclosure. The Court explicitly extended the privilege to licensed clinical social workers (the therapist in the case was an LCSW), not just psychiatrists/psychologists.",
    "type": "recall",
    "source_page": "wiki/concept-confidentiality-limits.md",
    "topic": "confidentiality",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "remember"
  },
  {
    "id": "u3-exceptions-freerecall-01",
    "prompt": "Blank page: list the major exceptions to confidentiality under ACA B.2, plus the everyday non-breach disclosures clients should be told about.",
    "answer": "B.2 exceptions: (1) serious and foreseeable harm to the client or identified others (danger to self; danger to others/duty to protect); (2) legal requirements — chiefly mandated reporting of child/vulnerable-adult abuse; (3) contagious life-threatening disease with an identifiable at-risk third party (permissive); (4) court-ordered disclosure; (5) end-of-life decisions (option to maintain). Everyday disclosures: supervision, treatment teams, office staff, third-party payers/insurance (diagnosis required), consultation. Governing rule: minimal disclosure (B.2.e).",
    "type": "recall",
    "source_page": "wiki/concept-confidentiality-limits.md",
    "topic": "confidentiality",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "remember"
  },
  {
    "id": "u3-b2a-wording-cloze-01",
    "prompt": "ACA B.2.a permits disclosure to protect clients or identified others from serious and {{foreseeable}} harm — the 2014 Code's deliberate replacement for the older 'imminent' standard.",
    "answer": "foreseeable",
    "type": "cloze",
    "source_page": "wiki/concept-confidentiality-limits.md",
    "topic": "confidentiality",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "remember"
  },
  {
    "id": "u3-minimal-disclosure-explain-01",
    "prompt": "You must breach confidentiality to report suspected abuse. Per B.2.e, what two things govern HOW you disclose?",
    "answer": "(1) To the extent possible, inform the client beforehand and involve them in the disclosure decision; (2) reveal only essential information — the necessary fact to the necessary party, never the client's whole story. You breach the seal, not the vault.",
    "type": "explain",
    "source_page": "wiki/concept-confidentiality-limits.md",
    "topic": "confidentiality",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "understand"
  },
  {
    "id": "u3-court-order-apply-01",
    "prompt": "You receive a court order for a client's full treatment records in her custody dispute. She does not want them released. Per B.2.d, what do you do — in order?",
    "answer": "First seek the client's written informed consent. Absent consent, take steps to prohibit the disclosure or narrow it as much as possible (e.g., through counsel: quash the subpoena, limit scope, request in-camera review) because of potential harm to the client and the relationship. Compliance with a valid court order may ultimately be unavoidable — but narrow-first is the ethical sequence. Consult (attorney, supervisor) throughout.",
    "type": "vignette",
    "source_page": "wiki/concept-confidentiality-limits.md",
    "topic": "confidentiality",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "apply"
  },
  {
    "id": "u3-disease-apply-01",
    "prompt": "A client with HIV tells you he is having unprotected sex with his partner, who doesn't know his status. Under ACA B.2.c, is disclosure to the partner mandatory, prohibited, or permitted — and what must you assess first?",
    "answer": "Permitted ('may be justified'), not mandatory — for a disease known to be communicable and life-threatening, to an identifiable third party at serious, foreseeable risk. First assess the client's intent to inform the partner himself or to change the risky behavior; and check state law, which governs disease-status disclosure and varies. Work toward the client telling the partner — disclosure by you is the fallback, at minimal scope.",
    "type": "vignette",
    "source_page": "wiki/concept-confidentiality-limits.md",
    "topic": "confidentiality",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "apply"
  },
  {
    "id": "u3-conf-speech-produce-01",
    "prompt": "The syllabus practice rep, from memory: say (out loud, then write) the confidentiality speech you'd give a new client in the first five minutes — plain language, all major exceptions, no legalese.",
    "answer": "Model (compare, don't memorize): 'What you say here stays here. A few exceptions, so you're never surprised: if I believe you're in real danger of seriously hurting yourself, or someone else is in danger from you, I have to act to keep people safe — involving you as much as I can. If I hear that a child or vulnerable adult is being abused or neglected, the law requires me to report it. Rarely, a judge can order records released — I'd fight to keep that narrow. I also consult a supervisor, and if you use insurance they require a diagnosis. Everything else is between us. What questions do you have?' Score yourself on: all exceptions present (harm to self/others, abuse reporting, court order, supervision/insurance), plain words, stated reasons, invitation for questions, calm tone.",
    "type": "explain",
    "source_page": "wiki/concept-confidentiality-limits.md",
    "topic": "confidentiality",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "apply"
  },
  {
    "id": "u3-exception-discrim-mcq-01",
    "prompt": "Client says: 'My 78-year-old mother lives with my brother. He takes her Social Security checks and she's lost fifteen pounds because he \"forgets\" to buy food.' Which confidentiality doctrine is triggered?",
    "options": [
      "Mandated reporting (vulnerable-adult abuse/neglect)",
      "Duty to warn/protect an identifiable third party (Tarasoff)",
      "The contagious-disease exception (B.2.c)",
      "None — this is hearsay about someone who isn't the client"
    ],
    "correct": "Mandated reporting (vulnerable-adult abuse/neglect)",
    "answer": "Financial exploitation and neglect of an elder/dependent adult — mandated reporting to Adult Protective Services in most states, triggered by reasonable suspicion. It is not Tarasoff (no client threat of violence), and 'not my client' doesn't matter: reporting duties attach to what you learn, not who you treat.",
    "type": "mcq",
    "source_page": "wiki/concept-mandated-reporting.md",
    "topic": "mandated-reporting",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "analyze"
  }
]
```

## Tarasoff and the duty to warn / protect

```json
[
  {
    "id": "u3-tarasoff-facts-recall-01",
    "prompt": "Sketch the Tarasoff facts: who threatened whom, what the therapist actually did, and why liability attached anyway.",
    "answer": "1969: Prosenjit Poddar told his university psychologist, Dr. Lawrence Moore, that he intended to kill Tatiana Tarasoff. Moore DID act — he notified campus police, who briefly detained Poddar and released him; the psychiatry director then ordered the notes destroyed and no further action. No one warned Tatiana or her family; Poddar killed her. Liability attached because the system failed to protect the foreseeable victim — the case is not about a therapist who ignored a threat, which is what makes it instructive.",
    "type": "recall",
    "source_page": "wiki/study-tarasoff.md",
    "topic": "duty-to-warn",
    "cluster": "duty-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "u3-warn-protect-compare-01",
    "prompt": "Tarasoff I (1974) vs. Tarasoff II (1976): what duty did each announce, and why does the difference matter clinically?",
    "answer": "Tarasoff I: duty to WARN the intended victim. Tarasoff II (rehearing, the governing ruling): duty to PROTECT — take reasonable precautions, of which warning is only one option (others: hospitalization, intensified treatment, means removal, medication, involving family, notifying police). Clinically it matters because 'warn' framing pushes you to the most relationship-destroying option first; the actual duty is to do something effective, warning as last resort, with minimal disclosure.",
    "type": "compare",
    "source_page": "wiki/study-tarasoff.md",
    "topic": "duty-to-warn",
    "cluster": "duty-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-tobriner-cloze-01",
    "prompt": "Justice Tobriner's famous Tarasoff line: 'The protective privilege ends where {{the public peril}} begins.'",
    "answer": "the public peril",
    "type": "cloze",
    "source_page": "wiki/study-tarasoff.md",
    "topic": "duty-to-warn",
    "cluster": "duty-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "u3-protect-menu-recall-01",
    "prompt": "A client makes a credible threat against his ex. Warning her is one option. List four OTHER protective steps on the duty-to-protect menu.",
    "answer": "Any four of: increase session frequency / intensify treatment; arrange removal of weapons from the home (means restriction); initiate or adjust medication via a prescriber; voluntary or involuntary hospitalization; involve family or third parties in treatment; notify police. Choose the least intrusive steps that will actually protect.",
    "type": "recall",
    "source_page": "wiki/concept-duty-to-warn.md",
    "topic": "duty-to-warn",
    "cluster": "duty-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "u3-trigger-discrim-vignette-01",
    "prompt": "Client A fumes: 'Everyone at that company deserves to burn; I hope the whole place gets what's coming.' Client B says: 'If Marcus shows up at the reunion Saturday, I'll be waiting with my hunting rifle.' Which triggers Tarasoff-type duties, and why? What does the other one still require?",
    "answer": "Client B: specific identifiable victim (Marcus), stated means (rifle) and timeline (Saturday) — the classic trigger (identifiable victim + intent/ability + imminence; ACA: serious and foreseeable harm). Client A's generalized venting names no identifiable victim, so it typically does not trigger warn/protect duties — but it absolutely requires clinical risk assessment, exploration, and documentation. Threshold questions are legal; assessment is always clinical.",
    "type": "vignette",
    "source_page": "wiki/concept-duty-to-warn.md",
    "topic": "duty-to-warn",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-state-variation-mcq-01",
    "prompt": "Which statement about duty-to-warn/protect law in the U.S. is accurate?",
    "options": [
      "It varies by state: mandatory in many, permissive in some, absent in a few",
      "Tarasoff made warning the victim mandatory nationwide",
      "Federal law preempts state law on therapist disclosure duties",
      "Only psychiatrists, as physicians, carry Tarasoff duties"
    ],
    "correct": "It varies by state: mandatory in many, permissive in some, absent in a few",
    "answer": "There is no single national duty. Roughly: ~23 states mandate warn/protect by statute, ~10 via common law, ~11 are permissive (may disclose without liability), and a handful give no guidance. Tarasoff was a California case whose logic spread unevenly — 'what does Tarasoff require?' has 50 answers.",
    "type": "mcq",
    "source_page": "wiki/concept-duty-to-warn.md",
    "topic": "duty-to-warn",
    "cluster": "duty-concepts",
    "bloom_level": "understand"
  },
  {
    "id": "u3-tarasoff-critique-evaluate-01",
    "prompt": "Give the strongest scientific criticism of Tarasoff-type duties, and the professional practice that answers it.",
    "answer": "The duty assumes clinicians can predict violence, but validated tools for predicting dangerousness are lacking — the law demands foresight the science doesn't reliably deliver (this was the dissent's worry and remains true). The answer in practice: thorough assessment (plan/means/intent/history, review prior records per Jablonski), consultation with colleagues, and documentation — converting individual judgment into the professional standard of care. Secondary critique: the duty may deter dangerous clients from disclosing or seeking treatment at all; evidence on that chilling effect is thin either way.",
    "type": "explain",
    "source_page": "wiki/study-tarasoff.md",
    "topic": "duty-to-warn",
    "cluster": "duty-concepts",
    "bloom_level": "evaluate"
  },
  {
    "id": "u3-threat-stance-vignette-01",
    "prompt": "Session, minute 40: 'I swear, if I see him with her again I'm going to put him in the ground. I have my brother's gun.' Your gut says smooth it over ('I'm sure you don't mean that'). Why is that the wrong move, and what is the right first move?",
    "answer": "Minimizing forecloses assessment — if he means it you've closed the door, taught him threats end conversations, and done zero protective work. Right first move: take it seriously and ASSESS, staying in relationship: reflect the affect ('that's a lot of rage'), then ask directly about plan, means, intent, timeline. Recall the pre-disclosed limit ('you remember I said if someone were in real danger I'd have to act') and work collaboratively toward protective steps. Then consult and document. The stance skill: you can be warm and be the person who takes threats seriously — those aren't in tension; they're the job.",
    "type": "vignette",
    "source_page": "wiki/concept-duty-to-warn.md",
    "topic": "duty-to-warn",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "apply"
  }
]
```

## Mandated reporting

```json
[
  {
    "id": "u3-reporting-trigger-cloze-01",
    "prompt": "Mandated reporting is triggered by reasonable {{suspicion}} of abuse or neglect — not proof, and not the counselor's own investigation.",
    "answer": "suspicion",
    "type": "cloze",
    "source_page": "wiki/concept-mandated-reporting.md",
    "topic": "mandated-reporting",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "remember"
  },
  {
    "id": "u3-reporting-mechanics-recall-01",
    "prompt": "For mandated reporting, state: who is protected, how fast you must act, what protects you if you're wrong, and what happens if you fail to report.",
    "answer": "Protected: children (all 50 states + DC) and, in most states, elder/dependent/vulnerable adults. Timing: immediate — typically an oral report within 24–48 hours, written follow-up per state law. Protection: good-faith immunity in every state, even for unfounded reports. Failure: criminal charges (misdemeanor up to felony), fines/jail, civil liability for subsequent harm, licensure consequences.",
    "type": "recall",
    "source_page": "wiki/concept-mandated-reporting.md",
    "topic": "mandated-reporting",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "remember"
  },
  {
    "id": "u3-report-vs-warn-compare-01",
    "prompt": "The classic Unit 3 confusion: mandated reporting vs. duty to warn/protect. Contrast them on legal source, who is protected, trigger standard, and how much discretion you have.",
    "answer": "Mandated reporting: statutory in all 50 states; protects children and vulnerable adults; triggered by reasonable suspicion of abuse/neglect; essentially NO discretion — suspicion → report to CPS/APS (a bright-line rule; the legislature already made the call). Duty to warn/protect: case-law/statute varying by state (mandatory/permissive/silent); protects an identifiable third party from client violence; triggered by a serious, foreseeable threat; substantial clinical judgment in assessing and choosing protective steps (a standard, not a rule).",
    "type": "compare",
    "source_page": "wiki/concept-mandated-reporting.md",
    "topic": "mandated-reporting",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-reporting-hesitate-vignette-01",
    "prompt": "Your client describes her boyfriend 'disciplining' her 7-year-old with a belt, leaving marks. You think: 'I should explore this for a few more sessions first — I don't have proof, and reporting will destroy our alliance.' Name both errors.",
    "answer": "Error 1: the trigger is reasonable suspicion, not proof — marks from a belt is well past the threshold, and investigating first is not your job (it's CPS's) and delays a legally immediate duty; waiting is itself a violation. Error 2: alliance-protection reasoning inverts the duty — the child's safety is not yours to trade against rapport, and a well-handled honest report usually survives relationally, while a concealed one rarely does.",
    "type": "vignette",
    "source_page": "wiki/concept-mandated-reporting.md",
    "topic": "mandated-reporting",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "apply"
  },
  {
    "id": "u3-reporting-alliance-stance-01",
    "prompt": "You must report what your client disclosed about her son's treatment. Describe how to handle the conversation so the report is made AND the relationship has its best chance of surviving.",
    "answer": "Tell her directly, unless doing so would endanger the child. Moves: recall the pre-disclosed limit ('you remember I said the law requires me to report when a child may be being hurt'); name the duty plainly without apologizing for the law or blaming her; offer to make the call together in session; recommit to the work ('this doesn't end our work — I'm still in your corner'); talk through what happens next. Avoid the avoidant path (report secretly, hope it never surfaces) — discovered concealment is the alliance-killer, not the report.",
    "type": "explain",
    "source_page": "wiki/concept-mandated-reporting.md",
    "topic": "mandated-reporting",
    "cluster": "confidentiality-exceptions",
    "bloom_level": "evaluate"
  }
]
```

## Boundaries and dual relationships

```json
[
  {
    "id": "u3-dual-5year-cloze-01",
    "prompt": "ACA A.5.c prohibits sexual/romantic relationships with former clients (and their partners or family members) for {{5 years}} after the last professional contact — and even then requires documented forethought that it isn't exploitive.",
    "answer": "5 years",
    "type": "cloze",
    "source_page": "wiki/concept-dual-relationships.md",
    "topic": "boundaries",
    "cluster": "boundary-concepts",
    "bloom_level": "remember"
  },
  {
    "id": "u3-crossing-violation-compare-01",
    "prompt": "Boundary crossing vs. boundary violation: define each, give an example of each, and name the heuristic question that separates them.",
    "answer": "Crossing: a departure from standard practice that is not harmful or exploitative and may even serve the work — e.g., shaking an offered hand, extending a session for a client in crisis, attending a client's graduation (documented). Violation: a departure that harms or exploits the client or puts the work at serious risk — e.g., sexual contact, business deals with clients. Heuristic: WHOSE NEED does this meet? Crossings serve the client's interest; violations serve the counselor's.",
    "type": "compare",
    "source_page": "wiki/concept-dual-relationships.md",
    "topic": "boundaries",
    "cluster": "boundary-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-boundary-discrim-mcq-01",
    "prompt": "Which of these is best classified as a (potentially appropriate) boundary CROSSING rather than a violation, per the 2014 ACA Code's managed-boundaries approach?",
    "options": [
      "Attending a long-term client's college graduation, with rationale documented beforehand",
      "Going into a real-estate partnership with a current client",
      "Following a current client's personal Instagram from your personal account",
      "Beginning a romantic relationship two years after termination"
    ],
    "correct": "Attending a long-term client's college graduation, with rationale documented beforehand",
    "answer": "A.6.b treats attending a client's formal ceremony as a boundary EXTENSION that may benefit the client — permitted with risk-benefit thinking, consent, and prior documentation (A.6.c). The others: business enmeshment (exploitative violation), A.5.e's prohibited personal virtual relationship, and a violation of the 5-year rule (A.5.c — two years is the APA code's number, a classic distractor).",
    "type": "mcq",
    "source_page": "wiki/concept-dual-relationships.md",
    "topic": "boundaries",
    "cluster": "boundary-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-rural-apply-01",
    "prompt": "You're the only licensed counselor in a town of 2,400. Your new client bags your groceries; her aunt teaches your daughter's class. Older ethics advice said 'avoid all dual relationships.' What's the modern standard, and what does managing this look like concretely?",
    "answer": "Unavoidable overlap is managed, not merely avoided — refusing every overlapping client would deny the town care. Concretely: name the overlap openly and early (an informed-consent conversation: 'we'll run into each other — here's how I handle it: I won't greet you first; nothing from out there comes in here unless you bring it'); minimize additional role mixing; consult; document the reasoning (A.6). The bright lines (A.5: sexual/romantic, exploitative roles) don't bend for geography.",
    "type": "vignette",
    "source_page": "wiki/concept-dual-relationships.md",
    "topic": "boundaries",
    "cluster": "boundary-concepts",
    "bloom_level": "apply"
  },
  {
    "id": "u3-slippery-slope-explain-01",
    "prompt": "Why does A.6.c require documenting a boundary extension BEFORE the interaction (when feasible)? Connect it to how violations actually develop.",
    "answer": "Violations rarely begin as violations — they develop by slippery slope: small, unexamined crossings that drift toward exploitation. Writing the rationale, expected benefit, and anticipated consequences down in advance forces the examination the drift depends on skipping: if you can't write a client-centered rationale, you've just learned whose need the extension serves. It also creates the record showing your judgment process if harm occurs (with an obligation to attempt remedy).",
    "type": "explain",
    "source_page": "wiki/concept-dual-relationships.md",
    "topic": "boundaries",
    "cluster": "boundary-concepts",
    "bloom_level": "understand"
  }
]
```

## Scope of practice & competence

```json
[
  {
    "id": "u3-scope-competence-compare-01",
    "prompt": "Scope of practice vs. competence: who draws each fence, what question does each answer, and give an example of being inside one but outside the other.",
    "answer": "Scope of practice is drawn by LAW (the license statute): 'may a counselor do this at all?' — e.g., no LPC may prescribe. Competence is drawn by ETHICS (C.2, your own training): 'may I do this?' — based on education, training, supervised experience, credentials. Inside-scope/outside-competence example: an adult-trained LPC taking on a 6-year-old play-therapy case — perfectly legal, ethically out of bounds. That's the subtler, more common failure.",
    "type": "compare",
    "source_page": "wiki/concept-scope-of-practice.md",
    "topic": "competence",
    "cluster": "duty-concepts",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-c2b-newspecialty-recall-01",
    "prompt": "Per C.2.b, what three things must precede practicing in a specialty area new to you — and what is explicitly NOT a substitute for them?",
    "answer": "Appropriate education, training, and SUPERVISED EXPERIENCE (while developing the skill, you also take steps to ensure work quality and protect others from harm). Not substitutes: enthusiasm, having read the book, a weekend webinar certificate, or 'learning on the client.' In clinical work, unsupervised self-teaching is itself the ethics violation.",
    "type": "recall",
    "source_page": "wiki/concept-scope-of-practice.md",
    "topic": "competence",
    "bloom_level": "remember"
  },
  {
    "id": "u3-values-referral-vignette-01",
    "prompt": "A counselor tells his supervisor: 'This client is in a same-sex marriage and that conflicts with my faith — I'd like to refer him out.' The client's presenting problem is workplace anxiety, well within the counselor's training. How does the 2014 ACA Code rule on this, and what's the principle?",
    "answer": "Not permitted. The 2014 Code (A.4.b personal values; A.11.b values within termination/referral — post-Ward v. Wilbanks) prohibits referrals based solely on the counselor's personally held values, attitudes, or beliefs about a client's identity or behavior. Counselors refer for lack of SKILL, never lack of approval — and are expected to seek training/consultation to work with clients who differ from them. Values-based referral is discrimination wearing referral's clothes; this is heavily tested.",
    "type": "vignette",
    "source_page": "wiki/concept-scope-of-practice.md",
    "topic": "competence",
    "bloom_level": "apply"
  },
  {
    "id": "u3-impairment-vignette-01",
    "prompt": "Mid-divorce, a counselor is drinking most nights, canceling sessions, and catching himself not listening. 'My clients need me — taking a leave would abandon them,' he reasons. What does C.2.g actually require, and what's wrong with his framing?",
    "answer": "C.2.g requires counselors to monitor themselves for impairment and REFRAIN from providing services while impaired — seek help, and if needed limit, suspend, or terminate the practice (with proper transfer, which is the opposite of abandonment; A.11 governs). His framing treats self-care as selfishness, but impaired care IS the harm — nonmaleficence attaches to sessions delivered while unable to function, not to the responsibly-managed pause. Counselor self-care is an ethical competency (this thread returns in Unit 8).",
    "type": "vignette",
    "source_page": "wiki/concept-scope-of-practice.md",
    "topic": "competence",
    "bloom_level": "apply"
  },
  {
    "id": "u3-multicultural-floor-cloze-01",
    "prompt": "C.2.a lists one competency as required across ALL counseling specialties rather than being a specialty itself: {{multicultural counseling competency}}.",
    "answer": "multicultural counseling competency",
    "type": "cloze",
    "source_page": "wiki/concept-scope-of-practice.md",
    "topic": "competence",
    "bloom_level": "remember"
  }
]
```

## The helping professions

```json
[
  {
    "id": "u3-professions-prescribe-mcq-01",
    "prompt": "Your client's depression isn't budging and she asks about medication. In most states, which professionals could evaluate and prescribe? (Select the best answer.)",
    "options": [
      "A psychiatrist or a psychiatric-mental-health nurse practitioner",
      "Any doctoral-level psychologist",
      "Her LPC, with a supervising physician's sign-off",
      "An LCSW with psychopharmacology training"
    ],
    "correct": "A psychiatrist or a psychiatric-mental-health nurse practitioner",
    "answer": "Psychiatrists (MD/DO) prescribe everywhere; PMHNPs prescribe in every state and handle much real-world medication management; primary-care physicians actually write most psychotropic prescriptions. Psychologists prescribe only with special postdoctoral training in a handful of states (~7 as of 2024–25). Counselors and social workers prescribe nowhere; there is no 'sign-off' pathway.",
    "type": "mcq",
    "source_page": "wiki/concept-helping-professions-compared.md",
    "topic": "helping-professions",
    "cluster": "the-helping-professions",
    "bloom_level": "apply"
  },
  {
    "id": "u3-professions-testing-mcq-01",
    "prompt": "A school asks for a full evaluation of a 9-year-old for a learning disability and possible ADHD, including IQ and neuropsychological testing. Whose distinctive turf is this?",
    "options": [
      "A clinical/school psychologist (doctoral-level)",
      "A licensed professional counselor",
      "A licensed clinical social worker",
      "A psychiatrist"
    ],
    "correct": "A clinical/school psychologist (doctoral-level)",
    "answer": "Formal psychological assessment — IQ, personality, neuropsychological testing — is largely the psychologist's distinctive function (doctoral training is heavy on psychometrics). Counselors and LCSWs use screening tools; psychiatrists do medical evaluation and prescribing. Referral fluency means knowing these distinctive functions.",
    "type": "mcq",
    "source_page": "wiki/concept-helping-professions-compared.md",
    "topic": "helping-professions",
    "cluster": "the-helping-professions",
    "bloom_level": "apply"
  },
  {
    "id": "u3-professions-lens-compare-01",
    "prompt": "An LPC and an LCSW may run indistinguishable therapy hours. Contrast the professions' signature lenses and training centers of gravity anyway — and name the LCSW's structural advantage for complex-needs clients.",
    "answer": "Counseling (LPC): wellness, development, prevention — grew from the guidance/vocational and humanistic traditions; the person navigating problems of living. Social work (LCSW): person-in-environment — the individual embedded in systems and resources; training includes advocacy and case management alongside therapy. Structural advantage: for clients who need housing, benefits, elder services, or discharge coordination WITH their therapy, the LCSW's case-management training is purpose-built.",
    "type": "compare",
    "source_page": "wiki/concept-helping-professions-compared.md",
    "topic": "helping-professions",
    "cluster": "the-helping-professions",
    "bloom_level": "analyze"
  },
  {
    "id": "u3-professions-paths-recall-01",
    "prompt": "For each profession, name the degree and the typical post-degree licensure requirement: professional counselor, psychologist, clinical social worker, psychiatrist.",
    "answer": "Counselor: master's in counseling (CACREP-accredited standard) → ~2 years supervised practice + exam (NCE/NCMHCE) → LPC/LMHC. Psychologist: doctorate (PhD/PsyD/EdD, 4–6 yrs + internship) → 1–2 years supervised practice + EPPP. Clinical social worker: MSW (~2 yrs) → ~2–3 years supervised clinical work + exam → LCSW. Psychiatrist: MD/DO → 3–4 year psychiatry residency → medical license/board certification.",
    "type": "recall",
    "source_page": "wiki/concept-helping-professions-compared.md",
    "topic": "helping-professions",
    "cluster": "the-helping-professions",
    "bloom_level": "remember"
  },
  {
    "id": "u3-rxp-recall-01",
    "prompt": "Name the first two RxP states (with rough dates) and the training required for a psychologist to prescribe there. Why should you hold the full state list loosely?",
    "answer": "New Mexico (2002, first) and Louisiana (2004). Training: a postdoctoral master's in clinical psychopharmacology, supervised practice hours, and a national psychopharmacology exam. Hold the list loosely because it's a moving legislative target — Illinois, Iowa, Idaho followed, then Colorado (2023) and Utah (2024), ~7 states as of 2024–25, plus DoD/USPHS/Indian Health Service — and bills are pending elsewhere.",
    "type": "recall",
    "source_page": "wiki/concept-helping-professions-compared.md",
    "topic": "helping-professions",
    "cluster": "the-helping-professions",
    "bloom_level": "remember"
  }
]
```
