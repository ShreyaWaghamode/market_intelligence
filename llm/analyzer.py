from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze(financials, retrieved_news, query):
    try:
        context = "\n".join(retrieved_news[:5])

        prompt = f"""
You are a senior investment analyst.

Analyze the stock using ONLY the provided financial data and retrieved news.

Query:
{query}

Financial Data:
{financials}

Relevant News:
{context}

Generate the report in the following format:

# MARKET INTELLIGENCE REPORT

## Executive Summary
Provide a brief 2-3 sentence summary of the company's current position and outlook.

## Key Insights
- Insight 1
- Insight 2
- Insight 3

## Financial Analysis
- Market Capitalization:
- Revenue Growth:
- P/E Ratio:
- Debt-to-Equity Ratio:
- Overall Financial Health:

## Risks
- Risk 1
- Risk 2
- Risk 3

## Opportunities
- Opportunity 1
- Opportunity 2
- Opportunity 3

## News Impact
Summarize how the retrieved news may positively or negatively affect the company and stock performance.

## Investment Recommendation
Recommendation: BUY / HOLD / SELL

Reasoning:
- Reason 1
- Reason 2
- Reason 3

## Confidence Level
Provide a confidence score between 1 and 10 along with a short explanation.

Instructions:
- Use clear headings and bullet points.
- Base conclusions only on the provided financial data and news.
- Do not make up facts that are not present in the data.
- Keep the analysis professional, concise, and investor-focused.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert financial analyst."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating analysis: {str(e)}"