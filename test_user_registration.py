import pytest


@pytest.mark.parametrize("actual,expected",
                         [("Nida", True), ("NAJ", True), ("nida", False), ("n2", False), ("NIDA", True)])
def test_first_name(actual, expected, user_register):
    assert user_register.first_name_validation(actual) == expected


@pytest.mark.parametrize("actual,expected",
                         [("Jawre", True), ("J", False), ("jawre", False), ("Jaw", True), ("JAWRE", True)])
def test_last_name(actual, expected, user_register):
    assert user_register.first_name_validation(actual) == expected


@pytest.mark.parametrize("actual,expected",
                         [("nida.jawre@gmail.com", True), ("NIDA@gmail.xo", False), ("nida.gmail.com", False),
                          ("nidajawre@yahoo.com", True), ("nidajawre@google.in", True)])
def test_email(actual, expected, user_register):
    assert user_register.email_validation(actual) == expected



@pytest.mark.parametrize("actual,expected", [("91 9422484996", True), ("919422484996", False), ("9422484996", False),
                                             ("91 7020665302", True), ("91 9421359551", True)])
def test_phone_number(actual, expected, user_register):
    assert user_register.phone_number_validation(actual) == expected



@pytest.mark.parametrize("actual,expected", [("Nidajawre@123", True), ("snidaJ%123", True), ("9768nidaJ&", True)])
def test_password(actual, expected, user_register):
    assert user_register.password_validation(actual) == expected
