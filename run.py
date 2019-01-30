#!/usr/bin/env python3.6
from user import User
from user import Credential


def create_user(fname, lname, phone, email):
    '''
    Function to create a new user
    '''
    new_user = User(fname, lname, phone, email)
    return new_user


def create_credential(u_name, p_word, email):
    '''
    Function to create a new user
    '''
    new_credential = Credential(u_name, p_word, email)
    return new_credential


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user_details()
    Credential.save_credential()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def display_user():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()
    return Credential.display_credential()


def main():
    print("Hey There!!! What site do you want to create an account for?")
    site = input()

    print(f"Aah!! So you love {site}? Regarding {site} what would you like to do?")
    print('\n')

    while True:
        print("Allowed Actions :\n ca - create a new user account\n cc - create credentials\n da - display all user accounts\n ex -exit the contact list \n")

        short_code = input().lower()

        if short_code == 'ca':
            print("New User")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Enter username ...")
            user_name = input()

            save_user (create_user(f_name,l_name,p_number,e_address)) # create and save new user account.
            print ('\n')
            print(f" A new user account by {f_name} {l_name} has successfully been created")
            print ('\n')

        elif short_code == 'da':

            if display_user():
                print("Here is a list of all your user accounts")
                print('\n')

                for user in display_user():
                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                print('\n')
            else:
                print('\n')
                print("You don't seem to have any existing accounts")
                print('\n')

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print(" :( Only key in the allowed actions !!")

if __name__ == '__main__':

    main()