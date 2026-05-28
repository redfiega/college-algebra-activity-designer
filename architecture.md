# Architecture

## Project: College Algebra Activity Designer

---

## 1. Overview

This is a locally-run Python application with a simple browser-based interface built
using Streamlit. The instructor runs it on their own computer. It connects to the
Anthropic Claude API to power the AI agents.

There is no server, no cloud hosting, and no database in the cloud. Everything lives on
the instructor's machine.

---

## 2. Tech Stack

| Layer         | Technology         | Why                                              |
|---------------|--------------------|--------------------------------------------------|
| Interface     | Streamlit          | Simple browser UI, no web development needed     |
| Language      | Python 3.11+       | Widely supported, readable, great AI libraries   |
| LLM Provider  | Anthropic Claude   | Best-in-class reasoning for educational content  |
| Storage       | SQLite             | Simple local database, no setup required         |
| Config        | python-dotenv      | Loads API key from .env file safely              |
| Version Control | GitHub           | Standard; enables collaboration and backup       |

---

## 3. System Components

```
┌─────────────────────────────────────────────────────────────┐
│                      Streamlit UI (app.py)                   │
│                                                             │
│   [Generate Activity Tab]    [Evaluate Activity Tab]        │
└──────────────────┬──────────────────────┬───────────────────┘
                   │                      │
                   ▼                      ▼
┌──────────────────────────────────────────────────────────────┐
│                    Orchestrator Agent                         │
│              (claude-opus-4-5 — plans & delegates)           │
└──────┬───────────┬──────────┬──────────┬──────────┬──────────┘
       │           │          │          │          │
       ▼           ▼          ▼          ▼          ▼
  Activity     Rigor      Collab.    Timing    Resource
  Generator   Evaluator   Auditor   Estimator   Mapper
  (Sonnet)    (Opus)      (Haiku)   (Haiku)    (Sonnet)
       │           │          │          │          │
       └───────────┴──────────┴──────────┴──────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  Reviewer Agent │
                    │    (Opus)       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  SQLite Database│
                    │  (activities.db)│
                    └─────────────────┘
```

---

## 4. Data Flow

### Generate Activity Flow
1. Instructor fills out form in UI (topic, constraints, resource preferences)
2. UI sends request to Orchestrator
3. Orchestrator delegates to Activity Generator (Sonnet)
4. Activity Generator drafts activity using prompt from `/prompt-library/`
5. Rigor Evaluator (Opus) checks mathematical correctness
6. Collaboration Auditor (Haiku) checks structural collaboration mechanism
7. Timing Estimator (Haiku) validates time breakdown
8. Resource Mapper (Sonnet) ensures physical resources are incorporated
9. Reviewer (Opus) gives final approval or sends back for revision
10. Approved activity displayed in UI and saved to SQLite database

### Evaluate Activity Flow
1. Instructor pastes draft activity into UI
2. UI sends to Orchestrator
3. Orchestrator runs all five evaluator agents in parallel
4. Each agent returns a score (1–5) and written feedback
5. Reviewer (Opus) synthesizes feedback into a structured report
6. Report displayed in UI

---

## 5. File Structure

```
college-algebra-activity-designer/
├── app.py                    # Streamlit entry point
├── agents.py                 # Python code that runs each agent
├── database.py               # SQLite read/write functions
├── .env                      # API key (never committed to GitHub)
├── requirements.txt          # Python dependencies
├── activities.db             # SQLite database (auto-created on first run)
│
├── prompt-library/           # All LLM prompts stored as text files
│   ├── system-prompts.txt
│   ├── generate-activity.txt
│   └── evaluate-activity.txt
│
├── .agents/                  # Agent definition Markdown files
├── .skills/                  # Skill recipe Markdown files
└── synthetic-data/           # Sample activities for testing
```

---

## 6. Model Routing Logic

```
Task                              → Model
─────────────────────────────────────────────────────
Orchestration / planning          → claude-opus-4-5
Mathematical rigor evaluation     → claude-opus-4-5
Final review / synthesis          → claude-opus-4-5
Activity generation               → claude-sonnet-4-5
Resource mapping                  → claude-sonnet-4-5
Collaboration structure check     → claude-haiku-4-5-20251001
Timing estimation                 → claude-haiku-4-5-20251001
```

---

## 7. Privacy and Security

- The API key is stored only in the `.env` file on the instructor's local machine
- The `.gitignore` file prevents `.env` from being uploaded to GitHub
- No student data is collected or stored
- All data stays on the instructor's local machine