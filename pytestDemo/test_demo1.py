def test_demo001():
    A = "Vinoth"
    assert A == "Babu" ,  "This is worng Name"

def test_sample1():
    print("sample_test1")

def test_sample2():
    print("sample_test1")

def test_card():
    print("sample_test1")


'''
pytest
pytest -v
pytest -v -s
pytest test_demo1.py -v -s
pytest -k card -v -s
pytest -m regression -v -s


@pytest.mark.skip (reason= "its under development") -->  pytest test_calculator.py -v -s

'''