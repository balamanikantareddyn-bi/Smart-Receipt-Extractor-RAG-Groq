import os
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from response_structure import ReceiptData
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model_name = "qwen/qwen3.8-27b",
    api_key=os.getenv('GROQ_API_KEY')
)

llm = llm.with_structured_output(ReceiptData)

prompt = PromptTemplate.from_template(
    """
    Extract the receipt details from the text below.
    Use this company policy context to help categorize the expense:
    {rag_context}
    
    Receipt Text:
    {raw_text}
    """
)

# Data flows from Prompt -> LLM -> Pydantic Model automatically
expense_chain = prompt | llm

def process_receipt_to_excel(raw_text: str, rag_context: str):
    """Executes the chain and exports the structured data to Pandas/Excel."""
    
    # Run the LCEL chain
    result: ReceiptData = expense_chain.invoke({
        "raw_text": raw_text,
        "rag_context": rag_context
    })
    data = result.model_dump()
    items_df = pd.DataFrame(data['items'])

    items_df['merchant'] = data['merchant_name']
    items_df['date'] = data['date']
    items_df['category'] = data['category']
    items_df['receipt_total'] = data['total_amount']

    file_name = 'expenses.xlsx'
    items_df.to_excel(file_name, index=False)

    return data, file_name