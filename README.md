---
title: RAG LLM App
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: streamlit
app_file: app.py
pinned: false
---

📁 Project Structure
your-space/
│── app.py              # UI (ENTRY POINT for Spaces)
│── rag.py              # RAG pipeline logic (FAISS + HF inference)
│── requirements.txt
│── data/
│     └── LLM Cheatsheet.pdf

🚀 Setup
1. Clone or move into project
cd RAG_LC
2. Create virtual environment (recommended)

Mac/Linux

python -m venv venv
source venv/bin/activate

Windows

python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Set environment variables

Create a .env file in the project root:

HuggingFaceToken=your_huggingface_api_token_here
5. Run locally
python app.py
6. Streamlit (if used locally)
streamlit run app.py
☁️ Deploy on Hugging Face Spaces

Make sure:

app_file: app.py
requirements.txt exists
Your Hugging Face token is added under Space → Settings → Secrets
