import anthropic
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Works locally with .env and on Streamlit Cloud with secrets
if "ANTHROPIC_API_KEY" in st.secrets:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
else:
    api_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=api_key)

# Model names for each tier
OPUS = "claude-opus-4-5"
SONNET = "claude-sonnet-4-5"
HAIKU = "claude-haiku-4-5-20251001"


def load_prompt(filename: str) -> str:
    """Load a prompt from the prompt-library folder."""
    path = os.path.join("prompt-library", filename)
    with open(path, "r") as f:
        return f.read()


def load_domain_primer() -> str:
    """Load the domain primer for context."""
    with open("domain-primer.md", "r") as f:
        return f.read()


def load_evaluation_rubric() -> str:
    """Load the evaluation rubric for scoring guidance."""
    with open("evaluation.md", "r") as f:
        return f.read()


def generate_activity(topic: str, constraints: str, resources: str) -> str:
    """Generate a new activity using the Activity Generator agent (Sonnet)."""
    domain_primer = load_domain_primer()
    prompt_template = load_prompt("generate-activity.txt")

    prompt = prompt_template.replace("{TOPIC}", topic)
    prompt = prompt.replace("{CONSTRAINTS}", constraints)
    prompt = prompt.replace("{RESOURCES}", resources)

    message = client.messages.create(
        model=SONNET,
        max_tokens=3000,
        system=(f"You are an expert mathematics education activity designer. "
                f"Here is your domain knowledge:\n\n{domain_primer}"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text


def evaluate_rigor(activity_text: str) -> str:
    """Evaluate mathematical rigor using the Rigor Evaluator agent (Opus)."""
    domain_primer = load_domain_primer()
    rubric = load_evaluation_rubric()
    prompt_template = load_prompt("evaluate-activity.txt")

    prompt = prompt_template.replace("{ACTIVITY_TEXT}", activity_text)
    prompt = prompt.replace("{DIMENSION}", "Mathematical Rigor")

    message = client.messages.create(
        model=OPUS,
        max_tokens=1000,
        system=(f"You are a rigorous mathematics education reviewer. "
                f"Here is your domain knowledge:\n\n{domain_primer}\n\n"
                f"Here is your scoring rubric:\n\n{rubric}"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def evaluate_accessibility(activity_text: str) -> str:
    """Evaluate accessibility using the Accessibility Evaluator agent (Haiku)."""
    domain_primer = load_domain_primer()
    rubric = load_evaluation_rubric()
    prompt_template = load_prompt("evaluate-activity.txt")

    prompt = prompt_template.replace("{ACTIVITY_TEXT}", activity_text)
    prompt = prompt.replace("{DIMENSION}", "Accessibility")

    message = client.messages.create(
        model=HAIKU,
        max_tokens=500,
        system=(f"You are an expert in mathematics education accessibility. "
                f"Here is your domain knowledge:\n\n{domain_primer}\n\n"
                f"Here is your scoring rubric:\n\n{rubric}"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def evaluate_collaboration(activity_text: str) -> str:
    """Evaluate structural collaboration using the Collaboration Auditor (Haiku)."""
    domain_primer = load_domain_primer()
    rubric = load_evaluation_rubric()
    prompt_template = load_prompt("evaluate-activity.txt")

    prompt = prompt_template.replace("{ACTIVITY_TEXT}", activity_text)
    prompt = prompt.replace("{DIMENSION}", "Structural Collaboration")

    message = client.messages.create(
        model=HAIKU,
        max_tokens=1000,
        system=(f"You are a collaborative learning expert. "
                f"Here is your domain knowledge:\n\n{domain_primer}\n\n"
                f"Here is your scoring rubric:\n\n{rubric}"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text


def evaluate_timing(activity_text: str) -> str:
    """Evaluate timing using the Timing Estimator agent (Haiku)."""
    rubric = load_evaluation_rubric()
    prompt_template = load_prompt("evaluate-activity.txt")

    prompt = prompt_template.replace("{ACTIVITY_TEXT}", activity_text)
    prompt = prompt.replace("{DIMENSION}", "Timing")

    message = client.messages.create(
        model=HAIKU,
        max_tokens=500,
        system=(f"You are an expert at estimating how long classroom activities take."
                f"\n\nHere is your scoring rubric:\n\n{rubric}"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text


def evaluate_resources(activity_text: str) -> str:
    """Evaluate resource use using the Resource Mapper agent (Sonnet)."""
    rubric = load_evaluation_rubric()
    prompt_template = load_prompt("evaluate-activity.txt")

    prompt = prompt_template.replace("{ACTIVITY_TEXT}", activity_text)
    prompt = prompt.replace("{DIMENSION}", "Resource Use")

    message = client.messages.create(
        model=SONNET,
        max_tokens=500,
        system=(f"You are an expert in creative use of physical classroom resources."
                f"\n\nHere is your scoring rubric:\n\n{rubric}"),
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text


def synthesize_feedback(activity_text: str, rigor: str, accessibility: str, collaboration: str,
                        timing: str, resources: str) -> str:
    """Synthesize all evaluations into a final report using the Reviewer (Opus)."""
    message = client.messages.create(
        model=OPUS,
        max_tokens=1500,
        system=("You are a senior mathematics education reviewer. Your job is to "
                "synthesize evaluation reports into clear, actionable feedback for "
                "a university instructor. "
                "Use these exact passing thresholds when deciding APPROVED or NEEDS REVISION:\n"
                "- Mathematical Rigor: must score 4 or higher\n"
                "- Accessibility: must score 4 or higher\n"
                "- Structural Collaboration: must score 4 or higher\n"
                "- Timing: must score 3 or higher\n"
                "- Resource Use: must score 3 or higher\n"
                "An activity is APPROVED only if ALL dimensions meet their threshold. "
                "A timing score of 3 is a PASS, not a failure."),
        messages=[
            {"role": "user", "content": f"""
You have received four evaluation reports for a college algebra activity.
Synthesize them into a final feedback report.

ORIGINAL ACTIVITY:
{activity_text}

RIGOR EVALUATION:
{rigor}

ACCESSIBILITY EVALUATION:
{accessibility}

COLLABORATION EVALUATION:
{collaboration}

TIMING EVALUATION:
{timing}

RESOURCE USE EVALUATION:
{resources}

Write a final report with:
1. A summary paragraph
2. A scorecard table (all four dimensions with scores)
3. Overall verdict: APPROVED or NEEDS REVISION
4. Required changes (if NEEDS REVISION)
5. One sentence of genuine encouragement
"""}
        ]
    )
    return message.content[0].text