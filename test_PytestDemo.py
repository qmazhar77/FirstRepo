import pytest

@pytest.yield_fixture()
def setup():
    print("Runs before every method")
    yield
    print ("Runs after every method")

def testmethod1(setup):
    print ("This is test method 1")

def testmethod2(setup):
    print ("This is test method 2")

def testmethod3():
    print ("This is test method 3")

#pytest -v -s test_PytestDemo.py