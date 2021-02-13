

def get_corpus(article_list):
    corpus = []
    for article in article_list:
        corpus.append(article.text)
    return corpus