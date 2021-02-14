import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import TSNE
from umap import UMAP


class DimReducer():
    def __init__(self, alg='umap'):
        if alg == 'umap':
            self.reducer = UMAP()
        elif alg == 'tsne':
            self.reducer = TSNE()
        elif alg == 'svd':
            self.reducer = TruncatedSVD()

    def fit_transform(self, data):
        return self.reducer.fit_transform(data)
        
    def transform(self, data):
        if len(data.shape) == 1:
            data = np.array([data])
        return self.reducer.transform(data)
