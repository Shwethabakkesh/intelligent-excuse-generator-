import streamlit as st
from ai_model import generate_excuse, generate_apology
from proof_generator import create_fake_document
from emergency_alert import simulate_emergency_text, simulate_call_message
from history_manager import save_excuse, get_history
from translator import translate_text

st.set_page_config(page_title="Intelligent Excuse Generator", layout="centered")

st.title("🤖 Intelligent Excuse Generator")

context = st.selectbox("Where do you need an excuse?", ["Work", "School", "Family", "Friends"])
urgency = st.slider("Urgency Level", 1, 5)
tone = st.radio("Tone", ["Professional", "Emotional", "Casual"])
name = st.text_input("Enter your name")
reason = st.text_input("Enter reason (for fake proof)")

if st.button("Generate Excuse"):
    if not name or not reason:
        st.warning("Please fill in all fields.")
    else:
        excuse = generate_excuse(context, urgency, tone)
        st.success(f"Excuse: {excuse}")
        save_excuse(excuse)

        st.subheader("Apology Message")
        st.info(generate_apology(context))

        st.subheader("Fake Proof Document")
        path = create_fake_document(name, reason)
        st.write(f"Document saved to: {path}")

        st.subheader("Emergency Message")
        st.warning(simulate_emergency_text(name, "family emergency"))
        st.warning(simulate_call_message(name))

        st.subheader("Hindi Translation")
        st.write(translate_text(excuse, 'hi'))

        st.subheader("Past Excuses")
        for i, item in enumerate(get_history()):
            st.text(f"{i+1}. {item}")
