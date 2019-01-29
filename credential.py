import pyperclip
class Credential:
    '''
    a class that generates new credential for users
    '''
    pass

    credential_array = []

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_user_details(self):
        '''
        save_contact method saves contact objects into user_array
        '''
        Credential.credential_array.append(self)

    def delete_user(self):
        '''
        delete_contact method deletes contact objects from user_array
        '''
        User.users_array.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.users_array

