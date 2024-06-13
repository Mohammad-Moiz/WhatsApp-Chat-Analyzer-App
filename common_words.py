from collections import Counter
import pandas as pd

def most_common_words(selected_user, df):
    stopwords_path = 'stop_hinglish.txt'
    try:
        with open(stopwords_path, 'r') as f:
            stop_words = f.read().splitlines()
    except FileNotFoundError:
        stop_words = []

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[(df['user'] != 'group_notification') & (df['message'] != '<Media omitted>\n')]
    words = [word.lower() for message in temp['message'] for word in message.split() if word not in stop_words]

    most_common_df = pd.DataFrame(Counter(words).most_common(20), columns=['word', 'count'])

