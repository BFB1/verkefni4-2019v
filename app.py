from flask import Flask, render_template
from requests import get
from json import loads

app = Flask(__name__)


@app.route('/')
def hello_world():
    raw_data = get('https://apis.is/currency/arion').content
    data = loads(raw_data)
    return render_template('home.html', data=data)


if __name__ == '__main__':
    app.run()
