import PyPDF2
import re

def extract_skills(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    skills = re.findall(r'\b(Python|Java|Docker|AWS|React)\b', text, re.IGNORECASE)
    return list(set(skills))
