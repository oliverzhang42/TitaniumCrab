class Article():
    def __init__(self, text, category=None, author=None, title=None):
        self.text = text
        self.metadata = {
            'category': category,
            'author': author,
            'title': title
        }
        self.embedding = None
        self.coordinates = None

    def set_embedding(self, embedding):
        self.embedding = embedding
    
    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
