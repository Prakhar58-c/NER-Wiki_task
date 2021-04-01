from flask import Flask, render_template, Response
from IPython.core.display import HTML
from main import ner

doc = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

if __name__ == '__main__':
    app.run(debug=True, port=8080)