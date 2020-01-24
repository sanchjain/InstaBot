from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def user_input_cli():
    username = input(print("Enter your Instagram Username : "))
    password = input("Enter your Password : ")


class InstaBot():

    username = ''
    password = ''

    def login(self):
        driver = webdriver.Chrome()

        driver.get('http://www.instagram.com/')








i1 = InstaBot()

user_input_cli()
i1.login()

