import pandas as pd
import re

# Load the dataset
df = pd.read_csv('.\\bbc_text_cls.csv')



from collections import Counter

# Tokenize the titles
words = ' '.join(df['text']).split()

# Get word frequencies
word_freq = Counter(words)

# Show the most common words
print(word_freq.most_common(20))

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))

# Display the word cloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Convert titles into a matrix of token counts
count_vect = CountVectorizer(stop_words='english')
doc_term_matrix = count_vect.fit_transform(df['text'])

# Apply LDA
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(doc_term_matrix)

# Show the topics
words = count_vect.get_feature_names_out()
for i, topic in enumerate(lda.components_):
    print(f"Topic {i}:")
    print([words[i] for i in topic.argsort()[-10:]])    

from textblob import TextBlob

# Function to get the sentiment polarity (-1: negative, 1: positive)
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Apply sentiment analysis
df['sentiment'] = df['text'].apply(get_sentiment)

# Display the first few sentiment values
print(df[['text', 'sentiment']].head())

# Plot the sentiment distribution
import seaborn as sns
sns.histplot(df['sentiment'], bins=30)
plt.title('Sentiment Distribution')
plt.show()
