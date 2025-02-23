import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words_english = set(stopwords.words('english'))
print(stop_words_english)
print(len(stop_words_english))


data = {'text':['This $is @Bangladesh!','^ I *love & my #country']}

df = pd.DataFrame(data)


print(df.columns)

df['stop'] = df['text'].apply(lambda x: ' '.join(word for word in x.split() if word.lower() not in stop_words_english))
print(df['stop'])
