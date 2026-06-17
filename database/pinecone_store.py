from pinecone import Pinecone
from config import INDEX_NAME, PINECONE_API_KEY
from embeddings.embedding_model import model

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

index = pc.Index(
    INDEX_NAME
)


def store_news(news):
    """Store news articles in Pinecone using text embeddings."""
    if not news:
        return

    records = []

    for item in news:
        text = (
            item.get("content")
            or item.get("snippet")
            or item.get("title")
            or item.get("summary")
            or ""
        ).strip()

        if not text:
            continue

        embedding = model.encode(text).tolist()

        records.append(
            {
                "id": str(
                    item.get("id")
                    or item.get("url")
                    or item.get("title")
                    or len(records)
                ),
                "values": embedding,
                "metadata": {
                    "text": text,
                    "title": item.get("title") or "",
                    "url": item.get("url") or "",
                    "published_date": item.get("published_date")
                    or item.get("date")
                    or "",
                },
            }
        )

    if records:
        index.upsert(vectors=records)