import PyPDF2
from docx import Document


import PyPDF2


def extract_resume_text(uploaded_file):

    text = ""

    try:
        reader = PyPDF2.PdfReader(uploaded_file)

        for page in reader.pages:
            text += page.extract_text()

        return text

    except Exception as e:
        return f"Error reading PDF: {e}"