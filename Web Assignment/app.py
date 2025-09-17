import streamlit as st
from document_parser import parse_documents
from qa_engine import get_llm_answer

st.title("📊 Financial Document QA")

uploaded_files = st.file_uploader("Upload PDF or Excel", type=['pdf', 'xlsx'], accept_multiple_files=True)
if uploaded_files:
    docs_data = parse_documents(uploaded_files)
    if docs_data:
        st.success("Documents processed successfully.")
        user_query = st.text_input("Ask your question about the financials:")
        if user_query:
            answer = get_llm_answer(user_query, docs_data)
            st.write(f"**Answer:** {answer}")
    else:
        st.error("Could not process documents.")
else:
    st.info("Upload at least one financial document to begin.")
