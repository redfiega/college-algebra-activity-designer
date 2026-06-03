🔗 **Live App:** [College Algebra Activity Designer](https://college-algebra-activity-designer.streamlit.app/)

# College Algebra Activity Designer

An AI-powered tool that helps a university mathematics instructor generate and evaluate
rigorous, engaging 30-minute collaborative classroom activities for college algebra —
specifically the rational functions unit.

---

## What This Tool Does

- **Generates** new collaborative activities based on your criteria
- **Evaluates** activity drafts you have already written
- Ensures every activity is mathematically rigorous, structurally collaborative, and
  completable in approximately 30 minutes

---

## How to Use

### Generating an Activity
1. Go to the **Generate Activity** tab
2. Select a topic from the dropdown menu
3. Optionally add special instructions or resource preferences
4. Click **Generate Activity** and wait 20-30 seconds
5. Review the generated activity and click **Save** to keep it

### Evaluating an Activity
1. Go to the **Evaluate Activity** tab
2. Paste the full text of your activity into the text box
3. Click **Evaluate Activity** and wait 30-60 seconds
4. Review the feedback report with scores across five dimensions
5. Use the required changes to improve your activity

### Viewing Saved Activities
1. Go to the **Saved Activities** tab
2. Click **View** next to any saved activity to read it in full

## Directory Structure

```
college-algebra-activity-designer/
│
├── app.py                          # Main entry point — run this to start the app
├── copilot-instructions.md         # Master ruleset for all AI agents
├── claude.md                       # Claude Code version of the master ruleset
├── requirements.txt                # Python packages needed to run the project
│
├── README.md                       # This file
├── architecture.md                 # How the system is built and how data flows
├── prd.md                          # Product requirements document
├── personas.md                     # Who uses this tool and how
├── domain-primer.md                # College algebra and pedagogy background
├── synthetic-data-strategy.md      # How test data is created
├── evaluation.md                   # How we measure success
├── development-checklist.md        # Step-by-step build plan
├── feedback-log.md                 # Record of all user feedback
│
├── .agents/                        # AI sub-agent definition files
│   ├── orchestrator.md
│   ├── activity-generator.md
│   ├── rigor-evaluator.md
│   ├── collaboration-auditor.md
│   ├── timing-estimator.md
│   ├── resource-mapper.md
│   └── reviewer.md
│
├── .skills/                        # Reusable task recipes for agents
│   ├── generate-activity.md
│   ├── evaluate-activity.md
│   ├── check-collaboration-structure.md
│   ├── estimate-timing.md
│   └── map-resources.md
│
├── prompt-library/                 # All LLM prompts stored here (never in code)
│   ├── generate-activity.txt
│   ├── evaluate-activity.txt
│   └── system-prompts.txt
│
├── activities/
│   ├── generated/                  # Activities created by the AI
│   └── drafts/                     # Your own drafts to be evaluated
│
└── synthetic-data/                 # Sample activities used for testing
```

---

## Setup Instructions

> **Note for new coders:** Follow these steps exactly, one at a time.
> If anything goes wrong, check the Troubleshooting section below.

### Step 1 — Make sure Python is installed

Open a terminal (in VS Code: go to **Terminal → New Terminal**) and type:

```bash
python --version
```

You should see something like `Python 3.11.x`. If you get an error, download Python from
https://www.python.org/downloads/ and install it first.

### Step 2 — Clone the repository from GitHub

```bash
git clone https://github.com/YOUR-USERNAME/college-algebra-activity-designer.git
cd college-algebra-activity-designer
```

Replace `YOUR-USERNAME` with your actual GitHub username.

### Step 3 — Create a virtual environment

A virtual environment keeps this project's packages separate from everything else on
your computer.

```bash
python -m venv venv
```

Then activate it:

- **On Mac/Linux:** `source venv/bin/activate`
- **On Windows:** `venv\Scripts\activate`

You should see `(venv)` appear at the start of your terminal line.

### Step 4 — Install required packages

```bash
pip install -r requirements.txt
```

### Step 5 — Add your Anthropic API key

Create a file called `.env` in the root of the project folder. Add this line:

```
ANTHROPIC_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual key from https://console.anthropic.com

> **Important:** Never share this file or commit it to GitHub.
> The `.gitignore` file will prevent it from being uploaded automatically.

### Step 6 — Run the app

```bash
streamlit run app.py
```

Your browser should open automatically to `http://localhost:8501`

---

## Troubleshooting

- **"command not found: python"** → Try `python3` instead of `python`
- **"No module named streamlit"** → Make sure your virtual environment is activated
  (you should see `(venv)` in your terminal)
- **API key errors** → Double-check your `.env` file has no extra spaces or quotes

---

## Pushing Changes to GitHub

After making changes, run these three commands in your terminal:

```bash
git add .
git commit -m "Describe what you changed here"
git push
```

## Evaluation Criteria

Activities generated and evaluated by this tool are scored on five dimensions:

| Dimension | Passing Score | What It Measures |
|-----------|--------------|------------------|
| Mathematical Rigor | 4 or higher | Content is correct, appropriately challenging, and in scope |
| Accessibility | 4 or higher | Solvable by college algebra students with prior knowledge |
| Structural Collaboration | 4 or higher | Collaboration is required by the task design, not just invited |
| Timing | 3 or higher | Activity fits within 30 minutes with a realistic breakdown |
| Resource Use | 3 or higher | Physical resources are used purposefully and creatively |

An activity is **APPROVED** only when all five dimensions meet their passing threshold.

### Scoring Scale
- **5** — Excellent, exceeds expectations
- **4** — Good, meets expectations
- **3** — Acceptable, meets minimum threshold
- **2** — Below expectations, needs revision
- **1** — Failing, requires significant rework

---

## Build Log

### Project Design Decisions

**Why three different AI models?**
This project uses deliberate model routing to balance cost and quality:
- **Claude Opus** is used for mathematical rigor evaluation and final synthesis
  because these tasks require the deepest reasoning and domain expertise
- **Claude Sonnet** is used for activity generation and resource mapping because
  these tasks require creativity and content quality
- **Claude Haiku** is used for collaboration auditing and timing estimation because
  these are structured checks that do not require deep reasoning

**Why multiple specialized agents instead of one?**
Each agent has a narrow, well-defined job. This makes the system more reliable and
easier to improve — if the collaboration feedback is too strict, we update only the
collaboration agent's context without touching anything else.

**Why a domain primer?**
Smaller models have less built-in knowledge about college algebra pedagogy. The
domain primer gives every agent the context it needs to make good decisions, including
what content is in scope, what common student errors look like, and what makes a
good collaboration mechanism.

### Iterations and Refinements

**Iteration 1 — Horizontal asymptote handling**
The rigor evaluator initially flagged functions where the numerator degree exceeds
the denominator degree as invalid. This was incorrect — these functions are valid
and desirable for student learning. The domain primer was updated to explicitly
allow these cases.

**Iteration 2 — Linear simplification edge cases**
The rigor evaluator flagged rational functions that simplify to linear functions as
needing replacement. These are excellent edge cases for students. The domain primer
was updated to explicitly allow them.

**Iteration 3 — Organic discussion phases**
The collaboration auditor was too strict, requiring defined roles for every phase
of an activity. Brief organic discussion phases (5 minutes or less) are valid
pedagogically. The domain primer was updated to allow them.

**Iteration 4 — Passing threshold consistency**
The reviewer agent was marking a timing score of 3 as NEEDS REVISION despite the
passing threshold being 3 or higher. The passing thresholds were added explicitly
to the reviewer agent's system prompt to fix this.

**Iteration 5 — Evaluation rubric integration**
The evaluation rubric in evaluation.md was not being read by the agents. A
load_evaluation_rubric() function was added to agents.py so all evaluator agents
now receive the scoring rubric in their system prompt.

### Known Limitations
- The tool is currently optimized for rational functions only. Other college algebra
  topics would require updating the domain primer.
- The accessibility dimension was added after initial deployment and may be less
  calibrated than the other four dimensions.
- Timing estimates are approximate and may vary based on class size and student
  preparation level.
- Saved activities are stored locally and do not persist on the deployed version. Important activities should be saved as files in the repository.
- **App sleep:** The deployed app on Streamlit Community Cloud may go to sleep
  after periods of inactivity. If the app does not load immediately, wait 
  30-60 seconds for it to wake up and then refresh the page.