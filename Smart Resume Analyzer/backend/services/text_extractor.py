import os
import re

def clean_extracted_text(raw_text: str) -> str:
    """Clean and normalize raw extracted text from resumes."""
    if not raw_text:
        return ""
    # Remove control characters except standard whitespace
    cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', ' ', raw_text)
    # Replace multiple spaces/newlines with single space
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def extract_text_from_pdf(filepath: str) -> str:
    """Extract readable text from a PDF file using PyMuPDF, pdfplumber, or pypdf."""
    text = ""
    
    # 1. Try PyMuPDF (fitz)
    try:
        try:
            import pymupdf as fitz
        except ImportError:
            import fitz
        doc = fitz.open(filepath)
        for page in doc:
            page_text = page.get_text("text")
            if page_text:
                text += page_text + "\n"
        doc.close()
    except Exception as e:
        print(f"[WARN] PyMuPDF extraction notice: {e}")

    # 2. If text is empty, try pypdf
    if not text.strip():
        try:
            from pypdf import PdfReader
            reader = PdfReader(filepath)
            for page in reader.pages:
                p_text = page.extract_text()
                if p_text:
                    text += p_text + "\n"
        except Exception as e:
            print(f"[WARN] pypdf extraction notice: {e}")

    # 3. If still empty, try pdfplumber
    if not text.strip():
        try:
            import pdfplumber
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    p_text = page.extract_text()
                    if p_text:
                        text += p_text + "\n"
        except Exception as e:
            print(f"[WARN] pdfplumber extraction notice: {e}")

    # 4. Fallback: Raw byte decode
    if not text.strip():
        try:
            with open(filepath, "rb") as f:
                raw_bytes = f.read()
                text = raw_bytes.decode("utf-8", errors="ignore")
                # Filter printable ascii
                text = "".join([c for c in text if c.isprintable() or c in "\n\r\t"])
        except Exception:
            pass

    return clean_extracted_text(text)

def extract_text_from_docx(filepath: str) -> str:
    """Extract text from DOCX file using python-docx."""
    full_text = []
    try:
        import docx
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text.strip())
        
        # Also extract table text if present
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if cell.text.strip():
                        full_text.append(cell.text.strip())
                        
        return clean_extracted_text(" ".join(full_text))
    except Exception as e:
        print(f"[WARN] DOCX text extraction notice: {e}")
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                return clean_extracted_text(f.read())
        except Exception:
            return ""

def extract_resume_text(filepath: str) -> str:
    """Extract text based on file extension with resilient fallbacks."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif ext == ".docx":
        return extract_text_from_docx(filepath)
    else:
        # Generic text read
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                return clean_extracted_text(f.read())
        except Exception:
            return ""
