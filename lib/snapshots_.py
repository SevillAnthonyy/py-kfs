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
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[5]/a').click()

    # 1/4
    common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/table/tbody/tr[7]/td/p/label/span[1]').click()
    common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/table/tbody/tr[1]/td/p/label/span[1]').click()
    common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/table/tbody/tr[2]/td/p/label/span[1]').click()
    common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/table/tbody/tr[3]/td/p/label/span[1]').click() 
    #next
    common.xpath(driver, '/html/body/div[5]/div/div[2]/ul/li[2]/a').click()

    # 2 / 4
    common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[3]/div/table/tbody/tr[2]/td/p/label/span[1]').click()
    #next
    common.xpath(driver, '/html/body/div[5]/div/div[2]/ul/li[2]/a').click()

    # 3 / 4
    taskname = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[4]/div/table/tbody/tr[1]/td/input')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    #next
    common.xpath(driver, '/html/body/div[5]/div/div[2]/ul/li[2]/a').click()
    
    # 4 / 4
    common.xpath(driver, '/html/body/div[5]/div/div[2]/ul/li[3]/a').click()

    # In progress
    console.log('Snapshot in progress...')
    common.wait(driver, '//*[@id="common-progress-table-content"]')

    last_detail = ''
    while(1):
        try:
            status = common.wait(driver, '//*[@id="common-progress-table-content"]/tbody/tr/td[2]/span').text
            detail = common.wait(driver, '//*[@id="common-progress-table-content"]/tbody/tr/td[4]/span').text
        except StaleElementReferenceException as e:
            #Exception on the WebDriverWait. Added ignore parameters for stale element.
            #Applicable for cases that is constantly changing DOM behavior
            pass
        
        if(detail != last_detail):
            console.log(detail)
            last_detail = detail
            
        if(status == 'Successful'):
            console.log(status)
            common.xpath(driver, '//*[@id="progress-modal-close-btn"]').click()
            break

        #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
        time.sleep(1)
    
