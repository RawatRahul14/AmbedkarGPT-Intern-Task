# === Python Modules ===
import os
from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# === Function to create retriever ===
def create_retriever(
        chunks,
        persist_directory: Path = Path("data/chroma_store")
):
    """
    Creates embeddings for document chunks and initializes ChromaDB retriever.

    Args:
        chunks (List[Document]): The document chunks generated from text.
        persist_directory (Path): Directory to store Chroma vector DB.

    Returns:
        retriever: A LangChain retriever object.
    """
    try:
        ## === Ensure directory exists ===
        os.makedirs(
            persist_directory,
            exist_ok = True
        )

        ## === Create Embeddings Model ===
        embedding_model = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/all-MiniLM-L6-v2"
        )

        ## === Create ChromaDB Vector Store ===
        vectorstore = Chroma.from_documents(
            documents = chunks,
            embedding = embedding_model,
            persist_directory = str(persist_directory)
        )

        ## === Persist the DB to disk ===
        vectorstore.persist()

        ## === Create Retriever ===
        retriever = vectorstore.as_retriever(
            search_type = "similarity",
            search_kwargs = {
                "k": 2
            }
        )

        return retriever

    except Exception as e:
        raise ValueError(f"Error creating retriever: {e}")