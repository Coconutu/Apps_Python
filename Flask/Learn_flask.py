from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Hello World!"

@app.route('/hello')
def welcome1():
    return "Hello World!"

@app.route('/welcome')
def welcome2():
    return "Hello World!"
app.run()
