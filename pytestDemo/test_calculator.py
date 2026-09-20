import pytest

@pytest.mark.smoke
def test_add():
    a= 10
    b = 5
    result = a+b

    assert result == 15

@pytest.mark.regression
def test_sub():
    a= 10
    b = 5
    result = a-b

    assert result == 5

@pytest.mark.sanity
def test_mul():
    a= 10
    b = 5
    result = a*b

    assert result == 50

@pytest.mark.skip (reason= "its under development")
def test_div():
    a= 10
    b = 5
    result = a/b

    assert result == 2
