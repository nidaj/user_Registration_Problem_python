import pytest


@pytest.mark.parametrize("actual,expected",
                         [("Sanket", True), ("SSD", True), ("sanket", False), ("n2", False), ("SANKET", True)])
def test_first_name(actual, expected, user_register):
    assert user_register.first_name_validation(actual) == expected


@pytest.mark.parametrize("actual,expected",
                         [("Dulange", True), ("D", False), ("dulange", False), ("Dul", True), ("DULANGE", True)])
def test_last_name(actual, expected, user_register):
    assert user_register.first_name_validation(actual) == expected


@pytest.mark.parametrize("actual,expected",
                         [("sanketdulange@gmail.com", True), ("SANKET@gmail.xo", False), ("dulange.gmail.com", False),
                          ("msdhoni7@yahoo.com", True), ("shubhamshinde@google.in", True)])
def test_email(actual, expected, user_register):
    assert user_register.email_validation(actual) == expected
