import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

categories = []
corpus = []
num_articles = 1000

# Vectorize
with open('bbc-text.csv', 'r') as f:
    i = 0
    reader = csv.reader(f)
    first_line = True
    for line in reader:
        if first_line:
            first_line = False
            continue
        category, article_text = line
        categories.append(category)
        corpus.append(article_text)
        i += 1
        if i == num_articles:
            break

vectorizer = TfidfVectorizer(stop_words=text.ENGLISH_STOP_WORDS)
X = vectorizer.fit_transform(corpus)

# Umap Down
import umap
reducer = umap.UMAP()

#reducer = TSNE()
#scalar = StandardScaler() ACTUALLY TERRIBLE LMAO
#scaled_data = scalar.fit_transform(X.toarray())
reduced_data = reducer.fit_transform(X.toarray())

# TSNE


#from sklearn.decomposition import TruncatedSVD
#svd = TruncatedSVD()
#reduced_data = svd.fit_transform(X)

# Display
category_dict = {}
for category, coords in zip(categories, reduced_data):
    if category in category_dict:
        category_dict[category].append(coords)
    else:
        category_dict[category] = [coords]

for category in category_dict:
    coords_list = np.array(category_dict[category])
    plt.scatter(coords_list[:, 0], coords_list[:, 1], label=category)
plt.legend()
plt.show()