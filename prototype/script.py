import numpy as np
import matplotlib.pyplot as plt
from dataset_reader import DatasetReader
from dim_reducer import DimReducer
from text_embedder import TextEmbedder
from utils import *


# Initialization
reader = DatasetReader()
embedder = TextEmbedder()
reducer = DimReducer(alg='umap')
article_list = []

# Get article_list
num_limit = 100
i = 0
for article in reader:
    article_list.append(article)
    i += 1
    if i == num_limit:
        break
corpus = get_corpus(article_list)

# Get Embeddings
embedding_list = embedder.fit_transform(corpus)
for i, embedding in enumerate(embedding_list):
    article_list[i].set_embedding(embedding)

# Getting Coordinates
embedding_list = np.array(embedding_list)
import pudb; pudb.set_trace()
reduced_data = reducer.fit_transform(embedding_list)
for i, coords in enumerate(reduced_data):
    article_list[i].set_coordinates(coords)

#'''
# Display (Not necessary for the backend!)
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
plt.legend()
plt.show()
#'''