import pyautogui
import time
from . import console
from . import console
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException

def login(driver, user, pw):
    time.sleep(3)
    console.log('Username: '+ user+' / Password: '+pw)
    console.log('Logging in...')
    username = xpath(driver, '//*[@id="user-id"]')
    password = xpath(driver,'//*[@id="password"]')
    login = xpath(driver,'//*[@id="login-btn"]')

    username.send_keys(user, Keys.ARROW_DOWN)
    password.send_keys(pw, Keys.ARROW_DOWN)

    login.click()
    wait(driver, '//*[@id="hd-login-user-name"]')

    console.log('You are logged in!')

def searchDevice(driver, kfsServer, serialNumber):
    console.log("Searching for device "+ serialNumber +" ...")
    driver.get(kfsServer+'AdvancedSearch/List?0=serialNumber%07105%07'+serialNumber)
    wait(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[3]')

    result = xpath(driver,'/html/body/div[1]/div[1]/div/div/div/div[1]/div/span').text
    fw_version = xpath(driver,'//*[@id="device-list-table-body"]/tr/td[5]/div').text
    if(result == '1 devices found.'):
        console.log('Device found! FW Version:')
        console.log(fw_version)
        time.sleep(2) #add delay
        #xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[4]/div/table/tbody/tr/td[1]').click()
    else:
        console.log('Device not found, please check if the device is registered to KFS')

def setup(settings):
    console.log('Setting up autotest...')
    if(settings['BROWSER'] == 1):
        driver = webdriver.Chrome()
        console.log('Running in Chrome browser')
    elif(settings['BROWSER'] == 2):
        driver = webdriver.Firefox()
        console.log('Running in Firefox browser')

    console.log('Accessing '+ str(settings['KFS_SERVER']) + '...')    
    driver.get(settings['KFS_SERVER'])

    login(driver, settings['KFS_USERNAME'], settings['KFS_PASSWORD'])
    searchDevice(driver, settings['KFS_SERVER'], settings['SERIAL_NUMBER'])
    return driver

def statusReady(driver):
    count = 0
    #exception = False

    #Special case, to avoid ever changing css
    driver.refresh()
    time.sleep(3)
    #Select device
    xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[4]/div/table/tbody/tr/td[1]').click()
    while(1):
        status = xpath(driver, '//*[@id="device-list-table-body"]/tr/td[4]/div/span[2]').text
        if(count == 1200):
            console.log('Error timeout! already 20 mins has passed and the device is not in Ready status')
            exit()
            
        if(status != 'Ready'):
            xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[3]/a').click()
            console.log('Status is in '+status+'. Refreshing...')
            #time.sleep(5)
        else:
            console.log('Device status: '+status)
            time.sleep(3)
            #Click tasks
            xpath(driver, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[3]/div/ul/li[1]/a').click()
            break
        time.sleep(3)
        count = count + 3

def inProgress(driver, xpath_status, xpath_detail):
    last_detail = ''
    while True:
        try:
            #Note: Percent xpath is unstable, can't retrieve and returns timeout exception
            status = wait(driver, xpath_status).text
            detail = wait(driver, xpath_detail).text
            
            if(detail != last_detail):
                console.log(detail)
                last_detail = detail
                
            if(status == 'Successful' or status == 'Failed' or status == 'Completed'):
                console.log('Status: '+status)
                break
            
        except StaleElementReferenceException as e:
            #Exception on the WebDriverWait. Added ignore parameters for stale element.
            #Applicable for cases that is constantly changing DOM behavior
            pass
        
        

        #TODO: NEED TO FILTER OTHER STATUS TEXTS for continuous testing.
        time.sleep(1)

    return status

def wait(driver, xpath):
    element = WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return element

def xpath(driver, xpath):
    wait(driver,xpath)
    element = driver.find_element_by_xpath(xpath)
    return element

def count(driver, xpath):
    cnt = len(driver.find_elements_by_xpath(xpath))
    return cnt
