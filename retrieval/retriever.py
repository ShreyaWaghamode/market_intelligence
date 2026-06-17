from embeddings.embedding_model import model
from database.pinecone_store import index


def retrieve(query):

    query_embedding = model.encode(
        query
    ).tolist()

    results = index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True
    )

    return [
        match["metadata"]["text"]
        for match in results["matches"]
    ]