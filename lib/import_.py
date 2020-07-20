import time
from . import common
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.common.action_chains import ActionChains

def execute(driver, count):
    #check if device is ready to perform event
    common.status_ready(driver)
    
    #Task
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/a').click()
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[9]/a').click()
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[9]/div/ul/li[1]/a').click()
    
    # 1 / 3
    common.xpath(driver, '//*[@id="import-data-browse-proxy"]').click()
    
    actions = ActionChains(driver)
    actions.send_keys('import.zip')
    actions.perform()
