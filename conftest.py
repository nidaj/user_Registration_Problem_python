import pytest




@pytest.fixture
def user_register():
    from user_registration import UserRegistration
    return UserRegistration()
