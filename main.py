from fastapi import FastAPI, HTTPException
from engine.rag_logic import VectorStore, ContextualRAG
import uvicorn

app = FastAPI(title="Vector-Context-Engine", version="1.0.0")

# Singleton instances
store = VectorStore()
rag = ContextualRAG(store)

@app.get("/")
async def status():
    return {"status": "RAG Engine Online", "vector_store": "Ready"}

@app.post("/query")
async def query_rag(payload: dict):
    user_query = payload.get("query")
    if not user_query:
        raise HTTPException(status_code=400, detail="Query is required.")
    
    result = rag.generate_response(user_query)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
