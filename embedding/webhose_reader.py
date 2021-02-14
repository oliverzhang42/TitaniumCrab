from .article import Article
import webhoseio 


class WebhoseReader():
    def __init__(self):
        webhoseio.config(token='')
        self.params = {
            'q': 'site.type:news',
            'from': 0
        }
        results = webhoseio.query('nseFilter', self.params)
        self.total_results = results['totalResults']
        self.page = 0
        self.batches = max(self.total_results // 10, 10)
        self.news_batch = results['docs']

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.news_batch) == 0 and self.page == self.batches:
            raise StopIteration
        if len(self.news_batch) == 0:
            self.page += 1
            self.params['from'] = self.page * 10
            results = webhoseio.query('nseFilter', self.params)
            self.news_batch = results['docs']
        news_instance = self.news_batch.pop()
        article_raw = news_instance['article']
        site_raw = news_instance['site']
        for i in range(len(article_raw['categories'])):
            category_name = article_raw['categories'][i]['name'].lower()
            if 'politics' in category_name or 'election' in category_name:
                category = 'politics'
                break
            elif 'business' in category_name or 'economics' in category_name or 'money' in category_name:
                category = 'business'
                break
            elif 'entertainment' in category_name or 'culture' in category_name or 'movies' in category_name or 'games' in category_name:
                category = 'entertaiment'
                break
            elif 'health' in category_name or 'covid' in category_name or 'medicine' in category_name:
                category = 'health'
                break
            elif 'technology' in category_name or 'science' in category_name or 'electronics' in category_name:
                category = 'technology'
                break
            else:
                category = 'uncategorized'
        article = Article(
            article_raw['text'],
            category=category,
            source=site_raw['name'],
            author=article_raw['author'],
            title=article_raw['title'],
            url=article_raw['url'],
            urlToImage=article_raw['media']['main_image'],
            publishedAt=article_raw['published'],
            viewCount=article_raw['social']['facebook']['likes']
        )
        article.set_summary(article_raw['summary'])
        return article
