# LLMs
Performing various tasks using LLMs.

These tasks include: RAG using two different methods, Email generation, summarization, text to speech, image segmentation, etc.

Summarizing is one of my main areas of interest, as the LLMs I frequently use tend to be overly verbose.

README for Test Dorna
Overview
This repository contains an implementation of a Question-Answering (QA) system leveraging Retrieval-Augmented Generation (RAG) and other advanced techniques like Chroma and LangChain. The system uses a combination of pre-trained models and custom indexing to retrieve context from a set of documents and generate context-aware answers to questions. It also includes a web-browsing agent to fetch real-time information from the web.

Key Features
RAG-based Search: Use FAISS or Chroma to index and retrieve document chunks based on cosine similarity.
Answer Generation: Combines document retrieval with large language models (LLM) like llama3.2 to generate coherent answers.
Web Browsing Tool: An agent that can scrape the web for up-to-date information.
Multilingual: Supports multi-language queries (e.g., Persian).
Installation
Prerequisites
Ensure you have the following libraries installed:

bash
Copy
pip install faiss-cpu sentence-transformers ollama numpy
pip install langchain chromadb sentence-transformers ollama
pip install -U langchain-community
Libraries
faiss-cpu: Used for efficient similarity search and clustering.
sentence-transformers: To embed documents and queries for similarity search.
ollama: A Python package for interacting with Ollama models.
langchain: For chaining multiple LLMs and tools in complex workflows.
chromadb: A vector store used for Chroma-based RAG.
numpy: For array manipulation.
Usage
Initialization
RAG System: The RAG system creates an index or loads an existing one. The system works with multiple document sources (defined in DOCUMENT_PATHS) and splits them into chunks for efficient retrieval.
Answer Generator: Uses the RAG system to fetch relevant document chunks based on the question and generates a response using the LLM.
Web Browsing Tool: Fetches real-time information from the web using a specific URL.
Example Flow
Document Processing:

Chunks are created from documents (e.g., .txt files).
The system creates or loads an index to facilitate similarity-based search.
Query Execution:

A list of predefined questions is processed.
For each query, the system searches for relevant context and generates a response using the LLM.
Running the Main Script
To run the script, execute the following:

bash
Copy
python main.py
This will process a set of predefined queries, generate responses using the RAG system, and save the results to a file (e.g., response.txt).

Agent with Web Browsing
The system can use a web browsing agent to fetch live web data. The agent uses the requests and BeautifulSoup libraries to scrape web pages and return content up to 5000 characters.

Example of using the Agent:
python
Copy
from langchain.agents import Tool, initialize_agent, AgentType

# Define tools
tools = [
    Tool(
        name="Document_Search",
        func=document_search_function,  # Function for document search
        description="For questions about documents"
    ),
    Tool(
        name="Web_Browser",
        func=web_browser_tool,  # Web browsing function
        description="For fetching live web data"
    )
]

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llama_model,  # Use your pre-trained LLM here
    agent_type=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory_buffer,  # Optional: To use conversation memory
    verbose=True
)
Results
Queries will be processed sequentially, and the results will be saved to the specified output file.

Example output:

makefile
Copy
سوال 1 (1):
چرا اینترنت همراه اول گوشی وصل نمیشود؟

پاسخ:
برای حل این مشکل، اول باید اطمینان حاصل کنید که شبکه موبایل شما به درستی فعال است...
Customization
Document Paths: Modify the DOCUMENT_PATHS list to point to your own documents.
Embedding Models: You can change the EMBEDDING_MODEL and LLM_MODEL to other pre-trained models.
Chunking Parameters: Modify CHUNK_SIZE and OVERLAP to control the document chunking behavior.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
This project leverages LangChain, Ollama, FAISS, and Chroma for building efficient and scalable RAG systems.
