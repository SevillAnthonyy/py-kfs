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
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[5]/a').click()

    # 1/4
    for x in range (7):
        x = x + 1 #Index starts at 0
        isSelected(driver, x)
    
    #next
    common.xpath(driver, '//*[@id="retrieve-snapshots-wizard-modal-next-btn"]').click()

    # 2 / 4
    common.xpath(driver, '//*[@id="retrieve-snapshots-retry-chckbx"]/span[1]').click()
    #next
    common.xpath(driver, '//*[@id="retrieve-snapshots-wizard-modal-next-btn"]').click()

    # 3 / 4
    taskname = common.xpath(driver, '//*[@id="retrieve-snapshots-task-input"]')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    #next
    common.xpath(driver, '//*[@id="retrieve-snapshots-wizard-modal-next-btn"]').click()
    
    # 4 / 4
    common.xpath(driver, '//*[@id="retrieve-snapshots-wizard-modal-next-btn"]').click()

    # In progress
    console.log('Snapshot in progress...')

    status = '//*[@id="common-progress-table-content"]/tbody/tr/td[2]/span'
    detail = '//*[@id="common-progress-table-content"]/tbody/tr/td[4]/span'
    ret = common.inProgress(driver, status, detail)
    #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
    common.xpath(driver, '//*[@id="progress-modal-close-btn"]').click()
    return ret 

#Special case Page 1 / 5
def isSelected(driver, index):
    xpath = '//*[@id="'+str(index)+'"]'

    try:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element = driver.find_element_by_xpath(xpath)
        
        cb = element.get_attribute("class")

        # Check only the following:
        # 1 - Status Page / 2 - Service Status / 3 - Network / 4 - Maintenance Report
        if (index == 1 or index == 2 or index == 3  or index == 4): 
            if cb.find('checked') != -1:
                common.xpath(driver, xpath) # DO NOTHING
            else:
                element.click()
        else:
            if cb.find('checked') != -1:
                element.click()
    except Exception as e:
        pass
