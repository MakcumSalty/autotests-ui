import pytest


def test_user_login():
    print("Hello World!")


class TestUserLogin:
    def test_1(self):
        ...

    def test_2(self):
        ...


def test_greeting():
    greeting = "Hello, world!"
    assert greeting == "Hi, world!"

def test_in_list():
    assert 3 in [1, 2, 3, 4]

def test_boolean():
    is_authenticated = True
    assert is_authenticated

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_sum():
    assert 1 + 1 == 3, "Сумма 1 и 1 должна быть 2!"