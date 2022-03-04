from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/search/')
def search():
    return render_template("search.html")


@app.route('/result/')
def result():
    return render_template("result.html")


@app.route('/request/')
def request():
    return 'request page'


if __name__ == '__main__':
    app.run(debug=True)
