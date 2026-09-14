# Elective module items — Supporting Survivors of Sexual Abuse & Assault

Source of truth for this **elective/ad-hoc module** (off-spine; `aux-` namespace). Each fenced
`json` block is a JSON array merged by `apps/build_items.py` into `build/items.json`. Items span
Bloom levels and lean hard toward **application + stance**, per the generate rules in
[`../CLAUDE.md`](../CLAUDE.md) — this is material where knowing the definition and still saying the
wrong sentence is the characteristic failure.

Clusters: `sexual-violence-definitions`, `csa-dynamics`, `disclosure-response`,
`sexual-trauma-effects`, `reporting-pathways`, `sexual-trauma-treatments`, `survivor-support`.
Item id prefix: `ax-sas-`.

**Two deliberate emphases.** (1) A large share of items are **negative-space items** — what *not* to
say, ask, or do — because the documented harms here come from well-meant action, not from ignorance
of facts. (2) The **contested** material (CSAAS, self-blame taxonomy, memory fragmentation, recovered
memory, Title IX status) is quizzed at evaluate level rather than smoothed away; if a session
surfaces confusion between "what the framework claims" and "what the evidence supports," that is the
intended discrimination.

**Not covered here by design:** general trauma-informed-care content (SAMHSA's three E's, four R's,
six principles, re-traumatization, trauma-informed vs. trauma-focused). Those items live with Unit 8's
`concept-trauma-informed-care` and are expected to move to a dedicated trauma-informed-care unit.

## Cluster: sexual-violence-definitions

```json
[
  {
    "id": "ax-sas-cdc-definition-cloze-01",
    "prompt": "The CDC defines sexual violence as sexual activity when consent is {{not obtained or freely given}}.",
    "answer": "not obtained or freely given",
    "type": "cloze",
    "source_page": "wiki/concept-sexual-violence-scope.md",
    "topic": "sv-definition",
    "cluster": "sexual-violence-definitions",
    "bloom_level": "remember"
  },
  {
    "id": "ax-sas-consent-voids-recall-01",
    "prompt": "Name the three conditions that void consent regardless of what a person said, and give the clinical reason the third one matters most for self-blame.",
    "answer": "1) Force or threat (physical force, weapons, threats to the person or others); 2) Coercion (pressure, manipulation, blackmail, abuse of authority — a yes obtained by making refusal costly is not freely given); 3) Incapacity (unconscious, asleep, substantially impaired by alcohol or drugs, or below the legal age of consent). Incapacity matters most for self-blame because a survivor who was drinking often concludes their own intoxication disqualifies them, blames themselves before anyone else gets the chance, and may never use the word 'assault' — presenting instead with depression, insomnia, or relationship problems.",
    "type": "recall",
    "source_page": "wiki/concept-sexual-violence-scope.md",
    "topic": "consent",
    "cluster": "sexual-violence-definitions",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-made-to-penetrate-understand-01",
    "prompt": "What is the CDC category 'made to penetrate,' and why does a counselor who doesn't know it listen worse?",
    "answer": "'Made to penetrate' is a distinct category of contact sexual violence in which the person was forced to penetrate someone else — CDC puts its lifetime prevalence at about 1 in 26 men. It is invisible in legal definitions that define rape solely as being penetrated. A counselor whose mental model of rape is only penetrative assault OF a victim may hear a man describe being forced to penetrate someone and fail to name it as sexual assault — which is precisely the invalidation male survivors report, and part of why they commonly take decades to tell anyone.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-violence-scope.md",
    "topic": "sv-categories",
    "cluster": "sexual-violence-definitions",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-prevalence-apply-01",
    "prompt": "A colleague says 'about half of women have been raped — the CDC says so.' Correct this precisely, using the right figures and the right survey.",
    "answer": "The figure is conflated. CDC's NISVS (2016/2017 data) puts CONTACT SEXUAL VIOLENCE — an umbrella covering rape, being made to penetrate, sexual coercion, and unwanted sexual contact — at nearly half of women. COMPLETED OR ATTEMPTED RAPE is more than 1 in 5 women. For men: more than 1 in 6 for contact sexual violence, 1 in 31 for completed or attempted rape, 1 in 26 made to penetrate. The category structure is not pedantry — quoting the umbrella figure as a rape figure is the kind of error that gets the whole claim dismissed.",
    "type": "vignette",
    "source_page": "wiki/concept-sexual-violence-scope.md",
    "topic": "prevalence",
    "cluster": "sexual-violence-definitions",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-nisvs-vs-ncvs-compare-01",
    "prompt": "CDC's NISVS and BJS's NCVS report different numbers for sexual violence and never reconcile. Compare what each measures, and state what a careful person concludes from the discrepancy.",
    "answer": "NISVS (CDC) is a public-health surveillance survey measuring BEHAVIORALLY-DEFINED experiences via random-digit-dial telephone self-report of non-institutionalized adults — it asks what happened to you, not whether you considered it a crime. NCVS (BJS) is a criminal-victimization survey measuring CRIME-FRAMED incidents, and is the source of reporting-rate data (46% of rape/sexual assaults reported to police in 2023, ±8.2%). They measure different constructs, so their numbers differ by design. The conclusion is NOT that one is wrong or that the figures are unreliable — it is a definitional gap, not a contradiction. The practical rule: quote the survey with the number, or don't quote the number.",
    "type": "compare",
    "source_page": "wiki/concept-sexual-violence-scope.md",
    "topic": "prevalence",
    "cluster": "sexual-violence-definitions",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-known-perpetrator-analyze-01",
    "prompt": "About 90% of child sexual abuse is perpetrated by someone known and trusted by the child or family, and the adult pattern runs the same direction. Name four things about survivor behavior this single fact explains.",
    "answer": "1) Delayed disclosure — telling means accusing someone the family loves and depends on, not reporting a stranger. 2) Survivors protecting the person who harmed them — the relationship is real and often still needed. 3) Why 'why didn't you just leave' misunderstands the situation — the person is embedded in the survivor's life, home, or family. 4) Why assault by a partner or friend can be HARDER to name than stranger assault — there's no cultural script for it and the person remains in your life. It also dismantles the stranger-in-an-alley model that makes counselors slower to recognize a disclosure that doesn't match it.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-violence-scope.md",
    "topic": "perpetrator-known",
    "cluster": "sexual-violence-definitions",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-trans-data-evaluate-01",
    "prompt": "A student notes that NISVS reports no national sexual violence estimates for transgender people and concludes the data suggest lower risk in that population. What's wrong with the inference, and what is the honest statement?",
    "answer": "It infers a finding from a measurement gap. CDC states the 2016/2017 NISVS sample was TOO SMALL to produce reliable national estimates for transgender people — that is a limitation of the instrument, not evidence about prevalence. The honest statement is 'we don't have good national numbers for this population,' not 'the data suggest lower risk.' This generalizes: absence of evidence in a survey with a stated sampling limitation is not evidence of absence, and it is a common way advocacy-adjacent statistics get misread in both directions.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-violence-scope.md",
    "topic": "prevalence",
    "cluster": "sexual-violence-definitions",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-sas-victim-survivor-evaluate-01",
    "prompt": "A client refers to herself as a 'victim.' Your training materials emphasize the word 'survivor.' What do you do, and what principle decides it?",
    "answer": "Use her word. Both terms are in legitimate professional use and neither is universally correct: 'victim' is the legal/criminological term and is precise about harm done by someone else; 'survivor' emphasizes agency and continuation; some people reject both. Correcting someone's word for their own experience is a small act of taking over — and this module's central mechanism is that a good response RETURNS control rather than removing it (Ullman: positive reactions predict perceived control, which predicts fewer PTSD symptoms). The terminology rule is that mechanism applied to vocabulary. If you don't know their word yet, describe rather than label: 'what happened to you,' 'the assault,' or their own phrasing.",
    "type": "vignette",
    "source_page": "wiki/concept-sexual-violence-scope.md",
    "topic": "terminology",
    "cluster": "sexual-violence-definitions",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: csa-dynamics

```json
[
  {
    "id": "ax-sas-csa-contact-cloze-01",
    "prompt": "CDC's definition of child sexual abuse — involving a person under 18 in sexual activity they cannot comprehend or consent to — notably does {{not}} require physical contact.",
    "answer": "not",
    "type": "cloze",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "csa-definition",
    "cluster": "csa-dynamics",
    "bloom_level": "remember"
  },
  {
    "id": "ax-sas-grooming-stages-recall-01",
    "prompt": "Name the five stages of sexual grooming, and identify which one adults most often miss.",
    "answer": "1) Victim selection (accessible, often isolated or poorly supervised); 2) Gaining access and isolating (engineering time alone, often via a legitimizing role — coach, tutor, relative, youth leader); 3) Developing trust with the child AND with the protective adults; 4) Desensitization to touch and sexual content (an escalating gradient); 5) Post-abuse maintenance of compliance and secrecy (affection, gifts, shared-secret framing, blame, or threat). Stage 3 is the one adults miss: the PARENTS are groomed too. The perpetrator becomes the helpful, generous, reliable adult the family is grateful for — which is exactly what makes the later disclosure unbelievable and the family's first instinct to defend him.",
    "type": "recall",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "grooming",
    "cluster": "csa-dynamics",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-grooming-gradient-apply-01",
    "prompt": "An adult survivor says, 'I don't understand why I didn't stop it. There were a hundred chances.' Using what's known about grooming, what do you say?",
    "answer": "The gradient is the answer: desensitization escalates in steps small enough that no single step presents itself as the moment to refuse. There was never a discrete instance where an obviously wrong thing was proposed and could be declined — that's the mechanism, not a failure of nerve. Grooming also manufactures a felt complicity (accepting gifts, keeping the secret, feeling affection for the person), which is where the shame comes from; the child was not a participant, they were engineered. Empirically grooming is near-universal: 99% of adult CSA survivors endorse at least one grooming behavior, averaging around 14. Naming the process is often what loosens the self-blame.",
    "type": "vignette",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "grooming",
    "cluster": "csa-dynamics",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-disclosure-process-understand-01",
    "prompt": "Explain what 'disclosure is a process, not an event' means for child sexual abuse, and why the expectation of an event harms children.",
    "answer": "Systematic review evidence (33 studies, 2000–2016) finds children commonly delay, disclose partially, test the water with an indirect or nonverbal hint first, and retreat if that hint lands badly — with barriers at every ecological level (individual shame and lack of words; family loyalty and dependence; community lack of privacy; cultural taboo, honor, and disbelief of children). So a delayed, fragmentary, inconsistent disclosure is the NORMAL presentation. The harm: adults who expect a single complete consistent account read the normal course as fabrication, and the child — who was testing whether it was safe to say more — gets their answer and stops.",
    "type": "explain",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "csa-disclosure",
    "cluster": "csa-dynamics",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-csaas-components-mcq-01",
    "prompt": "Of CSAAS's five components, which one did the New Jersey Supreme Court in State v. J.L.G. (2018) carve out as retaining independent scientific support, even while holding CSAAS testimony generally inadmissible?",
    "answer": "Delayed disclosure. Independent empirical work (London, Bruck, Ceci & Shuman) supports secrecy and delayed, partial disclosure as real and common. Routine RETRACTION is the component that failed — most children who disclose in a competent interview do not later recant. The court's split mirrors the evidence: keep the disclosure dynamics, discard the syndrome as a detector.",
    "options": [
      "Retraction",
      "Delayed disclosure",
      "Entrapment and accommodation",
      "Helplessness"
    ],
    "correct": "Delayed disclosure",
    "type": "mcq",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "csaas",
    "cluster": "csa-dynamics",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-csaas-falsifiability-evaluate-01",
    "prompt": "State the structural objection to using CSAAS as evidence that abuse occurred — the one that is independent of whether any individual component is empirically supported.",
    "answer": "As applied, CSAAS is not falsifiable. If a child discloses, that is consistent with abuse; if the child does not disclose, that is secrecy and accommodation; if the child recants, that is retraction. A framework in which every possible behavior confirms the hypothesis cannot DISCRIMINATE abused from non-abused children, and therefore cannot be evidence that abuse occurred. This is why peer-reviewed forensic-psychiatry critique (JAAPL) and an increasing line of appellate decisions reject it for that purpose — and Summit himself objected to its use as proof. Note the objection survives even for the components that ARE supported: delayed disclosure is real AND still cannot establish that a particular child was abused.",
    "type": "explain",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "csaas",
    "cluster": "csa-dynamics",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-sas-csaas-compare-01",
    "prompt": "Compare the half of CSAAS that survived empirical scrutiny with the half that did not, and state what a counselor should carry from each.",
    "answer": "SURVIVED: secrecy and delayed, partial disclosure. Independently supported by disclosure research and explicitly carved out by the New Jersey Supreme Court in J.L.G. Carry these — they tell you that a delayed, fragmentary disclosure is the normal course, not a suspicious one. DID NOT SURVIVE: routine recantation. London, Bruck, Ceci & Shuman found most children who disclose in a competent interview do NOT later retract; recantation happens (and family pressure raises it) but is not the expected course, and teaching it as expected was the most damaging part of the model. ALSO DISCARD: CSAAS as a detector of abuse — it is a clinical description, never a validated diagnostic instrument, and cannot discriminate abused from non-abused children. Summary: hold the disclosure dynamics, drop the syndrome.",
    "type": "compare",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "csaas",
    "cluster": "csa-dynamics",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-warning-signs-analyze-01",
    "prompt": "A school counselor wants a checklist of behavioral warning signs to identify sexually abused children. What's wrong with the request, and what is the closest thing to a specific indicator?",
    "answer": "No behavioral indicator or set of indicators is specific enough to diagnose CSA. The plausible signs — sleep problems, withdrawal, regression, school decline — overlap with a dozen ordinary childhood stressors, so a checklist generates false positives (harming families) and false confidence. It's the same falsifiability failure as CSAAS in miniature. The closest thing to a specific indicator is sexualized behavior well outside developmental norms — and it is still not proof. The right posture is not detection but availability: be an adult a child could tell, respond well when they do, and report on reasonable suspicion rather than trying to reach certainty first.",
    "type": "vignette",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "csa-indicators",
    "cluster": "csa-dynamics",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-contamination-apply-01",
    "prompt": "A nine-year-old tells you during a session that her uncle 'does stuff' when he babysits. Your instinct is to gently establish what happened so your report is credible. Why is that instinct wrong, and what do you do instead?",
    "answer": "Questioning contaminates the forensic interview. A forensic interview at a Children's Advocacy Center is a single recorded conversation by a trained neutral interviewer using a standardized protocol, structured to gather the account WITHOUT shaping it — and by the time a child reaches the CAC they may already have recounted the allegation to as many as six untrained adults, each likely asking leading questions a trained interviewer is trained to avoid, letting a defense argue the account was tainted before anyone qualified heard it. Instead: receive, don't develop. Let her use her own words, don't supply names or details or ask 'did he touch you here?', don't press for more, don't ask her to repeat it for someone else, write down what she said IN HER WORDS as soon as you can, stay visibly calm, never promise secrecy — and report on reasonable suspicion, which is the standard. You are not required to be sure.",
    "type": "vignette",
    "source_page": "wiki/concept-child-sexual-abuse.md",
    "topic": "forensic-interview",
    "cluster": "csa-dynamics",
    "bloom_level": "apply"
  }
]
```

## Cluster: disclosure-response

```json
[
  {
    "id": "ax-sas-ullman-mechanism-recall-01",
    "prompt": "State Ullman's core finding about social reactions to sexual assault disclosure, including the mediator — and explain why the mediator is what makes the finding clinically usable.",
    "answer": "Social reactions to disclosure predict PTSD symptoms: negative reactions predict MORE symptoms; positive reactions predict greater PERCEIVED CONTROL OVER RECOVERY, which in turn predicts FEWER symptoms. Perceived control is the mediator. That's what makes it usable: it isn't that sympathy soothes, it's that a good response RETURNS control to a person whose control was taken. Sexual violence removes control over one's own body, so a response that takes further decisions away — even kindly, even protectively — replays the injury. Every practice rule in the module derives from this one mechanism.",
    "type": "recall",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "social-reactions",
    "cluster": "disclosure-response",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-three-sentences-cloze-01",
    "prompt": "The three core sentences for receiving a disclosure: 'I {{believe}} you,' 'It's not your {{fault}},' and 'Thank you for {{telling me}}.'",
    "answer": "believe / fault / telling me",
    "type": "cloze",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "what-to-say",
    "cluster": "disclosure-response",
    "bloom_level": "remember"
  },
  {
    "id": "ax-sas-negative-reactions-compare-01",
    "prompt": "Compare the two empirically distinct types of negative social reaction to a sexual assault disclosure. Which is more damaging, and why does the split matter for helpers specifically?",
    "answer": "TURNING AGAINST: overtly negative responses aimed at the survivor — blaming, doubting, questioning their account, stigmatizing, treating them as damaged or different now, pulling away. UNSUPPORTIVE ACKNOWLEDGMENT: responses that acknowledge the assault but fail the person — distraction, changing the subject, TAKING CONTROL and making decisions for them, egocentric responses ('I can't handle this'). Turning Against is more strongly predictive of PTSD. Why the split matters for helpers: 'taking control' is classified as a NEGATIVE reaction, not a neutral one. The person who immediately calls the police, books the appointment, drives them to the hospital, or tells the family without asking is delivering a measured harm while feeling helpful — which is the failure mode competent, caring people are most prone to.",
    "type": "compare",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "social-reactions",
    "cluster": "disclosure-response",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-harmful-questions-analyze-01",
    "prompt": "'Are you sure?', 'Why didn't you fight back?', 'What were you wearing?', 'Why didn't you report it sooner?' — name the structure these share, and give the specific counter-evidence for the second and fourth.",
    "answer": "Shared structure: each transfers scrutiny from the person who did it to the person it was done to. They investigate the survivor. Counter-evidence for 'why didn't you fight back?': tonic immobility — in the key prospective study of 298 assaulted women, 70% reported significant and 48% extreme involuntary motor inhibition during the assault. Resistance usually wasn't available. Counter-evidence for 'why didn't you report it sooner?': delayed and partial disclosure is the empirically normal course (London et al.; Alaggia et al.), not the suspicious one; for male survivors the delay is commonly two decades or more. Both questions presuppose a behavior that the evidence says is the exception, and punish the person for the rule.",
    "type": "explain",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "what-not-to-say",
    "cluster": "disclosure-response",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-believe-not-investigate-evaluate-01",
    "prompt": "A supervisor argues that saying 'I believe you' compromises clinical neutrality — you can't know what happened. Resolve the tension.",
    "answer": "The argument conflates two different claims. 'I believe you' is not a forensic conclusion about what occurred; it is a statement that you take the person seriously, treat their account as their account, and do not require them to prove themselves before receiving help. That is fully compatible with not knowing — and not being able to know — what happened. What it is NOT compatible with is interrogation. The real error the supervisor's position invites is role-switching: a counselor who responds by gathering details, checking consistency, and reserving judgment pending evidence has silently moved from a therapeutic role into a forensic one, is untrained for it, and cannot avoid contaminating the account. You are not a fact-finder. The evidence this matters inside therapy: over a third of CSA survivors report harmful therapist responses — disbelief, belittlement, blame — predicting the abuse staying hidden, alliance damage, and dropout.",
    "type": "explain",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "believe-dont-investigate",
    "cluster": "disclosure-response",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-sas-dont-ask-narrative-understand-01",
    "prompt": "Why should you NOT say 'tell me what happened' when an adult client discloses a sexual assault — and what do you do if they start telling you anyway?",
    "answer": "Two reasons. (1) Pressing for the narrative re-enacts the loss of control the assault created — the survivor is again being required to produce something for someone else. (2) Detailed retelling is not what makes people better; that work belongs in trauma treatment, with a trained clinician, when the person is ready (Herman's Stage 2), not at first disclosure. If nothing is volunteered, nothing is missing. If they DO start telling you: receive it without flinching and without redirecting — stopping them mid-disclosure communicates that it's too much for you, which is its own harm. The rule is don't ASK, not don't LISTEN.",
    "type": "explain",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "believe-dont-investigate",
    "cluster": "disclosure-response",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-taking-over-vignette-01",
    "prompt": "A client discloses she was assaulted two nights ago. You say how sorry you are, tell her she needs to go to the hospital tonight for a forensic exam, offer to call the police from your office, and book her a follow-up for tomorrow. Evaluate this response.",
    "answer": "Warm, competent, and harmful. Every action after the expression of sympathy takes a decision away from her — and 'taking control and making decisions for them' is classified as a NEGATIVE social reaction (Unsupportive Acknowledgment), not a neutral one. The injury was the removal of control over her own body and life; a decisive rescue reproduces that structure. Pressure to report is specifically identified as retraumatizing. The corrected version: 'I believe you. It's not your fault. Thank you for telling me.' Then hand control back — 'What would be helpful right now?' — and be willing to hear 'I don't know.' Then INFORM without deciding: there is a medical forensic exam available, having it does not obligate her to report, she can decline any part of it and still get care, and there's a time window worth checking. Give her the local rape crisis center number. Let her choose.",
    "type": "vignette",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "taking-control",
    "cluster": "disclosure-response",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-counselor-reaction-analyze-01",
    "prompt": "Name the two opposite failure modes in a counselor's own visible reaction to a disclosure, and state the target.",
    "answer": "FLINCHING — visible shock, a changed face, a shift in tone — is read instantly as disgust or as 'this is too much for you,' and shuts the disclosure down. OVER-REACTING — tears, outrage, declaring how awful it is — makes the survivor comfort YOU, which is the egocentric response in the Unsupportive Acknowledgment category. The target is steadiness: unhurried, unshocked, unmistakably present. If the material lands on something personal, that's information rather than failure — take it to supervision and your own therapy (vicarious trauma / counselor self-care), not to the client.",
    "type": "recall",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "counselor-reaction",
    "cluster": "disclosure-response",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-child-vs-adult-disclosure-compare-01",
    "prompt": "Compare responding to an adult's disclosure with responding to a child's. What carries over, and what three rules change?",
    "answer": "CARRIES OVER: believe, don't investigate; 'I believe you / it's not your fault / thank you for telling me'; stay steady; don't press for the narrative; hand back what control is available. CHANGES: (1) NEVER PROMISE SECRECY, before or after — for an adult, confidentiality has limits you disclose; for a child, 'promise you won't tell' must be met with 'I can't promise that, but I promise I'll do everything I can to keep you safe, and I'll tell you what I'm doing.' (2) STAY VISIBLY CALM is sharper — a child reads adult shock or anger as directed at THEM and stops talking. (3) DO NOT DEVELOP THE ACCOUNT AT ALL, because untrained questioning contaminates the CAC forensic interview; report on reasonable suspicion (you are not required to be sure) and record the child's own words. The underlying difference: for an adult the constraint is their autonomy; for a child it is a mandatory duty plus an evidentiary chain you can damage.",
    "type": "compare",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "child-vs-adult",
    "cluster": "disclosure-response",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-secondary-victimization-evaluate-01",
    "prompt": "Campbell called it 'the second rape.' What did the research find, and why does it make a referral a clinical act rather than an administrative one?",
    "answer": "Campbell's work on secondary victimization found that most survivors who engaged legal or medical systems did NOT receive needed services, and that system contact left many feeling guilty, depressed, anxious, and reluctant to seek further help — with secondary victimization POSITIVELY CORRELATED with PTSD symptoms. So the systems a survivor turns to for help can themselves inflict measurable harm. That makes WHERE you send someone part of your clinical response, not paperwork: a referral into a harmful process undoes the good response you just gave. It's also the rationale for the SANE/SART model and for rape crisis advocates, whose function is precisely to make the systems less harmful to traverse.",
    "type": "explain",
    "source_page": "wiki/concept-disclosure-response.md",
    "topic": "secondary-victimization",
    "cluster": "disclosure-response",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: sexual-trauma-effects

```json
[
  {
    "id": "ax-sas-tonic-immobility-cloze-01",
    "prompt": "In Möller et al.'s prospective study of 298 women presenting after sexual assault, {{70}}% reported significant tonic immobility and 48% reported extreme tonic immobility during the assault.",
    "answer": "70",
    "type": "cloze",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "tonic-immobility",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "remember"
  },
  {
    "id": "ax-sas-tonic-immobility-recall-01",
    "prompt": "Define tonic immobility and state the three clinical consequences that follow from the evidence on it.",
    "answer": "Tonic immobility is an involuntary, temporary state of motor inhibition under inescapable threat — the body locks. It is not a decision, not compliance, and not consent; it's an evolutionarily conserved defensive response at the far end of the cascade past fight and flight. Consequences: (1) 'Why didn't you fight back?' has an empirical answer — you almost certainly couldn't (70% significant / 48% extreme in the key study). (2) Absence of injury or resistance is NOT evidence that an assault didn't occur — the reasoning 'she didn't fight, so it wasn't really rape' is physiologically wrong. (3) The immobility itself becomes a source of shame — survivors read their own freezing as consent, weakness, or complicity — which makes naming it often the intervention that loosens self-blame.",
    "type": "recall",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "tonic-immobility",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-ti-psychoeducation-apply-01",
    "prompt": "A client says: 'I just lay there. I didn't scream, I didn't fight, I didn't do anything. What does that say about me?' Respond, and name what makes this response an intervention rather than reassurance.",
    "answer": "Something like: 'What you're describing has a name — tonic immobility. Under inescapable threat the body can lock up involuntarily. It isn't a choice and it isn't consent. In the largest study of women presenting after sexual assault, 70% reported significant immobility and nearly half reported extreme immobility. What happened to you is what usually happens.' What makes it an intervention rather than reassurance: it's information, not comfort. It doesn't say 'don't be hard on yourself' — it supplies a fact that directly contradicts the inference she's drawn, targeting BEHAVIORAL self-blame at its premise. This is the highest-yield piece of psychoeducation in the module and requires no trauma-treatment training to deliver.",
    "type": "vignette",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "tonic-immobility",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-self-blame-compare-01",
    "prompt": "Compare behavioral and characterological self-blame, then state precisely what held up and what didn't in Janoff-Bulman's claim about them.",
    "answer": "BEHAVIORAL self-blame attributes to something you DID ('I shouldn't have walked home alone') — a modifiable source, preserving a sense of future control. CHARACTEROLOGICAL self-blame attributes to something you ARE ('I'm the kind of person this happens to') — a non-modifiable source, carrying deservingness. WHAT HELD UP: the distinction itself is clinically useful — it tells you what KIND of blame you're hearing, and they need different responses (behavioral blame is often addressed by information, e.g. tonic immobility; characterological blame is an identity wound and is slower work). WHAT DIDN'T: Janoff-Bulman's claim that behavioral self-blame is ADAPTIVE because it maintains control. Later survivor-sample research (Frazier) found BOTH forms associated with GREATER post-rape depression and distress. Keep the taxonomy, drop the claim that one kind is good for people.",
    "type": "compare",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "self-blame",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-shame-analyze-01",
    "prompt": "Sexual violence produces unusual amounts of shame relative to other traumas. Give the reasons specific to it, and name the disclosure a counselor should be ready for rather than surprised by.",
    "answer": "Reasons: the body was involved; sexuality is already culturally loaded with secrecy; the perpetrator was usually someone trusted, so the betrayal is relational; and in child sexual abuse, grooming MANUFACTURES a felt complicity the child never actually had (accepting gifts, keeping the secret, feeling affection). Guilt is about an act; shame is about the self — which is why this lands on identity. The disclosure to be ready for: physiological arousal during the assault. It happens, it's a reflex and not consent, survivors who experienced it carry the deepest shame, and they're the least likely to mention it — a particularly common and silencing confusion for male survivors. You don't raise it uninvited; you make it clear, by not flinching at anything else, that you're someone it could be said to.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "shame",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-revictimization-evaluate-01",
    "prompt": "Women with childhood sexual abuse histories face a 2- to 13-fold increased risk of sexual violence in adulthood. State the danger in how this is said, and the danger in not knowing it.",
    "answer": "DANGER IN SAYING IT BADLY: stated carelessly it sounds like a claim that survivors invite what happens to them, or that something about them attracts it — a characterological self-blame message delivered by a professional. It is a statement about what early abuse does to a person's capacity to detect danger, assert boundaries, and be protected, and about the environments that produce repeated victimization. DANGER IN NOT KNOWING IT: a counselor unaware of the pattern treats a second assault as implausible — 'this happened to you TWICE?' — which is a Turning Against reaction from the person the survivor finally told. Both errors harm; the fact has to be held accurately rather than avoided.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "revictimization",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-sas-rts-mcq-01",
    "prompt": "A colleague says a client 'has rape trauma syndrome.' What is the most accurate correction?",
    "answer": "RTS is not a current diagnosis. Burgess & Holmstrom described it in 1974 in two phases (an acute phase of disorganization, and a long-term reorganization phase beginning roughly 2–3 weeks out) — before PTSD entered DSM-III in 1980. PTSD substantially absorbed it: nightmares, hypervigilance, avoidance, and intrusive memories are core PTSD features. Survivors today are assessed and treated under the PTSD framework. RTS persists mainly as a courtroom term, and courts describe it accordingly — New York's evidence guide calls it 'a therapeutic concept' with limited evidentiary use. The useful residue of the two-phase model is that acute presentation varies enormously, and a calm survivor is not an unaffected one.",
    "options": [
      "Correct — RTS is the sexual-assault-specific diagnosis in DSM-5-TR",
      "RTS is a 1974 concept largely absorbed by PTSD in 1980; it is history and a courtroom term, not a current diagnosis",
      "RTS was disproven and has no descriptive value",
      "RTS is the correct diagnosis only in the first two weeks, after which it becomes PTSD"
    ],
    "correct": "RTS is a 1974 concept largely absorbed by PTSD in 1980; it is history and a courtroom term, not a current diagnosis",
    "type": "mcq",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "rape-trauma-syndrome",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-calm-survivor-apply-01",
    "prompt": "A survivor presents to an emergency department composed, matter-of-fact, almost flat. A staff member notes 'she seems fine.' What's the error?",
    "answer": "Misreading composure as absence of impact. Acute presentation after sexual assault varies enormously — some survivors present visibly distressed, others flat, composed, or apparently fine, and flatness can reflect dissociation, shock, or simply how that person holds themselves together in public. A calm survivor is not a survivor who is unaffected, and 'she seems fine' is a documented route to under-serving people: it lowers the urgency of the exam offer, the advocacy referral, and the follow-up. The 38.1% PTSD rate at six months in Möller et al.'s cohort was not predicted by how anyone looked in the first hour.",
    "type": "vignette",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "acute-presentation",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-memory-fragmentation-evaluate-01",
    "prompt": "Is it true that traumatic memories are stored as fragmented, non-narrative sensory pieces? Give the state of the evidence and the clinically usable consequence.",
    "answer": "Genuinely disputed — do not treat it as settled. Brewin holds that PTSD trauma memories are disorganized and lack narrative coherence (Brewin & Field's 2024 meta-analysis supports incoherence). Rubin and colleagues, testing 60 trauma-exposed adults across 28 coherence measures, found trauma memories AS COHERENT as very positive and very important memories, with no PTSD deficit. Reviews from 2006–2016 call the evidence inconclusive, partly because 'coherence' is operationalized inconsistently. THE CONSEQUENCE, which is independent of who wins: an account that comes out non-chronologically, with gaps, or differently on a second telling is NEITHER proof that trauma occurred NOR proof of fabrication — and you're not equipped to adjudicate which. Treating inconsistency as a lie harms survivors; treating it as diagnostic of trauma produces false confidence and, historically, false accusations. Both errors come from believing the debate is settled.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-trauma-effects.md",
    "topic": "trauma-memory",
    "cluster": "sexual-trauma-effects",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: reporting-pathways

```json
[
  {
    "id": "ax-sas-forensic-exam-purpose-recall-01",
    "prompt": "What are the two simultaneous purposes of a medical forensic exam, and what two facts about it most change a survivor's decision to have one?",
    "answer": "Two purposes: MEDICAL CARE (injury treatment, STI prophylaxis, emergency contraception, follow-up) and EVIDENCE COLLECTION (physical evidence, injury documentation, the patient's account). Calling it a 'rape kit' is misleading — the kit is one component. The two decision-changing facts: (1) HAVING THE EXAM DOES NOT OBLIGATE ANYONE TO REPORT OR PROSECUTE — in most jurisdictions a kit can be collected and stored while the person decides later. Survivors routinely believe the exam IS reporting, decline on that basis, and lose the option irreversibly. (2) THE EXAM IS SURVIVOR-DIRECTED — DOJ's national protocol is explicit that the patient may decline ANY part (any step, any sample, the photographs) and still receive medical care.",
    "type": "recall",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "forensic-exam",
    "cluster": "reporting-pathways",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-sane-cloze-01",
    "prompt": "A {{SANE}} — Sexual Assault Nurse Examiner — is a nurse with specialized forensic training who conducts the medical forensic exam; in many jurisdictions they work within a SART, a coordinated {{Sexual Assault Response Team}} of nurse examiner, advocate, and law enforcement.",
    "answer": "SANE / Sexual Assault Response Team",
    "type": "cloze",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "sane-sart",
    "cluster": "reporting-pathways",
    "bloom_level": "remember"
  },
  {
    "id": "ax-sas-120-hours-analyze-01",
    "prompt": "Evidence is generally collectable up to about 120 hours after an assault. Why is quoting '120 hours' to a survivor a mistake, and what should you say instead?",
    "answer": "Because it's a rule of thumb, not a universal deadline: windows, payment rules, and age-related requirements are set by jurisdiction and have widened in many states. Quoting it as fixed can cost someone an exam they were still eligible for — the worst possible error to make from over-confidence. Say instead: 'There is a time window and it may be longer than you think — let's find out what it is here,' then call the local rape crisis center or hotline. Also worth adding: medical care itself has no deadline. And the practical note, offered only if asked and never as pressure — evidence is better preserved if they haven't showered, changed, or laundered clothes, AND having done so doesn't make the exam pointless. A person who wants a shower more than a kit is making a legitimate choice about their own body, which is the entire point.",
    "type": "explain",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "forensic-exam",
    "cluster": "reporting-pathways",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-restricted-unrestricted-compare-01",
    "prompt": "Compare Restricted and Unrestricted Reporting in the DoD SAPR system, and state the lesson that generalizes beyond the military.",
    "answer": "RESTRICTED: confidential — no investigation, no command notification. Gives access to medical care, advocacy, and counseling. May be made ONLY to a SARC, SAPR Victim Advocate, or healthcare provider. UNRESTRICTED: not confidential — triggers a law-enforcement investigation and command notification; may be made to anyone, including the chain of command. THE GENERALIZABLE LESSON: reporting is not one binary decision, and WHO YOU TELL DETERMINES WHAT HAPPENS NEXT. A service member who discloses to their commander cannot then file restricted — the confidential option is foreclosed permanently by the choice of listener. That's why a counselor seeing service members or veterans should know this before the client starts talking, and why the same structural question ('who are you, and what are you obligated to do with this?') applies on campuses and in agencies.",
    "type": "compare",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "military-reporting",
    "cluster": "reporting-pathways",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-mst-access-mcq-01",
    "prompt": "A veteran discharged in 1998 mentions she was assaulted during service but never reported it and has no documentation. What is true about her access to VA care for it?",
    "answer": "MST-related care is free and available to any veteran or service member regardless of era of service or discharge status, with NO requirement that the assault was ever reported and NO documentation requirement. 'MST' (Military Sexual Trauma) is VA's term for sexual assault or harassment experienced during military service. This is a concrete, checkable referral fact that most counselors don't know — and the absence of a report is exactly the barrier survivors assume disqualifies them.",
    "options": [
      "She is ineligible because she never filed a report at the time",
      "She is eligible for free MST-related care regardless of era, discharge status, or documentation, and no prior report is required",
      "She must first obtain a service-connection rating for PTSD",
      "She is eligible only if she was on active duty rather than in the Guard or Reserve"
    ],
    "correct": "She is eligible for free MST-related care regardless of era, discharge status, or documentation, and no prior report is required",
    "type": "mcq",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "mst",
    "cluster": "reporting-pathways",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-title-ix-evaluate-01",
    "prompt": "Why should a counselor NOT memorize current Title IX requirements — and what is the durable professional obligation that survives every regulatory change?",
    "answer": "Because the regulations are genuinely in flux: the 2024 Title IX Final Rule was VACATED NATIONWIDE on January 9, 2025 by the U.S. District Court for the Eastern District of Kentucky, and the Department of Education reverted to enforcing the 2020 regulations. Anything memorized now may be wrong shortly. THE DURABLE OBLIGATION is structural: on a campus, some employees are CONFIDENTIAL (typically counseling center, health services, designated advocates) and some are MANDATED to report to the Title IX Coordinator — and which one you are determines what you can honestly promise a student BEFORE they begin talking. So: know your own status and state it up front, before the disclosure rather than after. A student who tells a 'responsible employee' believing it was private, then finds an investigation underway they didn't choose, has experienced exactly the loss of control this module is organized around.",
    "type": "explain",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "title-ix",
    "cluster": "reporting-pathways",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-sas-adult-discloses-csa-vignette-01",
    "prompt": "A 34-year-old client discloses that her stepfather sexually abused her from ages 8 to 12. She has never told anyone. He is now retired and lives with her sister and her sister's two young children. Work the mandated-reporting question.",
    "answer": "This is the hard case, and it is NOT resolved by the general rule. Generally, historical abuse of a now-adult client is not itself reportable — the mandate is triggered by a child currently at risk. BUT it becomes a current-risk question where there's reason to believe the perpetrator CURRENTLY HAS ACCESS TO CHILDREN, and living with two young children is exactly that. State statutes vary substantially here and some impose broader duties, so this is a consult-and-document situation, not a solo judgment call: check your state's statute, consult your supervisor, document the reasoning. If a report is required, the clinical handling matters as much as the legal answer — a survivor who took 22 years to tell anyone may experience the report as a second loss of control and may end therapy. That doesn't relieve the duty. What it requires is (a) having front-loaded the confidentiality limits at intake so this isn't an ambush, and (b) TELLING HER you are making the report and why, rather than doing it behind her.",
    "type": "vignette",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "mandated-reporting",
    "cluster": "reporting-pathways",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-advocate-role-analyze-01",
    "prompt": "What is a rape crisis advocate, how do they differ from a counselor, and why is this the highest-value referral in the module?",
    "answer": "An advocate accompanies survivors to the hospital and to police interviews, explains what each system will do next, helps with practical needs, and — in many states under specific privilege statutes — holds a confidentiality privilege distinct from and sometimes broader than a counselor's. They are not therapists; the role is navigational, not clinical. Two reasons it's the highest-value referral: (1) it's the direct counter to secondary victimization — an advocate's function is to make the systems less harmful to traverse, which is precisely the harm Campbell documented; (2) it's available IMMEDIATELY, at any hour, with no intake, assessment, or waitlist — unlike you. The National Sexual Assault Hotline (800-656-HOPE) routes to local centers. Practical corollary: find your local center's number BEFORE you need it — looking it up while someone sits in your office is a worse experience than having it written down.",
    "type": "explain",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "advocacy",
    "cluster": "reporting-pathways",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-roles-analyze-02",
    "prompt": "Distinguish the four roles that appear around a sexual assault case — counselor, rape crisis advocate, SANE, forensic interviewer — by what each is for and what each must not do.",
    "answer": "COUNSELOR: therapeutic relationship, stabilization, treatment or referral. Must NOT investigate, gather the narrative for evidentiary purposes, or interview a child. ADVOCATE: navigation and accompaniment through medical/legal systems, practical support, often a statutory privilege. Not a therapist; doesn't provide treatment. SANE: the medical forensic exam — health care plus evidence collection, survivor-directed. Not an investigator and not a counselor. FORENSIC INTERVIEWER: the single recorded, protocol-driven CAC interview of a child, by a trained neutral party. Must not be pre-empted by anyone else's questioning. The organizing point is scope of practice: knowing WHICH of these you are is the skill, and the characteristic beginner error is a counselor drifting into the forensic-interviewer or investigator role because it feels like thoroughness.",
    "type": "compare",
    "source_page": "wiki/concept-reporting-and-advocacy.md",
    "topic": "roles",
    "cluster": "reporting-pathways",
    "bloom_level": "analyze"
  }
]
```

## Cluster: sexual-trauma-treatments

```json
[
  {
    "id": "ax-sas-herman-stages-cloze-01",
    "prompt": "Herman's three stages of trauma recovery: safety and {{stabilization}}, remembrance and {{mourning}}, and {{reconnection}} and integration — and the stages are explicitly not {{linear}}.",
    "answer": "stabilization / mourning / reconnection / linear",
    "type": "cloze",
    "source_page": "wiki/concept-sexual-trauma-treatment.md",
    "topic": "phase-based",
    "cluster": "sexual-trauma-treatments",
    "bloom_level": "remember"
  },
  {
    "id": "ax-sas-stage-one-understand-01",
    "prompt": "Which of Herman's stages does a foundations-level counselor mostly work in, and why is that not a consolation prize?",
    "answer": "Stage 1 — safety and stabilization: safety in the body, relationships, and life; emotion-regulation capacity; resources. It's not a consolation prize for three reasons. (1) It's where most of the time goes even for trauma specialists. (2) It's what makes Stage 2 survivable — trauma processing without prior stabilization is the classic beginner harm. (3) Stage 2 is the stage requiring specific training, so 'do Stage 1 well and refer for Stage 2' is a complete and competent plan, not a partial one. Also: the stages are not linear — a client who was doing Stage 2 work and needs to return to stabilization hasn't regressed, they've hit the normal shape of the work.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-trauma-treatment.md",
    "topic": "phase-based",
    "cluster": "sexual-trauma-treatments",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-stair-analyze-01",
    "prompt": "What is STAIR, what is its distinctive structural feature, and what clinical thesis does that structure encode?",
    "answer": "STAIR — Skills Training in Affective and Interpersonal Regulation, developed by Cloitre for adult survivors of CHILDHOOD abuse. Distinctive feature: eight sessions of skills work in emotion regulation and interpersonal functioning come BEFORE any trauma-focused narrative work — phase-based treatment made explicit. The thesis it encodes: chronic early interpersonal trauma disrupts affect regulation and relationships, so capacity is built before the story is touched. It's the module's whole argument in protocol form, and it's the answer to 'what do you actually do if you're not supposed to dig?'",
    "type": "explain",
    "source_page": "wiki/concept-sexual-trauma-treatment.md",
    "topic": "stair",
    "cluster": "sexual-trauma-treatments",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-cpt-vs-pe-compare-01",
    "prompt": "Compare CPT and PE for sexual assault survivors — what each targets, what the landmark trial found, and what the right clinical conclusion is from that finding.",
    "answer": "CPT (Cognitive Processing Therapy): cognitive, targeting 'stuck points' — distorted beliefs about the trauma, especially blame, safety, trust, power, esteem, and intimacy. Developed by Resick SPECIFICALLY for sexual assault survivors; its blame-focused work maps directly onto the near-universal self-blame in this population. PE (Prolonged Exposure): behavioral, using repeated imaginal and in-vivo exposure to trauma memories and avoided situations. THE TRIAL: Resick et al. (2002) randomized female rape victims with chronic PTSD to CPT, PE, or wait-list. Both active treatments produced large reductions versus wait-list and DID NOT DIFFER SIGNIFICANTLY FROM EACH OTHER; the 5–10 year follow-up found gains maintained. THE RIGHT CONCLUSION: when two treatments tie, offer a genuine CHOICE rather than picking a winner. Some survivors want to work on the beliefs, some want to stop avoiding. For a population whose defining injury was the removal of choice, offering it is not a procedural detail.",
    "type": "compare",
    "source_page": "wiki/concept-sexual-trauma-treatment.md",
    "topic": "cpt-pe",
    "cluster": "sexual-trauma-treatments",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-what-you-do-apply-01",
    "prompt": "You're a foundations-level counselor with a client who disclosed a sexual assault. You're not trained in CPT, PE, or EMDR and you know not to dig. List what you actually do.",
    "answer": "Six things, none of which require trauma-treatment training. (1) Stage 1 work: safety, stabilization, regulation skills, sleep, practical problems, reducing isolation. (2) The alliance itself — for someone harmed inside a relationship by someone trusted, a reliable, boundaried, non-exploitative relationship is a substantial part of the treatment, not preparation for it. (3) Psychoeducation — naming tonic immobility, normalizing delayed disclosure, explaining that self-blame is near-universal. Frequently the highest-yield thing you'll do. (4) Risk assessment — CSA survivors carry elevated suicide risk, so suicide-risk screening and safety planning are part of the work, not optional. (5) Referral, both clinical (a trained trauma clinician) and practical (rape crisis advocate). (6) Letting them not talk about it — a client can do useful work on sleep, relationships, and functioning without ever narrating the assault, and that's a legitimate course of therapy, not an avoidance to be overcome.",
    "type": "vignette",
    "source_page": "wiki/concept-sexual-trauma-treatment.md",
    "topic": "counselor-role",
    "cluster": "sexual-trauma-treatments",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-memory-wars-evaluate-01",
    "prompt": "In the 'memory wars,' separate what is genuinely disputed from what both camps accept — and state the practice rule that follows.",
    "answer": "DISPUTED: whether memories of real abuse can become inaccessible and later be recovered. Serious researchers hold opposing positions and the dispute is live in the peer-reviewed literature; don't claim it's settled either way. ACCEPTED BY BOTH CAMPS: suggestive techniques can generate confident, detailed, entirely FALSE memories — hypnosis for memory retrieval (which doesn't improve recall but increases false recollection while raising confidence in it), guided imagery and visualization of 'what might have happened,' age regression, repeated suggestive questioning, and symptom-checklist reasoning (concluding from present-day symptoms that abuse 'must have' occurred, then working to retrieve it). Historically these produced malpractice liability and de-licensure, and devastated families over events that didn't occur. THE PRACTICE RULE, which follows regardless of who's right about repression: never work to recover a memory.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-trauma-treatment.md",
    "topic": "recovered-memory",
    "cluster": "sexual-trauma-treatments",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-sas-spontaneous-memory-vignette-01",
    "prompt": "A client in her forties, in therapy for depression, arrives distressed: she has had what she experiences as a memory of being abused by an uncle, which she says she never had before. What do you do — and what do you not do?",
    "answer": "Stay neutral about its historical status while taking the distress entirely seriously. Those are compatible, and holding both IS the skill. DO: receive it without flinching; respond to her distress, which is real regardless of the memory's provenance; continue the clinical work on what she's actually presenting with. DO NOT: confirm it ('that explains everything'), challenge it ('are you sure?'), help elaborate it (guided imagery, hypnosis, 'let's see what else comes up'), or build a treatment plan around establishing whether it happened. Do not go looking for corroborating symptoms. Note the direct parallel to 'believe, don't investigate' at first disclosure: in both cases you're declining a forensic role you're not qualified for, and in both cases the client's distress is real either way. If she wants to pursue the question of what happened, that is hers to pursue — with family, records, or other means — not a therapeutic task you take on.",
    "type": "vignette",
    "source_page": "wiki/concept-sexual-trauma-treatment.md",
    "topic": "recovered-memory",
    "cluster": "sexual-trauma-treatments",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-adjudication-trap-evaluate-01",
    "prompt": "Explain the symmetrical trap a counselor falls into by holding a firm belief about whether trauma memories are fragmented.",
    "answer": "Either belief converts you into an adjudicator you're not qualified to be. A counselor convinced trauma memories are NECESSARILY fragmented will read a coherent, well-organized account as suspicious — 'too clean to be real.' A counselor convinced they are necessarily coherent will read gaps and non-chronology the same way — 'the story keeps changing.' Both are using a contested empirical claim as a lie detector, and the claim can't bear that weight: the evidence is inconclusive and 'coherence' is measured inconsistently across studies. The discipline is the same one as the recovered-memory rule and the believe-don't-investigate rule — decline the forensic role, respond to the distress, and let the account be whatever shape it is.",
    "type": "explain",
    "source_page": "wiki/concept-sexual-trauma-treatment.md",
    "topic": "trauma-memory",
    "cluster": "sexual-trauma-treatments",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: survivor-support

```json
[
  {
    "id": "ax-sas-informal-support-understand-01",
    "prompt": "Why is informal support (a partner, friend, or parent responding to a disclosure) not a lesser version of clinical work?",
    "answer": "Because it's where most disclosures actually land, and it's what the research was measuring. Ullman's finding — social reactions to disclosure predict PTSD symptoms, with positive reactions predicting the perceived control that tracks recovery — applies with full force to informal supporters. The person who receives the disclosure is the variable, whether or not they have a license. A supporter is not a substitute for a therapist; they occupy a different, earlier, and often more consequential position.",
    "type": "explain",
    "source_page": "wiki/concept-supporting-a-survivor.md",
    "topic": "informal-support",
    "cluster": "survivor-support",
    "bloom_level": "understand"
  },
  {
    "id": "ax-sas-ill-kill-him-apply-01",
    "prompt": "A friend tells you she was raped by someone at her workplace. You say, 'I'll kill him.' You meant it as loyalty. What did it actually do?",
    "answer": "Three harms. (1) It's the EGOCENTRIC RESPONSE in the Unsupportive Acknowledgment category — she now has to manage your feelings, reassure you, and possibly protect the person who harmed her from you. (2) It tells her, clearly, that telling you more will cost her — so she won't. (3) It moves the conversation from what she needs to what you feel. Rage on a survivor's behalf feels like loyalty and functions as a burden. Feel it; don't perform it at her; take it somewhere else. What she needed instead: 'I believe you. It's not your fault. Thank you for telling me. What do you need?' — and acceptance of 'I don't know' as an answer.",
    "type": "vignette",
    "source_page": "wiki/concept-supporting-a-survivor.md",
    "topic": "harmful-support",
    "cluster": "survivor-support",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-fragile-treatment-analyze-01",
    "prompt": "After a friend discloses, you start handling her carefully — no more teasing, gentler tone, checking in constantly. Why is this classified as a negative reaction rather than a kind one?",
    "answer": "Stigmatizing and treating someone differently sits in the TURNING AGAINST category — the more PTSD-predictive of the two negative-reaction types. The message it sends is 'you are damaged now.' She has already lost a great deal; having the ordinary texture of a friendship removed is a further loss, delivered by the person she trusted enough to tell. Keeping the relationship intact — same jokes, same normalcy, same person — is the support. The general principle: the supportive move is rarely the conspicuous one, and conspicuous gentleness is often about the supporter's discomfort rather than the survivor's need.",
    "type": "explain",
    "source_page": "wiki/concept-supporting-a-survivor.md",
    "topic": "harmful-support",
    "cluster": "survivor-support",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-intimacy-apply-01",
    "prompt": "A partner discloses a past sexual assault, and sex has become difficult. What's the workable stance, and what two things should the supporting partner understand?",
    "answer": "THE STANCE: they set the pace, with a standing, genuinely-meant option to STOP, CHANGE, OR START AGAIN at any point — and 'stop' must never cost them anything, or it isn't a real option. Talk about it outside of sex, when nobody is exposed and nothing is in progress. Expect non-linearity: a good week doesn't mean it's resolved, a bad one doesn't mean it's back to the start. Changes in sexual interest and response are common, and triggers may be unknown until encountered — including by the survivor — so 'just tell me what to avoid' can be unanswerable. TWO THINGS TO UNDERSTAND: (1) A flashback during sex is NOT about you — it's a threat-response system doing what the neurobiology of trauma describes, and reacting to it as rejection turns their trauma into an injury they've caused you. (2) You are allowed to have needs; you are not allowed to make meeting them the condition of the relationship's stability. If that gap is unmanageable, that's a real problem for a therapist of your own.",
    "type": "vignette",
    "source_page": "wiki/concept-supporting-a-survivor.md",
    "topic": "intimacy",
    "cluster": "survivor-support",
    "bloom_level": "apply"
  },
  {
    "id": "ax-sas-secondary-survivor-cloze-01",
    "prompt": "A {{secondary survivor}} is the partner, friend, or family member of someone who was assaulted — their distress is real and valid, and it is not the {{survivor}}'s job to manage.",
    "answer": "secondary survivor / survivor",
    "type": "cloze",
    "source_page": "wiki/concept-supporting-a-survivor.md",
    "topic": "secondary-survivor",
    "cluster": "survivor-support",
    "bloom_level": "remember"
  },
  {
    "id": "ax-sas-support-vs-therapy-compare-01",
    "prompt": "Compare what a loving supporter CAN do with what they cannot, and give the structural reasons the boundary exists — not reasons about competence.",
    "answer": "CAN: listen, believe, be steady, stay present over months, help with concrete practical things when asked, know the referral numbers. CANNOT: be their trauma clinician. THE STRUCTURAL REASONS — none of which are about skill: (1) you cannot be neutral about them; (2) you have your own stake in their recovery, which distorts your judgment; (3) you'll be tempted to dig because you want them better; (4) a relationship that becomes primarily therapeutic loses the thing that made it valuable — an ordinary relationship in which they're a whole person rather than a patient. This is the informal version of the dual-relationships problem, and for a counselor or trainee it's an ethical line too: you don't treat people you love, and 'I'm just using what I know' is how that line gets crossed. What helps most is the least specialized thing you have: you were there, you believed them, and you were still there later.",
    "type": "compare",
    "source_page": "wiki/concept-supporting-a-survivor.md",
    "topic": "support-boundary",
    "cluster": "survivor-support",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-sas-long-haul-evaluate-01",
    "prompt": "Which form of support matters most over time, and why do most supporters fail at it despite good intentions?",
    "answer": "The least dramatic form: still being there in month six, when everyone else has moved on and the survivor has stopped bringing it up because they can tell people are tired of it. Supporters fail at it because the crisis phase supplies obvious things to do — drive them somewhere, sit with them, be outraged — and generates a feeling of usefulness, while the long phase supplies neither. Nothing signals when to check in, the survivor stops volunteering, and silence gets misread as recovery. It's the same lesson as supporting the bereaved: keep showing up after the casseroles stop. Related failure in the other direction: 'why didn't you tell me sooner?' — usually hurt, heard as accusation. Delayed disclosure is the norm, and for male survivors the delay is commonly two decades or more. They're telling you now; that's the event.",
    "type": "explain",
    "source_page": "wiki/concept-supporting-a-survivor.md",
    "topic": "long-term-support",
    "cluster": "survivor-support",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-sas-supporter-load-apply-01",
    "prompt": "A man's wife disclosed a childhood sexual abuse history six months ago. He's not sleeping, is preoccupied with it, and feels guilty for struggling since 'it didn't happen to me.' What's the framing, and where does it go?",
    "answer": "He is a SECONDARY SURVIVOR — the partner, friend, or family member of someone who was assaulted — and his distress is real and valid. The guilt is the common trap: 'it didn't happen to me' is used to disqualify his own need for support, which keeps him carrying it silently. But the distress is also NOT his wife's job to manage — routing it to her converts her disclosure into a new burden. WHERE IT GOES: his own friends, his own therapist, a support line. Many rape crisis centers serve loved ones as well as survivors, and the National Sexual Assault Hotline (800-656-HOPE) is available to supporters, not only survivors. If this has activated something from his own history, that's common and warrants its own help — the same counsel Unit 8 gives counselors about vicarious trauma and self-care, applied to a non-professional helper.",
    "type": "vignette",
    "source_page": "wiki/concept-supporting-a-survivor.md",
    "topic": "secondary-survivor",
    "cluster": "survivor-support",
    "bloom_level": "apply"
  }
]
```
