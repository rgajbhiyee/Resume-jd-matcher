from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    text = ""

    try:
        reader = PdfReader(pdf_file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    except Exception as e:
        print("Error: ", e)
    
    return text.strip()

def extract_text_from_txt(file):

    try:
        return file.read().decode("utf-8")
    except Exception as e:
        print("Error: ", e)
        return ""   