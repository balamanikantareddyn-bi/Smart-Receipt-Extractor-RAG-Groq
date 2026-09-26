import os
import streamlit as st
from PIL import Image
from ocr import extract_text_from_image
from rag import get_context
from chain import process_receipt_to_excel

# Page Configuration
st.set_page_config(
    page_title="AI Expense Parser & RAG Pipeline",
    page_icon="🧾",
    layout="centered"
)

st.title("🧾 AI-Powered Expense & Document RAG Pipeline")
st.markdown("Upload a receipt image to extract data, query policy context via ChromaDB, and export structured financial records to Excel.")

# File Uploader component
uploaded_file = st.file_uploader("Choose a receipt image...", type=["jpg", "jpeg", "png", "bmp", "tiff"])

if uploaded_file is not None:
    # Create temp directory if it doesn't exist
    os.makedirs("./receipts", exist_ok=True)
    file_path = os.path.join("./receipts", uploaded_file.name)
    
    # Save the uploaded file temporarily
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display image preview
    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_file, caption="Uploaded Receipt", use_container_width=True)

    with col2:
        if st.button("🚀 Process Receipt", type="primary"):
            with st.spinner("Running OCR, ChromaDB RAG, and Groq LLM extraction..."):
                try:
                    # Step A: OCR Extraction
                    raw_text = extract_text_from_image(file_path)
                    
                    if not raw_text:
                        st.error("⚠️ Could not extract text from the image.")
                    else:
                        st.text_area("Extracted OCR Text", raw_text, height=150)

                        # Step B: RAG Context
                        context = get_context(raw_text)

                        # Step C: Chain Execution & Excel Export
                        extracted_json, saved_file = process_receipt_to_excel(
                            raw_text=raw_text,
                            rag_context=context
                        )

                        st.success("Extraction Complete!")
                        
                        # Display JSON Results
                        st.subheader("Structured JSON Output")
                        st.json(extracted_json)

                        # Provide Download Button for Excel
                        with open(saved_file, "rb") as f:
                            st.download_button(
                                label="📥 Download Excel Report",
                                data=f,
                                file_name=os.path.basename(saved_file),
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )

                except Exception as e:
                    st.error(f"An error occurred during processing: {e}")