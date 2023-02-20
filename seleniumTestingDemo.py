import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
 
from selenium.webdriver.common.action_chains import ActionChains
import random

def myLogin(driver):
    #Entering web 
    driver.get('https://www.google.com')
    time.sleep(3)
    # skipIntro=driver.find_element_by_xpath('')
    # skipIntro.click()

    #Login


    time.sleep(2)

    