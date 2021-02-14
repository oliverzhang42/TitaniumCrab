import csv
from .article import Article


class BBCReader():
    def __init__(self, path='embedding/bbc-text.csv'):
        f = open(path, 'r')
        self.reader = csv.reader(f)
        next(self.reader) # Throwing away the first line.

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self.reader)
        if row == '':
            raise StopIteration
        category, text = row
        return Article(text, category=category)




