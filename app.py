
import os
import time

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
    st.error("Gemini API key is missing. Configure GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()


@st.cache_resource
def initialize_gemini(key):

    return genai.Client(api_key=key)


try:
    gemini_client = initialize_gemini(api_key)

except Exception as e:
    st.error(f"Gemini initialization failed: {e}")
    st.stop()


# =========================================================
# APPLICATION HEADER
# =========================================================

st.markdown(
    """
    <div style="text-align:center;">
        <img
            src="https://www.freepnglogos.com/uploads/medicine-logo-png-1.png"
            width="90"
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
# GEMINI RESPONSE FUNCTION - OPTIMIZED
# =========================================================

def ans(user_text, language):

    # Keep input size manageable
    user_text = user_text.strip()[:4000]

    if not user_text:
        return "Please enter a medicine or disease name.", 0

    system_prompt = f"""
You are a concise, evidence-aware medical information assistant.

Respond in {language}.

For a medicine or disease, provide these sections where relevant:

1. Overview
2. Medical uses
3. How it works
4. Common side effects
5. Precautions
6. Important interactions
7. When to seek medical attention

Safety rules:
- Provide general educational information only.
- Never diagnose or prescribe medicines or dosages.
- Never invent medical facts or interactions.
- State uncertainty when appropriate.
- Do not recommend stopping prescribed medication.
- Recommend consulting a qualified healthcare professional.
- For emergencies, recommend immediate medical care.
- If the medicine name is unclear, ask the user to verify it.
- Treat OCR text as unverified input.
- Keep the answer clear, concise and well structured.
"""

    try:

        start_time = time.perf_counter()

        response = gemini_client.models.generate_content(
            model="gemini-flash-latest",

            contents=(
                "Provide educational medical information about:\n"
                + user_text
            ),

            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.2,
                max_output_tokens=700
            )
        )

        elapsed_time = time.perf_counter() - start_time

        if response.text:
            return response.text, elapsed_time

        return "Gemini returned an empty response. Please try again.", elapsed_time

    except Exception as e:

        return f"Gemini API request failed: {str(e)}", 0


# =========================================================
# DISPLAY AI RESPONSE
# =========================================================

def display_response(user_text, language):

    with st.spinner("⚡ Gemini is generating your response..."):

        result, elapsed_time = ans(user_text, language)

    if elapsed_time > 0:

        st.success(
            f"Response generated in {elapsed_time:.2f} seconds"
        )

    if result.startswith("Gemini API request failed:"):

        st.error(result)

    else:

        st.subheader("📋 Medical Information")
        st.markdown(result)


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

language = st.selectbox(
    "Choose your preferred language",
    ["English", "Hindi", "Nepali"]
)

st.divider()


# =========================================================
# IMAGE UPLOAD
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

            with st.spinner("Extracting text using OCR..."):

                extracted_text = get_text(image)

            if extracted_text:

                st.success("Text extracted successfully!")

                with st.expander("View Extracted Text"):

                    st.text(extracted_text)

                display_response(
                    extracted_text,
                    language
                )

            else:

                st.warning(
                    "No readable text detected. "
                    "Please upload a clearer medicine image."
                )

    except Exception as e:

        st.error(f"Unable to process image: {e}")


# =========================================================
# MANUAL MEDICINE SEARCH
# =========================================================

st.markdown("### OR")

st.subheader("💊 Enter Medicine or Disease Name")

with st.form("medicine_search_form"):

    user_input = st.text_input(
        "Medicine or disease name",
        placeholder="Example: Paracetamol"
    )

    submitted = st.form_submit_button(
        "Get Medical Information",
        use_container_width=True
    )


if submitted:

    if user_input.strip():

        display_response(
            user_input,
            language
        )

    else:

        st.warning("Please enter a medicine or disease name.")


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

st.caption(
    "Powered by Google Gemini AI | Medical Assistant"
)
