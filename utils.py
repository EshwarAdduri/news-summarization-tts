import requests
from textblob import TextBlob
from gtts import gTTS
import os

API_KEY = "9bcbb8a6922c4e88ac0dd8c14ebfcd07"  # Replace with your valid NewsAPI key


# Fetch news articles
def fetch_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"API Error: {data.get('message', 'Unknown error')}")
            return []

        if "articles" not in data or len(data["articles"]) == 0:
            print("No news articles found.")
            return []

        articles = []
        for item in data["articles"][:10]:
            articles.append(
                {
                    "title": item["title"],
                    "summary": item["description"] or "No summary available.",
                    "content": item["content"] or "No content available.",
                    "url": item["url"],
                }
            )

        return articles

    except Exception as e:
        print(f"Error fetching news: {str(e)}")
        return []


# Sentiment analysis
def analyze_sentiment(text):
    if not text or text.strip() == "":
        return "Neutral"

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# Hindi Text-to-Speech (TTS)
def generate_tts(text, company):
    output_path = f"{company}_summary.mp3"

    try:
        tts = gTTS(text=text, lang="hi")
        tts.save(output_path)
        return output_path
    except Exception as e:
        print(f"TTS Generation Error: {str(e)}")
        return None
