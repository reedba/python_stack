from mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getall(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_cr_db').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users