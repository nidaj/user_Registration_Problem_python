import re

FIRST_NAME_PATTERN = "^[A-Z][a-zA-Z]{2,}$"
LAST_NAME_PATTERN = "^[A-Z][a-zA-Z]{2,}$"


class UserRegistration:

    def __init__(self):
        pass

    def first_name_validation(self, first_name_input):
        if re.match(FIRST_NAME_PATTERN, first_name_input):
            print("Valid first name")
            return True
        else:
            print("Invalid first name ")
            return False

    def last_name_validation(self, last_name_input):
        if re.match(LAST_NAME_PATTERN, last_name_input):
            print("Valid Last name")
            return True
        else:
            print("Invalid Last Name ")
            return False