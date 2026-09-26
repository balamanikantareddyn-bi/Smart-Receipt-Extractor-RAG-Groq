# 🧾 AI-Powered Expense Agent & Document RAG Pipeline

A production-ready, full-stack AI application that extracts unstructured receipt data from images using OCR, enriches context with company expense policies via a ChromaDB RAG pipeline, enforces strict type-safety using Pydantic, and exports structured financial records directly into Microsoft Excel through an interactive Streamlit web interface.

---

## 🌟 Project Description & Overview

Handling expense reports, manually sorting receipts, and categorizing line items into proper accounting ledgers is a tedious, error-prone administrative burden. This project solves that problem by building an autonomous document processing pipeline. 

When a user drops a receipt image into the web interface:
1. **OCR Extraction:** The system reads the image file and extracts raw, unformatted text strings.
2. **RAG Context Retrieval:** A local **ChromaDB** vector store searches pre-loaded company policies (e.g., travel guidelines, software spending rules) and injects the relevant context.
3. **Structured Generation (Groq + LangChain):** Utilizing **Groq's** blazing-fast `llama-3.1-8b-instant` model combined with **Pydantic** schemas, the LLM parses the messy text into a validated, type-safe JSON object.
4. **Data Engineering & Export:** **Pandas** cleans the numerical data, structures line items, and generates an automated `.xlsx` spreadsheet ready for instant download.

---

## 🛠️ Tech Stack

* **AI & Orchestration:** LangChain (LCEL), Groq API (`llama-3.1-8b-instant`), Pydantic
* **RAG & Embeddings:** ChromaDB, HuggingFace Local Embeddings (`all-MiniLM-L6-v2`)
* **Data Processing:** Python, Pandas, Openpyxl
* **Computer Vision & UI:** Tesseract OCR, Pillow (PIL), Streamlit

---

## 📂 Project Architecture

```text
expense_project/
│
├── .env                 # Environment variables (API keys)
├── schemas.py           # Pydantic data models for structured validation
├── rag.py               # ChromaDB vector store and policy retriever setup
├── ocr.py               # Image processing and Tesseract OCR wrapper
├── chain.py             # LangChain LCEL pipeline & Pandas Excel exporter
├── app.py               # Streamlit interactive frontend UI
└── receipts/            # Local directory for uploaded receipt files
