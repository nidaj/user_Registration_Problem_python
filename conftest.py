import pytest


# from user_registration import UserRegistration


@pytest.fixture
def user_register():
    from user_registration import UserRegistration
    return UserRegistration()

