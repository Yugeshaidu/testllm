
import PyPDF2
import os
from typing import List, Dict, Optional

class PDFProcessor:
    def __init__(self, input_directory: str):
        self.input_directory = input_directory
        
    def read_pdf(self, file_path: str) -> str:
        text = ""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            return ""
    
    def batch_process_pdfs(self) -> Dict[str, str]:
        results = {}
        for filename in os.listdir(self.input_directory):
            if filename.lower().endswith('.pdf'):
                file_path = os.path.join(self.input_directory, filename)
                extracted_text = self.read_pdf(file_path)
                if extracted_text:
                    results[filename] = extracted_text
        return results

# Now you can use it like this:
path = r"C:\Users\naidu\Desktop\Data\rawdata\pdfs"
processor = PDFProcessor(path)

# Process all PDFs in the directory
pdf_texts = processor.batch_process_pdfs()

# Print results
for filename, text in pdf_texts.items():
    print(f"Processed {filename}: {len(text)} characters extracted")