from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)
app.config['SECRET_KEY'] = '629f3b11153de13c74b7a06a66f13bd6'

# Init
newsapi = NewsApiClient(api_key='9319a21a7472491897d5efd548f290dc')

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/news-india-latest')
def news_india():
    top_headlines = newsapi.get_top_headlines(language='en', country='in')
    li = [news['title'] for news in top_headlines['articles']]
    url = [news['url'] for news in top_headlines['articles']]
    dict = {news: url for news, url in zip(li, url)}
    final_india = [dict]

    return render_template("india.html", final_india=final_india)


@app.route('/news-america-latest')
def news_america():
    top_headlines_america = newsapi.get_top_headlines(language='en', country='us')
    li_america = [news['title'] for news in top_headlines_america['articles']]
    url_america = [news['url'] for news in top_headlines_america['articles']]
    dict_america = {news: url for news, url in zip(li_america, url_america)}
    final_america = [dict_america]

    return render_template("america.html", final_america=final_america)


@app.route('/news-australia-latest')
def news_australia():
    top_headlines_australia = newsapi.get_top_headlines(language='en', country='au')
    li_australia = [news['title'] for news in top_headlines_australia['articles']]
    url_australia = [news['url'] for news in top_headlines_australia['articles']]
    dict_australia = {news: url for news, url in zip(li_australia, url_australia)}
    final_australia = [dict_australia]

    return render_template("australia.html", final_australia=final_australia)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('search')
    query_results = newsapi.get_top_headlines(q=query, language='en')
    li_query = [news['title'] for news in query_results['articles']]
    url_query = [news['url'] for news in query_results['articles']]
    dict_query = {news: url for news, url in zip(li_query, url_query)}
    final_query = [dict_query]

    print(query_results)
    return render_template("search.html", final_query=final_query)


@app.route('/news-world-latest')
def news_world():
    all_articles = newsapi.get_everything(sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com',
                                          language='en',
                                          page=5)

    li2 = [news['title'] for news in all_articles['articles']]
    url2 = [news['url'] for news in all_articles['articles']]
    dict2 = {news: url for news, url in zip(li2, url2)}
    final_world = [dict2]

    return render_template("world.html", final_world=final_world)

@app.errorhandler(500)
def too_many_requests(e):
    return render_template("500.html"), 500


@app.errorhandler(404)
def too_many_requests(e):
    return render_template("404.html",), 404

if __name__ == '__main__':
    app.run(debug=False)
