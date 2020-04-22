from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/about.html')
def html_page():
    return render_template('about.html')
