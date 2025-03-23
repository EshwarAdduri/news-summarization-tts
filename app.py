import streamlit as st
import requests

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/analyze"

# Streamlit UI
st.title("📰 News Summarization & Sentiment Analysis")
st.write(
    "Enter a company name to fetch recent news articles and analyze their sentiment."
)

company = st.text_input("Company Name:")

if st.button("Fetch News & Analyze"):
    if company:
        response = requests.post(API_URL, json={"company": company})

        if response.status_code == 200:
            result = response.json()

            st.subheader(f"📢 News Analysis for {company}")
            for article in result["articles"]:
                st.markdown(f"### [{article['title']}]({article['url']})")
                st.write(f"**Summary:** {article['summary']}")
                st.write(f"**Sentiment:** {article['sentiment']}")
                st.write("---")

            st.subheader("📊 Comparative Sentiment Analysis")
            st.json(result["comparative_analysis"])

            st.subheader("🔊 Hindi TTS Output")
            st.audio(result["audio_url"])

        else:
            st.error("⚠️ Error fetching data. Try again.")

    else:
        st.warning("⚠️ Please enter a company name.")
