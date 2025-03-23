from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import fetch_news, analyze_sentiment, generate_tts
import os

app = FastAPI()


class RequestModel(BaseModel):
    company: str


@app.post("/analyze")
def analyze_news(request: RequestModel):
    company = request.company

    # Fetch news
    articles = fetch_news(company)
    if not articles:
        raise HTTPException(status_code=404, detail="No news articles found.")

    # Perform sentiment analysis
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["content"])

    # Generate comparative sentiment analysis
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for article in articles:
        sentiment_counts[article["sentiment"]] += 1

    comparative_analysis = {"Sentiment Distribution": sentiment_counts}

    # Generate Hindi TTS
    summary_text = " ".join([article["summary"] for article in articles])
    audio_path = generate_tts(summary_text, company)

    return {
        "company": company,
        "articles": articles,
        "comparative_analysis": comparative_analysis,
        "audio_url": audio_path,
    }
