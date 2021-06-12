import pytest


@pytest.mark.parametrize("actual,expected",
                         [("Sanket", True), ("SSD", True), ("sanket", False), ("n2", False), ("SANKET", True)])
def test_first_name(actual, expected, user_register):
    assert user_register.first_name_validation(actual) == expected
