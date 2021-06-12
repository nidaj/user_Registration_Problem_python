from user_registration import UserRegistration

if __name__ == '__main__':
    user_reg = UserRegistration()
    first_name_input = input("Enter First Name:")
    user_reg.first_name_validation(first_name_input)