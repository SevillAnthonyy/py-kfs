import time
import random
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
    elif(setting == enum.COMMON):
        common_settings(driver)
    elif(setting == enum.TIMER):
        timer(driver, count)
    elif(setting == enum.COPY_FEED):
        copy_feed(driver)
    elif(setting == enum.DATE_AND_TIME):
        date_time(driver)
    elif(setting == enum.EMAIL_ADD):
        email_address(driver)
    elif(setting == enum.TIMER):
        timer(driver, count)
    elif(setting == enum.FAX_REPORT):
        fax_report(driver)
    elif(setting == enum.EMAIL_SMTP):
        email_smtp(driver)
    elif(setting == enum.EMAIL_REPORT):
        email_report(driver)
    elif(setting == enum.ENHANCED_WSD):
        enhanced_wsd(driver)
    elif(setting == enum.MEDIA_INPUT):
        media_input(driver)
    elif(setting == enum.MEDIA_TYPE):
        media_type(driver)
    elif(setting == enum.OUTPUT):
        output(driver)
    elif(setting == enum.OUTPUT_DEFAULT):
        output_default(driver)
    elif(setting == enum.POWER_OFF):
        power_off(driver)
    elif(setting == enum.SCAN):
        scan(driver)
    elif(setting == enum.SECURITY):
        security(driver)
    elif(setting == enum.SLEEP_LEVEL):
        sleep_level(driver)
    elif(setting == enum.IPV4):
        ipv4(driver)
    elif(setting == enum.WEEKLY_TIMER):
        weekly_timer(driver)

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



def update_value(old_value, min, max):
    new_value = old_value
    
    while int(old_value) == int(new_value):
        new_value = random.randint(min, max)
        
        if int(new_value) != int(old_value):
            return new_value
        

def change_input(driver, input_xpath, min, max):
    input_field = common.xpath(driver, input_xpath)
    old_value = input_field.get_attribute('value')
    input_field.clear()
    time.sleep(3)
    new_value = update_value(old_value, min, max)
    input_field.send_keys(new_value)
    
    
def get_selected_option(selected, items):

    for index, item in enumerate(items):

        if item.text == selected:
            return int(index)


def dropdown_selection(driver,
                       xpath_current_value,
                       xpath_dropdown_options):

    time.sleep(3)
    selected = common.xpath(driver, xpath_current_value).text

    option = common.xpath(driver, xpath_dropdown_options)
    options = option.find_elements_by_tag_name('li')

    current = get_selected_option(selected, options)
    index = update_value(current, 1, len(options)-1)

    options[index].click()
    time.sleep(3)

    
def common_settings(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')
    
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')

    low_toner = common.xpath(driver, '//*[@id="droplist-12"]/button/div').text
    
    if(low_toner == "On"):
        change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[4]/div/div/input', 5, 100)
    
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    
def timer(driver, count):
    if(count % 2 == 0):
        common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[1]').click()
    else:
        common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[2]').click()

    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def copy_density(driver):
    change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li/div/div/input', -3, 3)
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def copy_feed(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
    time.sleep(5)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    
def date_time(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    
def email_address(driver):
    common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[1]').click()
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    

def email_report(driver):
    common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li/div/div[4]/div/div/div[1]/a[1]').click()
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div','//*[@id="droplist-12"]/ul')
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def email_smtp(driver):
    change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[4]/div/div/input', 5, 180)
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    

def enhanced_wsd(driver):
    time.sleep(60)
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    time.sleep(3)
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
    time.sleep(3)
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    time.sleep(3)
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div','//*[@id="droplist-12"]/ul')
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    time.sleep(3)
    common.xpath(driver, '//*[@id="confirm-restart-dialog-ok-btn"]').click()
    time.sleep(60)
    

def fax_report(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

def ipv4(driver):
    common.xpath(driver, '//*[@id="droplist-20"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-20"]/button/div','//*[@id="droplist-20"]/ul')
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    

def media_input(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
    common.xpath(driver, '//*[@id="droplist-13"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-13"]/button/div', '//*[@id="droplist-13"]/ul')
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def media_type(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul' )
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def output(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul' )
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul' )
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def output_default(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')

    eco_print = common.xpath(driver, '//*[@id="droplist-11"]/button/div').text
    
    if(eco_print == "On"):
        change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[2]/div/div/input', 1, 5)
        
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def power_off(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')
    time.sleep(3)
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def scan(driver):
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
    change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[6]/div/div/input', 1, 5)
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def security(driver):
    time.sleep(60)
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')
    time.sleep(3)

    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
    time.sleep(3)    
    
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    common.xpath(driver, '//*[@id="confirm-restart-dialog-ok-btn"]').click()
    time.sleep(60)
    
    
def sleep_level(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul' )
    common.xpath(driver, '//*[@id="droplist-13"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-13"]/button/div', '//*[@id="droplist-13"]/ul' )
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    

def weekly_timer(driver):
    common.xpath(driver, '//*[@id="droplist-11"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul' )
    common.xpath(driver, '//*[@id="droplist-12"]/button').click()
    dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul' )
    time.sleep(3)
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
