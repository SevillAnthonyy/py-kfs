import time
from . import common
from . import console
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def execute(driver, count):
    #check if device is ready to perform event
    common.statusReady(driver)

    #Task
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[1]/a').click()

    # 1/4 Select FW to upload
    common.xpath(driver, '//*[@id="fwupgrade-readme-chckbx"]').click()
    #next
    common.xpath(driver, '//*[@id="fwupgrade-wizard-modal-next-btn"]').click()

    # 2 / 4
    common.xpath(driver, '//*[@id="fwupgrade-enable-retry-chckbx"]/span[1]').click()
    #next
    common.xpath(driver, '//*[@id="fwupgrade-wizard-modal-next-btn"]').click()

    # 3 / 4
    taskname = common.xpath(driver, '//*[@id="fwupgrade-task-input"]')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    #next
    common.xpath(driver, '//*[@id="fwupgrade-wizard-modal-next-btn"]').click()
    
    # 4 / 4
    common.xpath(driver, '//*[@id="fwupgrade-wizard-modal-next-btn"]').click()

    # In progress
    console.log('Firmware Update in progress...')

    status = '//*[@id="firmware-progress-table-content"]/tbody/tr/td[2]/span'
    detail = '//*[@id="firmware-progress-table-content"]/tbody/tr/td[4]/span'
    ret = common.inProgress(driver, status, detail)
    #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
    time.sleep(5)
    common.xpath(driver, '//*[@id="fwupgrade-wizard-05-close-btn"]').click()
    
    
