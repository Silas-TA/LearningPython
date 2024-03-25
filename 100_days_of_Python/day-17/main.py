class User:
    def __init__(self, name, surname, user_id):
        self.name = name
        self.surname = surname
        self.id = user_id
        self.email = name+surname+'@company.com'


user = User('Angela', 'Jones', 5)

print(user.id)
