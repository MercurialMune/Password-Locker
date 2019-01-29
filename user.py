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

    def display_users(self):


