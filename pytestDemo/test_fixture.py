import pytest

# @pytest.fixture
# def database():
#     #setup
#     print("Connecting to Database")

#     yield 
#     print("Closing database connection")

# def test_get_customer(database):
#     print("Get Customer Details")
#     assert True

# def test_create_customer(database):
#     print("Create Customer")
#     assert True



@pytest.mark.usefixtures("database_class")
class Test_DB:
    def test_get_customer(self):
        print("Get Customer Details")
        assert True

    def test_create_customer(self):
        print("Create Customer")
        assert True
