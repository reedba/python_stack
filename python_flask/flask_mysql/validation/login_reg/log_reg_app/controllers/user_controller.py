from flask import render_template, redirect, session, request, flask
from log_reg_app import app
from log_reg_app.models.user_model import User

@app.route('/')
def index():
    return render_template('log_reg.html')