import time
import calendar

class calFunctions():
    def __init__(self):
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.days_in_month = {"Jan":["31"],
                        "Feb":["28", "29"],
                        "Mar":["31"],
                        "Apr":["30"],
                        "May":["31"],
                        "Jun":["30"],
                        "Jul":["31"],
                        "Aug":["31"],
                        "Sep":["30"],
                        "Oct":["31"],
                        "Nov":["30"],
                        "Dec":["31"]}
    
    def is_leap(self, year):
        status = calendar.isleap(year)
        return status
    
    def update_birth_month(self, driver, month):
        months = driver.find_element_by_id("today_Month_ID")
        months.click()
        months.find_element_by_css_selector("option[value='%s']" %month).click()
        
    def update_birth_day(self, driver, day):
        days = driver.find_element_by_id("today_Day_ID")
        days.click()
        self.select_dropdown(days, day)
        
    def update_birth_year(self, driver, year):
        driver.find_element_by_id("today_Year_ID").clear()
        driver.find_element_by_id("today_Year_ID").send_keys(year)
        
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