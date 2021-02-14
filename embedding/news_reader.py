from .article import Article
from newsapi import NewsApiClient

class NewsReader():
    def __init__(self):
        self.categories = ['business', 'entertainment', 'health', 'sports', 'technology']
        self.api = NewsApiClient(api_key='')
        self.page = 0
        results = self.api.get_top_headlines(
            category=self.categories[self.page % 5]
        )
        self.total_results = results['totalResults']
        self.batches = self.total_results // 20
        self.news_batch = results['articles']

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.news_batch) == 0 and self.page == self.batches:
            raise StopIteration
        if len(self.news_batch) == 0:
            self.page += 1
            self.news_batch = self.api.get_top_headlines(
                category=self.categories[self.page % 5]
            )['articles']
        article = self.news_batch.pop()
        if article['description'] != None:
            return Article(
                article['description'],
                category=self.categories[self.page % 5],
                source=article['source'],
                author=article['author'],
                title=article['title'],
                url=article['url'],
                urlToImage=article['urlToImage'],
                publishedAt=article['publishedAt']
            )
        else:
            return Article(
                '',
                category=self.categories[self.page % 5],
                source=article['source'],
                author=article['author'],
                title=article['title'],
                url=article['url'],
                urlToImage=article['urlToImage'],
                publishedAt=article['publishedAt']
            )
