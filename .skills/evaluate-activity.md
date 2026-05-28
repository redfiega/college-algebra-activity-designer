# Evaluate Activity Prompt Template

## Instructions for Use
Replace {ACTIVITY_TEXT} and {DIMENSION} with the actual values before sending.
Each evaluator agent receives this prompt with their specific dimension filled in.

---

## Prompt

You are evaluating a college algebra classroom activity on the following dimension:

**Dimension:** {DIMENSION}

**Activity to evaluate:**

{ACTIVITY_TEXT}

Using the scoring rubric from evaluation.md and the content knowledge from
domain-primer.md, evaluate this activity on the specified dimension.

Return your evaluation in this exact format:

---

**Dimension:** [name]
**Score:** [1–5]
**Verdict:** [APPROVE / REVISE]

**Findings:**
[Specific observations about this dimension. Reference the exact location in the
activity if identifying a problem.]

**Required changes (if verdict is REVISE):**
1. [Specific, actionable change]
2. [Specific, actionable change]

**Suggestions (optional improvements even if approving):**
- [Suggestion]

---

Be specific. "The collaboration mechanism is weak" is not useful feedback.
"Step 3 instructs students to 'discuss with your group' but does not prevent a student
from completing the problem independently. Consider using a jigsaw structure where
each student receives a different rational function." is useful feedback.