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

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit_user.html', user = Users.get_one(data))

@app.route('/update', methods = ['POST'])
def update():
    Users.update(request.form)
    return redirect('/users')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    Users.delete(data)
    return redirect('/users')

@app.route('/show/<int:id>')
def show(id):
    data = {
        'id':id
    }
    return render_template('single_user.html', user = Users.get_one(data))




if __name__=="__main__":
    app.run(debug=True)