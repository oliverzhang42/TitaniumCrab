import script
from embedding.utils import to_json

def build():
    article_list = script.embeds(dataset='webhose', num_articles=10, dim_reducer='umap', plot_fig=False)
    to_json(article_list, 'webhose.json')
    article_list = script.embeds(dataset='bbc', num_articles=10, dim_reducer='umap', plot_fig=False)
    to_json(article_list, 'bbc.json')
    article_list = script.embeds(dataset='newsapi', num_articles=10, dim_reducer='umap', plot_fig=False)
    to_json(article_list, 'newsapi.json')
    article_list = script.embeds(dataset='arxiv', num_articles=10, dim_reducer='umap', plot_fig=False)
    to_json(article_list, 'arxiv.json')

# run the build
if __name__ == '__main__':
    build()