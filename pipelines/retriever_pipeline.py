# === Components ===
from components.data_extract import extract
from components.vectorstore import create_retriever

# === Pipeline Body ===
class RetrieverPipeline:
    def __init__(self):
        pass

    def retriever(self):
        try:
            ## === Creating chunks ===
            chunks = extract()

            ## === Creating retriever ===
            retriever = create_retriever(chunks = chunks)

            return retriever

        except Exception as e:
            raise ValueError(f"Error running the retriever pipeline: {e}")