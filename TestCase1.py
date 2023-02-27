import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('http://www.google.com')
time.sleep(2)

coockiesSkip=driver.find_element(by=By.XPATH, value='//*[@id="W0wltc"]')
coockiesSkip.click()

time.sleep(2)

verifyUrl=driver.current_url
if verifyUrl == 'https://www.google.com/?gws_rd=ssl':
    print('link verified')

time.sleep(10)

inputSearch=driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
inputSearch.click()

time.sleep(2)

inputSearch.send_keys('Zurich')

time.sleep(1)

inputSearch.send_keys(Keys.ENTER)

time.sleep(2)





