https://github.com/user-attachments/assets/04627f5d-3538-4ac1-89ba-f2ef942b4ed9

# Deploying Agentic RAG Systems to Perform Various Tasks Using LLMs

This repository showcases the implementation of a Retrieval-Augmented Generation (RAG) system for answering questions using large language models (LLMs) and document retrieval. The system integrates document indexing, chunking, and similarity search with advanced language models like `gemma2:9b` to provide context-aware responses. Additionally, it incorporates a web-browsing agent for retrieving live data.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
  - [RAG System](#rag-system)
  - [Answer Generator](#answer-generator)
  - [Web Browsing Agent](#web-browsing-agent)
  - [Chroma-based RAG](#chroma-based-rag)
- [Results](#results)
- [License](#license)

## Overview
The project is designed to perform tasks like document-based question answering, real-time information retrieval via web scraping, and context-aware response generation. It leverages multiple techniques:
- **RAG (Retrieval-Augmented Generation)**: Uses document indexing and retrieval for question answering.
- **Web Browsing**: Fetches live data to answer real-time queries.
- **Chroma and FAISS**: Index and retrieve relevant document chunks efficiently.

The system is multilingual and supports Persian language queries.

## Installation

To set up the environment, clone the repository and install the required dependencies:

```
git clone https://github.com/yourusername/agentic-rag-system.git
cd agentic-rag-system
pip install -r requirements.txt
The requirements.txt includes dependencies such as:

faiss-cpu: For efficient similarity search.
sentence-transformers: For embedding models.
ollama: For LLM interactions.
langchain: For chaining models and agents.
chromadb: For Chroma-based document retrieval.
Install the additional dependencies for web browsing:

pip install requests beautifulsoup4
Usage
Run the following command to execute the main script:

python main.py
The script processes predefined queries using the RAG system and generates answers based on documents and/or live web data.
```

Steps Performed:
Document Processing: The documents are chunked into smaller segments for efficient retrieval.
Index Creation or Loading: An FAISS index or Chroma-based vector store is created or loaded for similarity search.
Query Answering: A set of queries is processed, and answers are generated using LLMs, based on the retrieved document chunks or web content.
Results are saved in an output file (response.txt or agent_results.txt).

## Components
### RAG System
The RAG system includes:

Document Chunking: Splitting large documents into smaller chunks to improve retrieval performance.
Index Creation: Using FAISS (or Chroma) for indexing the document chunks based on their embeddings.
Similarity Search: Utilizing cosine similarity for retrieving relevant chunks during query processing.
### Answer Generator
The Answer Generator class interacts with the RAG system to fetch the most relevant document chunks based on a given question. It then uses the LLM to generate a context-aware response.

### Web Browsing Agent
The Web Browsing Agent fetches real-time information from the web by scraping web pages. The agent can be used to get live data on current events, statistics, and more.

### Chroma-based RAG
An alternative RAG implementation using Chroma for storing and querying document embeddings is also included. This utilizes LangChain's Chroma integration for efficient vector store management and querying.

## Results
The system successfully processes predefined questions and generates responses based on the relevant document context. Additionally, the web-browsing agent retrieves live data for real-time questions, providing a comprehensive, multi-source approach to answering queries.

Example:
```
سوال 1 (1):
شاه عباس صفوی کیست؟

پاسخ:


The system demonstrates effective integration of multiple techniques to solve complex QA tasks.

## License
This project is licensed under the MIT License.
