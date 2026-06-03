# Feedback Log

## Project: College Algebra Activity Designer

> Every user-provided prompt, correction, or decision is logged here in order.
> This log is the project's memory. Read it before starting any new round of work.

---

## Session 1 — Project Discovery

**Date:** 2026-05-28

**User input (paraphrased from conversation):**
- Instructor teaches college algebra at a 4-year university; expert in mathematics
  education; new to coding
- Wants to create an agentic workflow using tools, MCP, and model routing for a
  generative AI course
- Goal: create better in-class collaborative activities
- Activities must be rigorous but doable; build communication, collaboration,
  problem-solving, and critical thinking; fit within ~30 minutes
- Biggest pain point: coming up with ideas; defaults to card sorts
- Physical resources available: large tabletop whiteboards, individual student markers,
  math manipulatives, printer, scissors, standard office supplies
- Students engage best with "stretch questions" and tasks that structurally require
  collaboration (they go quiet and work alone without structural enforcement)
- Topic focus for prototype: rational functions (simplify, holes, vertical asymptotes,
  horizontal asymptotes, x-intercepts, y-intercepts; NO oblique asymptotes)
- Wants the system to both generate new activities AND evaluate/improve drafts
- Prefers Python in VS Code; will push to GitHub
- Project instructions provided from previous course project (encoded in
  copilot-instructions.md)
- User is new to coding — all instructions must be beginner-friendly

**Decisions made:**
- Tech stack: Python + Streamlit + SQLite + Anthropic Claude API
- Interface: Streamlit (simple, no web development needed)
- Model routing: Opus for orchestration/evaluation, Sonnet for generation, Haiku for
  lightweight checks
- Sub-agents: Orchestrator, Activity Generator, Rigor Evaluator, Collaboration Auditor,
  Timing Estimator, Resource Mapper, Reviewer
- Full repository structure created and pushed to GitHub

---

*Append new entries below as the project develops.*

## Session 2 — Evaluation Refinements

**Date:** 2026-05-28

**User input:**
- Rigor evaluator was too restrictive in two areas:
  1. Flagged functions with no horizontal asymptote as needing replacement
  2. Flagged rational functions that simplify to linear functions as invalid
- Both of these are intentional and desirable for student learning
- Students should recognize when no horizontal asymptote exists and may be
  introduced to the vocabulary "oblique asymptote" without computing it
- Rational functions that simplify to linear functions are excellent edge cases

**Fix applied:**
- Updated domain-primer.md to explicitly allow both cases
- Rigor evaluator reads domain-primer.md before every evaluation, so this
  change takes effect immediately with no code changes needed

---

## Session 3 — Collaboration Evaluation Refinements

**Date:** 2026-05-28

**User input:**
- Collaboration evaluator was too strict about requiring defined roles
- Brief organic discussion phases (≤5 minutes) are valid and desirable
- Example: a quick card sort discussion before a larger structured activity
  should not require individual role assignments
- The tool should evaluate the activity as a whole, not penalize any phase
  that uses organic discussion

**Fix applied:**
- Updated domain-primer.md to explicitly allow organic discussion phases
- Clarified that only activities with NO structural mechanism at all should
  be penalized for collaboration

---

## Session 4 — Evaluation Rubric Integration

**Date:** 2026-05-28

**Issue identified:**
- evaluation.md contained the scoring rubric but was not being read by the code
- Agents were using general judgment rather than the defined 1-5 rubric

**Fix applied:**
- Added load_evaluation_rubric() function to agents.py
- All four evaluator agents now receive the scoring rubric in their system prompt
- Scores should now be more consistent and aligned with defined criteria

---

## Session 5 — Instructor Feedback Revisions

**Date:** 2026-06-03

**Feedback received:**
- App was asleep on deployment — woken and documented in README
- Architecture described a revision loop that wasn't in the code — built it
- No function calling present — needed at least one tool with typed output

**Fixes applied:**
- Added sleep note to Known Limitations in README
- Built revision loop in generate_activity — fails back to generator up to 2 times
- Wrapped evaluate_rigor as a real tool using Claude function calling
- Structured rigor result now displays separately in the Evaluate tab