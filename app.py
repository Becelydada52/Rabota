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

@app.route('/price1')
def price1():
    return render_template('price1.html')

@app.route('/price2')
def price2():
    return render_template('price2.html')

@app.route('/price3')
def price3():
    return render_template('price3.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
