from selenium import webdriver
from time import sleep



class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path='/Users/sanchitjain/Downloads/chromedriver')
        self.driver.get("https://www.instagram.com/?hl=en")
        sleep(10)
        self.driver.find_element_by_xpath("").click()
