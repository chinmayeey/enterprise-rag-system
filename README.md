# 🏢 Enterprise RAG System – Resume Q&A with Hybrid Retrieval

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-orange?logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🚀 Project Overview

**Enterprise RAG System** is a **local hybrid Retrieval-Augmented Generation (RAG) AI system** built to answer questions from PDF resumes.  

- Upload PDF resumes  
- Automatically process and split documents  
- Retrieve the most relevant sections using **Vector Search + BM25 keyword retrieval**  
- Display answers interactively in **Streamlit**  

Fully local, **Python-based**, privacy-safe, and portfolio-ready.

---

## 🎯 Features

- ✅ Upload multiple PDF resumes  
- ✅ Hybrid retrieval (Vector + BM25 keyword search)  
- ✅ Easy-to-use Streamlit interface  
- ✅ Fully offline; data never leaves your machine  
- ✅ Lightweight and beginner-friendly Python project  

---

## 📁 Folder Structure

```text
enterprise-rag-system/
├── app.py                # Streamlit application
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── data/                 # Uploaded PDFs (not pushed to GitHub)
└── src/                  # Project source code
    ├── ingestion.py      # Load & split PDFs
    ├── embedding.py      # Vector store for retrieval
    └── retriever.py      # Hybrid retriever logic


📌 How It Works
PDF Loading: Extracts text from all uploaded resumes (src/ingestion.py)

Document Splitting: Breaks long documents into smaller chunks for better retrieval

Embedding: Generates vector representations for semantic search (src/embedding.py)

Hybrid Retrieval: Combines vector similarity and BM25 keyword search to find relevant sections (src/retriever.py)

Streamlit UI: Shows the most relevant resume sections based on user query

🛠 Installation (Python 3.13)
Clone the repository:
git clone https://github.com/chinmayeey/enterprise-rag-system.git
cd enterprise-rag-system

Create a virtual environment and activate it:
python -m venv venv
venv\Scripts\activate

Upgrade pip, setuptools, and wheel:
python -m pip install --upgrade pip setuptools wheel

Install dependencies:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

Open your browser → upload PDF resumes → ask questions.
