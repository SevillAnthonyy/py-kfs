import time
from . import common
from . import console
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import StaleElementReferenceException

def execute(driver, count):
    #check if device is ready to perform event
    common.statusReady(driver)
    
    #Task
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/a').click()
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
    common.wait(driver, '//*[@id="restart-progress-table-content"]')
    
    last_detail = ''
    while(1):
        try:
            status = common.wait(driver, '//*[@id="restart-progress-table-content"]/tbody/tr/td[2]/span').text
            detail = common.wait(driver, '//*[@id="restart-progress-table-content"]/tbody/tr/td[4]/span').text
        except StaleElementReferenceException as e:
            #Exception on the WebDriverWait. Added ignore parameters for stale element.
            #Applicable for cases that is constantly changing DOM behavior
            pass
        
        if(detail != last_detail):
            console.log(detail)
            last_detail = detail
            
        if(status == 'Successful'):
            console.log(status)
            common.xpath(driver, '//*[@id="restart-progress-close-btn"]').click()
            break

        #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
        time.sleep(1)
