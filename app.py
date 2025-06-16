import streamlit as st
from backend import generate_flashcards
from utils import extract_text_from_file

st.set_page_config(page_title="LLM Flashcard Generator", layout="wide")

st.title("📚 LLM-Powered Flashcard Generator")

uploaded_file = st.file_uploader("Upload your study material (.txt or .pdf)", type=["txt", "pdf"])
manual_input = st.text_area("Or paste educational content directly", height=300)

subject = st.selectbox("Select subject type (optional)", ["General", "Biology", "History", "CS", "Physics", "Math"])

if st.button("Generate Flashcards"):
    if uploaded_file:
        content = extract_text_from_file(uploaded_file)
    elif manual_input.strip():
        content = manual_input
    else:
        st.warning("Please upload a file or paste some content.")
        st.stop()

    with st.spinner("Generating flashcards..."):
        flashcards = generate_flashcards(content, subject=subject)

    if flashcards:
        st.success(f"✅ Generated {len(flashcards)} flashcards:")

        for i, card in enumerate(flashcards, 1):
            with st.expander(f"Flashcard {i}"):
                st.markdown(f"**Q:** {card['question']}")
                st.markdown(f"**A:** {card['answer']}")

        # ✅ Show raw output at bottom (optional but useful)
        st.subheader("🧠 Raw Flashcard List")
        raw_text_output = "\n\n".join([f"Q: {fc['question']}\nA: {fc['answer']}" for fc in flashcards])
        st.code(raw_text_output, language="markdown")

    else:
        st.error("⚠️ No flashcards generated. Try with different input.")
