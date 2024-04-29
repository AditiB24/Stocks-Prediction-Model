import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

st.set_option('deprecation.showPyplotGlobalUse', False)

# Page title
st.title('Stock News Sentiment Analysis Dashboard')

# Sidebar
st.sidebar.header('User Input')

# Function to get user input
def get_input():
    selected_company = st.sidebar.selectbox('Select Company', ['TikTok', 'Disney', 'Wirecard', 'Twitter', 'Google', 'Delta', 'S&P', 'FTC', 'BlackRock', 'Boohoo', 'Pemex'])
    return selected_company

# Get user input (selected company)
selected_company = get_input()

# Read stock news data from CSV
file_path = 'C://Users//HP//Desktop//stremlit//dataset//up.csv'  # Replace with the path to your CSV file
news_data = pd.read_csv(file_path)

# Filter news data for the selected company
filtered_data = news_data[news_data['Company'] == selected_company]

# Display top 10 news headlines in a table
st.subheader(f'Top 10 News Headlines for {selected_company}')
top_10_news = filtered_data.head(10)

# Truncate description to a certain number of characters (e.g., 100 characters)
top_10_news['Description'] = top_10_news['Description'].str[:100] + '...'

# Display the table with adjusted column widths
st.table(top_10_news[['Time', 'Headlines', 'Description', 'Score']])

# Plot sentiment distribution
st.subheader('Sentiment Distribution')
fig, ax = plt.subplots()

# Calculate sentiment counts
sentiment_counts = top_10_news['Score'].value_counts().sort_index()

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
