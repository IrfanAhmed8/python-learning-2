from flask import Flask,render_template,jsonify,request
from quoteGenerator import Generator
from Newspaper import get_news_articles
from assistant import speak,command_process,listen

app = Flask(__name__)

@app.route("/")
def hello_world():
  
    return render_template('home.html',quote=Generator(),newsdata=get_news_articles())

@app.route('/assistant',methods=['POST'])
def assistant():
    command=listen()
    command_process(command)
    return jsonify({"message": "Command processed: " + command})




app.run(debug=True)