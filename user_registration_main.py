'''
Author: Nida Jawre
Date of implementation: 12th june 2021

'''




from user_registration import UserRegistration

if __name__ == '__main__':
    user_reg = UserRegistration()
    first_name_input = input("Enter First Name:")
    user_reg.first_name_validation(first_name_input)
    last_name_input = input("Enter Last Name:")
    user_reg.last_name_validation(last_name_input)
    email_input = input("Enter Email:")
    user_reg.email_validation(email_input)
    phone_input = input("Enter Phone:")
    user_reg.phone_number_validation(phone_input)
    password_input = input("Enter Password:")
    user_reg.password_validation(password_input)
