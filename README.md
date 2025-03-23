# News Summarization & Text-to-Speech (TTS) Application

## Overview
This web application extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a Hindi text-to-speech (TTS) output.

## Features
- **News Extraction:** Fetches and displays at least 10 news articles related to a company.
- **Sentiment Analysis:** Analyzes whether each article is Positive, Negative, or Neutral.
- **Comparative Analysis:** Compares sentiment across articles.
- **Text-to-Speech:** Converts summary into Hindi speech.
- **User Interface:** Simple UI built using Streamlit.
- **Deployment:** The application can be deployed on Hugging Face Spaces.

## Installation

### 1. Clone the Repository
```bash
git clone <repo>
cd project directory
```

### 2. Create a Virtual Environment
```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

### 1. Start the API Server
```bash
python api.py
```
This will start the FastAPI backend on http://127.0.0.1:8000.

### 2. Run the Streamlit App
Open a new terminal and run:
```bash
streamlit run app.py
```
This will open the UI in a web browser.

## Usage
1. Enter a company name in the input field.
2. Click "Fetch News & Analyze".
3. View the structured sentiment report.
4. Play the Hindi TTS audio of the summary.

## Deployment on Hugging Face Spaces
To deploy, follow Hugging Face's guidelines for Streamlit/FastAPI apps.

## API Endpoints
### **POST /analyze**
**Request:**
```json
{
  "company": "Tesla"
}
```

**Response:**
```json
{
  "company": "Tesla",
  "articles": [...],
  "comparative_analysis": {...},
  "audio_url": "Tesla_summary.mp3"
}
```

## Notes
- If news scraping fails, modify `fetch_news()` in `utils.py` to use another news source.
- The app currently saves TTS audio locally; modify it for cloud storage if needed.