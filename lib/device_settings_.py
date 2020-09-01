import time
from . import common
from . import console
from lib import enum
from random import randrange
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.common.action_chains import ActionChains

def execute(driver, count, setting):
    #check if device is ready to perform event
    common.statusReady(driver)
    
    #Task
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/a').click()
    common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[2]/a').click()
    
    # 1 / 5
    search = common.xpath(driver, '//*[@id="device-setting-single-edit2"]/table/tbody/tr/td/div[2]/settings-selector/table/tbody/tr/td[2]/div[1]/input')
    search.send_keys(setting, Keys.ARROW_DOWN)
    common.xpath(driver, '//*[@id="device-setting-single-edit2"]/table/tbody/tr/td/div[2]/settings-selector/table/tbody/tr/td[2]/div[1]/button').click()
    common.xpath(driver, '//*[@id="available-settings"]/li/div/label').click()
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    # 2 / 5
    common.xpath(driver, '//*[@id="single-edit-settings-dropdown"]/button').click()
    common.xpath(driver, '//*[@id="single-edit-settings-dropdown"]/ul/li/a').click()

    if(setting == enum.COPY_DENSITY):
        copy_density(driver)
    elif(setting == enum.TIMER):
        timer(driver, count)
    elif(setting == enum.COPY_FEED):
        copy_feed(driver)
    elif(setting == enum.EMAIL_ADD):
        email_address(driver)

    # 3 / 5
    common.xpath(driver, '//*[@id="device-setting-single-edit5"]/table/tbody/tr[2]/td/label/span[1]').click()
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    # 4 / 5
    taskname = common.xpath(driver, '//*[@id="device-setting-single-edit-task-input"]')
    taskname.send_keys('RMNT Autotest: count = '+ str(count), Keys.ARROW_DOWN)
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    # 5 / 5
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    #In progress
    console.log('Device settings for ' + setting + ' in progress...')
    status = '//*[@id="device-setting-single-edit-progress-table-content"]/tbody/tr/td[2]'
    detail = '//*[@id="device-setting-single-edit-progress-table-content"]/tbody/tr/td[4]'
    ret = common.inProgress(driver, status, detail)
    #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
    common.xpath(driver, '//*[@id="device-setting-single-edit-progress-close-btn"]').click()
    

def timer(driver, count):
    #sleep timer adjustment
    if(count % 2 == 0):
        common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[1]').click()
    else:
        common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[2]').click()

    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def copy_density(driver):
    up = common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li/div/div/div[1]/a[1]')
    down = common. xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li/div/div/div[1]/a[2]')
    up_btn_classes = up.get_attribute('class')
    
    #check if the element is disabled which means that copy density is maxed out and needs to be decreased
    if 'disabled' in up_btn_classes:
        down.click()
    else:
        up.click()
        
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def copy_feed(driver):
    common.xpath(driver, '//*[contains(@data-bind,"droplistId")]').click()
    
    #get the list of dropdown options
    items = common.xpath(driver, '//*[contains(@data-bind,"droplistId")]/ul')
    options = items.find_elements_by_tag_name('li')
    
    time.sleep(5)
    #select random option from the dropdown
    options[randrange(len(options))].click()
    
    time.sleep(5)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

def email_address(driver):
    common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[1]').click()

    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    
