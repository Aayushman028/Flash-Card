import pdfplumber
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering
import re

# Load QA and QG models
QG_MODEL = "iarfmoose/t5-base-question-generator"
QA_MODEL = "deepset/roberta-base-squad2"

# Load generators
qg_tokenizer = AutoTokenizer.from_pretrained(QG_MODEL)
qg_model = AutoModelForSeq2SeqLM.from_pretrained(QG_MODEL)
qa_model = AutoModelForQuestionAnswering.from_pretrained(QA_MODEL)
qa_tokenizer = AutoTokenizer.from_pretrained(QA_MODEL)

device = 0 if torch.cuda.is_available() else -1
question_generator = pipeline("text2text-generation", model=qg_model, tokenizer=qg_tokenizer, device=device)
question_answerer = pipeline("question-answering", model=qa_model, tokenizer=qa_tokenizer, device=device)

# Extract text from uploaded file
def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return ""

# Chunking function
def split_text_into_chunks(text, max_words=250):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

# Generate flashcards using QG + QA
def generate_flashcards(content, subject="General"):
    chunks = split_text_into_chunks(content)
    flashcards = []

    for i, chunk in enumerate(chunks[:3]):  # Limit to 3 chunks for speed
        print(f"\n📄 Processing chunk {i+1}...")

        # Step 1: Generate Questions
        prompt = f"generate questions: {chunk}"
        try:
            result = question_generator(prompt, max_length=128, do_sample=False, num_beams=5, num_return_sequences=5)
            questions = [r["generated_text"] for r in result]
        except Exception as e:
            print(f"❌ QG error: {e}")
            continue

        # Step 2: Get Answers for each question
        for q in questions:
            try:
                answer = question_answerer(question=q, context=chunk)["answer"]
                if answer and answer.strip() != "":
                    flashcards.append({"question": q.strip(), "answer": answer.strip()})
            except Exception as e:
                print(f"⚠️ QA error: {e}")

    return flashcards[:15]
