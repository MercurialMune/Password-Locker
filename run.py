#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random


def create_user(fname, lname, phone, email):
    """
    Function to create a new user
    """
    new_user = User(fname, lname, phone, email)
    return new_user


def create_credential(uname, pword, email):
    """
    Function to create new user credentials
    """
    new_credential = Credential(uname, pword, email)
    return new_credential


def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()


def save_cred(credential):
    """
    Function to save user credentials
    """
    credential.save_credential()


def del_user(user):
    """
    Function to delete a user
    """
    user.delete_user()


def del_cred(credential):
    """
    Function to delete all users credentials
    """
    credential.delete_credential()


def display_user():
    """
    Function that returns saved users
    """
    return User.display_users()


def display_cred():
    """
    function that returns saved user credentials
    """
    return Credential.display_credential()


def main():

    print("Welcome to your Password Locker, choose your path from the list of allowed actions")

    while True:
        print("Allowed Actions: \n ad - create a new user account with a user-defined password\n ag - create a new user account with a auto-generated password\n da - display all user accounts \n ex -exit the contact list \n")

        short_code = input().lower()

        if short_code == 'ad':
            print("New User")
            print("-"*10)
            print("Hey There!!! What site do you want to create an account for?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Enter username ...")
            user_name = input()

            print("Enter Password ...")
            pword = input()

            save_user(create_user(f_name, l_name, p_number, e_address))  # create and save new user account.
            save_cred(create_credential(user_name, pword, e_address))  # create and save a credential listing for the above user
            print('\n')
            print(f" A new {site} account by {f_name} {l_name} has successfully been created")
            print(f" The username is {user_name} and the password is {pword}")
            print('\n')

        elif short_code == 'ag':
            print("New User")
            print("-" * 10)
            print("Hey There!!! What site do you want to create an account for?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            f_name = input()

            print("Last name ...", )
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Enter username ... Hint: a secure password will be generated for you...")
            user_name = input()

            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            pword = "".join(random.sample(s, 8))

            save_user(create_user(f_name,l_name,p_number,e_address))  # create and save new user account.
            save_cred(create_credential(user_name, pword, e_address))  # create and save a credential listing for the above user
            print('\n')
            print(f" A new {site} account by {f_name} {l_name} has successfully been created")
            print(f" The username is {user_name} and the password is {pword}")
            print('\n')

        elif short_code == 'da':

            if display_user():
                print("Here is a list of all your user accounts")
                print('\n')

                for user in display_user():
                    print(f"{user.first_name} {user.last_name} has an account for {site}")

                print('\n')
            else:
                print('\n')
                print("You don't seem to have any existing accounts")
                print('\n')

        elif short_code == "ex":
            print(":/ See you soon then...")
            break
        else:
            print(" :( Only key in the allowed actions !!")


if __name__ == '__main__':
    main()
