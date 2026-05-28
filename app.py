import streamlit as st
from database import initialize_database, save_activity, get_all_activities, get_activity_by_id
from agents import (
    generate_activity,
    evaluate_rigor,
    evaluate_collaboration,
    evaluate_timing,
    evaluate_resources,
    synthesize_feedback
)

# Initialize the database when the app starts
initialize_database()

# Page configuration
st.set_page_config(
    page_title="College Algebra Activity Designer",
    page_icon="📐",
    layout="wide"
)

st.title("📐 College Algebra Activity Designer")
st.write("Generate and evaluate collaborative classroom activities for rational functions.")

# Create two tabs
tab1, tab2, tab3 = st.tabs(["Generate Activity", "Evaluate Activity", "Saved Activities"])

# ─────────────────────────────────────────
# TAB 1 — GENERATE ACTIVITY
# ─────────────────────────────────────────
with tab1:
    st.header("Generate a New Activity")
    st.write("Fill in the form below and click Generate to create a new activity.")

    topic = st.selectbox(
        "Select a topic:",
        [
            "Simplifying rational expressions and factoring",
            "Finding holes (removable discontinuities)",
            "Finding vertical asymptotes",
            "Finding horizontal asymptotes",
            "Finding x-intercepts and y-intercepts",
            "All features of rational functions (comprehensive)"
        ]
    )

    constraints = st.text_area(
        "Any special instructions? (optional)",
        placeholder="Example: I want students to use the whiteboards. "
                    "Or: Make it a gallery walk format.",
        height=100
    )

    resources = st.text_area(
        "Available resources:",
        value="Large tabletop whiteboards, individual dry-erase markers, "
              "math manipulatives, printer, scissors, tape, standard office supplies",
        height=100
    )

    if st.button("✨ Generate Activity", type="primary"):
        with st.spinner("Generating your activity... this may take 20-30 seconds."):
            try:
                activity = generate_activity(topic, constraints, resources)
                st.session_state["generated_activity"] = activity
                st.session_state["generated_topic"] = topic
            except Exception as e:
                st.error(f"Something went wrong: {e}")

    if "generated_activity" in st.session_state:
        st.subheader("Your Generated Activity")
        st.markdown(st.session_state["generated_activity"])

        if st.button("💾 Save This Activity"):
            lines = st.session_state["generated_activity"].split("\n")
            title = lines[0].replace("#", "").strip()
            save_activity(
                title=title,
                topic=st.session_state["generated_topic"],
                content=st.session_state["generated_activity"]
            )
            st.success("Activity saved!")

# ─────────────────────────────────────────
# TAB 2 — EVALUATE ACTIVITY
# ─────────────────────────────────────────
with tab2:
    st.header("Evaluate an Activity Draft")
    st.write("Paste your activity below and click Evaluate to receive structured feedback.")

    draft = st.text_area(
        "Paste your activity here:",
        placeholder="Paste the full text of your activity here...",
        height=400
    )

    if st.button("🔍 Evaluate Activity", type="primary"):
        if not draft.strip():
            st.warning("Please paste an activity before evaluating.")
        else:
            with st.spinner("Running evaluation... this may take 30-60 seconds."):
                try:
                    rigor = evaluate_rigor(draft)
                    collaboration = evaluate_collaboration(draft)
                    timing = evaluate_timing(draft)
                    resources_eval = evaluate_resources(draft)
                    report = synthesize_feedback(
                        draft, rigor, collaboration, timing, resources_eval
                    )
                    st.session_state["evaluation_report"] = report
                except Exception as e:
                    st.error(f"Something went wrong: {e}")

    if "evaluation_report" in st.session_state:
        st.subheader("Evaluation Report")
        st.markdown(st.session_state["evaluation_report"])

# ─────────────────────────────────────────
# TAB 3 — SAVED ACTIVITIES
# ─────────────────────────────────────────
with tab3:
    st.header("Saved Activities")
    st.write("All activities you have saved are listed here.")

    activities = get_all_activities()

    if not activities:
        st.info("No activities saved yet. Generate one in the first tab!")
    else:
        for activity in activities:
            activity_id, title, topic, created_at = activity
            with st.expander(f"{title} — {topic}"):
                st.write(f"**Saved on:** {created_at[:10]}")
                if st.button(f"View Full Activity", key=f"view_{activity_id}"):
                    full = get_activity_by_id(activity_id)
                    st.markdown(full[3])