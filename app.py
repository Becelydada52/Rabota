import os
from flask import Flask, render_template, request

app = Flask(__name__)

app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')
app.static_folder = os.path.join(os.path.dirname(__file__), 'static')

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/Price')
def price():
    return render_template('Price.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
