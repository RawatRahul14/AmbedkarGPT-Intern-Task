# === Python Packages ===
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# === Function to load and create chunks of data ===
def extract(
        file_path: Path = Path("data/speech.txt")
):
    """
    Loads the speech.txt file and splits it into manageable chunks.

    Args:
        file_path (str): Path to the text file.

    Returns:
        List[Document]: List of chunked documents.
    """
    try:
        ## === Initiating the loader ===
        loader = TextLoader(file_path = file_path)

        ## === Loading data ===
        documents = loader.load()

        ## === Initiating the splitter ===
        splitter = CharacterTextSplitter(
            separator = "\n",
            chunk_size = 300,
            chunk_overlap = 50
        )

        ## === Splitting the data ===
        chunks = splitter.split_documents(documents = documents)

        return chunks

    except Exception as e:
        raise ValueError(f"Error Creating data chunks: {e}")