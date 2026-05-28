# Synthetic Data Strategy

## Project: College Algebra Activity Designer

---

## 1. Purpose

Synthetic data is used to test whether the evaluation agents are working correctly.
We create sample activities with known properties (including deliberate flaws) and
verify that the system correctly identifies them.

---

## 2. What Data We Need

We need **three sample activity files** in Markdown format:

| File                                  | Description                                      |
|---------------------------------------|--------------------------------------------------|
| `synthetic-data/activity-good.md`     | A well-formed activity that should pass all dimensions |
| `synthetic-data/activity-math-error.md` | An activity with a deliberate math mistake     |
| `synthetic-data/activity-no-collab.md` | An activity with no structural collaboration   |

---

## 3. Format

Each synthetic activity follows the standard activity template from `domain-primer.md`:

```
# Activity Title

## Learning Objectives
## Time Estimate
## Materials
## Setup Instructions
## Student Instructions
## Collaboration Mechanism
## Stretch Question
## Facilitator Notes
## Debrief Prompts
```

---

## 4. Planted Signals

### activity-good.md
- Topic: Finding holes and vertical asymptotes
- Collaboration mechanism: Jigsaw — each student receives a different rational function
  and must share findings with the group
- Time: 5 min intro + 18 min group work + 7 min debrief = 30 min
- Resources: Tabletop whiteboards, markers
- Math: All correct
- **Expected result: All dimensions score ≥ 4**

### activity-math-error.md
- Topic: Horizontal asymptotes
- Deliberate error: States that when degree of numerator > degree of denominator,
  the horizontal asymptote is y = 0 (this is WRONG — correct answer is no horizontal
  asymptote)
- **Expected result: Mathematical Rigor scores 1 or 2**

### activity-no-collab.md
- Topic: Finding x-intercepts and y-intercepts
- Issue: Instructions say "work with your group" but each student is given the same
  problem and there is no mechanism requiring them to collaborate
- **Expected result: Structural Collaboration scores 1 or 2**

---

## 5. Real-World Analogs

These synthetic activities are modeled on common formats from mathematics education
research, including:

- NCTM (National Council of Teachers of Mathematics) activity structures
- Active learning frameworks used in university mathematics (e.g., POGIL, IBL)
- The instructor's own existing activity library (to be provided as reference)

---

## 6. Conversion Rules

All activity files must be in Markdown (`.md`) format. If the instructor provides
activities in Word, PDF, or any other format, convert to Markdown before processing.

Log the original file name, destination path, and conversion date in `feedback-log.md`.