import streamlit as st
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Sample list of top 10 companies from Nifty 50
top_10_companies = ['TikTok', 'Disney', 'Wirecard', 'Twitter', 'Google', 'Delta', 'S&P', 'FTC', 'BlackRock', 'Boohoo', 'Pemex']

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Mock sentiment analysis function using VADER
def analyze_sentiment_vader(title):
    sentiment_scores = []
    for headline in title:
        sentiment = sid.polarity_scores(headline)
        if sentiment['compound'] >= 0.05:
            sentiment_scores.append('Positive')
        elif sentiment['compound'] <= -0.05:
            sentiment_scores.append('Negative')
        else:
            sentiment_scores.append('Neutral')
    return sentiment_scores

# Page title
st.title('Stock News Sentiment Analysis Dashboard')

# Sidebar
st.sidebar.header('User Input')

# Dropdown menu to select company
selected_company = st.sidebar.selectbox('Select Company', top_10_companies)

# Read stock news data from CSV (Replace with your data loading logic)
file_path = 'C://Users//HP//Desktop//stremlit//dataset//searchbar_updated.csv'
news_data = pd.read_csv(file_path)

# Filter news data for the selected company
filtered_data = news_data[news_data['Company'] == selected_company]

# Display top 10 news headlines for the selected company in a table
st.subheader(f'Top 10 News Headlines for {selected_company}')
top_10_news = filtered_data.head(10)

# Truncate description to a certain number of characters (e.g., 100 characters)
top_10_news['Description'] = top_10_news['Description'].str[:100] + '...'

# Display the table with adjusted column widths
st.table(top_10_news[['Date', 'Headline', 'Description']])

# Perform sentiment analysis using VADER on news headlines
sentiment_scores = analyze_sentiment_vader(top_10_news['Headline'])

# Display sentiment analysis results
st.subheader('Sentiment Analysis')
sentiment_df = pd.DataFrame({
    'Headline': top_10_news['Headline'],
    'Sentiment': sentiment_scores
})
st.table(sentiment_df)

# Plot sentiment distribution
st.subheader('Sentiment Distribution')
sentiment_counts = pd.DataFrame(sentiment_scores, columns=['Sentiment']).value_counts().reset_index()
sentiment_counts.columns = ['Sentiment', 'Count']
st.bar_chart(sentiment_counts)

# Additional Features
st.sidebar.subheader('Additional Features')
# Add additional features/options here based on user requirements
