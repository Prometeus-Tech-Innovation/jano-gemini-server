from flask import Flask, request
from jano import make_question

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return '<p>Hello, world!</p>'


@app.route('/api/')
def question_jano():
    question = request.args.get('question')
    res = make_question(question)
    return res
