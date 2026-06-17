from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze(financials, retrieved_news, query):
    try:
        context = "\n".join(retrieved_news[:5])

        prompt = f"""
You are an investment analyst.

Query:
{query}

Financial Data:
{financials}

Relevant News:
{context}

Provide:
1. Key insights
2. Risks
3. Opportunities
4. Investment recommendation

Keep the response concise and professional.
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