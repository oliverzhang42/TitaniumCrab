import numpy as np
import openai
import requests
import json
from .article import Article
openai.api_key = ''


def get_corpus(article_list):
    corpus = []
    for article in article_list:
        corpus.append(article.text)
    return corpus


def get_keywords(article_text):
    suffix = '\nKeywords:\n'
    response = openai.Completion.create(
        engine="davinci",
        prompt=article_text + suffix,
        temperature=0.3,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.8,
        presence_penalty=0,
        stop=['\n']
    )
    return response['choices'][0]['text']


def article_list_from_json(path, objects=False):
    with open(path, 'r') as f:
        json_list = json.load(f)
    if not(objects):
        return json_list
    article_list = []
    for d in json_list:
        article = Article(
            d['text'],
            source=d['metadata']['source'],
            author=d['metadata']['author'],
            title=d['metadata']['title'],
            url=d['metadata']['url'],
            urlToImage=d['metadata']['urlToImage'],
            publishedAt=d['metadata']['publishedAt'],
            viewCount=d['metadata']['viewCount']
        )
        article.set_embedding(d['embedding'])
        article.set_coordinates(d['coordinates'])    
        article.set_summary(d['summary'])
        article_list.append(article)
    return article_list


def to_json(article_list, path):
    with open(path, 'w') as f:
        json_reps = []
        for article in article_list:
            json_reps.append(article.to_json())
        json.dump(json_reps, f)
    return json_reps


def get_category(article_text):
    prefix = 'Article: '
    suffix = '\nCategory: '
    response = openai.Completion.create(
        engine="curie-instruct-beta",
        prompt=prefix + article_text + suffix,
        temperature=0.3,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['\n']
    )
    return response['choices'][0]['text']


def get_category_search(article_text):
    url = "https://api.openai.com/v1/engines/davinci/search"
    categories = ["Business", "Politics", "Entertainment", "Sports", "Tech", "Misc"]
    for c in categories:            
        data = {
            "documents": [
                article_text
            ],
            "query": c
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(openai.api_key)
        }
        results = requests.post(
            url,
            data=data,
            headers=headers
        )
        print(results)
        print(results.json())
        resp = results.json()['data']
        scores = [
            resp[0]['score'], 
            resp[1]['score'],
            resp[2]['score'],
            resp[3]['score'],
            resp[4]['score']
        ]
        category = np.argmax(scores)
    return categories[category]


    
