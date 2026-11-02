# 💊 Medical Assistant – AI-Powered Medicine Information Assistant

An AI-powered medical information assistant built with **Python, Streamlit, Google Gemini API, and Tesseract OCR**. The application helps users understand medicines and diseases by extracting text from medicine images and generating structured, educational medical information in English, Hindi, and Nepali.

---

## 📌 Table of Contents

1. [Project Overview](#-project-overview)
2. [Key Features](#-key-features)
3. [How It Works](#-how-it-works)
4. [Application Architecture](#-application-architecture)
5. [Technology Stack](#-technology-stack)
6. [Project Structure](#-project-structure)
7. [Prerequisites](#-prerequisites)
8. [Installation and Setup](#-installation-and-setup)
9. [Environment Configuration](#-environment-configuration)
10. [Running the Application](#-running-the-application)
11. [Using the Application](#-using-the-application)
12. [Google Gemini API Integration](#-google-gemini-api-integration)
13. [Optical Character Recognition](#-optical-character-recognition)
14. [Deployment on Streamlit Community Cloud](#-deployment-on-streamlit-community-cloud)
15. [Troubleshooting](#-troubleshooting)
16. [Security Best Practices](#-security-best-practices)
17. [Limitations](#-limitations)
18. [Future Enhancements](#-future-enhancements)
19. [Contributing](#-contributing)
20. [License](#-license)

---

## 🚀 Project Overview

Medical Assistant is a web-based application designed to make general medicine and disease information more accessible through artificial intelligence.

Users can either:

- Upload an image of a medicine package, label, or prescription.
- Manually enter a medicine name or disease.

When an image is uploaded, the application uses **Tesseract OCR** to extract readable text. The extracted text is then passed to **Google Gemini**, which generates structured educational information in the user's selected language.

The application is designed with a simple and intuitive interface using Streamlit, making it accessible without requiring advanced technical knowledge.

### 🎯 Project Objectives

- Simplify access to general medicine information.
- Use OCR to extract text from medicine images.
- Integrate generative AI for natural-language medical information.
- Support multiple languages.
- Provide an accessible, user-friendly interface.
- Encourage responsible and informed healthcare decisions.

---

## ✨ Key Features

### 1. AI-Powered Medical Information

Uses Google's Gemini API to generate structured educational information about medicines and diseases.

Information may include:

- Introduction and overview.
- Medical uses and purpose.
- General mechanism of action.
- Common side effects.
- Important precautions.
- Potential drug interactions.
- When to seek medical attention.

### 2. Medicine Image Recognition

Upload medicine-related images in supported formats:

- JPG
- JPEG
- PNG

The application uses Tesseract OCR to extract text from uploaded images.

### 3. Manual Medicine Search

Users can directly enter a medicine name or disease to receive AI-generated educational information.

Example:

`Paracetamol 500 MG`

### 4. Multilingual Support

The application supports three response languages:

| Language | Support |
|---|---|
| English | Yes |
| Hindi | Yes |
| Nepali | Yes |

### 5. Google Gemini Integration

Uses Google's Gemini API to generate natural-language responses based on the user's input.

### 6. Medical Safety Instructions

The AI is instructed not to:

- Diagnose medical conditions.
- Prescribe medicines or dosages.
- Invent medical facts.
- Recommend stopping prescribed medication.
- Replace professional medical advice.

---

## 🔄 How It Works

The application follows a straightforward processing pipeline.

**Image-based workflow:**

1. User uploads a medicine image.
2. Streamlit receives the uploaded image.
3. Pillow converts the image into RGB format.
4. Tesseract OCR extracts readable text.
5. Extracted text is passed to the Gemini API.
6. Gemini generates structured medical information.
7. The response is displayed in the Streamlit interface.

**Manual-input workflow:**

1. User enters a medicine name or disease.
2. User selects a preferred language.
3. Input is passed to the Gemini API.
4. Gemini processes the request using the configured instructions.
5. Generated information is displayed to the user.

---

## 🏗️ Application Architecture

```text
                 USER
                   |
                   v
          STREAMLIT WEB INTERFACE
                   |
          +--------+--------+
          |                 |
          v                 v
     IMAGE UPLOAD       MANUAL INPUT
          |                 |
          v                 |
      PILLOW IMAGE           |
      PROCESSING             |
          |                 |
          v                 |
       TESSERACT OCR         |
          |                 |
          v                 |
     EXTRACTED TEXT          |
          |                 |
          +--------+--------+
                   |
                   v
            GEMINI API
                   |
                   v
          AI RESPONSE GENERATION
                   |
                   v
          STRUCTURED MEDICAL
              INFORMATION
                   |
                   v
          STREAMLIT RESULTS UI
```

### Architecture Components

| Component | Responsibility |
|---|---|
| Streamlit | Web application and user interface |
| Pillow | Image loading and processing |
| Tesseract OCR | Text extraction from images |
| Google Gemini API | AI-powered information generation |
| Google Gen AI SDK | Python integration with Gemini |
| Python | Application logic and processing |

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Frontend and web application framework |
| Google Gemini API | Generative AI integration |
| Google Gen AI SDK | Gemini API communication |
| Tesseract OCR | Optical character recognition |
| Pytesseract | Python wrapper for Tesseract |
| Pillow | Image processing |
| TOML | API secret configuration |
| Git & GitHub | Version control and source code management |
| Streamlit Community Cloud | Application deployment |

---

## 📂 Project Structure

```text
Medical-Assistant/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── example.txt
├── requirements.txt
├── packages.txt
├── README.md
├── .gitignore
│
└── Other project resources
```

### Important Files

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `example.txt` | Optional reference template used in AI instructions |
| `requirements.txt` | Python dependencies |
| `packages.txt` | System packages required for deployment |
| `.streamlit/secrets.toml` | Local API key configuration |
| `.gitignore` | Prevents sensitive and unnecessary files from being committed |
| `README.md` | Project documentation |

---

## 📋 Prerequisites

Before installing the project, ensure you have:

- Python 3.10 or later.
- pip package manager.
- Git.
- Google Gemini API key.
- Tesseract OCR installed on your system.

### Required Accounts

**Google AI Studio**

Generate your Gemini API key:

https://aistudio.google.com/apikey

**GitHub**

https://github.com/

**Streamlit Community Cloud**

https://share.streamlit.io/

---

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/gprabhat65/Medical-Assistant.git
```

Navigate to the project directory:

```bash
cd Medical-Assistant
```

### Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv med
```

Activate it on Windows PowerShell:

```powershell
.\med\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source med/bin/activate
```

### Step 3: Install Python Dependencies

Install all required dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Install Tesseract OCR

Tesseract is required for extracting text from uploaded medicine images.

**Windows:**

Download and install Tesseract OCR:

https://github.com/UB-Mannheim/tesseract/wiki

Verify the installation:

```powershell
tesseract --version
```

If Windows cannot locate Tesseract, configure its executable path:

```powershell
$env:TESSERACT_CMD = "C:\Program Files\Tesseract-OCR\tesseract.exe"
```

**Ubuntu / Debian:**

```bash
sudo apt update
sudo apt install tesseract-ocr
```

Verify:

```bash
tesseract --version
```

**macOS:**

```bash
brew install tesseract
```

---

## 🔐 Environment Configuration

The application requires a Google Gemini API key.

### Step 1: Create a Gemini API Key

Visit:

https://aistudio.google.com/apikey

Create a new API key and copy it securely.

### Step 2: Configure Streamlit Secrets

Create the following directory and file:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace `YOUR_GEMINI_API_KEY` with your actual API key.

**Important:** Never upload this file to GitHub.

### Step 3: Configure `.gitignore`

Ensure your `.gitignore` contains:

```gitignore
# API secrets
.streamlit/secrets.toml
.env

# Virtual environments
med/
venv/
.venv/

# Python cache
__pycache__/
*.pyc

# IDE files
.idea/

# Jupyter files
.ipynb_checkpoints/

# Operating system files
.DS_Store
Thumbs.db
```

### Step 4: Configure Dependencies

Your `requirements.txt` should contain:

```text
streamlit
pytesseract
Pillow
google-genai
```

Your `packages.txt` should contain:

```text
tesseract-ocr
```

---

## ▶️ Running the Application

After completing the installation and configuration, start the application:

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

To stop the application:

```text
CTRL + C
```

---

## 🖥️ Using the Application

### Method 1: Upload a Medicine Image

1. Open the Medical Assistant application.
2. Select your preferred language.
3. Navigate to the image upload section.
4. Upload a JPG, JPEG, or PNG image.
5. Click **Extract Medicine Information**.
6. Review the extracted text.
7. View the AI-generated medical information.

### Method 2: Manual Medicine Search

1. Open the application.
2. Select English, Hindi, or Nepali.
3. Enter a medicine name or disease.
4. Click **Get Medical Information**.
5. Review the generated response.

### Example Input

```text
Paracetamol 500 MG
```

### Example Response Structure

```text
1. Introduction

2. Medical Uses and Purpose

3. General Mechanism of Action

4. Common Side Effects

5. Important Precautions

6. Potential Drug Interactions

7. When to Seek Medical Attention
```

*Actual responses depend on the input and Gemini API output.*

---

## 🤖 Google Gemini API Integration

The application uses the official Google Gen AI Python SDK.

### Import the SDK

```python
from google import genai
from google.genai import types
```

### Initialize the Gemini Client

```python
gemini_client = genai.Client(
    api_key=api_key
)
```

### Generate AI Responses

```python
response = gemini_client.models.generate_content(
    model="gemini-flash-latest",
    contents="Explain Paracetamol.",
    config=types.GenerateContentConfig(
        temperature=0.3,
        max_output_tokens=1500
    )
)
```

### Display the Generated Response

```python
print(response.text)
```

The application also provides system instructions to guide the model toward structured, educational, and medically cautious responses.

**Note:** Model availability and API usage limits depend on Google's current Gemini API configuration and account access.

Official documentation:

https://ai.google.dev/gemini-api/docs

---

## 📷 Optical Character Recognition (OCR)

The application uses Tesseract OCR to recognize text from uploaded images.

### OCR Implementation

```python
import pytesseract
from PIL import Image

def get_text(image_data):

    extracted_text = pytesseract.image_to_string(
        image_data
    )

    return extracted_text.strip()
```

### OCR Processing Flow

```text
Uploaded Image
      |
      v
Pillow Image Processing
      |
      v
Tesseract OCR
      |
      v
Extracted Text
      |
      v
Gemini API
```

OCR accuracy depends on image quality, text visibility, lighting, resolution, and supported languages.

Always verify extracted medicine names and details before relying on them.

---

## ☁️ Deployment on Streamlit Community Cloud

The application can be deployed publicly using Streamlit Community Cloud.

### Step 1: Push Your Project to GitHub

Initialize Git if necessary:

```bash
git init
```

Add your project files:

```bash
git add .
```

Commit:

```bash
git commit -m "Deploy Gemini-powered Medical Assistant"
```

Connect your GitHub repository if it is not already connected:

```bash
git remote add origin https://github.com/gprabhat65/Medical-Assistant.git
```

Push:

```bash
git branch -M main
git push -u origin main
```

### Step 2: Open Streamlit Community Cloud

Visit:

https://share.streamlit.io/

Sign in using your GitHub account.

### Step 3: Create a New App

1. Click **Create app**.
2. Select your GitHub repository.
3. Select the `main` branch.
4. Set the main file path to:

```text
app.py
```

5. Click Deploy.

### Step 4: Configure Gemini API Secrets

Open your deployed application's settings.

Navigate to:

**Settings → Secrets**

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Save the configuration.

### Step 5: Verify Deployment

Once deployment completes:

- Open the public application URL.
- Verify that the interface loads.
- Test manual medicine search.
- Test medicine image upload.
- Verify OCR extraction.
- Check Gemini API responses.
- Test the available languages.

Your application should now be accessible through its Streamlit public URL.

---

## 🐛 Troubleshooting

### 1. Gemini API Key Missing

**Error:**

```text
Gemini API key is missing.
```

**Solution:**

Verify that `.streamlit/secrets.toml` contains:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

For Streamlit Cloud, configure the key in App Settings → Secrets.

### 2. Gemini API Request Failed

Possible causes:

- Invalid API key.
- API quota exceeded.
- Billing or account restrictions.
- Unsupported model.
- Network connectivity problems.

**Solution:**

Verify your API key and check your Google AI Studio API usage and model availability.

### 3. Tesseract Not Found

**Error:**

```text
TesseractNotFoundError
```

**Solution:**

Install Tesseract OCR and verify that its executable is available.

On Windows:

```powershell
$env:TESSERACT_CMD = "C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 4. No Text Extracted from Image

Possible causes:

- Blurry image.
- Poor lighting.
- Small text.
- Low image resolution.
- Unsupported or difficult-to-read text.

**Solution:**

Upload a clearer image with readable medicine labels.

### 5. Module Not Found

**Error:**

```text
ModuleNotFoundError
```

**Solution:**

Activate your virtual environment and reinstall dependencies:

```bash
pip install -r requirements.txt
```

### 6. Streamlit Application Not Starting

Try:

```bash
python -m streamlit run app.py
```

Check the terminal output for missing dependencies or configuration errors.

---

## 🔒 Security Best Practices

Security is important because the application uses an external AI API.

- Never hardcode API keys in Python files.
- Never commit `.streamlit/secrets.toml` to GitHub.
- Use Streamlit Secrets for deployment.
- Regenerate exposed API keys immediately.
- Do not upload private medical documents unless you understand the privacy implications.
- Avoid storing personal medical information unnecessarily.
- Review API usage and quotas regularly.
- Keep project dependencies updated.

**Privacy note:** User inputs and uploaded images are processed by the application and may be sent to Google Gemini when generating responses. Review Google's applicable API data-use and privacy terms before using the application with sensitive information.

---

## ⚠️ Limitations

- OCR accuracy depends on image quality.
- AI-generated responses may contain inaccuracies.
- Extracted text may be incomplete or incorrect.
- The application does not verify medicine authenticity.
- The application does not access an individual's medical records.
- The application does not provide personalized diagnoses.
- The application does not prescribe medicines or dosages.
- AI-generated information must not replace professional medical advice.
- API availability, quotas, and costs depend on the Google Gemini account and selected model.

**Medical Disclaimer:** This project is intended for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional before making medical decisions.

---

## 🚀 Future Enhancements

Potential improvements for future versions include:

- [ ] Medicine identification using advanced computer vision.
- [ ] Improved OCR preprocessing and image enhancement.
- [ ] Support for additional regional languages.
- [ ] Medicine information retrieval using trusted medical databases.
- [ ] Retrieval-Augmented Generation (RAG) integration.
- [ ] Medicine interaction information backed by verified sources.
- [ ] Downloadable medical information reports in PDF format.
- [ ] User authentication and personalized preferences.
- [ ] Medicine history and search history.
- [ ] Voice-based medicine search.
- [ ] Improved mobile-responsive interface.
- [ ] Automated testing and application monitoring.

---

## 🤝 Contributing

Contributions, feature suggestions, and bug reports are welcome.

### Contribution Steps

1. Fork this repository.
2. Create a new feature branch.
3. Implement your changes.
4. Test the application locally.
5. Commit your changes.
6. Submit a Pull Request.

Example:

```bash
git checkout -b feature/new-feature
```

Commit:

```bash
git add .
git commit -m "Add new feature"
```

Push:

```bash
git push origin feature/new-feature
```

---

## 📜 License

This project is available for educational and research purposes.

Before redistributing or using the project commercially, check the repository's license and the terms of the third-party services and dependencies.

---

## 👨‍💻 Author

**Prabhat Kumar Gupta**

AI & Data Science | Generative AI | Machine Learning | Full Stack Development

GitHub: https://github.com/gprabhat65

Project Repository: https://github.com/gprabhat65/Medical-Assistant

---

## ⭐ Support the Project

If you find this project useful:

- Give the repository a ⭐ Star.
- Fork the repository.
- Share your feedback.
- Contribute improvements.

**Built with Python, Streamlit, Tesseract OCR, and Google Gemini AI.**

*Making medicine information more accessible through artificial intelligence.* 💊
