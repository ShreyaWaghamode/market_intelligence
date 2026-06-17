from pydantic import BaseModel
from typing import List


class AnalysisOutput(BaseModel):

    news_sentiment_score: float

    identified_financial_risks: List[str]

    competitor_threats: List[str]

    metric_divergence_alert: bool

    recommendation: str