from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

rag_texts = [
    # Travel & Transportation
    "Ola, Uber, Rapido, and local auto-rickshaw receipts should always be categorized as 'Local Transport'.",
    "Flight tickets from IndiGo, Air India, or Akasa Air are classified as 'Airfare'.",
    "Hostel bookings, OYO rooms, Zostel, or MakeMyTrip stays fall under 'Accommodation'.",
    "Train tickets from IRCTC, RedBus bookings, and local metro recharges (DMRC, Namma Metro) should be marked as 'Travel'.",
    "Two-wheeler or car rentals from Zoomcar, Bounce, or Royal Brothers belong in 'Vehicle Rental'.",
    
    # Meals & Entertainment
    "Any receipt from Chai Point, Chaayos, or local campus canteens is 'Food & Beverages'.",
    "Treating juniors, seniors, or club meetings at restaurants should be coded as 'Club Meetings & Events'.",
    "Late-night study or hackathon food deliveries from Zomato, Swiggy, or EatSure belong in 'Team Perks'.",
    
    # Cloud & IT Infrastructure (For Projects/Hackathons)
    "AWS Educate, DigitalOcean, and Google Cloud (GCP) are 'Project Infrastructure' expenses.",
    "Domain registration and web hosting from Hostinger, GoDaddy, or BigRock is 'Domain & Hosting'.",
    
    # Software & Subscriptions (SaaS & Learning)
    "Monthly charges for ChatGPT Plus, Canva Pro, or Notion belong to 'Software Subscriptions'.",
    "Subscriptions for LeetCode Premium, GeeksforGeeks, or Coursera are categorized as 'Learning & Development'.",
    "Design tools like Adobe Creative Cloud or Figma (if paid) are 'Design Tools'.",
    
    # Study Materials & Electronics
    "Purchases of laptops or tablets from HP, Lenovo, Dell, or Asus are 'Electronics' and must be flagged as assets.",
    "Classmate notebooks, pens, and printouts from the local stationery shop or Blinkit are 'Stationery & Study Supplies'.",
    "General Amazon or Flipkart purchases should be reviewed manually, but default to 'Stationery' if under ₹500.",
    "Study tables, lap desks, or chairs from IKEA or Pepperfry fall under 'Hostel Furniture'.",
    
    # Fest Promotions & Event Organization
    "Charges for Instagram Ads or Facebook Ads to promote college fests are 'Marketing & Promotions'.",
    "Flex printing, banner creations, and stall booking fees are 'Event Organization'.",
    
    # Utilities & Telecommunications
    "Prepaid mobile recharges for Jio, Airtel, or Vi are 'Mobile Recharges'.",
    "Hostel or flat Wi-Fi bills from JioFiber, Airtel Xstream, or ACT Fibernet fall under 'Broadband & Internet'."
]

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = Chroma.from_texts(rag_texts, embeddings)
retriver = vector_store.as_retriever(search_kwargs={'k':2})

def get_context(query:str) -> str:
    """Retrieve relevant policies based on the receipt text and type"""
    docs = retriver.invoke(query)
    return '\n'.join([doc.page_content for doc in docs])