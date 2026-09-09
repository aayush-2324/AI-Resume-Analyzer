from pathlib import Path

from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a text-based PDF resume."""
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"Resume not found: {pdf_path}")

    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")

    text = "\n".join(pages).strip()
    if not text:
        raise ValueError("No extractable text found in the PDF.")
    return text


if __name__ == "__main__":
    print("Resume parser module ready. Import extract_text_from_pdf() to use it.")
