import os
import time
import unittest
from selenium import webdriver

class TestNYTNav(unittest.TestCase):
    def setUp(self):
        browser = webdriver.DesiredCapabilities.CHROME
        self.driver = webdriver.Remote(desired_capabilities=browser)
        self.path = os.getcwd()+"/nyt_errors/"+time.strftime("%m-%d-%Y")
        self.verificationErrors = []
        
    def test_mini_nav(self):
        self.driver.get("http://www.nytimes.com")
        nav = self.driver.find_element_by_id("mini-navigation")
        a_tags = nav.find_elements_by_tag_name("a")
        links =[]
        
        for i in range(0,len(a_tags)):
            if a_tags[i].text != "": #don't append empty tags
                links.append(a_tags[i].text)
                
        for i in range(0,len(links)):
            if links[i] != "ALL": #clicking all displays a dropdown nav on the left.
                nav = self.driver.find_element_by_id("mini-navigation")
                nav.find_element_by_link_text(links[i]).click()
                
                try:
                    self.driver.find_element_by_css_selector("a[id='nyt-button-sub']")
                except Exception:
                    print "The subscription button is missing from the "+links[i]+" page."
                    jpg = links[i]+"_"+time.strftime("%Y-%m-%d_%H-%M-%S")+".jpg"
                    self.take_screen_shot(self.driver, jpg) #take a screenshot if the button is missing.
                    
                self.driver.delete_all_cookies() #Delete cookies after each attempt or you may run into a random ad page.   
                self.driver.get("http://www.nytimes.com")      
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors, self.verificationErrors)
        
    def take_screen_shot(self, driver, jpg): 
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        os.chdir(self.path)
        driver.get_screenshot_as_file(jpg)
        
if __name__ == "__main__":
    unittest.main()