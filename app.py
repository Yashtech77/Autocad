import os
import streamlit as st
from PIL import Image
from openai import OpenAI
from dotenv import load_dotenv
from utils import ocr, material_estimator, detection_model

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Validate API key
if not OPENAI_API_KEY:
    st.error("OpenAI API key not found. Please set OPENAI_API_KEY in your environment.")
    st.stop()

# Initialize OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)

# UI Title and Description
st.title("AutoCAD Image-Based Material Estimation")
st.write("""
This app analyzes AutoCAD images to automatically estimate materials required for construction. Upload your AutoCAD image below to get started.
""")

# File uploader widget
uploaded_file = st.file_uploader("Upload an AutoCAD Drawing (Image or PDF)", type=["jpg", "png", "jpeg", "pdf"])

if uploaded_file is not None:
    # Image or PDF handling
    if uploaded_file.type == "application/pdf":
        st.write("Processing PDF...")
        # Handle PDF extraction here
        # pdf_data = extract_pdf_data(uploaded_file)
    else:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded AutoCAD Image", use_column_width=True)

        # Perform image-based analysis and extraction
        with st.spinner('Analyzing the image...'):
            # OCR Text Extraction
            extracted_text = ocr.extract_text(image)
            st.write("### Extracted Text:")
            st.text(extracted_text)

            # Estimate Materials using object detection and material estimation logic
            detected_elements = detection_model.detect_architectural_elements(image)
            st.write("### Detected Architectural Elements:")
            for element, count in detected_elements.items():
                st.write(f"{element}: {count}")

            # Material Estimation based on detected elements
            estimated_materials = material_estimator.estimate_materials(detected_elements)
            st.write("### Raw Material Estimate:")
            for category, materials in estimated_materials.items():
                st.write(f"**{category}:**")
                for material, details in materials.items():
                    st.write(f"**{material}:** {details}")

            # Provide a brief description of the image
            description = material_estimator.generate_image_description(detected_elements)
            st.write("### Image Description:")
            st.write(description)

    # Follow-up questions
    user_question = st.text_input("Ask a follow-up question about the material estimate:")
    if user_question:
        try:
            response = client.chat.completions.create(
                model="gpt-4",  # Update to use GPT-4
                messages=[
                    {"role": "system", "content": "You are a helpful assistant with expertise in construction and material estimation."},
                    {"role": "user", "content": user_question}
                ],
                temperature=0.7,
                max_tokens=150
            )
            answer = response.choices[0].message['content'].strip()  # Fix response access
            st.write(f"*Response:* {answer}")
        except Exception as e:
            st.error(f"Error from OpenAI: {e}")
