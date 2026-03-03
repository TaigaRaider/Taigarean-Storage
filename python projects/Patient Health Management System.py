class  User:
    def __init__(self, username, account_state):
        self.username= username
        self.account_state= account_state

    def login(self):
        pass
    def logout(self):
        pass
    def __delete__(self, instance):
        pass

class Doctor(User):
    pass
class Patient(User):
    pass
class Administrator(User):
    pass