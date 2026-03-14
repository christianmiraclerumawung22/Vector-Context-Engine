import json
import time

class VectorStore:
    """
    Simulates a high-performance Vector Database (Pinecone/Milvus/Qdrant).
    """
    def __init__(self):
        # Mock vector store
        self.documents = [
            {"id": "doc1", "content": "PT Adi Data Informatika specializes in AI and IT solutions."},
            {"id": "doc2", "content": "Christian Miracle Rumawung is a senior AI Engineer focusing on Backend."},
            {"id": "doc3", "content": "Retrieval Augmented Generation (RAG) is the gold standard for LLM context."}
        ]

    def similarity_search(self, query: str, top_k=2):
        """Simulates finding relevant document chunks for a query."""
        # Simple string-matching mock for the vector search logic
        print(f"[VectorStore] Performing similarity search for: '{query}'")
        time.sleep(0.05)
        return self.documents[:top_k]

class ContextualRAG:
    """
    Retrieval Augmented Generation Orchestrator.
    Bridges LLM with Contextual Data.
    """
    def __init__(self, vector_store: VectorStore):
        self.store = vector_store

    def generate_response(self, user_query: str):
        # 1. Retrieve context
        context_chunks = self.store.similarity_search(user_query)
        context_str = "\n".join([c['content'] for c in context_chunks])

        # 2. Construct Augmented Prompt
        augmented_prompt = f"""
        System: Use the context below to answer the user query.
        Context: {context_str}
        User Query: {user_query}
        """

        # 3. Simulate LLM Generation
        print(f"[RAG Engine] Generating response using augmented prompt...")
        time.sleep(0.1)
        
        return {
            "query": user_query,
            "context_retrieved": [c['id'] for c in context_chunks],
            "ai_response": f"Based on the context, {user_query} is related to {context_chunks[0]['id']}.",
            "pipeline_latency": "150ms"
        }

if __name__ == "__main__":
    store = VectorStore()
    rag = ContextualRAG(store)
    
    result = rag.generate_response("Who is Christian Miracle Rumawung?")
    print(json.dumps(result, indent=2))
