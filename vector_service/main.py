import os
from fastapi import FastAPI
from .vector_db import VectorDatabase
from .models import QueryRequest, QueryResponse, Document
from src.utils.paths import get_project_path

app = FastAPI()

vector_db = VectorDatabase(
    db_path=os.path.join(get_project_path(), "db", "intfloat_multilingual-e5-large"),
    model_name='intfloat/multilingual-e5-large'
)

@app.post("/query", response_model=QueryResponse)
def query_vector_db(request: QueryRequest):
    """
    Queries the vector database using the given query text and parameters.

    Args:
        request (QueryRequest): The query request containing the query text and parameters.

    Returns:
        QueryResponse: A response containing the list of relevant documents.
    """
    documents = vector_db.query(request.query, request.k, request.lambda_mult, request.fetch_k)
    response_documents = [
        Document(content=doc.page_content, metadata=doc.metadata) for doc in documents
    ]
    return QueryResponse(documents=response_documents)

@app.get("/num_documents")
def get_num_documents():
    """
    Returns the number of documents stored in the vector database.

    Returns:
        dict: A dictionary with a single key "num_documents" containing the number of documents in the vector database.
    """
    num_documents = vector_db.get_num_documents()
    return {"num_documents": num_documents}
