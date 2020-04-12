from unittest import TextTestRunner
from selenium import webdriver
from PytestDemo.locators.MercurySignOnLocators import MercurySignOnLocators
from PytestDemo.TestBase.EnvironmentSetup import EnvironmentSetup
from PytestDemo.Scripts.test_MercuryTours_SignOn import MercuryTours_SignOn
from PytestDemo.TestUtility.test_ScreenShot import SS
import testtools as testtools

def TestLoader():
    pass


class TestSuite(object):
    pass


if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(MercuryTours_SignOn)
    ))

# run test sequnitiallly using simple text test runner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

