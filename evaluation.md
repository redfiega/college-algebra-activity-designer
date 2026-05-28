# Evaluation

## Project: College Algebra Activity Designer

---

## 1. What We Are Measuring

Every generated or evaluated activity is scored on five dimensions. Each dimension is
scored 1–5, where 5 is excellent and 1 is failing.

| Dimension               | What It Measures                                              |
|-------------------------|---------------------------------------------------------------|
| Mathematical Rigor      | Content is correct, appropriately challenging, in scope       |
| Accessibility           | Solvable by college algebra students with prior knowledge     |
| Structural Collaboration| Collaboration is required by the task design, not just invited|
| Timing                  | Activity fits within 30 minutes with a realistic breakdown    |
| Resource Use            | Physical resources are used purposefully and creatively       |

---

## 2. Scoring Rubric

### Mathematical Rigor (1–5)
- **5:** All mathematics is correct, content matches rational functions scope, stretch
  question requires genuine higher-order thinking
- **4:** All mathematics is correct, minor scope issue (e.g., a concept slightly beyond
  the unit)
- **3:** One mathematical error present, or content is too shallow for the level
- **2:** Multiple mathematical errors, or content is significantly off-scope
- **1:** Mathematically incorrect or completely off-topic

### Accessibility (1–5)
- **5:** All prerequisite knowledge is covered in the course, entry point is clear,
  scaffolding is appropriate
- **4:** Mostly accessible, one step may be challenging for struggling students
- **3:** Some prerequisite knowledge not covered, or the entry point is unclear
- **2:** Requires knowledge beyond what has been taught
- **1:** Inaccessible to the target student population

### Structural Collaboration (1–5)
- **5:** Task is impossible or severely degraded without all group members contributing;
  mechanism is clearly described in the instructions
- **4:** Strong collaboration mechanism present but not fully enforced by task structure
- **3:** Collaboration is encouraged but a motivated student could complete it alone
- **2:** No collaboration mechanism; group work is cosmetic
- **1:** Activity is designed as individual work with no collaborative element

### Timing (1–5)
- **5:** Time breakdown is explicit, total is 25–30 minutes, each phase is realistic
- **4:** Total is within range, one phase estimate seems slightly off
- **3:** Total is within range but no phase breakdown given, or one phase is unrealistic
- **2:** Total exceeds 30 minutes or is under 15 minutes
- **1:** No timing information provided

### Resource Use (1–5)
- **5:** Uses 2+ physical resources creatively; resources serve the pedagogical goal
- **4:** Uses one physical resource well
- **3:** Mentions a resource but use is generic (e.g., "students write on whiteboards")
- **2:** Only uses paper/pencil; physical resources ignored
- **1:** Requires resources the instructor does not have

---

## 3. Passing Thresholds

A generated activity is **approved** when:
- Mathematical Rigor ≥ 4
- Accessibility ≥ 4
- Structural Collaboration ≥ 4
- Timing ≥ 3
- Resource Use ≥ 3
- No dimension scores below 3

An activity below any threshold is returned for revision with specific feedback.

---

## 4. Test Cases (Synthetic Data)

These test activities live in `/synthetic-data/`. Each has a known expected evaluation
outcome used to verify the system is working correctly.

| File                            | Planted Issue                        | Expected Weak Dimension     |
|---------------------------------|--------------------------------------|-----------------------------|
| synthetic-data/activity-good.md | None — should pass all dimensions    | All ≥ 4                     |
| synthetic-data/activity-math-error.md | Incorrect horizontal asymptote rule | Mathematical Rigor ≤ 2 |
| synthetic-data/activity-no-collab.md | No structural collaboration mechanism | Structural Collaboration ≤ 2 |

---

## 5. Evaluation Results Log

> Append results here each time the evaluation harness is run.

| Date | File Tested | Rigor | Access. | Collab. | Timing | Resources | Pass/Fail |
|------|-------------|-------|---------|---------|--------|-----------|-----------|
| —    | —           | —     | —       | —       | —      | —         | —         |