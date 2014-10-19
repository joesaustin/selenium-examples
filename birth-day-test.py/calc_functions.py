import calendar
from datetime import date
from dateutil import relativedelta as rdelta
from random import randrange
import time

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
    
    def genereate_random_birthday(self):
        month = randrange(0,len(self.months))
        month_text = self.months[month]
        day = randrange(1,int(self.days_in_month[month_text][0]))
        year = randrange(1800,2015)
        birthday = {"month":month_text, "day":str(day), "year": str(year), "month_num":(self.months.index(month_text)+1)}
        return birthday
        
    def update_birth_month(self, driver, month):
        months = driver.find_element_by_id("today_Month_ID")
        months.click()
        self.select_dropdown(months, month)
        
    def update_birth_day(self, driver, day):
        days = driver.find_element_by_id("today_Day_ID")
        days.click()
        self.select_dropdown(days, day)
        
    def update_birth_year(self, driver, year):
        driver.find_element_by_id("today_Year_ID").clear()
        driver.find_element_by_id("today_Year_ID").send_keys(year)
        
    def get_results_text(self,driver):
        content = driver.find_element_by_id("content")
        text = content.text
        start = text.index("Age:")
        end = text.index("Date of Birth")
        results = text[start:end]
        return results
    
    def calculate_age(self, born, given_date):
        age={}
        measure = self.age_measurements(given_date, born)
        relative = self.relative_age(given_date, born)
        
        for key, value in measure.iteritems():
            age[key]= str(value)
        
        for key, value in relative.iteritems():
            age[key] =str(value)
        return age
        
    def age_measurements(self, given_date, born):
        total_days = (given_date - born)
        hours = (int(total_days.days)*24)
        weeks = (int(total_days.days)/7)
        remain_days = (total_days.days - (weeks * 7))
        minutes = (hours*60)
        seconds = (minutes*60)
        results = {"total_days":format(total_days.days, ",d"),
                   "hours":format(hours, ",d"),
                   "weeks":weeks,
                   "minutes":format(minutes, ",d"),
                   "remaining_days":remain_days,
                   "seconds":format(seconds, ",d")}
        return results
        
    def relative_age(self, given_date, born):
        rd = rdelta.relativedelta(given_date,born)
        years = rd.years
        months = rd.months
        days = rd.days
        total_months =(months + (years*12))
        rd_age = {"years":years,
                  "rd_months":months,
                  "rd_days":days,
                  "total_months":total_months} 
        return rd_age

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