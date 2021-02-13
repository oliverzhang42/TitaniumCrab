import numpy as np
import matplotlib.pyplot as plt
from dataset_reader import DatasetReader
from dim_reducer import DimReducer
from text_embedder import TextEmbedder


# Initialization
reader = DatasetReader()
embedder = TextEmbedder()
reducer = DimReducer()
article_list = []
embedding_list = []

# Getting Embeddings
num_limit = 1000
i = 0
for article in reader:
    embedding = embedder.to_embedding(article.text)
    embedding_list.append(embedding)
    article.set_embedding(embedding)
    article_list.append(article)
    i += 1
    if i == num_limit:
        break

# Getting Coordinates
embedding_list = np.array(embedding_list)
reduced_data = reducer.fit(embedding_list)
for i, coords in enumerate(reduced_data):
    article_list[i].set_coordinates(coords)

# Display
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