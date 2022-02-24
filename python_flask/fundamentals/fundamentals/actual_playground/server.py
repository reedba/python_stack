from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/playground/')
def index():
    return render_template('index.html', num = 3, color = 'lightblue')

@app.route('/playground/<int:num>')
def add_box(num):
    return render_template('index.html', num = num, color = 'lightblue')

@app.route('/playground/<int:num>/<color>')
def add_color(num, color):
    return render_template('index.html', num = num, color = color)





if __name__ == "__main__":
    app.run(debug = True)