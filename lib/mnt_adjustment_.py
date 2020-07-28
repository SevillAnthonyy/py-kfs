import time
from . import common
from . import console
from . import enum
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def execute(driver, count, settings, mode):
    SERIAL_NUM = settings['SERIAL_NUMBER']
    KFS_SERVER = settings['KFS_SERVER']
    #check if device is ready to perform event
    common.statusReady(driver)
    
    driver.implicitly_wait(10) # seconds
    driver.get(KFS_SERVER+'Device/PD_KY'+SERIAL_NUM+'/DeviceSetting')

    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div[4]/ul/li[4]/a').click()

    # 1 / 4
    console.log('Adjustment mode: '+ mode)
    if(mode == enum.MA_LSU):
        common.xpath(driver, '//*[@id="maintenande-mode-method-action1-rbtn"]/span[1]').click()
    elif(mode == enum.MA_CALIB):
        common.xpath(driver, '//*[@id="maintenande-mode-method-action2-rbtn"]/span[1]').click()
    elif(mode == enum.MA_DRUM_REF):
        common.xpath(driver, '//*[@id="maintenande-mode-method-action3-rbtn"]/span[1]').click()
    elif(mode == enum.MA_DEV_REF):
        common.xpath(driver, '//*[@id="maintenande-mode-method-action4-rbtn"]/span[1]').click()

    common.xpath(driver, '//*[@id="adjust-mmode-actions-wizard-next-btn"]').click()

    # 2 / 4
    common.xpath(driver, '//*[@id="adjust-mmode-retry-chckbx"]/span[1]').click()
    common.xpath(driver, '//*[@id="adjust-mmode-actions-wizard-next-btn"]').click()

    # 3 / 4
    taskname = common.xpath(driver, '//*[@id="adjust-mmode-actions-wizard-3-page"]/div/table/tbody/tr[1]/td/input')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    #next
    common.xpath(driver, '//*[@id="adjust-mmode-actions-wizard-next-btn"]').click()

    # 4 / 4
    common.xpath(driver, '//*[@id="adjust-mmode-actions-wizard-next-btn"]').click()

    # In progress
    console.log('Adjust maintenance mode in progress...')

    status = '//*[@id="progress-table-content"]/tbody/tr/td[2]/span'
    detail = '//*[@id="progress-table-content"]/tbody/tr/td[4]/span'
    ret = common.inProgress(driver, status, detail)

    time.sleep(3) #Delay
    common.xpath(driver, '//*[@id="progress-modal-close-btn"]').click()

    #Go back to original page
    driver.implicitly_wait(10) # seconds
    driver.get(KFS_SERVER+'AdvancedSearch/List?0=serialNumber%07105%07'+SERIAL_NUM)
