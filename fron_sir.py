from dotenv import load_dotenv
import os
from pinecone import Pinecone
from google import genai
import fitz  # PyMuPDF

load_dotenv()


pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

vector_index = pinecone_client.Index("student-kb")

google_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def embed_text(text):
    result = google_client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config={
            'output_dimensionality': 768
        })
    vector = result.embeddings[0].values
    return vector


def upsert_vectors_to_pinecone(document_texts):
    upsert_data = []
    for doc_id, text in enumerate(document_texts):
        vector = embed_text(text)
        record_id = f"doc_{doc_id}"
        metadata = {
            "text": text
        }
        upsert_data.append((record_id, vector, metadata))
    vector_index.upsert(upsert_data)


if __name__ == "__main__":
    pdf_dir = "documents"

    document_dirs = os.listdir(pdf_dir)

    document_texts = []
    for file_path in document_dirs:
        full_path = os.path.join(pdf_dir, file_path)  # documents/aboutme.pdf
        text = extract_text_from_pdf(full_path)
        document_texts.append(text)

    upsert_vectors_to_pinecone(document_texts)
    print("Yayyy! Vectors upserted to Pinecone successfully.")
