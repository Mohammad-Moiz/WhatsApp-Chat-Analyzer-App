import matplotlib.pyplot as plt
from textblob import TextBlob


def sentiment_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    sentiments = df['message'].apply(lambda msg: TextBlob(msg).sentiment.polarity)
    df['sentiment'] = sentiments.apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')

    sentiment_counts = df['sentiment'].value_counts()
    return sentiment_counts

def plot_sentiment_pie(sentiment_counts):
    labels = sentiment_counts.index
    sizes = sentiment_counts.values
    colors = ['#FF6347', '#32CD32', '#FFD700']
    explode = (0.1, 0, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=140)
    ax1.axis('equal')  

    return fig1
