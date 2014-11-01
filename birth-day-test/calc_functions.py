import calendar, time
from datetime import date
from dateutil import relativedelta as rdelta
from random import randrange

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
    
    def update_birthday(self, driver, bday):
        self.update_birth_month(driver, bday["month"])
        self.update_birth_day(driver, bday["day"])
        self.update_birth_year(driver, bday["year"])
        
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
        results = (results.split("\n"))
        web_ages = {"years_months_days":str(results[1]),
                "months_days":str(results[2]),
                "weeks_days":str(results[3]),
                "total_days":str(results[4]),
                "total_hours":str(results[5]),
                "total_minutes":str(results[6]),
                "total_seconds":str(results[7])}
        return web_ages
    
    def generate_age_string(self, born, given_date):
        age = self.calculate_age(born, given_date)
        age_str={"years_months_days":"%s years %s months %s days" %(age["years"], age["rd_months"], age["rd_days"]),
                 "months_days":"or %s months %s days" %(age["total_months"], age["rd_days"]),
                 "weeks_days":"or %s weeks %s days" %(age["weeks"], age["remaining_days"]),
                 "total_days":"or %s days" %(age["total_days"]),
                 "total_hours":"or %s hours" %(age["hours"]),
                 "total_minutes":"or %s minutes" %(age["minutes"]),
                 "total_seconds":"or %s seconds" %(age["seconds"])}
        return age_str
        
    
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
