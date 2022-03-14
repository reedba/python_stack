from flask import render_template, redirect, request, session, flash
from log_reg_app import app
from log_reg_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



#This wil render the main page
@app.route('/')
def index():
    return render_template('index.html')


#This route is for registering and saving the user data
@app.route('/user/register',methods=['POST'])
def register():
    #If there is an error message in the request form will return the redirect to the main page
    if not User.validate_register(request.form):
        return redirect('/')
    #This will pass all the data from the form
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])#Remember to hash passwords using bcrypt to ensure password security
    }
    id = User.save(data)# setting the save data to the id variable
    session['user_id'] = id # id is now set to the session

    return redirect('/success') #If all runs this will take you to the success page


#This will run the route to login the already registered user
@app.route('/login',methods=['POST'])
def login():
    #the user variable will be set to the users email in the form 
    user = User.get_by_email(request.form)

    # If there is no user with that login credentials, it will send a flash and redirect to the index page
    if not user:
        flash("Invalid Email")
        return redirect('/')
    # If the password does no match the password in the database will redirect to the main page
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password")
        return redirect('/')
    #must set the session to the user id
    session['user_id'] = user.id
    #upon success you will be taken to the success page
    return redirect('/success')

#Route that takes you to the success page
@app.route('/success')
def success():
    #if the user id is not in session then log the user out
    if 'user_id' not in session:
        return redirect('/logout')
    # set data id equals seesion user id
    data ={
        'id': session['user_id']
    }
    # return the template with the user in sessions data
    return render_template("success.html",user=User.get_by_id(data))

# This will log the user out
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')