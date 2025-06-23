import easyocr
import numpy as np

# Function to extract text from image using OCR
def extract_text(image):
    # Convert PIL Image to NumPy array
    img_array = np.array(image)
    
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img_array)
    text = " ".join([item[1] for item in result])
    return text
