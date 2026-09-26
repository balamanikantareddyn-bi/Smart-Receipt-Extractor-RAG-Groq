from rag import get_context
from chain import process_receipt_to_excel
from pathlib import Path
from ocr import extract_text_from_image
import os


file_name = os.listdir('./receipts')[0]
file_path = os.path.join('./receipts', file_name)

receipt_text = extract_text_from_image(file_path)

if __name__ == "__main__":
    print("Fetching context from ChromaDB...")
    context = get_context(receipt_text)
    
    print("Extracting data via Groq and LangChain LCEL...")
    extracted_json, saved_file = process_receipt_to_excel(
        raw_text=receipt_text,
        rag_context=context
    )
    
    print("\n--- Extracted JSON Data ---")
    print(extracted_json)
    print(f"\n✅ Success! Data exported to {saved_file}")