# BBC News Headlines Dataset Analysis

## Overview
This project aims to analyze the **BBC News Headlines Dataset** using **Natural Language Processing (NLP)** techniques. Specifically, I performed **Topic Modeling** using **Latent Dirichlet Allocation (LDA)** and **Sentiment Analysis** to uncover patterns and insights in the news titles. The dataset reveals important trends across different domains, providing a deeper understanding of the topics and sentiments conveyed through BBC headlines.

## Dataset
The dataset consists of BBC News headlines collected over several years. Each headline is a short text representing the main theme of the associated news article. It includes various categories, such as business, politics, sports, culture, and technology.

## Analysis Workflow
The analysis was carried out in the following steps:

1. **Data Preprocessing**:
    - Tokenized the headlines for further analysis.

2. **Word Frequency Analysis**:
    - Identified the most frequent words in the dataset to understand the dominant terms and patterns in BBC headlines.

3. **Topic Modeling**:
    - Applied **LDA (Latent Dirichlet Allocation)** to extract hidden topics from the news titles.
    - The model generated five major topics, each focusing on distinct domains of news coverage.

4. **Sentiment Analysis**:
    - Performed sentiment analysis on the headlines to gauge the general tone of the news.
    - Sentiment scores ranged from positive to negative, allowing for insights into the emotional weight of the headlines.

## Results

### Word Frequency Analysis
The most frequent words were primarily stopwords, which are common and carry little information. After removing these, the most common meaningful word was **"said"**, indicating that reporting quotes or statements plays a significant role in the news. Other frequent words like *market, growth, win,* and *government* pointed to major themes in the dataset.

### Topic Modeling (LDA)
**Topic 0**: Business & Economy  
- Keywords: *2004, sales, economy, growth, market, company, year*

**Topic 1**: Sports  
- Keywords: *play, club, world, win, game, England*

**Topic 2**: UK Politics  
- Keywords: *Blair, party, election, Labour, government, people*

**Topic 3**: Music & Culture  
- Keywords: *rock, album, song, band, music*

**Topic 4**: Technology & Entertainment  
- Keywords: *digital, mobile, TV, film, music*

Each topic reflects a different area of focus in BBC's news coverage. For example, **Topic 0** highlights economic themes, while **Topic 1** captures sports-related content.

### Sentiment Analysis
- The sentiment analysis revealed that headlines related to **business** and **economic growth** often carried a **positive tone** (e.g., "Ad sales boost Time Warner profit").
- Political headlines were more **neutral or negative**, reflecting the contentious and complex nature of these topics (e.g., "Yukos unit buyer faces loan claim").
- Overall, the sentiment was skewed towards neutrality, with some positive sentiment in specific domains like business and technology.

## Conclusions

1. **Quotes Drive Headlines**: The dominance of the word *"said"* suggests that a large portion of BBC’s headlines are based on what people or organizations are saying. This reflects the importance of quotes and statements in news reporting.
  
2. **Distinct Topic Categories**: Topic modeling successfully revealed five major categories—business, sports, politics, music, and technology. These topics align with general trends in news coverage and provide insight into the most discussed themes.

3. **Sentiment is Balanced**: Sentiment analysis showed a generally neutral tone across most headlines, with some positive sentiment in business-related articles. Political and issue-based headlines often carried a more cautious or neutral tone.

## Future Recommendations

Here are potential improvements and future extensions for the analysis:

1. **Refining Topic Modeling**:
    - Increase the number of topics or fine-tune the model to capture more nuanced differences in overlapping topics, especially where business and culture themes blend.

2. **Time-Based Analysis**:
    - Analyze how the sentiment and topic distribution change over time. For example, tracking sentiment trends during major political events or economic shifts could yield fascinating insights.

3. **Deep Dive into Specific Topics**:
    - Perform a deeper analysis on specific topics (e.g., politics or technology) to understand the sub-themes driving each category.

4. **Expand Sentiment Analysis**:
    - Use advanced sentiment analysis models to better capture the subtleties of tone in the headlines, such as sarcasm or mixed sentiment in complex stories.

5. **Visualization**:
    - Build interactive visualizations using libraries like Plotly or Dash to explore the topics and sentiments dynamically.

---

## How to Run the Code

### Prerequisites:
- Python 3.x
- Required Libraries: `pandas`, `nltk`, `gensim`, `sklearn`, `matplotlib`, `seaborn`, `wordcloud`, `vaderSentiment`

### Steps:
1. Clone this repository:
    ```bash
    git clone https://github.com/NadaHossam97/bbc-headlines-analysis.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the analysis:
    ```bash
    python analysis.py
    ```

---

## Author
Nada Hossam  
Data Scientist

Feel free to connect with me on [LinkedIn](https://linkedin.com/in/nada-hossameldeen) or check out my other projects on [GitHub](https://github.com/NadaHossam97).

