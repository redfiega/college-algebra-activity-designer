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