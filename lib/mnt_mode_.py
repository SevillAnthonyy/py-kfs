import time
from . import common
from . import console
from . import enum
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Important note: If you want to add a new maintenance
#mode scenario, modify enum.py
def execute(driver, count, mode):
    UXXX = mode[0:4]
    #check if device is ready to perform event
    common.statusReady(driver)

    #Task
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[3]/a').click()
    console.log(mode)

    # Determine if maintenance mode type is Action or Settings
    for val in enum.MM_TYPE_SETTINGS:
        if(val == mode):
            common.xpath(driver, '//*[@id="maintenance-mode-edit-settings-rbtn"]').click()
            break
        
    # 1 / 5
    mm_search = common.xpath(driver, '//*[@id="maintenance-mode-edit-02"]/div[1]/div[2]/div[2]/div/available-settings-selector/table/tbody/tr/td[2]/div[1]/input')
    mm_search.send_keys(UXXX, Keys.ARROW_DOWN)
    mm_search.send_keys(Keys.ENTER)
    common.xpath(driver, '//*[@id="setting-select-all-anchor"]').click()
    #next
    common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-next-btn"]').click()
    
    # 2 / 5
    common.xpath(driver, '//*[@id="maintenance-mode-settings-dropdown"]/button').click()
    common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/ul/li[2]/a').click()
    #TODO: Custom settings for those modes that have user inputs.
    #next
    common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-next-btn"]').click()

    # 3 / 5
    common.xpath(driver, '//*[@id="maintenance-mode-retry-chckbx"]/span[1]').click()
    common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-next-btn"]').click()

    # 4 / 5
    taskname = common.xpath(driver, '//*[@id="maintenance-mode-task-input"]')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    #next
    common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-next-btn"]').click()

    # 5 / 5
    common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-next-btn"]').click()

    # In progress
    console.log('Maintenance mode in progress...')

    status = '//*[@id="maintenance-mode-progress-table-content"]/tbody/tr/td[2]/span'
    detail = '//*[@id="maintenance-mode-progress-table-content"]/tbody/tr/td[4]/span'
    ret = common.inProgress(driver, status, detail)
    #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
    time.sleep(3)
    common.xpath(driver, '//*[@id="maintenance-mode-edit-07-close-btn"]').click()
    
