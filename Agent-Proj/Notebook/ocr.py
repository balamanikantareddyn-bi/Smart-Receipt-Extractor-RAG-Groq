import pytesseract
from PIL import Image
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def extract_text_from_image(image_path: str, ) -> str:
    """Reads an image file and returns extracted text using OCR."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text.strip()
