# Market Intelligence

This project is a simple AI-powered stock analysis tool that combines:
- live financial data from Yahoo Finance
- recent news from Tavily
- vector search using Pinecone
- LLM-based analysis using OpenAI

The goal is to help a user understand a company’s current position by combining financial metrics and relevant news context.

## What this project does

When you run the program, it:
1. asks for a stock ticker and a question/query
2. fetches key financial metrics for that company
3. pulls recent news articles related to the company
4. stores the news in a vector database
5. retrieves the most relevant news for the user’s query
6. generates a professional investment-style report

## How the workflow works

The flow is:

1. User input
   - The program asks for:
     - a ticker (for example, `AAPL`)
     - an analysis query (for example, `Is Apple a good investment right now?`)

2. Financial data collection
   - The `FinancialFetcher` uses `yfinance` to read the company’s financial details.
   - It returns values such as:
     - market capitalization
     - P/E ratio
     - debt-to-equity ratio
     - revenue growth

3. News collection
   - The `TavilyNewsFetcher` searches for recent company-related news.
   - This gives the model fresh market context beyond just raw financial numbers.

4. Embedding and storage
   - Each news article is converted into embeddings using `SentenceTransformer`.
   - The embeddings are stored in Pinecone so the app can later search similar content efficiently.

5. Retrieval of relevant news
   - The user’s query is also embedded.
   - The system searches Pinecone for the most relevant news snippets.

6. LLM analysis
   - The financial data + relevant news + user query are sent to OpenAI.
   - The model generates a report with:
     - summary
     - key insights
     - risks
     - opportunities
     - investment recommendation

## Why each tool is used

- `yfinance`
  - Used to get reliable stock and company financial indicators.

- `Tavily`
  - Used to gather up-to-date news articles from the web.

- `SentenceTransformer`
  - Used to convert text into numerical vectors so meaning-based similarity search is possible.

- `Pinecone`
  - Used as a vector database to store and retrieve news based on semantic similarity.

- `OpenAI`
  - Used to turn structured inputs into a readable investment analysis report.

## Project structure

- `main.py`  
  Main entry point that runs the whole pipeline.

- `config.py`  
  Stores API key configuration values.

- `data_fetcher/`  
  Contains logic for fetching financial and news data.

- `database/`  
  Handles Pinecone storage.

- `embeddings/`  
  Contains the embedding model setup.

- `retrieval/`  
  Handles query-based retrieval of relevant news.

- `llm/`  
  Handles report generation using the language model.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add your API keys in `config.py`:
   - `TAVILY_API_KEY`
   - `PINECONE_API_KEY`
   - `OPENAI_API_KEY`
   - `INDEX_NAME`

3. Make sure your Pinecone index exists and is correctly named.

## How to run

```bash
python main.py
```

You will be prompted to enter:
- the ticker symbol
- the analysis question

## Example flow

Input:
- Ticker: `AAPL`
- Query: `Should I invest in Apple based on recent news and financials?`

Output:
- financial metrics summary
- relevant news context
- an AI-generated investment report

## Summary

This project is essentially a  research assistant for stock analysis. It combines financial data, current news, semantic search, and AI reasoning to provide a decision-support report.
