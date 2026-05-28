# Development Checklist

## Project: College Algebra Activity Designer

> Check off each item as it is completed. Do not move to the next phase until all items
> in the current phase are done.

---

## Phase 0 — Project Setup

- [ ] Repository created on GitHub
- [ ] All Markdown documentation files created (README, PRD, architecture, etc.)
- [ ] `.gitignore` file created (must include `.env` and `venv/`)
- [ ] `requirements.txt` created with all dependencies listed
- [ ] `claude.md` symlinked or copied from `copilot-instructions.md`
- [ ] Pushed to GitHub

---

## Phase 1 — Environment Setup

- [ ] Python virtual environment created (`venv`)
- [ ] All packages from `requirements.txt` installed successfully
- [ ] `.env` file created with `ANTHROPIC_API_KEY`
- [ ] API connection tested (simple test script confirms Claude responds)

---

## Phase 2 — Agent and Skill Files

- [ ] `.agents/orchestrator.md` created
- [ ] `.agents/activity-generator.md` created
- [ ] `.agents/rigor-evaluator.md` created
- [ ] `.agents/collaboration-auditor.md` created
- [ ] `.agents/timing-estimator.md` created
- [ ] `.agents/resource-mapper.md` created
- [ ] `.agents/reviewer.md` created
- [ ] `.skills/generate-activity.md` created
- [ ] `.skills/evaluate-activity.md` created
- [ ] `.skills/check-collaboration-structure.md` created
- [ ] `.skills/estimate-timing.md` created
- [ ] `.skills/map-resources.md` created

---

## Phase 3 — Prompt Library

- [ ] `prompt-library/system-prompts.txt` created
- [ ] `prompt-library/generate-activity.txt` created
- [ ] `prompt-library/evaluate-activity.txt` created
- [ ] All prompts reference `domain-primer.md` for context

---

## Phase 4 — Core Python Modules

- [ ] `database.py` — SQLite setup, save activity, retrieve activity functions
- [ ] `agents.py` — Functions that call each agent with correct model and prompt
- [ ] Model routing logic implemented (Opus / Sonnet / Haiku correctly assigned)
- [ ] All API calls use environment variable for key (never hardcoded)

---

## Phase 5 — Streamlit UI

- [ ] `app.py` created with two tabs: Generate and Evaluate
- [ ] Generate tab: form with topic selector, constraint input, resource preferences
- [ ] Generate tab: displays generated activity in readable format
- [ ] Generate tab: save button stores activity to SQLite
- [ ] Evaluate tab: text area for pasting draft activity
- [ ] Evaluate tab: displays structured feedback report
- [ ] App runs without errors on `streamlit run app.py`

---

## Phase 6 — Synthetic Data and Testing

- [ ] Three sample activities created in `synthetic-data/`
- [ ] One sample activity has a deliberate error (for testing the evaluator)
- [ ] One sample activity is missing a collaboration mechanism (for testing)
- [ ] Evaluation harness run against all three samples
- [ ] Results documented in `evaluation.md`

---

## Phase 7 — Final Review

- [ ] All quality gates in `copilot-instructions.md` section 8 are passing
- [ ] README setup instructions tested from scratch (follow them exactly)
- [ ] No API keys in any committed file
- [ ] All prompts are in `prompt-library/`, none inline in Python code
- [ ] Final push to GitHub
- [ ] Instructor can demo the full workflow end to end