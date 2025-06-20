import pytesseract
from pdf2image import convert_from_path
import mlflow
import os

def run_ocr(pdf_path):
    images = convert_from_path(pdf_path )
    full_text = ""
    for page in images:
        text = pytesseract.image_to_string(page)
        full_text += text + "\n"
    return full_text

if __name__ == "__main__":
    mlflow.start_run()
    doc_path = "scanned_docs/example.pdf"
    extracted_text = run_ocr(doc_path)

    mlflow.log_param("file", doc_path)
    mlflow.log_metric("num_chars", len(extracted_text))
    
    with open("ocr_output.txt", "w") as f:
        f.write(extracted_text)
    
    mlflow.log_artifact("ocr_output.txt")
    mlflow.end_run()