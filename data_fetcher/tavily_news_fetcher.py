from tavily import TavilyClient
from config import TAVILY_API_KEY


class TavilyNewsFetcher:

    def __init__(self):

        self.client = TavilyClient(
            api_key=TAVILY_API_KEY
        )

    def fetch_news(self, ticker):

        query = f"{ticker} company latest financial news"

        response = self.client.search(
            query=query,
            max_results=10
        )

        return response["results"]