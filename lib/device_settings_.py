import time
import random
import re
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
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.action_chains import ActionChains

def execute(driver, count, setting):
    try:
        #check if device is ready to perform event
        common.statusReady(driver)
        
        #Task
        common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/a').click()
        common.xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/div/ul/li[2]/a').click()
        
        # 1 / 5
        search = common.xpath(driver, '//*[@id="device-setting-single-edit2"]/table/tbody/tr/td/div[2]/settings-selector/table/tbody/tr/td[2]/div[1]/input')
        search.send_keys(setting, Keys.ARROW_DOWN)
        common.xpath(driver, '//*[@id="device-setting-single-edit2"]/table/tbody/tr/td/div[2]/settings-selector/table/tbody/tr/td[2]/div[1]/button').click()

    except TimeoutException as e:
        console.log('***Halting... Process takes too long to complete.***')
        pass
        return

    #Check if the device setting is applicable on the device
    try:
        common.xpath(driver, '//*[@id="available-settings"]/li/div/label').click()
    except Exception as e:
        console.log('***' + setting + ' setting is not applicable on the device.')
        pass
        return
    
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    # 2 / 5
    try:
        common.xpath(driver, '//*[@id="single-edit-settings-dropdown"]/button').click()
    except TimeoutException as e:
        console.log('***Unable to retrieve required information from the device.***')
        common.xpath(driver, '//*[@id="custom-btn-ok"]/a').click()
        pass
        return

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
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    # 5 / 5
    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    try:
        #In progress
        console.log('Device settings for ' + setting + ' in progress...')
        status = '//*[@id="device-setting-single-edit-progress-table-content"]/tbody/tr/td[2]'
        detail = '//*[@id="device-setting-single-edit-progress-table-content"]/tbody/tr/td[4]'
        ret = common.inProgress(driver, status, detail)
        
    except TimeoutException as e:
        console.log('***Process takes too long to complete.***')
        pass
        return
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

#returns a list containing the range of accepted values
#range[0] is the min and range[1] is the max
def get_range(driver, error_msg_xpath):
    error_element = driver.find_element_by_xpath(error_msg_xpath)
    error_msg = driver.execute_script("return arguments[0].innerHTML", error_element)
    range = [int(d) for d in re.findall(r'-?\d+', error_msg)]
    
    return range


def common_settings(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')
        
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')

        low_toner = common.xpath(driver, '//*[@id="droplist-12"]/button/div').text
        
        if(low_toner == "On"):
            range = get_range(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[4]/div/ul/li/span[2]')
            change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[4]/div/div/input', range[0], range[1])
        
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    except Exception as e:
        console.log('***Common settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return

    
def timer(driver, count):
    if(count % 2 == 0):
        common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[1]').click()
    else:
        common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[2]').click()

    common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()


def copy_density(driver):
    try:
        range = get_range(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li/div/ul/li/span[2]')
        change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li/div/div/input', range[0], range[1])
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
        
    except Exception as e:
        console.log(e)
        console.log('***Copy density settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        #if are you sure dialog pops up, just click ok
        pass
        return


def copy_feed(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***Copy feed settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return

    
def date_time(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***Date time settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return

    
def email_address(driver):
    try:
        common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[1]/div/div/div[1]/a[1]').click()
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***Copy density settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return
    

def email_report(driver):
    try:
        common.xpath(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li/div/div[4]/div/div/div[1]/a[1]').click()
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div','//*[@id="droplist-12"]/ul')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***Email report settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return


def email_smtp(driver):
    try:
        range = get_range(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[4]/div/ul/li/span[2]')
        change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[4]/div/div/input', range[0], range[1])
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***Email report settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return
    

def enhanced_wsd(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div','//*[@id="droplist-12"]/ul')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
        common.xpath(driver, '//*[@id="confirm-restart-dialog-ok-btn"]').click()
        
    except Exception as e:
        console.log('***Enhanced WSD settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return
    

def fax_report(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div','//*[@id="droplist-11"]/ul')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***FAX advanced report settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return

def ipv4(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-20"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-20"]/button/div','//*[@id="droplist-20"]/ul')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***IPV4 settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return
    

def media_input(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
        common.xpath(driver, '//*[@id="droplist-13"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-13"]/button/div', '//*[@id="droplist-13"]/ul')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***Media input settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return


def media_type(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul' )
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***Media type settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return


def output(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul' )
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul' )
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
        
    except Exception as e:
        console.log('***Output settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return


def output_default(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')

        eco_print = common.xpath(driver, '//*[@id="droplist-11"]/button/div').text
        
        if(eco_print == "On"):
            range = get_range(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[2]/div/ul/li/span[2]')
            change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[2]/div/div/input', range[0], range[1])
            
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
        
    except Exception as e:
        console.log('***Output default settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return


def power_off(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    except Exception as e:
        console.log('***Power off settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return


def scan(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
        range = get_range(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[6]/div/ul/li/span[2]')
        change_input(driver, '//*[@id="device-setting-single-edit4"]/table/tbody/tr[2]/td/div/ul/li[6]/div/div/input', range[0], range[1])
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    except Exception as e:
        console.log('***Scan process takes too long to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return

        
def security(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul')
        
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul')
        
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
        common.xpath(driver, '//*[@id="confirm-restart-dialog-ok-btn"]').click()
        
    except Exception as e:
        console.log('***Security settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return
    
    
def sleep_level(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul' )
        common.xpath(driver, '//*[@id="droplist-13"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-13"]/button/div', '//*[@id="droplist-13"]/ul' )
        
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()

    except Exception as e:
        console.log('***Sleep level settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return
    

def weekly_timer(driver):
    try:
        common.xpath(driver, '//*[@id="droplist-11"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-11"]/button/div', '//*[@id="droplist-11"]/ul' )
        common.xpath(driver, '//*[@id="droplist-12"]/button').click()
        dropdown_selection(driver, '//*[@id="droplist-12"]/button/div', '//*[@id="droplist-12"]/ul' )
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-next-btn"]').click()
    except Exception as e:
        console.log('***Weekly timer settings takes too much time to complete.***')
        common.xpath(driver, '//*[@id="set-device-config-wizard-modal-hide-btn"]').click()
        pass
        return
