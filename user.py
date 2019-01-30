import pyperclip
class User:
    '''
    a class that generates new instances of users
    '''
    pass

    users_array = []

    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_user_details(self):
        '''
        save_contact method saves contact objects into contact_list
        '''
        User.users_array.append(self)

    def delete_user(self):
        '''
        delete_contact method deletes contact objects from contact_list
        '''
        User.users_array.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the contact list
        '''
        return cls.users_array


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

    def save_credential(self):
        '''
        save_contact method saves contact objects into user_array
        '''
        Credential.credential_array.append(self)

    def delete_credential(self):
        '''
        delete_contact method deletes contact objects from user_array
        '''
        Credential.credential_array.remove(self)

    @classmethod
    def display_credential(cls):
        '''
        method that returns the contact list
        '''
        return cls.credential_array


