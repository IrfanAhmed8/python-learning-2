from flask import Flask,render_template
from quoteGenerator import Generator
app = Flask(__name__)

@app.route("/")


def hello_world():
  
    return render_template('home.html',quote=Generator())

app.run(debug=True)