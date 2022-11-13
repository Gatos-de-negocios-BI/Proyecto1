from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
import pandas as pd
import contractions, nltk, string

class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        print("TextPreprocessor initialized")
        self.stop_words = set(stopwords.words('english'))

    def fit(self, X, y=None):
        print("Fitting TextPreprocessor...")
        return self

    def transform(self, X, y=None):
        print("Transforming text...")
        return self.preprocess(X)

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        print("Preprocessing text...")
        # convert series to dataframe
        df = pd.DataFrame(df)
        print("Step 1/10", end="\r")
        df['text'] = df['text'].str.encode(
            'ascii', 'ignore').str.decode('ascii')
        print("Step 2/10", end="\r")
        df['no_constractions'] = df['text'].apply(
            lambda x: [contractions.fix(word) for word in x.split()])
        print("Step 3/10", end="\r")
        df['text'] = [' '.join(map(str, l)) for l in df['no_constractions']]
        print("Step 4/10", end="\r")
        df['tokenized'] = df['text'].apply(nltk.word_tokenize)
        print("Step 5/10", end="\r")
        df['tokenized'] = df['tokenized'].apply(
            lambda x: [word.lower() for word in x])
        print("Step 6/10", end="\r")
        punc = string.punctuation
        df['tokenized'] = df['tokenized'].apply(
            lambda x: [word for word in x if word not in punc])
        print("Step 7/10", end="\r")
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
        print("Step 8/10", end="\r")
        df['tokenized'] = df['tokenized'].apply(
            lambda x: [word for word in x if word not in stop_words])
        print("Step 9/10", end="\r")
        df['tokenized_str'] = [' '.join(map(str, l)) for l in df['tokenized']]
        print("Step 10/10")
        df_clean = df['tokenized_str']
        # rename tokenized_str to text
        print("Finished preprocessing text...")
        return df_clean
