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
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[4]/a').click()

    # 1 / 1
    common.xpath(driver, '//*[@id="device-restart-network-rbtn"]/span[1]').click()
    common.xpath(driver, '//*[@id="device-restart-retry-chckbx"]/span[1]').click()
    common.xpath(driver, '//*[@id="device-restart-wizard-modal-next-btn"]').click()

    # 2 / 2
    taskname = common.xpath(driver, '//*[@id="device-restart-task-input"]')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    #next
    common.xpath(driver, '//*[@id="device-restart-wizard-modal-next-btn"]').click()

    #Execute
    common.xpath(driver, '//*[@id="device-restart-wizard-modal-next-btn"]').click()

    # In progress
    console.log('Device restart in progress...')

    status = '//*[@id="restart-progress-table-content"]/tbody/tr/td[2]/span'
    detail = '//*[@id="restart-progress-table-content"]/tbody/tr/td[4]/span'
    ret = common.inProgress(driver, status, detail)
    #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
    common.xpath(driver, '//*[@id="restart-progress-close-btn"]').click()
    
    time.sleep(5) #Add delay since network device is reconnecting
