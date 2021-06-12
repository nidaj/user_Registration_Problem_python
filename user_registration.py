import re

FIRST_NAME_PATTERN = "^[A-Z][a-zA-Z]{2,}$"
LAST_NAME_PATTERN = "^[A-Z][a-zA-Z]{2,}$"
EMAIL_PATTERN = "^[a-zA-z]{3}[0-9a-zA-Z\\.\\_\\-\\+]*@[a-z]*\\.(co|com.au|in|net|in|com.com|com|)$"
PHONE_NUMBER_PATTERN = "^[0-9]{2} [0-9]{10}$"

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

    def email_validation(self, email_input):
        if re.match(EMAIL_PATTERN, email_input):
            print("Valid Email")
            return True
        else:
            print("Invalid Email ")
            return False


    def phone_number_validation(self, phone_number_input):
        if re.match(PHONE_NUMBER_PATTERN, phone_number_input):
            print("Valid Phone")
            return True
        else:
            print("Invalid Phone ")
            return False
