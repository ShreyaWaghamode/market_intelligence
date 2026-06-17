from data_fetcher.financial_fetcher import FinancialFetcher
from data_fetcher.tavily_news_fetcher import TavilyNewsFetcher

from database.pinecone_store import store_news

from retrieval.retriever import retrieve

from llm.analyzer import analyze


def main():

    ticker = input("Ticker: ").strip()

    query = input("Analysis Query: ").strip()

    print("\nFetching financial data...")

    financials = FinancialFetcher.get_financials(
        ticker
    )

    print("Fetching news...")

    news = TavilyNewsFetcher().fetch_news(
        ticker
    )

    print("Storing news in Pinecone...")

    store_news(news)

    print("Retrieving relevant news...")

    retrieved_news = retrieve(
        query
    )

    print("Generating analysis...\n")

    analysis = analyze(
        financials,
        retrieved_news,
        query
    )

    print("=" * 80)
    print("MARKET INTELLIGENCE REPORT")
    print("=" * 80)

    print(analysis)


if __name__ == "__main__":
    main()