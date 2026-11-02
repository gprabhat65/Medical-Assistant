
import os
import streamlit as st
import pytesseract

from PIL import Image
from google import genai
from google.genai import types


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Medical Assistant",
    page_icon="💊",
    layout="centered"
)


# =========================================================
# TESSERACT OCR CONFIGURATION
# =========================================================

# Optional: Set TESSERACT_CMD in your local environment
# if Windows cannot locate the Tesseract executable.

tesseract_path = os.getenv("TESSERACT_CMD")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path


# =========================================================
# GEMINI API CONFIGURATION
# =========================================================

def get_gemini_api_key():

    api_key = os.getenv("GEMINI_API_KEY", "")

    if not api_key:
        try:
            api_key = st.secrets.get("GEMINI_API_KEY", "")
        except Exception:
            api_key = ""

    return api_key


api_key = get_gemini_api_key()

if not api_key:
    st.error(
        "Gemini API key is missing. "
        "Add GEMINI_API_KEY to your Streamlit secrets."
    )
    st.stop()


@st.cache_resource
def initialize_gemini(key):

    return genai.Client(api_key=key)


try:
    gemini_client = initialize_gemini(api_key)
except Exception as e:
    st.error(f"Unable to initialize Gemini: {e}")
    st.stop()


# =========================================================
# APPLICATION HEADER
# =========================================================

st.markdown(
    """
    <div style="text-align:center;">
        <img
            src="https://www.freepnglogos.com/uploads/medicine-logo-png-1.png"
            width="100"
        >
        <h1>MEDICAL ASSISTANT</h1>
        <h3>Your AI-powered medicine information assistant</h3>
        <p>Understand medicines and health information with AI.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("⚙️ Settings")
st.sidebar.success("Gemini AI Connected")
st.sidebar.caption("Powered by Google Gemini")


# =========================================================
# LOAD EXAMPLE TEMPLATE
# =========================================================

@st.cache_data
def load_example():

    try:
        with open("example.txt", "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return ""


example = load_example()


# =========================================================
# GEMINI RESPONSE FUNCTION
# =========================================================

def ans(inp, lang):

    system_prompt = f"""
You are a professional medical information assistant.

Your purpose is to provide clear, general, evidence-based
educational information about medicines and diseases.

Respond in this language: {lang}

For medicine or disease-related questions, organize the
response using these sections where applicable:

1. Introduction
2. Medical Uses and Purpose
3. General Mechanism of Action
4. Common Side Effects
5. Important Precautions
6. Potential Drug Interactions
7. When to Seek Medical Attention

Reference format, where applicable:

{example}

IMPORTANT MEDICAL SAFETY RULES:

- Do not diagnose medical conditions.
- Do not prescribe medicines or dosages.
- Do not recommend stopping prescribed medication.
- Do not invent medical facts or drug interactions.
- Clearly communicate uncertainty.
- Ask the user to verify unclear medicine names.
- Explain that medical treatment depends on individual
  circumstances.
- Recommend consulting a qualified healthcare professional.
- For emergencies, advise seeking immediate medical care.
- Do not treat OCR-extracted text as verified medical information.
"""

    try:

        response = gemini_client.models.generate_content(
            model="gemini-flash-latest",

            contents=f"""
Provide educational medical information about:

{inp}
""",

            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.3,
                max_output_tokens=1500
            )
        )

        if response.text:
            return response.text

        return "Gemini returned an empty response. Please try again."

    except Exception as e:

        return f"Gemini API request failed: {str(e)}"


# =========================================================
# OCR FUNCTION
# =========================================================

def get_text(image_data):

    try:
        extracted_text = pytesseract.image_to_string(
            image_data
        )

        return extracted_text.strip()

    except Exception as e:

        raise RuntimeError(f"OCR extraction failed: {e}")


# =========================================================
# LANGUAGE SELECTION
# =========================================================

st.divider()

st.subheader("🌐 Select Language")

option = st.selectbox(
    "Choose your preferred language",
    ["English", "Hindi", "Nepali"]
)

st.divider()


# =========================================================
# MEDICINE IMAGE UPLOAD
# =========================================================

st.subheader("📷 Upload Medicine Image")

uploaded_file = st.file_uploader(
    "Upload a medicine package, label or prescription image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file:

    try:

        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Medicine Image",
            use_container_width=True
        )

        if st.button(
            "Extract Medicine Information",
            use_container_width=True
        ):

            with st.spinner("Extracting text from image..."):

                extracted_text = get_text(image)

            if extracted_text:

                st.success("Text extracted successfully!")

                with st.expander("View Extracted Text"):
                    st.text(extracted_text)

                with st.spinner("Gemini is analyzing the information..."):

                    result = ans(extracted_text, option)

                st.subheader("💊 Medical Information")
                st.markdown(result)

            else:

                st.warning(
                    "No readable text detected. "
                    "Please upload a clearer image."
                )

    except Exception as e:

        st.error(f"Unable to process image: {e}")


# =========================================================
# MANUAL MEDICINE OR DISEASE INPUT
# =========================================================

st.markdown("### OR")

st.subheader("💊 Enter Medicine or Disease Name")

user_input = st.text_input(
    "Medicine or disease name",
    placeholder="Example: Paracetamol 500 MG"
)


if st.button(
    "Get Medical Information",
    use_container_width=True
):

    if user_input.strip():

        with st.spinner("Gemini is generating medical information..."):

            result = ans(user_input.strip(), option)

        st.subheader("📋 Medical Information")
        st.markdown(result)

    else:

        st.warning(
            "Please enter a medicine or disease name."
        )


# =========================================================
# MEDICAL DISCLAIMER
# =========================================================

st.divider()

st.warning(
    """
    **Medical Disclaimer**

    This application provides educational information only.
    It does not provide medical diagnosis, prescriptions or
    personalized treatment recommendations.

    Always consult a qualified healthcare professional before
    making medical decisions.
    """
)

st.caption("Powered by Google Gemini AI | Medical Assistant")
