from book_app.config.mysqlconnection import connectToMySQL
from book_app.models import book_model



class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        authors = []
        results = connectToMySQL('authors_books_schema').query_db(query)
        for row in results:
            authors.append(cls(row))
        return authors