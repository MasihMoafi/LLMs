# Deploying Agentic RAG Systems to Perform Various Tasks Using LLMs

This repository showcases the implementation of a Retrieval-Augmented Generation (RAG) system for answering questions using large language models (LLMs) and document retrieval. The system integrates document indexing, chunking, and similarity search with advanced language models like `gemma3` to provide context-aware responses. Additionally, it incorporates a web-browsing agent for retrieving live data.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Components](#components)
  - [RAG System](#rag-system)
  - [Chroma-based RAG](#chroma-based-rag)
- [The Power of Agentic Search](#the-power-of-agentic-search)
  - [Web Browsing Tool](#web-browsing-tool)
  - [Doc Search Tool](#doc-search-tool)
  - [Deep Search Agent](#deep-search-agent)
- [Conclusion](#conclusion)
- [License](#license)

## Overview
The project is designed to perform tasks like document-based question answering, real-time information retrieval via web scraping, and context-aware response generation. It leverages multiple techniques:
- **RAG (Retrieval-Augmented Generation)**: Uses document indexing and retrieval for question answering.
- **Web Browsing**: Fetches live data to answer real-time queries.
- **Chroma and FAISS**: Index and retrieve relevant document chunks efficiently.
- **Agentic search**: Deploying multiple agentic powers to perform various tasks, from web-scraping to document search. 
The system is multilingual and supports Persian language queries.

## Installation

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

### Chroma-based RAG

An alternative RAG implementation using Chroma for storing and querying document embeddings is also included. This utilizes LangChain's Chroma integration for efficient vector store management and querying.

### The Power of Agentic Search

### Web Browsing Tool
The Web Browsing Agent fetches real-time information from the web by scraping web pages. The agent can be used to get live data on current events, statistics, and more.

### Doc Search Tool
Searches across documents and chooses the most relevant document to answer the user's query from.

### Deep Search Agent
Prioritizes google search over the other available tools such as wikipedia, duckduckgo, and document search by using crewAI.

## Results
The system successfully processes predefined questions and generates responses based on the relevant document context. Additionally, the web-browsing tool allows enables the agent to retrieve live data for real-time questions, providing a comprehensive, multi-source approach to answering queries.

## Conclusion
The system demonstrates effective integration of multiple techniques to solve complex QA tasks.

## License
This project is licensed under the manually crafted license @LICENSE; which basically prohibits the use without the knowledge of the author, Masih Moafi. 
