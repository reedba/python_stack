from book_app import app
from flask import redirect, render_template, request
from book_app.models.book_model import Book
from book_app.models.author_model import Author




@app.route('/')
def authors():
    return rendirect('authors.html')

@app.route('/all_books')
def all_books():
    return render_template('books.html')