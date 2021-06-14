import pytest


@pytest.mark.parametrize("actual,expected",
                         [("Nida", True), ("NAJ", True), ("nida", False), ("n2", False), ("NIDA", True)])
def test_first_name(actual, expected, user_register):
    assert user_register.first_name_validation(actual) == expected
