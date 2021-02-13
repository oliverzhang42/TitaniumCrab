import numpy as np
import umap
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

class DimReducer():
    def __init__(self, alg='umap'):
        self.scalar = StandardScaler()
        if alg == 'umap':
            self.reducer = umap.UMAP()
        elif alg == 'tsne':
            self.reducer = TSNE()

    def fit(self, data):
        # scaled_data = self.scalar.fit_transform(data)
        reduced_data = self.reducer.fit_transform(data)
        return reduced_data
    
    def transform(self, data):
        if len(data.shape) == 1:
            data = np.array([data])
        return self.reducer.transform(data)
