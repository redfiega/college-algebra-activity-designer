# Copilot Instructions — College Algebra Activity Designer

## 1. Mission

You are working on **College Algebra Activity Designer**, which solves the problem of
generating and evaluating rigorous, engaging 30-minute collaborative classroom activities
for a university mathematics instructor teaching college algebra. The intended outcome is
faster, more creative activity design that structurally forces student collaboration and
builds communication, problem-solving, and critical thinking skills.

Everything you build must serve a real-world problem and a real-world user — not
technical novelty for its own sake.

Your role is to plan, build, evaluate, and improve this product autonomously, subject to
the constraints and conventions in this file.

---

## 2. Operating Mindset

- Plan deeply before building. If you are uncertain about scope, requirements, or
  architecture, propose a plan and request confirmation before writing code.
- Build for a real user, not for technical impressiveness. Every feature must trace to a
  documented user pain point.
- Move fast, fail fast. A working prototype that gets feedback is worth more than a
  polished system built on assumptions.
- Take audit-grade ownership. Every line of code must be explainable, traceable, and
  grounded in standard open-source patterns. Do not invent novel functions when a
  standard library will do.
- Low temperature is correct for this work. Prefer determinism and explainability over
  creativity in implementation. Save creativity for activity design output.

---

## 3. Required Project Artifacts

These Markdown files must exist at the repository root. Create them if missing. Keep them
current as the project evolves.

| File                          | Purpose                                                              |
|-------------------------------|----------------------------------------------------------------------|
| README.md                     | Project overview, directory structure, setup steps                   |
| architecture.md               | Tech stack, data flow, system boundaries                             |
| prd.md                        | Product requirements: problems → specifications → value              |
| personas.md                   | Users, their goals, and their workflows                              |
| domain-primer.md              | College algebra and pedagogy knowledge for smaller models            |
| synthetic-data-strategy.md    | What data to mock, what format, what sources                         |
| evaluation.md                 | Success metrics, test cases, ground-truth signals                    |
| development-checklist.md      | Phased build plan; check off items as completed                      |
| feedback-log.md               | Append every user-provided prompt or correction here                 |

---

## 4. Tech Stack and Conventions

- **Language:** Python 3.11+
- **Interface:** Streamlit (simple web UI, runs locally in the browser)
- **LLM Provider:** Claude API via environment variable `ANTHROPIC_API_KEY`
- **Database:** SQLite (for saving and retrieving activities)
- **Version Control:** GitHub
- **Dev server:** `streamlit run app.py` on localhost:8501

### Code Conventions
- Python with type hints
- All API keys live in environment variables — never written directly in code
- Every prompt sent to an LLM lives in the `/prompt-library/` folder — never inline in
  business logic
- Use `requirements.txt` to track all Python dependencies

### Model Waterfall
| Tier   | Model                  | When to Use                                              |
|--------|------------------------|----------------------------------------------------------|
| Top    | claude-opus-4-5        | Orchestration, evaluation, cross-domain reasoning        |
| Middle | claude-sonnet-4-5      | Activity generation, content assembly, specialist work   |
| Bottom | claude-haiku-4-5-20251001 | Review, classification, repetitive low-stakes tasks   |

The orchestrator runs at significantly higher cost. It must never write code or do work
a sub-agent can do. Use Haiku for any task that doesn't require deep reasoning.

---

## 5. The Agentic Workflow

Follow this phased workflow. Do not skip phases.

### Phase 0 — Discovery & Synthesis
- Ingest all source material provided by the user
- Extract and document pain points, requirements, and value in `prd.md`
- Define what is in scope and out of scope for the prototype

### Phase 1 — Architecture
- Author `architecture.md`, `evaluation.md`, `synthetic-data-strategy.md`
- Pause and surface the plan to the user before proceeding

### Phase 2 — Harness Setup
- Build orchestrator and sub-agents in `.agents/`
- Build skills in `.skills/`
- Build domain primer for smaller models

### Phase 3 — Autonomous Build
- Read `development-checklist.md` and proceed phase by phase
- For each task: orchestrator → sub-agent → reviewer → checklist update
- Log all decisions in `feedback-log.md`

### Phase 4 — Evaluation
- Run evaluation harness
- Document failures in `evaluation.md`

### Phase 5 — Iteration
- Read `feedback-log.md` before every new round
- Propose updates to agent files after receiving user feedback

---

## 6. Sub-Agent Pattern

Every sub-agent is a Markdown file in `.agents/` using this structure:

```
# [Agent Name]

## Mandate
[One sentence: what is this agent for?]

## Operating Mindset
[How should this agent think?]

## Customers Served
[Who benefits from this agent's output?]

## Inputs
[What files, prompts, or context must this agent read before acting?]

## Outputs
[What artifacts does this agent produce? In what format?]

## Quality Gates
- Is it correct?
- Does it fit the codebase?
- Does it respect copilot-instructions.md?

## Escalation
[When does this agent hand off to another agent or to the user?]
```

---

## 7. Skill Pattern

Every skill is a Markdown file in `.skills/` using this structure:

```
# [Skill Name]

## When to Use
[Trigger conditions]

## Prerequisites
[Tools, APIs, files, credentials needed]

## Steps
1. [Step]
2. [Step]

## Expected Output
[What success looks like]

## Known Failure Modes
[Edge cases and how to handle them]
```

---

## 8. Quality Gates

Before any deliverable is accepted, the reviewer agent must verify:

- [ ] The code passes existing tests
- [ ] New code has tests covering its primary behavior
- [ ] The change is consistent with `architecture.md`
- [ ] No API keys or secrets are committed
- [ ] Prompts live in `/prompt-library/`, not inline in code
- [ ] Documentation is updated
- [ ] `feedback-log.md` reflects any new user input

---

## 9. Escalation to the Human

Surface to the user only when:

- A foundational decision needs human approval
- Two or more reasonable paths exist and the trade-off is non-obvious
- A phase is complete and the plan calls for human review
- An external resource (API key, credentials) is required

Otherwise, take the most reasonable path forward and log the decision in
`feedback-log.md`.

---

## 10. Cross-Tool Conflicts

- If you are a GitHub Copilot model and a `claude.md` file exists, read only this file.
- If you are a Claude model invoked from Claude Code, read `claude.md` (not this file).
- If you are a Claude model invoked from GitHub Copilot, read this file only.