from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/potato')
def route():
    return "This is my first Flask app. Yay!"


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/bob')
def bob():
    return "Yo Bob. What's hapening man!!"


@app.route('/method', methods=['GET','POST'])
def method():
    if request.method == 'POST':
        return "You're sent a POST request"
    else:
        return "You're probably using a GET request"
app.run()