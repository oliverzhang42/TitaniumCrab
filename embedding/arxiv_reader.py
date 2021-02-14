import json
import os
from .article import Article


class ArxivReader():
    def __init__(self):
        if not(os.path.exists('embedding/arxiv-metadata-oai-snapshot.json')):
            raise Exception('You must download the ArXiv Metadata before you can parse it!')
        self.papers = open('embedding/arxiv-metadata-oai-snapshot.json')

    def __iter__(self):
        return self

    def __next__(self):
        paper = json.loads(next(self.papers).strip())
        url = "https://arxiv.org/abs/{}".format(paper['id'])
        article = Article(
            paper['abstract'],
            author=paper['authors'],
            title=paper['title'],
            url=url,
            publishedAt=paper['update_date']
        )
        return article
