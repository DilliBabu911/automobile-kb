import streamlit as st
from analyzer import analyze_and_save
from database import init_db, get_all_complaints, delete_complaint

init_db()

st.set_page_config(page_title="Car Complaint Analyzer KB", page_icon="🚗", layout="centered")
st.title("🚗 Car Complaint Analyzer — Knowledge Base")

tab1, tab2 = st.tabs(["Ask a Complaint", "View History"])

with tab1:
    st.subheader("Describe your car problem")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Grinding noise on brake"):
            st.session_state.complaint = "My car makes a grinding noise when I press the brake"
    with col2:
        if st.button("White smoke from exhaust"):
            st.session_state.complaint = "White smoke is coming from my exhaust pipe"
    with col3:
        if st.button("Engine light is on"):
            st.session_state.complaint = "My check engine light is on and car vibrates"

    st.markdown("---")

    complaint = st.text_area(
        "Enter your car complaint:",
        value=st.session_state.get("complaint", ""),
        placeholder="e.g. My engine light is on and car vibrates at high speed",
        height=120
    )

    if st.button("Analyze My Car Problem", type="primary"):
        if complaint.strip():
            with st.spinner("AI is analyzing your complaint..."):
                result = analyze_and_save(complaint)
            st.success("Analysis Complete! Saved to Knowledge Base.")
            st.markdown("### Diagnosis Report")
            st.markdown(result)
        else:
            st.warning("Please enter a complaint first")

with tab2:
    st.subheader("Past Complaints & Answers")

    records = get_all_complaints()

    if not records:
        st.info("No complaints yet. Ask one in the first tab!")
    else:
        st.markdown(f"**Total records: {len(records)}**")
        st.markdown("---")
        for record in records:
            record_id, complaint, answer, asked_at = record
            with st.expander(f"🔹 {complaint[:60]}... — {asked_at}"):
                st.markdown(f"**Complaint:** {complaint}")
                st.markdown("**AI Diagnosis:**")
                st.markdown(answer)
                if st.button(f"Delete", key=f"del_{record_id}"):
                    delete_complaint(record_id)
                    st.rerun()

st.markdown("---")
st.caption("Powered by Groq AI — For reference only. Always consult a certified mechanic.")
