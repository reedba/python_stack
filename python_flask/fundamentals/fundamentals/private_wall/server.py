from flask_app import app
from flask import render_template, redirect, session, request, flash


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/register', methods=['POST'])
    def register():
     USer.save(request.form)