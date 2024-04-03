# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Mock sentiment analysis function (replace this with your actual sentiment analysis code)
# def analyze_sentiment(news):
#     # Placeholder sentiment analysis
#     sentiment_scores = [-0.2, 0.5, -0.1, 0.8, 0.2]  # Example sentiment scores
#     return sentiment_scores

# # Page title
# st.title('Stock News Sentiment Analysis Dashboard')

# # Sidebar
# st.sidebar.header('User Input')

# # Function to get user input
# def get_input():
#     stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL")
#     return stock_symbol

# # Get user input
# stock_symbol = get_input()

# # Mock stock news data
# news_data = pd.DataFrame({
#     'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
#     'Headline': ['Apple announces record-breaking iPhone sales', 
#                  'Tech sector faces challenges amidst regulatory concerns', 
#                  'Tesla stock reaches all-time high', 
#                  'Amazon announces expansion into healthcare sector', 
#                  'Google unveils new AI-powered products']
# })

# # Display news data
# st.subheader('Nifty 50 ')
# st.table(news_data)

# # Perform sentiment analysis on news headlines
# sentiment_scores = analyze_sentiment(news_data['Headline'])

# # Display sentiment analysis results
# st.subheader('Sentiment Analysis')
# sentiment_df = pd.DataFrame({
#     'Date': news_data['Date'],
#     'Sentiment Score': sentiment_scores
# })
# st.line_chart(sentiment_df.set_index('Date'))

# # Plot sentiment distribution
# st.subheader('Sentiment Distribution')
# sentiment_counts = pd.cut(sentiment_df['Sentiment Score'], bins=[-1, -0.5, 0, 0.5, 1], labels=['Negative', 'Neutral (Negative)', 'Neutral (Positive)', 'Positive']).value_counts()
# st.bar_chart(sentiment_counts)

# # Additional Features
# st.sidebar.subheader('Additional Features')
# # Add additional features/options here based on user requirements



# ********************************** ANOTHER CODE ******************************************

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
st.set_option('deprecation.showPyplotGlobalUse', False)

# Mock sentiment analysis function (replace this with your actual sentiment analysis code)
def analyze_sentiment(title):
    sentiment_scores = []
    for headline in title:
        blob = TextBlob(headline)
        sentiment_score = blob.sentiment.polarity
        if sentiment_score > 0:
            sentiment_scores.append(1)  # Positive sentiment
        elif sentiment_score < 0:
            sentiment_scores.append(-1)  # Negative sentiment
        else:
            sentiment_scores.append(0)  # Neutral sentiment
    return sentiment_scores

# Page title
st.title('Stock News Sentiment Analysis Dashboard')

# Sidebar
st.sidebar.header('User Input')

# Function to get user input
def get_input():
    stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL)", "AAPL")
    return stock_symbol

# Get user input
stock_symbol = get_input()

# Read stock news data from CSV
file_path = 'C://Users//HP//Desktop//stremlit//dataset//all_merged_data.csv'  # Replace with the path to your CSV file
news_data = pd.read_csv(file_path)

# Display top 10 news headlines in a table
st.subheader('Top 10 News Headlines')
top_10_news = news_data.head(10)

# Truncate description to a certain number of characters (e.g., 100 characters)
top_10_news['Description'] = top_10_news['Description'].str[:100] + '...'

# Define column widths for the table
column_widths = {'Date': '10%', 'Title': '20%', 'Description': '70%'}

# Apply the table CSS style for adjusting column widths
table_css = """
<style>
table {
    width: 100%;
}
th {
    text-align: left;
}
th:nth-child(1) {
    width: """ + column_widths['Date'] + """;
}
th:nth-child(2) {
    width: """ + column_widths['Title'] + """;
}
th:nth-child(3) {
    width: """ + column_widths['Description'] + """;
}
</style>
"""

# Display the table with adjusted column widths
st.markdown(table_css, unsafe_allow_html=True)
st.table(top_10_news[['Date', 'Title', 'Description']])

# Perform sentiment analysis on news headlines
sentiment_scores = analyze_sentiment(news_data['Title'])

# Display sentiment analysis results
st.subheader('Sentiment Analysis')
sentiment_df = pd.DataFrame({
    'Date': news_data['Date'],
    'Sentiment Score': sentiment_scores
})
st.line_chart(sentiment_df.set_index('Date'))

# Plot sentiment distribution
st.subheader('Sentiment Distribution')
fig, ax = plt.subplots()

# Calculate sentiment counts
sentiment_counts = sentiment_df['Sentiment Score'].value_counts().sort_index()

# Plot sentiment distribution using a bar graph
sentiment_counts.plot(kind='bar', ax=ax)

# Customize plot labels and ticks
ax.set_xlabel('Sentiment Score')
ax.set_ylabel('Count')
ax.tick_params(axis='x', rotation=0)

# Show the plot in the Streamlit app
st.pyplot(fig)

# Additional Features
st.sidebar.subheader('Additional Features')
# Add additional features/options here based on user requirements