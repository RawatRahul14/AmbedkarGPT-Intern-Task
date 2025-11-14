# AmbedkarGPT-Intern-Task

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()
[![LangChain](https://img.shields.io/badge/LangChain-RAG%20Pipeline-green)]()
[![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-orange)]()
[![Ollama](https://img.shields.io/badge/LLM-Ollama%20Mistral%207B-yellow)]()

This project is a simple Retrieval-Augmented Generation (RAG) system built as part of the **KalpIT AI Intern Assignment**.  
The system loads a speech excerpt from Dr. B.R. Ambedkar, splits it into text chunks, embeds the chunks using a SentenceTransformer model, and stores them in a local ChromaDB vector store.  

A local **Ollama Mistral 7B** model is then used to answer user questions based solely on the speech content.  
The interaction takes place entirely through a **command-line interface (CLI)**, with no external APIs or internet access required.

The goal of this assignment is to demonstrate understanding of:
- Text loading & preprocessing  
- Embedding generation  
- Vector retrieval  
- LangChain’s RAG workflow  
- Local LLM integration using Ollama  

## Table of Contents
1. [Model Setup (Ollama + Mistral 7B)](#model-setup-ollama--mistral-7b)
2. [Installation](#installation)
3. [Custom Model Setup](#custom-model-setup)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. 

## Model Setup (Ollama + Mistral 7B)
This project uses a fully local LLM through **Ollama**.  
Before running the code, ensure Ollama and the Mistral model are installed.

### 1. Install Ollama
Download and install Ollama for your platform:
https://ollama.com/download

### 2. Pull the Mistral 7B Model
After installation, open a terminal and run:
```bash
ollama run mistral
```

This command **automatically downloads the model** (approx. 4GB) and then immediately **starts it in interactive mode**.

### 3. Exit the Model
Once the model has started successfully, exit the interactive session by typing:
```bash
/bye
```

After this step, the Mistral model is fully installed and ready to be used by the RAG system.

## Installation
Follow the steps below to set up the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/RawatRahul14/AmbedkarGPT-Intern-Task.git

cd AmbedkarGPT-Intern-Task
```

### 2. Create and Activate a Virtual Environment
It is recommended to isolate dependencies using `venv`.

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python Dependencies
Make sure your virtual environment is active, then run:
```bash
pip install -r requirements.txt
```

## Custom Model Setup
This project also supports creating a custom Ollama model called `ambedkargpt`, built on top of Mistral 7B, fine-tuned via a Modelfile for deterministic, context-bound answers.

### Build the Model Locally
Run the following command in your project directory:

```bash
ollama create ambedkargpt -f Modelfile
```

## Usage
Once your environment and model are ready, you can run the CLI version of AmbedkarGPT:

```bash
python main.py
```

You will see an interactive prompt:
```text
=== AmbedkarGPT RAG System ===
Ask anything based on the speech.txt file.
Type 'exit' to quit.
```

### Example Questions:
- What is the real remedy according to Ambedkar?
- What is described as the real enemy in the speech?
- Why does Ambedkar say the caste problem is not a social reform issue?
- What comparison does Ambedkar make to social reform?

## How It Works

1. Data Extraction:
The file speech.txt is loaded and split into smaller chunks using LangChain’s CharacterTextSplitter.
2. Embeddings Creation:
Each chunk is converted into numerical embeddings using the model sentence-transformers/all-MiniLM-L6-v2.
3. Vector Store (ChromaDB):
The embeddings are stored locally in ChromaDB for efficient retrieval.
4. Retriever:
When a user asks a question, relevant chunks are retrieved from ChromaDB.
5. LLM Query (Ollama Mistral):
The retriever output is passed to the Mistral model (via Ollama) to generate a context-aware answer.
6. Output:
The final response is printed in the terminal.

## Project Structure
```bash
Directory structure:
└── rawatrahul14-ambedkargpt-intern-task/
    ├── README.md
    ├── LICENSE
    ├── main.py
    ├── Modelfile
    ├── requirements.txt
    ├── trials.ipynb
    ├── components/
    │   ├── __init__.py
    │   ├── data_extract.py
    │   └── vectorstore.py
    ├── data/
    │   └── speech.txt
    └── pipelines/
        ├── __init__.py
        ├── rag_pipeline.py
        └── retriever_pipeline.py
```
