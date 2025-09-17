import pandas as pd
import pdfplumber
from io import BytesIO

def parse_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = " ".join(page.extract_text() or "" for page in pdf.pages)
    return text

def parse_excel(file):
    df = pd.read_excel(file, engine='openpyxl')
    return df.to_string()

def parse_documents(files):
    docs_data = []
    for file in files:
        if file.name.lower().endswith('.pdf'):
            file_content = BytesIO(file.read())
            text = parse_pdf(file_content)
            docs_data.append({'filename': file.name, 'content': text})
        elif file.name.lower().endswith('.xlsx'):
            text = parse_excel(file)
            docs_data.append({'filename': file.name, 'content': text})
    return docs_data