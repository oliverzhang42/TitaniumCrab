import json
import numpy as np


class Article():
    def __init__(self, text, category=None, source=None, author=None, title=None, url=None, urlToImage=None, publishedAt=None, viewCount=None):
        self.text = text
        self.metadata = {
            'source': source,
            'category': category,
            'author': author,
            'title': title,
            'url': url,
            'urlToImage': urlToImage,
            'publishedAt': publishedAt,
            'viewCount': viewCount
        }
        self.embedding = None
        self.coordinates = None
        self.summary = None
    
    def to_json(self):
        if type(self.embedding) == np.ndarray:
            embedding = self.embedding.tolist()
        else:
            embedding = self.embedding
        if type(self.coordinates) == np.ndarray:
            coordinates = self.coordinates.tolist()
        else:
            coordinates = self.coordinates
        json_rep = {
            'text': self.text,
            'metadata': self.metadata,
            'embedding': embedding,
            'coordinates': coordinates,
            'summary': self.summary
        }
        return json_rep

    def set_embedding(self, embedding):
        self.embedding = embedding
    
    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def set_summary(self, summary):
        self.summary = summary
