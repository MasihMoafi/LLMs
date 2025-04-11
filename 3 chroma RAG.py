# CHROMOA
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.schema import Document
from ollama import chat
import os
import re

DOCUMENT_PATHS = [
    r'/home/masih/rag_data/Hamrah.txt', #replace path
    r'/home/masih/rag_data/vape.txt',
    r'/home/masih/rag_data/Shah.txt',
    r'/home/masih/rag_data/Khalife.txt',
    r'/home/masih/rag_data/carbon.txt',
    r'/home/masih/rag_data/takapoo.txt'
]

EMBEDDING_MODEL = 'sentence-transformers/paraphrase-multilingual-mpnet-base-v2'
LLM_MODEL = 'gemma3'
CHUNK_SIZE = 1000
OVERLAP = 200
CHROMA_PERSIST_DIR = r'\home\Masih\chroma_db\chroma_db'  

class ChromaRAGSystem:
    def __init__(self):
        # Init embedding model
        self.embeddings = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL)
        # Vector store instance
        self.vector_db = None
        
    def build_vector_store(self):
        """Process documents and create Chroma vector store"""
        all_docs = []
        

        for doc_idx, path in enumerate(DOCUMENT_PATHS):
            with open(path, 'r', encoding='utf-8') as f:
                text = re.sub(r'\s+', ' ', f.read()).strip()
                # sliding window chunking
                chunks = [
                    text[i:i+CHUNK_SIZE] 
                    for i in range(0, len(text), CHUNK_SIZE - OVERLAP)
                ]
                # LangChain documents with metadata
                for chunk in chunks:
                    all_docs.append(Document(
                        page_content=chunk,
                        metadata={"source_doc": doc_idx}
                    ))
        
        # Chroma vector store
        self.vector_db = Chroma.from_documents(
            documents=all_docs,
            embedding=self.embeddings,
            persist_directory=CHROMA_PERSIST_DIR
        )
        self.vector_db.persist()
        
    def load_vector_store(self):
        """Load existing Chroma vector store"""
        self.vector_db = Chroma(
            persist_directory=CHROMA_PERSIST_DIR,
            embedding_function=self.embeddings
        )
        
    def document_query(self, query, doc_index, top_k=5):
        """Retrieve context from specific document"""
        # Chroma metadata filtering
        results = self.vector_db.similarity_search(
            query=query,
            k=top_k,
            filter={"source_doc": doc_index}
        )
        return [doc.page_content for doc in results]

class AnswerGenerator:
    def __init__(self, rag_system):
        self.rag = rag_system
        
    def generate_response(self, question, doc_index):
        """Generate context-aware answer using LLM"""
        # Retrieve relevant context
        context_chunks = self.rag.document_query(question, doc_index)
        context = "\n".join(context_chunks)
        
        prompt = f"""Answer the query from the document below:
{context}

If the answer is not found in the document, return "No answers were found in the provided context." 

query: {question}
response:"""
        
        response = chat(model=LLM_MODEL, messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']

if __name__ == "__main__":
    rag_system = ChromaRAGSystem()
    
    # Init vector store
    if not os.path.exists(CHROMA_PERSIST_DIR):
        print("Creating new vector store...")
        rag_system.build_vector_store()
    else:
        print("Loading existing vector store...")
        rag_system.load_vector_store()
    
    # Init answer generator
    answer_engine = AnswerGenerator(rag_system)

    queries = [
        ("؟", 0),
        ("؟", 1),
        ("؟", 2),
        ("؟", 3),
        ("؟", 4),
        ("؟", 5)
    ]
    
    with open( r'/home/masih/rag_data/response.txt', 'w', encoding='utf-8') as output_file: #repalce path
        for q_num, (query, doc_idx) in enumerate(queries):
            answer = answer_engine.generate_response(query, doc_idx)
            output_file.write(f"سوال {q_num+1} ({doc_idx+1}):\n{query}\n\nپاسخ:\n{answer}\n\n{'='*50}\n\n")
            print(f"پردازش سوال {q_num+1}/{len(queries)} تکمیل شد")

print("All queries have been processed!")
