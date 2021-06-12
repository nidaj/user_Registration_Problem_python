import pytest

from user_registration import UserRegistration


@pytest.fixture
def user_register():
    return UserRegistration()

