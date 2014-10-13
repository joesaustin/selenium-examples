from selenium import webdriver
import unittest

class AgeCalculator():
    def setUp(self):
        browser = webdriver.DesiredCapabilities.CHROME
        self.driver = webdriver.Remote(desired_capabilities=browser)
        self.url = "http://www.calculator.net/age-calculator.html"
        
    def test_age_calculator(self):
        self.driver.get(self.url)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()