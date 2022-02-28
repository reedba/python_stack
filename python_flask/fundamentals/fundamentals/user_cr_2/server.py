from flask import Flask, render_template, request, redirect

from users import Users

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = Users.getall()
    return render_template('users.html', users=users)

@app.route('/users/new')
def new_user():
    return render_template('new_users.html')

@app.route('/add_user', methods = ['POST'])
def create():
    Users.save(request.form)
    return redirect('/users')

if __name__=="__main__":
    app.run(debug=True)