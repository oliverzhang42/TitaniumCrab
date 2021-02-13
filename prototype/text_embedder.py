from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS

class TextEmbedder():
    def __init__(self, alg='tfidf'):
        self.alg = alg
        if alg == 'tfidf':
            self.vectorizer = TfidfVectorizer(stop_words=ENGLISH_STOP_WORDS)

    def fit_transform(self, corpus):
        vectorized_corpus = self.vectorizer.fit_transform(corpus)
        if self.alg == 'tfidf':
            vectorized_corpus = vectorized_corpus.toarray()
        return vectorized_corpus

    def transform(self, data):
        vectorized_data = self.vectorizer.transform(data)
        if self.alg == 'tfidf':
            vectorized_data = vectorized_data.toarray()
        return vectorized_data
