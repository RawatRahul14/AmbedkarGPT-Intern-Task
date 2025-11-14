# === Ignore Warnings ===
import warnings
warnings.filterwarnings(
    "ignore",
    category = DeprecationWarning
)

# === Pipelines ===
from pipelines.retriever_pipeline import RetrieverPipeline
from pipelines.rag_pipeline import RagPipeline

# === Main Function ===
def main_fn():
    ## === Retriever ===
    try:
        print(">>>>>>>> Creating Retriever <<<<<<<<")
        retriever = RetrieverPipeline().retriever()
        print(">>>>>>>> Retriever created successfully. <<<<<<<<")
    except Exception as e:
        raise ValueError(f"Error initialising the retriever pipeline: {e}")

    ## === Running LLM model ===
    try:
        print(">>>>>>>> Creating LLM chain <<<<<<<<")
        llm_chain = RagPipeline(
            model = "ambedkargpt",
            retriever = retriever
        ).rag()
        print(">>>>>>>> LLM chain created successfully. <<<<<<<<")

        return llm_chain
    
    except Exception as e:
        raise ValueError(f"Error initialising the rag pipeline: {e}")

if __name__ == "__main__":
    chain = main_fn()

    print(">>>>>>>> AmbedkarGPT RAG System <<<<<<<<")
    print("Ask anything based on the speech.txt file.")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Your question: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting... Goodbye!")
            break

        try:
            answer = chain(query)
            print("\nAnswer:", answer.get("result", "No output generated."), "\n")
        except Exception as e:
            print(f"Error generating answer: {e}")