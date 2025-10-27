import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class VectorDatabase:
    def __init__(self, db_path, model_name, documents=None):
        self.db_path = db_path
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        
        self.vector_store = self.load_vector_database()

    def load_vector_database(self):
        """Load existing vector database."""
        if not self._database_exists():
            raise FileNotFoundError(
                f"No existing vector database found at {self.db_path}. "
                f"Please provide documents to create a new database."
            )
        
        print("Loading existing vector database...")
        return FAISS.load_local(
            self.db_path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )

    def _database_exists(self):
        """Check if the vector database files exist."""
        required_files = [
            os.path.join(self.db_path, "index.faiss"),
            os.path.join(self.db_path, "index.pkl")
        ]
        return all(os.path.exists(f) for f in required_files)

    def query(self, query_text, k=5, lambda_mult=0.45, fetch_k=50):
        """Query the vector database."""
        retriever = self.vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={'k': k, 'lambda_mult': lambda_mult, "fetch_k": fetch_k}
        )
        return retriever.invoke(query_text)