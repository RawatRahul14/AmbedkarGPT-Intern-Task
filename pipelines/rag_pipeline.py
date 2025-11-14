# === Python Modules ===
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

# === Pipeline Body ===
class RagPipeline:
    def __init__(self, model, retriever):
        self.model = model
        self.retriever = retriever

    def rag(self):
        try:
            ## === Initiating the llm ===
            llm = Ollama(
                model = self.model
            )

            ## === initiating the chain ===
            qa = RetrievalQA.from_chain_type(
                llm = llm,
                retriever = self.retriever,
                chain_type = "stuff"
            )

            return qa
        
        except Exception as e:
            raise ValueError(f"Error creating the rag chain: {e}")