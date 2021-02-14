# import statements
from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import io
import os
import json
from build import build
from embedding.utils import article_list_from_json, to_json

# embedding script
import script

# initializes flask app
app = Flask(__name__, template_folder='templates', static_folder='static')

# main app route for all of our code
@app.route('/')
def home():
   # pull article_list representation
   article_list = article_list_from_json('webhose.json', objects=False)

   # we have to pass in through render then pass this into script.js
   return render_template('index.html', articles = json.dumps(article_list))


@app.route('/plot')
def plot():
   article_list = article_list_from_json('webhose.json', objects=False)
   return render_template('plot.html', articles=json.dumps(article_list))


# runs the app
if __name__ == '__main__':
   if not os.path.exists('bbc.json') or not os.path.exists('newsapi.json'):
      build()
   app.run(debug = True)