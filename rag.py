import os
from urllib import response
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

client = InferenceClient(
    model="openai/gpt-oss-120b",
    token=os.getenv("HuggingFaceToken")
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = PyPDFLoader("data/LLM Cheatsheet.pdf").load()

# ---- Split text ----
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
documents = splitter.split_documents(docs)

vectorstore = FAISS.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3}) 


def get_answer(query: str) -> str:
        """RAG pipeline: retrieve + generate answer"""

        retrieved_docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        response = client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user", 
                    "content": f"Context:\n{context}\n\nQuestion:\n{query}"}
            ],
            temperature=0.7,
        )
        answer = response.choices[0].message.content
        print("\nAnswer:\n", answer)
        return answer


if __name__ == "__main__":
    get_answer("What is the capital of India?")