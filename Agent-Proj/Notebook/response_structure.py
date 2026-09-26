from pydantic import BaseModel, Field
from typing import List, Optional

class LineItem(BaseModel):
    Name : str = Field(description="Name of the item purchased")
    quantity : int = Field(description=f"no.of {Name} Purchased")
    price: float = Field(description="Price of each item")
    Total : float = Field(description="Total Price : qunatity * Price")

class ReceiptData(BaseModel):
    merchant_name: str = Field(description="Name of the store or shop")
    date: str = Field(description="Date of purchase in DD-MM-YYYY format")
    total_amount: float = Field(description="Total amount paid for the bill")
    tax_amount: Optional[float] = Field(description="Tax amount", default=0.0)
    items: List[LineItem] = Field(description="List of individual items purchased one line item for one iem type")
    category: str = Field(description="Expense category (e.g., Software, Travel, Food)")

