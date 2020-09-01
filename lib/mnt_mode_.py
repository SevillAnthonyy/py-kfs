import time
from . import common
from . import console
from . import enum
from . import mnt_config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

#Important note: If you want to add a new maintenance
#mode scenario, modify enum.py
def execute(driver, count, mode, mm_type):    
    UXXX = mode[0:4]
    #check if device is ready to perform event
    common.statusReady(driver)

    #Task
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[3]/a').click()
    console.log(mode)

    # Determine if maintenance mode type is Action or Settings
    if(mm_type == enum.TYPE_SETTING):
        common.xpath(driver, '//*[@id="maintenance-mode-edit-settings-rbtn"]').click()
    #else do nothing, since default value is in Actions
        
    # 1 / 5
    mm_search = common.xpath(driver, '//*[@id="maintenance-mode-edit-02"]/div[1]/div[2]/div[2]/div/available-settings-selector/table/tbody/tr/td[2]/div[1]/input')
    mm_search.send_keys(UXXX, Keys.ARROW_DOWN)
    mm_search.send_keys(Keys.ENTER)

    opt_exist = True
    try:
        common.xpath(driver, '//*[@id="setting-select-all-anchor"]').click()
    except WebDriverException as e:
        opt_exist = False
        console.log('ERR!! MM does not exist in type ['+mm_type+']')
        console.log('Please check the device mm features')
        pass

    if(opt_exist == False):
       common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-prev-btn"]').click()
       common.xpath(driver, '//*[@id="maintenance-mode-wizard-popup-ok-btn"]').click()
       return
    #next
    common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-next-btn"]').click()
    
    # 2 / 5
    try:
        config_text = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/button/span[1]').text
    except TimeoutException as e:
        #Error timeout, stuck at processing. Page 1/5 of Maintenance mode
        console.log('ERR!! Stuck at processing. Page 1/5 of Maintenance mode')
        pass
        return
    
    if(config_text != 'No further configuration is required.'):
        common.xpath(driver, '//*[@id="maintenance-mode-settings-dropdown"]/button').click()
        common.xpath(driver, '//*[@id="maintenance-mode-settings-dropdown"]/ul/li[2]').click()                      
    
        #TODO: Custom settings for those modes that have user inputs.
        for val in enum.MM_CUSTOM_INPUTS:
            if(val == mode):
                mnt_config.set(driver, mode, mm_type)            
                break
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

    # 5 / 5 : Summary page
    val = common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-next-btn"]').text
    common.xpath(driver, '//*[@id="maintenance-mode-wizard-modal-next-btn"]').click()
    

    # In progress
    console.log('Maintenance mode in progress...')
    
    if(val == 'Close'):
        time.sleep(5)
        check_task_status(driver)
        return

    status = '//*[@id="maintenance-mode-progress-table-content"]/tbody/tr/td[2]/span'
    detail = '//*[@id="maintenance-mode-progress-table-content"]/tbody/tr/td[4]/span'
    ret = common.inProgress(driver, status, detail)
    #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
    time.sleep(3)
    common.xpath(driver, '//*[@id="maintenance-mode-edit-07-close-btn"]').click()
    
def  check_task_status(driver):
    driver.get(enum.settings['KFS_SERVER']+'Group/TaskList/Device/PD_KY'+enum.settings['SERIAL_NUMBER'])
    common.wait(driver, '//*[@id="serial-number"]')
    last_status = ''
    while True:
        try:
            status = common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[4]/div/table/tbody/tr[1]/td[5]/span[2]').text
            if(status != last_status):
                console.log(status)
                last_status = status
                
            if(status == 'Successful' or status == 'Failed'):
                console.log('Status: '+status)
                break
        except StaleElementReferenceException as e:
            pass
        #refresh
        common.xpath(driver,'/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[4]/a').click()
        time.sleep(3)

    driver.get(enum.settings['KFS_SERVER']+'AdvancedSearch/List?0=serialNumber%07105%07'+enum.settings['SERIAL_NUMBER'])
    common.wait(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[3]')
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[4]/div/table/tbody/tr/td[1]/div/span').click()
    
