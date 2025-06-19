from flask import Flask,render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_books():
    response = requests.get("http://books.toscrape.com/")
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all("article", class_="product_pod")
    
    data = []
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        data.append({"title": title, "price": price})
    return data

@app.route("/")
def hello_world():
    news=get_books()
    print(news)
    return render_template("news.html",news=news)

app.run(debug=True)