from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def route():
    return "We are on route!"


@app.route('/hello')
def hello():
    return "Hello!"


@app.route('/welcome')
def welcome():
    return "Welcome!"


@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return "You're sent a POST request"
    else:
        return "You're probably using a GET request"
app.run()