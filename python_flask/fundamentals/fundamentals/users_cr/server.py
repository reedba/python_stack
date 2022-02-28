

from flask import Flask, render_template, request, redirect

from users import Users

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = Users.getall()
    return render_template('users.html', users = users)

if __name__=="__name__":
    app.run(debug=True)