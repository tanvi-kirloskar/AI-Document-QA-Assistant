import streamlit as st
from dotenv import load_dotenv

from utils.loader import split_text
from utils.embeddings import create_vector_store
from utils.qa_chain import get_qa_chain

load_dotenv()

st.set_page_config(page_title="AI Document QA Assistant")

st.title("📄 AI Document QA Assistant")

st.write("Upload a TXT file or paste text and ask questions from it.")

# Upload TXT file
uploaded_file = st.file_uploader(
    "Upload TXT File",
    type=["txt"]
)

# Paste text manually
manual_text = st.text_area(
    "Or Paste Text Here"
)

text = ""

# Read uploaded file
if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

# Read pasted text
elif manual_text:
    text = manual_text

# If text exists
if text:

    st.success("Document Loaded Successfully!")

    # Split into chunks
    chunks = split_text(text)

    # Create vector database
    vectorstore = create_vector_store(chunks)

    # User question
    question = st.text_input("Ask a Question")

    ask_button = st.button("Get Answer")

    if question and ask_button:

        # Search relevant chunks
        docs = vectorstore.similarity_search(question)

        # Get AI model
        # Get most relevant document chunk
        best_match = docs[0].page_content

        st.subheader("Answer")

        st.write(best_match)