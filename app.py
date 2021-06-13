import json
from backend import load_json, update_pdf
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    resume = load_json('static/resume.json')
    return render_template('home.html', resume=resume)


@app.route('/download')
def download():
    update_pdf()
    return render_template('download.html')


if __name__ == '__main__':
    app.run()
