# without parametraization
def test_valid_login():
    username = "admin"
    password = "Admin123"

    assert username == "admin"
    assert password == "Admin123"


def test_valid_login1():
    username = "admin1"
    password = "Admin1234"

    assert username == "admin1"
    assert password == "Admin1234"

def test_valid_login2():
    username = "admin2"
    password = "Admin12345"

    assert username == "admin2"
    assert password == "Admin12345"


#__________________________________________________________________________________

'''login test with parametrization'''

import pytest

@pytest.mark.parametrize("username,password",[
    ("admin","Admin123"),
    ("admin1","Admin1234"),
    ("admin2","Admin12345"),
])

def test_login(username,password):
    print(f"username: {username}")
    print(f"password: {password}")

    assert username is not None
    assert password is not None
