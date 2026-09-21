import pytest
@pytest.fixture(scope="class")
def database_class():
        #setup
    print("Connecting to Database")

    yield 
    print("Closing database connection")