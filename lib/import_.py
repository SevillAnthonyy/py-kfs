import time
import pyautogui
from . import common
from . import console
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import WebDriverException

from selenium.webdriver.common.action_chains import ActionChains

mouseX, mouseY = pyautogui.position()

def execute(driver, count):
    #check if device is ready to perform event
    common.statusReady(driver)
    
    #Task
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/a').click()
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[9]/a').click()
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[9]/div/ul/li[1]/a').click()

    # Customer scenario. Uncheck system
    common.xpath(driver, '/html/body/div[6]/div/div[2]/div[1]/div[1]/div/table/tbody/tr[2]/td/check-group/ul/li[8]/label/span[1]').click()
    
    # 1 / 3
    common.xpath(driver, '//*[@id="import-data-browse-proxy"]').click()
    time.sleep(3)
    pyautogui.write('IMPORT_FILE.zip', interval=0.1)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    try:
        common.xpath(driver, '//*[@id="import-data-wizard-next-btn"]').click()
    except WebDriverException as e:
        console.log('ERR!! File not found')
        console.log('Make sure you saved it in C:\\Users\\pcname')
        console.log('or the filename should be IMPORT_FILE')
        pyautogui.press('enter')
        pyautogui.press('esc')
        return
    time.sleep(3)

    # 2 / 3
    taskname = common.xpath(driver, '//*[@id="hypas-install-name-input"]')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    #next
    common.xpath(driver, '//*[@id="import-data-wizard-next-btn"]').click()

    # 3 / 3 Summary
    common.xpath(driver, '//*[@id="import-data-wizard-next-btn"]').click()
    time.sleep(1)
    common.xpath(driver, '/html/body/div[8]/div/div[4]/ul/li[1]/a').click()
    
    #In progress
    console.log('Import in progress...')

    status = '//*[@id="progress-table-content"]/tbody/tr/td[2]/span'
    detail = '//*[@id="progress-table-content"]/tbody/tr/td[4]/span'
    ret = common.inProgress(driver, status, detail)
    #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
    common.xpath(driver, '/html/body/div[6]/div/div[3]/ul/li/a').click()
