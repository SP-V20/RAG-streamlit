

your-space/
│── app.py              # Streamlit UI (ENTRY POINT for Spaces)
│── rag.py              # RAG pipeline logic (FAISS + HF inference)
│── requirements.txt
│── data/
│     └── LLM Cheatsheet.pdf



## Installation

### Prerequisites

- Python 3.9+
- pip  
- Hugging Face API token (for inference)

### Setup

1. **Clone or download the project**
   ```bash
   cd RAG_LC
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv # It will create a venv folder
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   HuggingFaceToken=your_huggingface_api_token_here
   ```

5. **Running the Application**
    ```bash
    python app.py
    ```
6. **To check the streamlit app**
    ```bash
    streamlit run app.py
    ```