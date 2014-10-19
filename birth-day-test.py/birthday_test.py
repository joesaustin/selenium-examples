from datetime import date
from selenium import webdriver
import calc_functions
import time
import unittest

class AgeCalculator(unittest.TestCase):
    def setUp(self):
        browser = webdriver.DesiredCapabilities.CHROME
        self.driver = webdriver.Remote(desired_capabilities=browser)
        self.url = "http://www.calculator.net/age-calculator.html"
        self.calculator = calc_functions.calFunctions()
        
        
    def test_age_calculator(self):
        self.driver.get(self.url)
        today = date.today()
        
        bday = self.calculator.genereate_random_birthday()
        born_date = date(int(bday["year"]), int(bday["month_num"]), int(bday["day"]))
        self.calculator.update_birth_month(self.driver, bday["month"])
        self.calculator.update_birth_day(self.driver, bday["day"])
        self.calculator.update_birth_year(self.driver, bday["year"])
        self.driver.find_element_by_css_selector("input[src='/img/calculate.png']").click()
        
        web_age = self.calculator.get_results_text(self.driver)       
        calc_age = self.calculator.generate_age_string(born_date, today)
        
        for key, value in web_age.iteritems():
            self.assertEqual(value,calc_age[key] , "web value reads %s, but should be %s" %(value, calc_age[key]))     
        
    def tearDown(self):
        self.driver.quit()

    def select_dropdown(self, driver, value):
        options = driver.find_elements_by_tag_name("option")
        i = len(options)
        x = 0
        while x < i:
            if options[x].text == value:
                options[x].click()
                break
            else:
                x = (x+1) 
        if x == i:
            print "could not find "+value+" in select drop down"

if __name__ == "__main__":
    unittest.main()