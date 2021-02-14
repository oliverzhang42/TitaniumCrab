import numpy as np
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from embedding.arxiv_reader import ArxivReader
from embedding.bbc_reader import BBCReader
from embedding.dim_reducer import DimReducer
from embedding.news_reader import NewsReader
from embedding.text_embedder import TextEmbedder
from embedding.webhose_reader import WebhoseReader
from embedding.summerizer import get_summary
from embedding.utils import get_corpus, get_category, to_json


def embeds(dataset='bbc', num_articles=10, embedder='tfidf', dim_reducer='tsne', plot_fig=True):
    # Initialization
    if dataset == 'bbc':
        reader = BBCReader()
    elif dataset == 'newsapi':
        reader = NewsReader()
    elif dataset == 'webhose':
        reader = WebhoseReader()
    elif dataset == 'arxiv':
        reader = ArxivReader()
    else:
        raise NotImplementedError
    embedder = TextEmbedder(alg=embedder)
    reducer = DimReducer(alg=dim_reducer)
    article_list = []

    # Get article_list
    i = 0
    for article in reader:
        # Get Summary
        if dataset == 'newsapi':
            article.set_summary(article.text)
        elif dataset == 'webhose' or dataset == 'arxiv':
            sentences = article.text.split('.') 
            summary = sentences[0] + '.'
            article.set_summary(summary)
        else:
            article.set_summary(get_summary(article.text))
        # Get Category
        #if dataset in ['newsapi' or 'arxiv']:
        #    category = get_category(article.text)
        #    article.metadata['category'] = category.strip()
        article_list.append(article)
        i += 1
        if i == num_articles:
            break
    
    # Get Embeddings
    corpus = get_corpus(article_list)
    embedding_list = embedder.fit_transform(corpus)
    for i, embedding in enumerate(embedding_list):
        article_list[i].set_embedding(embedding)

    # Getting Coordinates
    embedding_list = np.array(embedding_list)
    reduced_data = reducer.fit_transform(embedding_list)
    for i, coords in enumerate(reduced_data):
        article_list[i].set_coordinates(coords)

    # Display
    if plot_fig:
        categories = {}
        for article in article_list:
            category = article.metadata['category']
            if category in categories:
                categories[category].append(article.coordinates)
            else:
                categories[category] = [article.coordinates]

        for category in categories:
            coords_list = np.array(categories[category])
            plt.scatter(coords_list[:, 0], coords_list[:, 1], label=category)

        # save figure
        plt.legend()
        plt.savefig('static/test.png')

    return article_list

if __name__ == '__main__':
    embeds(dataset='bbc')