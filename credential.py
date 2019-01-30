# credential_array = []


class Credential:
    """
    a class that generates new credential for users
    """
    pass
    credential_array = []

    def __init__(self, user_name, password, email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self):
        """
        save_contact method saves contact objects into credential_array
        """
        Credential.credential_array.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the contact list
        """
        return cls.credential_array


