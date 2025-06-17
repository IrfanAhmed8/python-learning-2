from flask import Flask
from newspaper import Article
import feedparser

 
def get_news_articles(max_articles=3):
    feed_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries[:max_articles]:
        url = entry.link
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            articles.append({
                "title": article.title,
                "summary": article.summary,
                "Image":article.images,
                "link": url
            })
        except:
            continue

    return articles
