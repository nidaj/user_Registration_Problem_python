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
