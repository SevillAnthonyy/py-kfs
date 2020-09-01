import time
from . import common
from . import console
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

def execute(driver, count):
    #check if device is ready to perform event
    common.statusReady(driver)
    
    #Task
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[7]/a').click()

    # 1 / 4
    common.xpath(driver, '//*[@id="panel-note-title-input"]').send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    common.xpath(driver, '//*[@id="panel-note-message-input"]').send_keys('DO NOT SHUTDOWN THE DEVICE!!', Keys.ARROW_DOWN)
    common.xpath(driver, '//*[@id="panel-note-wizard-next-btn"]').click()

    # 2 / 4
    common.xpath(driver, '//*[@id="panel-note-wizard-next-btn"]').click()
    
    # 3 / 4
    taskname = common.xpath(driver, '//*[@id="panel-note-task-title"]')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    #next
    common.xpath(driver, '//*[@id="panel-note-wizard-next-btn"]').click()

    #Execute
    common.xpath(driver, '//*[@id="panel-note-wizard-next-btn"]').click()


    # In progress
    console.log('Panel note is sending...')

    status = '//*[@id="progress-table-content"]/tbody/tr/td[2]/span'
    detail = '//*[@id="progress-table-content"]/tbody/tr/td[4]/span'
    ret = common.inProgress(driver, status, detail)
    #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.

    #Special case, since close button css is not consistent.
    driver.refresh() #Refresh page when completed.
    
    #try:
        #Special condition, close button cant de detected using ID.
        #full xpath div is changing
    #    common.xpath(driver, '/html/body/div[20]/div/button').click()
    #except TimeoutException as e:
    #    common.xpath(driver, '/html/body/div[11]/div/button').click()
    #    pass
    time.sleep(3)
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[4]/div/table/tbody/tr/td[1]/div/span').click()
