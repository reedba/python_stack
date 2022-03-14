from crypt import methods
from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from private_wall_2_app import app
from private_wall_2_app.models.user_model import User
from private_wall_2_app.models.messages_model import Message

@app.route('/post_message', methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "sender_id":  request.form['sender_id'],
        "reciever_id" : request.form['reciever_id'],
        "message": request.form['message']
    }
    Message.save(data)
    return redirect('/success')

@app.route('/delete/message/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    Message.destroy(data)
    return redirect('/success')