import os
from dotenv import load_dotenv
from extractors.pdf_extractor import extract_pdf_text
from processors.text_processor import summarize_text

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("❌ GEMINI_API_KEY not found! Please set it in your .env file.")

if __name__ == "__main__":
    text = extract_pdf_text("data/pdf/sample.pdf")
    summary = summarize_text(text)
    print("✅ Summary Generated:")
    print(summary)
