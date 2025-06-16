# 🧠 LLM Flashcard Generator

A lightweight Flashcard Generation Tool using Hugging Face LLMs and Streamlit. This tool converts educational content (PDFs, text input) into clear, concise Q/A flashcards using modern NLP models. Ideal for students, educators, and AI enthusiasts.

---

## 🚀 Features

- 📄 Accepts `.txt`, `.pdf`, or pasted text input
- 🧠 Automatically generates 10–15 flashcards per submission
- 🗂️ Optional subject selection (e.g., Biology, History, CS)
- 🧼 Clean, minimal Streamlit UI
- ⚙️ GPU support for faster generation (if available)
- 🔀 Handles long content with chunked processing

---

## 📁 Project Structure

Your project folder (`AI Task`) should look like this:

```
AI Task/
├── app.py         # Frontend Streamlit interface
├── backend.py     # LLM prompt logic and flashcard generator
├── utils.py       # File and text parsing (PDF/TXT)
├── README.md      # This file
```

---

## 🛠️ Installation & Setup

### 1. Create and navigate into your project folder

```bash
mkdir "AI Task"
cd "AI Task"
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
# Activate:
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install all required dependencies

```bash
pip install streamlit transformers torch pdfplumber
```

---

## ▶️ How to Run the App

From the root of your project:

```bash
streamlit run app.py
```

Streamlit will launch in your browser, typically at [http://localhost:8501](http://localhost:8501)

---

## ✍️ Sample Input

You can paste this into the textbox or save it in a `.txt` file:

```text
Photosynthesis is the process by which green plants and some bacteria use sunlight to synthesize nutrients from carbon dioxide and water. It takes place mainly in the chloroplasts of plant cells. Chlorophyll plays a crucial role in absorbing light energy.
```

---

## ✅ Sample Output

```
Q: What is photosynthesis?
A: It is the process by which green plants and some bacteria use sunlight to make food.

Q: Where does photosynthesis mainly occur?
A: In the chloroplasts of plant cells.

Q: What is the role of chlorophyll in photosynthesis?
A: Chlorophyll absorbs light energy for the process.
```

---

## 🤖 LLMs Used

This project uses Hugging Face models:

| Purpose               | Model Name                             |
|-----------------------|-----------------------------------------|
| Question Generation   | `iarfmoose/t5-base-question-generator` |
| Answer Extraction     | `deepset/roberta-base-squad2`          |

These can be changed in `backend.py` if needed.

---

## ⚠️ Troubleshooting

- If you see: `⚠️ No flashcards generated`  
  ➤ Try shorter, simpler content  
  ➤ Use factual, topic-specific text (textbooks, summaries)

- If you see: `Token indices sequence length...`  
  ➤ Input is too long; the tool already chunks text but you can reduce input length

- If output only appears in terminal  
  ➤ Ensure `generate_flashcards` returns parsed output, not just prints

---

## 🔮 Optional Add-ons

You can extend this project by adding:

- Export flashcards to `.csv`, `.json`, or Anki
- Tagging flashcards by difficulty (Easy/Medium/Hard)
- Support for more subjects or languages
- Editable flashcards before download
- Flashcard grouping by subheading

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙏 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/)
- [Streamlit](https://streamlit.io/)
- [PyTorch](https://pytorch.org/)
