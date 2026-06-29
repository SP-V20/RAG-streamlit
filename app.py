import streamlit as st
from rag import get_answer

st.set_page_config(
    page_title="RAG Demo",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Simple RAG App")
st.write("Ask questions based on your PDF knowledge base.")

# ---- Session state for chat history ----
if "history" not in st.session_state:
    st.session_state.history = []

# ---- Input box ----
query = st.text_input("Ask a question:")

if st.button("Get Answer") and query:
    with st.spinner("Thinking..."):
        answer = get_answer(query)

    # Save to history
    st.session_state.history.append((query, answer))

# ---- Display chat history ----
st.divider()
st.subheader("Chat History")

for q, a in reversed(st.session_state.history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Assistant:** {a}")
    st.markdown("---")