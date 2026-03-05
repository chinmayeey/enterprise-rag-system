import streamlit as st
from src.ingestion import load_documents, split_documents
from src.embedding import create_vector_store
from src.retriever import HybridRetriever

st.set_page_config(page_title="Resume Assistant", layout="wide")

st.title("📝 Resume Assistant - Hybrid Retrieval System")
st.write("Upload your resume PDF(s) and ask questions. The system will find the most relevant sections.")

# Upload PDF
uploaded_files = st.file_uploader(
    "Upload PDF(s) of your resume",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    # Save uploaded files to temp folder
    import os
    data_path = "data"
    os.makedirs(data_path, exist_ok=True)
    for file in uploaded_files:
        with open(os.path.join(data_path, file.name), "wb") as f:
            f.write(file.getbuffer())
    
    # Process documents
    with st.spinner("Processing resumes..."):
        documents = load_documents(data_path)
        split_docs = split_documents(documents)
        vectorstore = create_vector_store(split_docs)
    
    # Initialize retriever
    retriever = HybridRetriever(vectorstore, split_docs)

    # User query
    query = st.text_input("Ask a question about the uploaded resume(s):")

    if query:
        retrieved_docs = retriever.retrieve(query)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        st.subheader("Relevant Resume Sections")
        st.write(context[:2000])  # show first 2000 chars