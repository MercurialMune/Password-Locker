import unittest
import pyperclip
from user import User
from credential import Credential


class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("user_name","password","email@ms.com") # create credential object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_array = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_name,"user_name")
        self.assertEqual(self.new_credential.password,"password")
        self.assertEqual(self.new_credential.email,"email@ms.com")

    def test_save_cred(self):
        '''
        test_save_user test case to test if the user object is saved into
         the users array
        '''
        self.new_credential.save_credential()  # saving the new credential
        self.assertEqual(len(Credential.credential_array), 1)

    def test_delete_user(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_credential.save_credential()
        test_user = User("Test", "user", "0712345678", "test@user.com")  # new user
        test_user.save_user_details()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.users_array), 1)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(), User.users_array)


if __name__ == '__main__':
    unittest.main()
