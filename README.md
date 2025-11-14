# AmbedkarGPT-Intern-Task

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