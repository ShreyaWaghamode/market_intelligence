import yfinance as yf


class FinancialFetcher:

    @staticmethod
    def get_financials(ticker):

        stock = yf.Ticker(ticker)

        info = stock.info

        return {
            "ticker": ticker,
            "market_cap": info.get("marketCap", 0),
            "pe_ratio": info.get("trailingPE", 0),
            "debt_to_equity": info.get("debtToEquity", 0),
            "revenue_growth": info.get("revenueGrowth", 0)
        }