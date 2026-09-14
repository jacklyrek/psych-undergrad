# Elective module items — Trauma-Informed Care

Source of truth for this **elective/ad-hoc module** (off-spine; `aux-` namespace). Each fenced
`json` block is a JSON array merged by `apps/build_items.py` into `build/items.json`. Clusters:
`retraumatization`, `ace-research`, `trauma-screening`, `tic-implementation`, `historical-trauma`,
`tic-evidence`. Item id prefix: `ax-tic-`.

**The organizing emphasis.** This module's defining feature is that it teaches a **mandated practice
standard whose outcome evidence is thin** (AHRQ 2025: insufficient for every outcome examined), so a
large share of items are **appraisal items** — distinguishing what the framework claims from what has
been demonstrated, and holding both without collapsing into either credulity or dismissal. The
characteristic failure this module guards against is not forgetting the six principles; it is
reciting them as though they were findings.

**Not covered here by design:** the three E's, four R's, six principles, and the trauma-informed vs.
trauma-treatment distinction. Those are Unit 8's `concept-trauma-informed-care`, which is **retained
on the spine** as the overview for a syllabus-named core concept; this module starts where it stops.

## Cluster: retraumatization

```json
[
  {
    "id": "ax-tic-retrauma-def-recall-01",
    "prompt": "Define retraumatization precisely, and explain why the common understanding ('reminding someone of something bad') is wrong in a way that matters clinically.",
    "answer": "Retraumatization is a structural RE-ENACTMENT: an interaction that reproduces the DYNAMICS of the original trauma — powerlessness, coercion, unpredictability, being unheard or disbelieved — regardless of whether the content resembles it at all. The common understanding is wrong because it points attention at topic rather than relational shape. A conversation about a car accident may not retraumatize a survivor of childhood abuse; a polite administrative process that leaves them with no say, no information, and no ability to refuse very well might — because that is what the abuse was like structurally. Clinically this matters because it means you can retraumatize someone without ever discussing trauma, and that avoiding difficult topics is not what protects people.",
    "type": "recall",
    "source_page": "wiki/concept-retraumatization.md",
    "topic": "retraumatization-definition",
    "cluster": "retraumatization",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-principles-inverse-understand-01",
    "prompt": "SAMHSA's six principles are often taught as a list of virtues. Explain the structural logic that actually generates them.",
    "answer": "Each principle is the INVERSE OF A RE-ENACTMENT. Predictability negates unpredictability; choice negates powerlessness; transparency negates the sense of being acted upon by hidden decisions; collaboration negates being done-to; trustworthiness negates adults-who-say-things-being-unreliable. They are not general niceness — they are the specific negations of the dynamics that constitute trauma. Read against the neurobiology, they are also exactly the conditions a threat-locked nervous system needs in order to settle (safe, predictable, controllable), which is the mechanistic argument for the framework and a good one even though the outcome trials are missing.",
    "type": "explain",
    "source_page": "wiki/concept-retraumatization.md",
    "topic": "principles-logic",
    "cluster": "retraumatization",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-coercion-evidence-analyze-01",
    "prompt": "What does the restraint and seclusion literature establish about retraumatization, and why is the specific texture of the finding significant?",
    "answer": "A peer-reviewed integrative review found physical and psychological harm INHERENT in restraint in mental health inpatient settings — including humiliation and retraumatization — and that coercive practice left patients feeling POWERLESS and convinced they WOULD NOT BE BELIEVED if they reported abusive treatment; service-user qualitative synthesis corroborates it. The texture matters because 'powerless' and 'not believed' are not generic complaints about unpleasant care: they are the exact dynamics of interpersonal abuse, reproduced by a therapeutic institution. People with abuse histories are also over-represented among those restrained, so the intervention concentrates on those most likely to be harmed by it. Professional direction of travel (argued in APA's own health-services journal) is toward cessation of seclusion and mechanical restraint.",
    "type": "explain",
    "source_page": "wiki/concept-retraumatization.md",
    "topic": "coercive-practice",
    "cluster": "retraumatization",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-quiet-version-apply-01",
    "prompt": "You will probably never restrain anyone. List the counseling-room re-enactments that are ordinary, well-intentioned, and institutionally normal — and give the test that identifies them.",
    "answer": "An intake form demanding a full trauma history before any relationship exists (compelled disclosure to a stranger); 'I just need to ask you a few questions' (the process is yours, not theirs); asking why they didn't leave/report/tell (disbelief and implied blame — the abuser's framing); changing the appointment, room, or plan without notice (unpredictability); deciding something for their own good without asking (benevolent powerlessness is still powerlessness); touching or entering their space without asking; pressing on when someone has gone quiet or flat (dissociation read as compliance); breaking a small promise — a callback, a referral, a timeline. THE TEST is not 'was I kind?' but 'DID THIS PERSON HAVE A REAL SAY, AND DID THEY KNOW WHAT WAS GOING TO HAPPEN?' Kindness is fully compatible with taking over, and taking over is the failure mode of competent, caring helpers.",
    "type": "vignette",
    "source_page": "wiki/concept-retraumatization.md",
    "topic": "clinical-reenactment",
    "cluster": "retraumatization",
    "bloom_level": "apply"
  },
  {
    "id": "ax-tic-universal-precautions-understand-01",
    "prompt": "Explain the 'universal precautions' logic in trauma-informed care, and the apparent contradiction it resolves.",
    "answer": "You cannot tell who is a survivor, and the framework does not ask you to find out. SAMHSA's three E's make EXPERIENCE the load-bearing term — the same event traumatizes one person and not another — so nothing about the event alone tells you who is carrying what. Hence the borrowed medical analogy: like universal precautions for bloodborne pathogens, you apply the safe practice to EVERYONE, because screening to decide who 'needs' it is both unreliable and itself intrusive. THE CONTRADICTION IT RESOLVES: how can care be trauma-informed if the client never discloses? It can, because trauma-informed care NEVER REQUIRED DISCLOSURE. That is the design, and it is why screening is not the entry point to being trauma-informed.",
    "type": "explain",
    "source_page": "wiki/concept-retraumatization.md",
    "topic": "universal-precautions",
    "cluster": "retraumatization",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-overcorrection-compare-01",
    "prompt": "Compare the two opposite over-corrections people make after learning about retraumatization, and give the principle that distinguishes correct practice from each.",
    "answer": "FRAGILITY THEATER: treating every client as breakable, avoiding all difficult subjects, never asking anything uncomfortable. This is avoidance wearing trauma-informed vocabulary, and it deprives people of effective treatment — exposure-based treatments like PE deliberately approach distressing material and are first-line for PTSD. Trauma-informed does NOT mean trauma-avoidant. CONCEPT INFLATION: calling ordinary distress, disagreement, an unwelcome boundary, or a necessary mandated report 'retraumatization.' If everything counts, the concept distinguishes nothing and stops being usable. THE DISTINGUISHING PRINCIPLE IS CONSENT AND CONTROL, NOT INTENSITY: a client who understands what the work involves and chooses it is not being re-traumatized by hard work they signed up for. And where you must act against a client's wishes (a mandated report, a hospitalization for acute risk), the obligation is not to avoid the action but to do it with maximum transparency, explanation, and whatever genuine choice remains inside it.",
    "type": "compare",
    "source_page": "wiki/concept-retraumatization.md",
    "topic": "overcorrection",
    "cluster": "retraumatization",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-mandated-action-apply-01",
    "prompt": "You must make a mandated report your client does not want you to make. Is this retraumatizing, and what does trauma-informed practice require here?",
    "answer": "It is not automatically retraumatizing, and the trauma-informed obligation is NOT to avoid the action — the duty stands. What it requires is doing it in the way that preserves the most control available: TELL THEM you are making it (rather than doing it behind them), TELL THEM WHY, TELL THEM WHAT HAPPENS NEXT, and give them a genuine say in every part that is still open — timing where there's latitude, who else is told, what happens in the next session, whether they're present when you call. The re-enactment to avoid is the ambush: a decision made about them, concealed from them, discovered afterward. This is also why front-loading confidentiality limits at intake matters — it converts a later report from betrayal into a known, pre-stated consequence.",
    "type": "vignette",
    "source_page": "wiki/concept-retraumatization.md",
    "topic": "mandated-action",
    "cluster": "retraumatization",
    "bloom_level": "apply"
  },
  {
    "id": "ax-tic-strongest-leg-evaluate-01",
    "prompt": "Given that AHRQ found insufficient evidence for trauma-informed care's effectiveness, why does retraumatization remain the strongest part of the framework?",
    "answer": "Because the HARM is documented even where the REMEDY's outcomes are not. The restraint and coercion literature establishes that re-traumatization occurs and causes measurable damage; what has not been established is that adopting an organizational TIC package improves outcomes. Those are separate claims, and conflating them produces both errors: dismissing retraumatization because TIC is unproven, or claiming TIC is proven because retraumatization is real. The defensible position is that you are avoiding a documented harm using a well-reasoned but under-tested approach — which is also why reducing seclusion and restraint has its own evidence base independent of the broader TIC package.",
    "type": "explain",
    "source_page": "wiki/concept-retraumatization.md",
    "topic": "evidence-link",
    "cluster": "retraumatization",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: ace-research

```json
[
  {
    "id": "ax-tic-ace-design-cloze-01",
    "prompt": "The CDC-Kaiser ACE Study surveyed over {{17,000}} Kaiser Permanente HMO members in Southern California between 1995 and 1997, measuring {{10}} categories of childhood adversity in three groups: abuse, household challenges, and neglect.",
    "answer": "17,000 / 10",
    "type": "cloze",
    "source_page": "wiki/study-ace.md",
    "topic": "ace-design",
    "cluster": "ace-research",
    "bloom_level": "remember"
  },
  {
    "id": "ax-tic-ace-categories-recall-01",
    "prompt": "Name the ten ACE categories in their three groups.",
    "answer": "ABUSE (3): emotional abuse, physical abuse, sexual abuse. HOUSEHOLD CHALLENGES (5): mother treated violently, household substance abuse, household mental illness, parental separation or divorce, incarcerated household member. NEGLECT (2): emotional neglect, physical neglect. The ACE score is simply the count of categories endorsed, 0–10 — an UNWEIGHTED count, which is the seed of most of the instrument's problems.",
    "type": "recall",
    "source_page": "wiki/study-ace.md",
    "topic": "ace-categories",
    "cluster": "ace-research",
    "bloom_level": "remember"
  },
  {
    "id": "ax-tic-dose-response-understand-01",
    "prompt": "What was the ACE study's landmark finding, and why was the SHAPE of the result more important than any single association?",
    "answer": "The graded DOSE-RESPONSE relationship: as ACE count rises, so does risk across an extraordinary range of adult outcomes — smoking, alcoholism, drug use, depression, suicide attempts, STIs, heart disease, cancer, chronic lung disease, liver disease, skeletal fractures. The shape mattered more than any single association because a monotonic gradient across many UNRELATED outcomes, in a large ordinary population, is hard to explain away and points at a common upstream cause. That is what reframed childhood adversity as a population-level determinant of PHYSICAL health, not just mental health, and put trauma on public-health agendas. Adversity was also common: nearly two-thirds reported at least one ACE, 12.5% reported four or more.",
    "type": "explain",
    "source_page": "wiki/study-ace.md",
    "topic": "dose-response",
    "cluster": "ace-research",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-ace-omissions-analyze-01",
    "prompt": "A child is exposed to chronic community violence and significant racial discrimination, and lives in a stable household. What is their likely ACE score, and what does that reveal?",
    "answer": "Likely ZERO. The ACE questionnaire was built around HOUSEHOLD adversity and inherits that boundary. NCTSN's list of what it omits is not marginal: racial trauma, community violence, traumatic bereavement, medical trauma, natural disasters, among others. It also discards frequency, severity, duration, and developmental timing — so a person scoring 1 may have suffered chronic intense abuse while another scoring 4 had brief low-level exposure to four things. What this reveals: the score is a category count, not a measure of how much harm a child has sustained, and a badly harmed child can be invisible to it.",
    "type": "vignette",
    "source_page": "wiki/study-ace.md",
    "topic": "ace-omissions",
    "cluster": "ace-research",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-anda-mcq-01",
    "prompt": "What did Robert Anda, co-principal investigator of the ACE study, publicly say about clinical use of the ACE score?",
    "answer": "Anda wrote that the ACE questionnaire was designed to RESEARCH — not screen — the relationship between childhood adversity and later outcomes, and that the ACE score 'is neither a diagnostic tool nor is it predictive at the individual level.' It is rare and clarifying for an author to disown a use of their own work this directly. His objection is corroborated by subsequent psychometric work showing ACE scores classify individuals poorly, and by a medical specialty society's formal position locating ACEs in population-level prevention.",
    "options": [
      "That it should be administered universally in primary care as a screening tool",
      "That it was designed to research, not screen, and is neither diagnostic nor predictive at the individual level",
      "That it is valid for individuals but not for populations",
      "That it should be replaced by a longer version with more categories"
    ],
    "correct": "That it was designed to research, not screen, and is neither diagnostic nor predictive at the individual level",
    "type": "mcq",
    "source_page": "wiki/study-ace.md",
    "topic": "anda-objection",
    "cluster": "ace-research",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-population-individual-compare-01",
    "prompt": "Compare what the ACE score does well with what it does badly, and name the general research principle the contrast illustrates.",
    "answer": "DOES WELL — population level: describes a real, replicated, graded association between cumulative childhood adversity and a broad range of adult health outcomes across a large sample. Legitimate for public-health argument, prevention targeting, and resource allocation. DOES BADLY — individual level: ACE scores predict MEAN GROUP DIFFERENCES but have LOW ACCURACY in identifying WHICH individuals will have poor health outcomes. THE GENERAL PRINCIPLE: a robust population-level association can have poor individual predictive accuracy, and conflating the two is one of the most consequential errors in applied research. Stated in Unit 7 terms, it's a validity failure of the purpose-relative kind — the ACE score isn't an invalid instrument, it's a valid instrument being used for a purpose it was never validated for.",
    "type": "compare",
    "source_page": "wiki/study-ace.md",
    "topic": "population-vs-individual",
    "cluster": "ace-research",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-determinism-evaluate-01",
    "prompt": "Beyond the psychometric objection, what is the practice-level critique of ACE framing — and what makes it more than a complaint about tone?",
    "answer": "That it oversimplifies complex lives, creates DETERMINISTIC NARRATIVES about children's futures, PATHOLOGIZES POVERTY AND STRUCTURAL DISADVANTAGE, and embeds a deficit-based stance toward families. It's more than tone for two reasons. (1) Children have actually been told their score means their future is fixed — a high ACE score describes elevated risk in a POPULATION and is not a prognosis, so this is a factual error with psychological consequences. (2) The gradient correlates heavily with material deprivation, which raises a substantive question about what is being measured: how much is 'childhood trauma' and how much is poverty measured indirectly? If it's substantially the latter, a clinical intervention aimed at the child's trauma may be the wrong response to a structural problem.",
    "type": "explain",
    "source_page": "wiki/study-ace.md",
    "topic": "ace-determinism",
    "cluster": "ace-research",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-ace-limits-analyze-02",
    "prompt": "State the ordinary methodological limitations of the 1998 ACE study, and explain why they are less important than the misuse critique.",
    "answer": "ORDINARY LIMITATIONS: retrospective self-report of childhood decades later (recall bias); cross-sectional design, so causation is inferred rather than demonstrated; and a non-representative cohort — insured Kaiser members in one Californian region, largely white and middle-class — limiting generalization in both directions. WHY THEY MATTER LESS: these are the standard caveats attaching to most large epidemiological work, and they don't undermine the core population-level finding, which has been broadly replicated. The misuse critique is more important because it concerns what people DO with the study — converting a population risk gradient into an individual screening score and a personal prognosis — which produces active harm rather than merely qualified confidence.",
    "type": "explain",
    "source_page": "wiki/study-ace.md",
    "topic": "ace-limitations",
    "cluster": "ace-research",
    "bloom_level": "analyze"
  }
]
```

## Cluster: trauma-screening

```json
[
  {
    "id": "ax-tic-screening-not-entry-understand-01",
    "prompt": "Why is trauma screening NOT the entry point to being trauma-informed, and what follows for an organization that adds a trauma screen?",
    "answer": "Because trauma-informed care is a UNIVERSAL stance that assumes any client might be a survivor and therefore does not require anyone to disclose anything. If safety, predictability, transparency, and choice are applied to everyone, no screening is needed to trigger them. Screening is therefore a SEPARATE decision requiring its own clinical justification — namely, what will change based on the answer. An organization that adds a trauma screen without changing anything else has not become trauma-informed; it has added a question.",
    "type": "explain",
    "source_page": "wiki/concept-trauma-screening.md",
    "topic": "screening-role",
    "cluster": "trauma-screening",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-screen-assess-treat-compare-01",
    "prompt": "Distinguish screening, assessment, and treatment in the trauma context, and state the rule about what a screen's output means.",
    "answer": "SCREENING asks 'is there a signal worth pursuing?' — brief, standardized, often self-report, minimal training, output is a FLAG. ASSESSMENT asks 'what exactly is going on and what maintains it?' — clinical interview over time, inside a relationship, output is a FORMULATION. TREATMENT asks 'can we reduce it?' — a specific trained protocol (PE, CPT, TF-CBT, EMDR), output is change. THE RULE: a screen is a flag, never a verdict — the same rule Unit 7 states for the PHQ-9 and GAD-7. A positive trauma screen means LOOK FURTHER; it does not mean the person has PTSD, and it certainly does not mean their problems are caused by trauma.",
    "type": "compare",
    "source_page": "wiki/concept-trauma-screening.md",
    "topic": "screen-vs-assess",
    "cluster": "trauma-screening",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-ace-screening-evaluate-01",
    "prompt": "Your agency adopts universal ACE screening and asks you to score every client. Evaluate the practice, and say what you actually do.",
    "answer": "THE PRACTICE IS A MEASUREMENT ERROR, not a preference. Anda, the study's own co-PI, wrote the questionnaire was designed to research not screen and 'is neither a diagnostic tool nor is it predictive at the individual level.' The reasons are structural and unfixable by better administration: it's an unweighted category count ignoring frequency, severity, duration and developmental timing; it omits whole adversity categories (racial trauma, community violence, traumatic bereavement, medical trauma); and it has NO STANDARDIZED CUT POINTS — no validated threshold at which a clinical decision follows. Empirically it predicts group differences but classifies individuals poorly. NCTSN: an ACE score gives insufficient information for treatment decision-making. WHAT YOU DO — not refusal, since you'll likely be required to: administer it as what it legitimately is, a CONVERSATION OPENER and a population-health data point. Never as a risk score, never as a prognosis, never as a number that drives a treatment decision on its own — and never tell a client their score means their future is determined, because it does not.",
    "type": "vignette",
    "source_page": "wiki/concept-trauma-screening.md",
    "topic": "ace-screening",
    "cluster": "trauma-screening",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-pcptsd5-cloze-01",
    "prompt": "On the PC-PTSD-5, a score of {{3}} or more is the optimally sensitive cut point (minimizing false negatives), while {{4}} or more suggests probable PTSD warranting further evaluation.",
    "answer": "3 / 4",
    "type": "cloze",
    "source_page": "wiki/concept-trauma-screening.md",
    "topic": "pc-ptsd-5",
    "cluster": "trauma-screening",
    "bloom_level": "remember"
  },
  {
    "id": "ax-tic-validated-screen-compare-01",
    "prompt": "Compare the ACE questionnaire with the PC-PTSD-5 as screening instruments. What does the second have that the first lacks?",
    "answer": "PC-PTSD-5: a trauma-exposure item, then five yes/no symptom items about the past month if endorsed. It has A DEFINED PURPOSE, VALIDATION AGAINST A CRITERION, PUBLISHED CUT POINTS (3+ optimally sensitive, 4+ probable PTSD, with evidence a lower cut point may fit women in VA primary care), and KNOWN PERFORMANCE CHARACTERISTICS including the sensitivity/specificity trade-off. The ACE questionnaire has none of these as a screening tool — no validation for that purpose, no cut points, no known individual-level performance. The comparison is the cleanest illustration that 'validity' is not a property an instrument has in general; it is relative to a stated purpose.",
    "type": "compare",
    "source_page": "wiki/concept-trauma-screening.md",
    "topic": "instrument-comparison",
    "cluster": "trauma-screening",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-lec5-analyze-01",
    "prompt": "The LEC-5 deliberately has no formal scoring protocol. Why, and what construct distinction does pairing it with a symptom measure teach?",
    "answer": "Because it is an EXPOSURE inventory, not a symptom measure: it identifies whether someone has experienced listed potentially traumatic events, and deliberately does NOT establish that exposure met DSM-5 Criterion A, nor say anything about symptoms. A score would imply a precision it doesn't have. It's typically paired with a symptom measure such as the PCL-5. THE DISTINCTION THIS TEACHES: exposure and symptoms are DIFFERENT CONSTRUCTS, and most trauma-exposed people do not develop PTSD. Which is exactly why an instrument that only counts EVENTS — which is what the ACE score is — cannot tell you who is symptomatic.",
    "type": "explain",
    "source_page": "wiki/concept-trauma-screening.md",
    "topic": "lec-5",
    "cluster": "trauma-screening",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-dont-screen-apply-01",
    "prompt": "State the rule that governs whether to screen at all, the questions that operationalize it, and why violating it is itself a re-enactment.",
    "answer": "THE RULE: do not screen for what you cannot respond to. THE QUESTIONS: What changes based on the answer? Who responds, and how fast? Is there somewhere to refer? Is the person told what will happen to this information before they answer? If those have no answers, the screen should not exist. WHY IT'S A RE-ENACTMENT: asking someone to disclose trauma creates an obligation. If a positive screen leads to nothing — no follow-up, no referral pathway, no change in care — you have asked a person to open something painful for the institution's benefit and given nothing back. The disclosure was extracted, the person was not helped, and control sat entirely with the organization. That is precisely the structure retraumatization describes, which is why screening sits inside SAMHSA's implementation domains rather than standing alone.",
    "type": "explain",
    "source_page": "wiki/concept-trauma-screening.md",
    "topic": "screening-rule",
    "cluster": "trauma-screening",
    "bloom_level": "apply"
  },
  {
    "id": "ax-tic-screening-practice-apply-02",
    "prompt": "Your clinic will screen for trauma at intake. Name three practice conditions that make it trauma-informed rather than extractive.",
    "answer": "1) TELL PEOPLE WHAT HAPPENS TO THE INFORMATION BEFORE THEY ANSWER, including mandated-reporting limits. Being asked about abuse without knowing what the answer triggers is exactly the ambush the framework exists to prevent. 2) LET PEOPLE DECLINE. A screen no one may refuse is inconsistent with a framework whose fifth principle is choice. 3) DON'T SCREEN AT FIRST CONTACT BY DEFAULT — compelled disclosure to a stranger before any relationship exists is itself a listed re-enactment. Sometimes it's necessary; it should be a considered decision rather than an artifact of the form's position in the packet.",
    "type": "vignette",
    "source_page": "wiki/concept-trauma-screening.md",
    "topic": "screening-practice",
    "cluster": "trauma-screening",
    "bloom_level": "apply"
  }
]
```

## Cluster: tic-implementation

```json
[
  {
    "id": "ax-tic-ten-domains-recall-01",
    "prompt": "Name SAMHSA's ten implementation domains for a trauma-informed approach.",
    "answer": "1) Governance and leadership; 2) Policy; 3) Physical environment; 4) Engagement and involvement (of clients and staff in the change process); 5) Cross-sector collaboration; 6) Screening, assessment, and treatment services; 7) Training and workforce development; 8) Progress monitoring and quality assurance; 9) Financing; 10) Evaluation.",
    "type": "recall",
    "source_page": "wiki/concept-tic-implementation.md",
    "topic": "ten-domains",
    "cluster": "tic-implementation",
    "bloom_level": "remember"
  },
  {
    "id": "ax-tic-domains-count-analyze-01",
    "prompt": "Count how many of SAMHSA's ten implementation domains an individual counselor actually controls. What does the answer establish?",
    "answer": "Realistically: part of domain 6 (screening, assessment, treatment services) and your own participation in domain 7 (training and workforce development). EIGHT OF THE TEN ARE STRUCTURAL — budgets, policies, buildings, governance, data systems, cross-sector relationships. This establishes the page's central claim: trauma-informed care is mostly something an ORGANIZATION IS, not something a clinician does. SAMHSA is explicit that implementation requires change at every level of an organization. When a clinician says 'I practice in a trauma-informed way,' they are describing a personal stance held inside a system whose policies may contradict it daily.",
    "type": "explain",
    "source_page": "wiki/concept-tic-implementation.md",
    "topic": "domains-scope",
    "cluster": "tic-implementation",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-environment-engagement-analyze-02",
    "prompt": "Domains 3 (physical environment) and 4 (engagement and involvement) are the ones organizations skip. What does each actually require, and what irony attaches to skipping domain 4?",
    "answer": "PHYSICAL ENVIRONMENT is not decoration: lighting, sightlines, whether a person can see the exit, whether the waiting room is exposed, whether someone can be overheard at a check-in desk, whether the space is predictable. These map directly onto retraumatization — an environment that cannot be anticipated or controlled is the thing being avoided. ENGAGEMENT AND INVOLVEMENT means clients and FRONTLINE STAFF participate in designing the change. THE IRONY: a trauma-informed approach imposed on staff from above, without their voice, RE-ENACTS THE POWERLESSNESS IT CLAIMS TO OPPOSE — which is a frequently-noted reason initiatives fail. Also worth noting: financing (9) and evaluation (10) are what separate a genuine initiative from a training day. If nobody paid for it and nobody is measuring it, it is a value statement.",
    "type": "explain",
    "source_page": "wiki/concept-tic-implementation.md",
    "topic": "domains-detail",
    "cluster": "tic-implementation",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-continuum-compare-01",
    "prompt": "Lay out the trauma-informed continuum, and state the two cautions that go with it.",
    "answer": "TRAUMA-AWARE: basic understanding that trauma is widespread. TRAUMA-SENSITIVE: that understanding shapes language, attitudes, interactions. TRAUMA-RESPONSIVE: practices actively change; universal screening with trauma-specific assessment and treatment offered to those who need it; ongoing adjustment. TRAUMA-INFORMED: embedded across policy, environment, workforce, governance — the full domain set. TRAUMA-SPECIFIC: clinical treatments for trauma symptoms (PE, CPT, TF-CBT, EMDR) delivered within that frame. CAUTION 1: the terminology is NOT STANDARDIZED — sources order and define these differently, so define your terms when you use them; this inconsistency is part of why the evidence base is hard to synthesize. CAUTION 2: trauma-informed and trauma-specific are DIFFERENT OBJECTS, not adjacent stages — organizational philosophy versus clinical treatments. An agency that trains everyone in trauma awareness has not thereby acquired anyone who can deliver CPT.",
    "type": "compare",
    "source_page": "wiki/concept-tic-implementation.md",
    "topic": "continuum",
    "cluster": "tic-implementation",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-workforce-evaluate-01",
    "prompt": "Domain 7 covers workforce development. What does it reframe about vicarious trauma, and what single question best tests an employer's TIC credentials?",
    "answer": "It reframes vicarious trauma from a PERSONAL responsibility into an ORGANIZATIONAL OBLIGATION. Domain 7 covers hiring and supervision practices, whether staff have enough control over their own work, how the organization responds to workplace incidents, and whether it treats vicarious trauma as an occupational reality rather than an individual weakness. The distinction isn't cosmetic: an agency that tells staff to practice self-care while assigning unmanageable trauma caseloads with no supervision has located a STRUCTURAL problem in the INDIVIDUAL — the framework's own critique applied to the framework's own institutions. THE TEST QUESTION: how are they treating the people doing the work? That single answer tells you more about an organization's trauma-informed credentials than its training materials do.",
    "type": "explain",
    "source_page": "wiki/concept-tic-implementation.md",
    "topic": "workforce",
    "cluster": "tic-implementation",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-bad-system-apply-01",
    "prompt": "You work in a system that is not trauma-informed and you cannot change its policies. What is actually available to you?",
    "answer": "Less than the framework implies, but not nothing. YOUR OWN DEFAULTS — explain before you act, offer choice wherever choice exists, keep your commitments, don't ambush, don't press. None of that requires permission. YOUR OWN ROOM — predictability, seating, where the door is, how sessions start and end. HOW YOU HAND PEOPLE ON — preparing someone for what an intake, a hospital, or a court process will be like restores some predictability even when you can't change the process (the counselor's version of what an advocate does against secondary victimization). NAMING IT IN SUPERVISION — a policy that routinely re-traumatizes clients is a clinical problem and can be raised as one. AND HONEST LIMITS — you cannot single-handedly make an organization trauma-informed, and burning out trying is a documented path. Know which domain a problem lives in before deciding whether it's yours to solve.",
    "type": "vignette",
    "source_page": "wiki/concept-tic-implementation.md",
    "topic": "individual-scope",
    "cluster": "tic-implementation",
    "bloom_level": "apply"
  },
  {
    "id": "ax-tic-practical-guide-evaluate-02",
    "prompt": "SAMHSA published a 'Practical Guide for Implementing a Trauma-Informed Approach' in 2023, nine years after the original framework. What does its existence tell you?",
    "answer": "That the implementation problem is recognized by the framework's own AUTHORS, not just its critics — the 2014 guidance proved hard to operationalize, and SAMHSA judged it insufficiently actionable. This is worth noticing as appraisal evidence: when the body that created a framework issues a guide to making it actually work nearly a decade later, that's a signal about the gap between a well-specified concept and a well-specified practice. It also connects to the definitional finding in the AHRQ review — organizations calling themselves trauma-informed were doing inconsistent things, which is what you'd expect when a framework is compelling but under-operationalized.",
    "type": "explain",
    "source_page": "wiki/concept-tic-implementation.md",
    "topic": "implementation-gap",
    "cluster": "tic-implementation",
    "bloom_level": "evaluate"
  }
]
```

## Cluster: historical-trauma

```json
[
  {
    "id": "ax-tic-historical-trauma-recall-01",
    "prompt": "Who introduced historical trauma into the mental health literature, how is it defined, and what is its central clinical payoff?",
    "answer": "Maria Yellow Horse Brave Heart (Hunkpapa/Oglala Lakota), in the mid-1990s, developed in work with Lakota communities in the context of colonization, forced relocation, the boarding-school system, and prohibition of language and ceremony. DEFINITION: cumulative emotional and psychological wounding across the lifespan AND ACROSS GENERATIONS, emerging from massive group trauma. Associated terms: HISTORICAL UNRESOLVED GRIEF (profound, unsettled bereavement from generations of losses never permitted to be mourned) and the 'SOUL WOUND.' THE CLINICAL PAYOFF: locating suffering in COLLECTIVE HISTORY rather than individual pathology REDUCES STIGMA AND ISOLATION. A person told their depression is a personal chemical failure and a person told their distress is an intelligible response to documented collective harm stand in different relationships to their own experience.",
    "type": "recall",
    "source_page": "wiki/concept-historical-trauma.md",
    "topic": "historical-trauma",
    "cluster": "historical-trauma",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-carter-understand-01",
    "prompt": "Summarize Carter's race-based traumatic stress model, and say why its publication venue matters for this curriculum specifically.",
    "answer": "Carter (2007) holds that racial discrimination experienced as OVERWHELMING OR BEYOND ONE'S CAPACITY TO COPE can produce responses resembling posttraumatic stress. He frames it as an EMOTIONAL INJURY RATHER THAN A PATHOLOGY — a distinction doing real work, because it refuses to locate the disorder in the person harmed. It operates at interpersonal, institutional, and cultural levels, and can be experienced directly OR VICARIOUSLY (witnessing, or repeated exposure through media and community). Cumulative low-grade exposure — microaggressions — is central to the model, not a lesser version of it. THE VENUE: it was published in The Counseling Psychologist, counseling psychology's own flagship journal, which is why it belongs in this curriculum as native material rather than borrowed from another discipline.",
    "type": "explain",
    "source_page": "wiki/concept-historical-trauma.md",
    "topic": "racial-trauma",
    "cluster": "historical-trauma",
    "bloom_level": "understand"
  },
  {
    "id": "ax-tic-criterion-a-analyze-01",
    "prompt": "How does race-based traumatic stress relate to the PTSD diagnosis, and what three clinical failures follow from the mismatch?",
    "answer": "The relationship is UNRESOLVED. DSM-5-TR's Criterion A does not straightforwardly encompass discrimination, so a person can have a genuinely trauma-shaped presentation that the diagnostic system does not recognize as trauma. THREE FAILURES THAT FOLLOW: (1) the distress gets coded as depression or anxiety, losing the trauma framing; (2) the racial content goes unaddressed because there's no diagnostic hook for it; (3) the clinician treats the client's account of racism as a SYMPTOM TO BE EXAMINED rather than an EVENT TO BE BELIEVED — which is its own injury. The general lesson: the absence of a diagnostic code is not evidence of the absence of the phenomenon.",
    "type": "explain",
    "source_page": "wiki/concept-historical-trauma.md",
    "topic": "criterion-a",
    "cluster": "historical-trauma",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-epigenetics-evaluate-01",
    "prompt": "Separate what is established from what is disputed about intergenerational trauma transmission, and give the sentence you can actually defend.",
    "answer": "LESS DISPUTED: that trauma's EFFECTS appear across generations — children of survivors of collective trauma show elevated rates of various difficulties, and discussion of clinically observable intergenerational effects has become less contentious. GENUINELY DISPUTED: the MECHANISM — whether EPIGENETIC transmission is established in humans. Yehuda's own paper is titled 'putative role of epigenetic mechanisms,' and a 2023 scoping review is more cautious still. THE CORE DIFFICULTY: separating BIOLOGICAL from SOCIAL transmission. Parenting shaped by a parent's trauma, family narrative, silence, and ongoing structural conditions all transmit effects across generations without requiring any epigenetic mechanism — and are usually the more parsimonious explanation. THE DEFENSIBLE SENTENCE: 'Trauma effects demonstrably travel across generations; the pathways include parenting, narrative, and continued structural conditions, and whether epigenetic transmission contributes in humans is still being worked out.' Popular claims that ancestral trauma memory is 'validated by scientists' outrun the evidence.",
    "type": "explain",
    "source_page": "wiki/concept-historical-trauma.md",
    "topic": "epigenetics",
    "cluster": "historical-trauma",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-ht-critique-evaluate-02",
    "prompt": "Historical trauma is criticized from WITHIN Indigenous mental health scholarship. What is the substance of that critique, and what practical warning does it carry?",
    "answer": "THE SUBSTANCE: whether the construct is empirically tractable enough to be tested; and whether framing collective suffering as INHERITED PATHOLOGY can itself become a deficit narrative — one that psychologizes what are also STRUCTURAL AND POLITICAL problems of land, sovereignty, poverty, and health-system access, competing with those explanations for attention and funding. It's important to meet this critique from inside the field rather than from a dismissive outsider. IT DOES NOT DISSOLVE THE CONCEPT — historical trauma should be taught as a serious framework with a live internal debate, like other contested constructs. THE PRACTICAL WARNING: a clinician who attributes an Indigenous client's presenting problem to historical trauma BY DEFAULT, without asking, has substituted a category for a person — which is precisely the multicultural error cultural humility exists to prevent.",
    "type": "explain",
    "source_page": "wiki/concept-historical-trauma.md",
    "topic": "ht-critique",
    "cluster": "historical-trauma",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-ht-apply-01",
    "prompt": "A Native American client presents with depression and heavy drinking. You have just learned about historical trauma. What do you do, and what are the two opposite errors?",
    "answer": "ASK, DON'T ASSUME. Group membership does not tell you what someone carries. Offer the frame if it seems relevant and see whether the client finds it useful; follow their language. ERROR ONE — IMPOSING IT: attributing the presentation to historical trauma by default is stereotyping, substitutes a category for a person, and some clients experience it as being told they're damaged by something they didn't live through. ERROR TWO — IGNORING IT: refusing the collective frame entirely when the client finds it clarifying and liberating denies them a reframe that demonstrably reduces stigma and isolation. Also: notice ONGOING conditions. Much of what gets called intergenerational trauma is ALSO CURRENT — present discrimination, present poverty, present under-resourced services — and treating a continuing harm as a historical inheritance is a way of not addressing it.",
    "type": "vignette",
    "source_page": "wiki/concept-historical-trauma.md",
    "topic": "ht-practice",
    "cluster": "historical-trauma",
    "bloom_level": "apply"
  },
  {
    "id": "ax-tic-principle-six-compare-01",
    "prompt": "SAMHSA's sixth principle is 'cultural, historical, and gender issues' and usually gets a sentence in training. Compare the thin version with what the principle actually requires.",
    "answer": "THE THIN VERSION: 'be culturally sensitive' — a gesture with no content, typically a slide with a stock photo. WHAT IT ACTUALLY REQUIRES: (a) Brave Heart's HISTORICAL TRAUMA — cumulative wounding across generations from massive group trauma, plus historical unresolved grief; (b) Carter's RACE-BASED TRAUMATIC STRESS — discrimination beyond one's coping producing PTSD-like responses, at interpersonal, institutional and cultural levels, directly or vicariously; (c) honest handling of INTERGENERATIONAL TRANSMISSION, where effects are less disputed than mechanism; (d) awareness that the ACE score OMITS racial trauma entirely, so these clients can be invisible to the standard instrument; and (e) the discipline not to apply any of it by default to a person because of their group. The gap between the two versions is the gap between a principle and a practice.",
    "type": "compare",
    "source_page": "wiki/concept-historical-trauma.md",
    "topic": "principle-six",
    "cluster": "historical-trauma",
    "bloom_level": "analyze"
  }
]
```

## Cluster: tic-evidence

```json
[
  {
    "id": "ax-tic-ahrq-recall-01",
    "prompt": "State what AHRQ's 2025 systematic review of trauma-informed care found — the numbers and the verdict.",
    "answer": "From 1,326 publications screened, only 12 unique eligible studies (across 16 publications) met inclusion criteria. The verdict, in the review's own words: there is 'insufficient evidence on the effectiveness of current TIC approaches for reducing future or repeat trauma exposure; improving healthcare processes and utilization as well as policies and procedures; improving patient/client-related behavioral and psychosocial wellness as well as physical health; or effecting changes in patient/client harm.' That is EVERY outcome category examined — not one produced sufficient evidence for a conclusion. AHRQ is the U.S. federal agency for health-services evidence synthesis, running the most rigorous review process available.",
    "type": "recall",
    "source_page": "wiki/concept-tic-evidence.md",
    "topic": "ahrq-finding",
    "cluster": "tic-evidence",
    "bloom_level": "remember"
  },
  {
    "id": "ax-tic-insufficient-evidence-evaluate-01",
    "prompt": "What does 'insufficient evidence' mean, and what are the two opposite misreadings?",
    "answer": "It is a statement about the STATE OF THE RESEARCH, not about the intervention. Twelve studies at high risk of bias cannot establish a negative any more than a positive. MISREADING ONE — 'TIC doesn't work': absence of evidence is not evidence of absence, and nothing in the review shows harm or failure. MISREADING TWO — 'so it's still evidence-based': you cannot claim effectiveness that has not been demonstrated; 'trauma-informed care is evidence-based' is not a defensible sentence as of this review. THE DEFENSIBLE SENTENCE: trauma-informed care is evidence-INFORMED, low-risk, and ethically coherent. And the correct response to thin evidence is better research — not abandonment, and not blind adherence.",
    "type": "explain",
    "source_page": "wiki/concept-tic-evidence.md",
    "topic": "insufficient-evidence",
    "cluster": "tic-evidence",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-pfa-parallel-compare-01",
    "prompt": "Compare the evidence situation for trauma-informed care with that for psychological first aid. What does the parallel teach?",
    "answer": "Both are widely mandated, intuitively sensible, expert-endorsed frameworks that are THIN ON OUTCOME TRIALS and defensible on grounds other than demonstrated efficacy. PFA is described as 'evidence-INFORMED, not evidence-PROVEN' — strong expert consensus, low risk, limited rigorous outcome trials. AHRQ's TIC finding puts TIC in the same category. WHAT THE PARALLEL TEACHES: this is a recurring pattern, not a one-off embarrassment. Frameworks that are ethically compelling and low-risk get adopted and mandated ahead of the evidence, and the profession's language ('evidence-based') gets applied loosely. The competency is being able to say 'this is the standard of care, here is what supports it, and here is what has not been demonstrated' — which is more useful than either reciting or debunking.",
    "type": "compare",
    "source_page": "wiki/concept-tic-evidence.md",
    "topic": "pfa-parallel",
    "cluster": "tic-evidence",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-hard-to-study-analyze-01",
    "prompt": "Give the structural reasons trauma-informed care is hard to study — and explain why 'structural' matters for predicting whether the evidence base will improve.",
    "answer": "1) YOU CANNOT EVALUATE WHAT YOU CANNOT DEFINE — AHRQ found 'little consistency' in TIC content across organizations, and no universally consistent operationalization exists; compare CPT or PE, which are manualized and replicable. 2) THE UNIT OF INTERVENTION IS THE ORGANIZATION, not the person — randomizing organizations is expensive and often impossible, blinding is out of the question, contamination and secular trends are hard to control. 3) OUTCOMES ARE DIFFUSE AND LONG-HORIZON — 'avoids re-traumatization' is harder to operationalize than 'PTSD symptom reduction at 12 weeks.' 4) EQUIPOISE IS POLITICALLY UNAVAILABLE — once something is mandated as an ethical obligation, a control arm looks like withholding good care, a genuine research-ethics bind that also makes it convenient not to test. 5) THE COMPARATOR PROBLEM — if TIC overlaps heavily with good care, the meaningful comparison is TIC versus GOOD CARE, a harder and less flattering study. WHY 'STRUCTURAL' MATTERS: these aren't fixable by simply funding more trials, so the evidence base may stay thin — meaning the appraisal skill is durably necessary, not a temporary inconvenience.",
    "type": "explain",
    "source_page": "wiki/concept-tic-evidence.md",
    "topic": "research-difficulty",
    "cluster": "tic-evidence",
    "bloom_level": "analyze"
  },
  {
    "id": "ax-tic-just-good-care-evaluate-02",
    "prompt": "AHRQ's Key Informants 'acknowledged debate around what TIC contributes beyond what many generally recognize as good care.' Evaluate that objection.",
    "answer": "It has real force and should not be dismissed — and note its provenance: this is recorded INSIDE a federal evidence review, by the review's own experts, not by a critic sniping from outside. If TIC's components (explain before you act, offer choice, don't coerce, be predictable, keep commitments) are just competent respectful practice, then 'trauma-informed' may be a rebranding rather than an addition, and the mandate imposes training and compliance costs for an unclear increment. WHAT SURVIVES THE OBJECTION: TIC makes the reasoning EXPLICIT and UNIVERSAL, and supplies a mechanism (avoiding re-enactment of powerlessness) that tells you WHICH courtesies matter and why — which is more than 'be nice' provides. It also drives structural change that individual good manners cannot: policy, physical environment, financing. But the objection also names the study that most needs doing, and hasn't been: TIC versus good care, not TIC versus usual care.",
    "type": "explain",
    "source_page": "wiki/concept-tic-evidence.md",
    "topic": "just-good-care",
    "cluster": "tic-evidence",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-what-to-do-apply-01",
    "prompt": "Given the thin evidence, what position should a counselor take on trauma-informed care? Give the four-part answer.",
    "answer": "1) PRACTICE IT — risk of harm is low; the components are individually defensible; it's consistent with what IS established about trauma's prevalence and about what a threat-locked nervous system needs; it's an ethical obligation in most settings; and the harm it targets, RE-TRAUMATIZATION, is itself documented even where the remedy's outcomes are not. 2) DESCRIBE IT ACCURATELY — don't tell a client, supervisor, or board that TIC is evidence-based without qualification. A field that overstates its evidence loses the credibility it needs when it has strong evidence to report. 3) KEEP COMPONENTS AND PACKAGE DISTINCT — some things under the TIC umbrella have their own evidence (reducing seclusion and restraint; the trauma-specific treatments). The weak finding is about the ORGANIZATIONAL PACKAGE, so don't let 'TIC is unproven' collapse into 'none of this is supported.' 4) TREAT THE GAP AS A LIVE RESEARCH QUESTION — someone has to do these studies.",
    "type": "vignette",
    "source_page": "wiki/concept-tic-evidence.md",
    "topic": "practice-position",
    "cluster": "tic-evidence",
    "bloom_level": "apply"
  },
  {
    "id": "ax-tic-transferable-evaluate-03",
    "prompt": "What is the transferable lesson from the TIC evidence situation, and which other examples in this curriculum show the same pattern?",
    "answer": "THE LESSON: a practice can be simultaneously MANDATED, NEAR-UNIVERSALLY ENDORSED, ETHICALLY COMPELLING, AND EMPIRICALLY UNPROVEN — and noticing this is a professional competency rather than disloyalty. You will meet the pattern repeatedly: a framework arrives, becomes policy, acquires the language of evidence, and is taught as settled. Evidence-based practice's three-legged definition (best available evidence, clinical expertise, client values) lets you be honest — the TIC answer leans on legs two and three while being straight about leg one. OTHER EXAMPLES IN THIS CURRICULUM: PFA's evidence-informed-not-proven caveat; the ACE score's migration from research instrument to screening tool; the recovered-memory and trauma-memory-fragmentation debates; 'no-suicide contracts' before they were abandoned; and EMDR, which works as a package while its distinctive mechanism stays contested.",
    "type": "explain",
    "source_page": "wiki/concept-tic-evidence.md",
    "topic": "transferable-lesson",
    "cluster": "tic-evidence",
    "bloom_level": "evaluate"
  },
  {
    "id": "ax-tic-implementation-gap-mcq-01",
    "prompt": "AHRQ noted that research on TIC's effectiveness 'and potential harms' is not keeping pace with implementation. Why does the phrase 'and potential harms' matter?",
    "answer": "Because it names something almost never considered: that some TIC implementations might do damage, and this is unstudied. Plausible mechanisms exist — universal trauma screening without response pathways (extractive disclosure), ACE scores delivered as prognoses (deterministic labelling), fragility theater depriving clients of effective treatment, and TIC imposed on staff without their voice (re-enacting powerlessness). None of these has been measured. The phrase is a reminder that 'low risk' is an assumption in this framework, not a finding — a widely-implemented intervention whose harms have never been studied is not the same as one shown to be harmless.",
    "options": [
      "It is a formality; systematic reviews always mention harms",
      "It names the unstudied possibility that some TIC implementations do damage, meaning 'low risk' is an assumption rather than a finding",
      "It indicates AHRQ found evidence that TIC causes harm",
      "It refers to the harms of trauma itself rather than of the intervention"
    ],
    "correct": "It names the unstudied possibility that some TIC implementations do damage, meaning 'low risk' is an assumption rather than a finding",
    "type": "mcq",
    "source_page": "wiki/concept-tic-evidence.md",
    "topic": "potential-harms",
    "cluster": "tic-evidence",
    "bloom_level": "evaluate"
  }
]
```
