from user_registration import UserRegistration

if __name__ == '__main__':
    user_reg = UserRegistration()
    first_name_input = input("Enter First Name:")
    user_reg.first_name_validation(first_name_input)
    last_name_input = input("Enter Last Name:")
    user_reg.last_name_validation(last_name_input)
    email_input = input("Enter Email:")
    user_reg.email_validation(email_input)