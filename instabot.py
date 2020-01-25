from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.driver = webdriver.Chrome(executable_path='/Users/sanchitjain/Downloads/chromedriver')
        self.driver.get("https://www.instagram.com/?hl=en")
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name = \'username\']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name = \'password\']").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(10)

    # def unfollowers(self):
    #     self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()
    #     self.driver.find_element_by_xpath("//a[contains(@href, '/Following')]").click()


username = input()
password = input()

InstaBot(username, password)
# bot.unfollowers()
