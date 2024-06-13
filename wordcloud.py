from wordcloud import WordCloud


def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['message'] = df['message'].astype(str)
    all_words = df['message'].str.cat(sep=" ").strip()
    
    if not all_words:
        raise ValueError("No messages to generate a word cloud")

    stopwords_path = 'stop_hinglish.txt'
    try:
        with open(stopwords_path, 'r') as f:
            stopwords = f.read().splitlines()
    except FileNotFoundError:
        stopwords = []

    wc = WordCloud(width=800, height=400, stopwords=stopwords, min_font_size=10, background_color='white')
    df_wc = wc.generate(all_words)
    return df_wc
