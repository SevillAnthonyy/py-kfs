import time
from . import common
from . import console
from . import enum
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def set(driver, mode, mm_type):
###############################################
## U136 = 'U136 Set Toner Near End Detection'
    if(mode == enum.U136):
        cmy_val = common.xpath(driver, '//*[@id="panel-holder"]/ul/li[1]/div/div/input').get_attribute('value')
        if(cmy_val != '0'): # Min value
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/div/a[2]').click()
        else:
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/div/a[1]').click()
        k_val = common.xpath(driver, '//*[@id="panel-holder"]/ul/li[1]/div/div/input').get_attribute('value')
        if(k_val != '0'): # Min value
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/a[2]').click()
        else:
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/a[1]').click()
#########################################
## U147 = 'U147 Set Toner Apply Mode'
    elif(mode == enum.U147):
        mode_val = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/button/div').text
        common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/button').click()
        if(mode_val == 'Mode 0'):
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/ul/li[2]/a').click()
        elif(mode_val == 'Mode 1'):
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/ul/li[3]/a').click()
        elif(mode_val == 'Mode 2'):
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/ul/li[1]/a').click()
        upperlimit_val = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/input').get_attribute('value')
        if(upperlimit_val != '2'):#Max value
            common.xpath(driver,'/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/a[1]').click()
        else:
            common.xpath(driver,'/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/a[2]').click()
        min_val = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[3]/div/div/input').get_attribute('value')
        if(min_val != '30'): #Max value
            common.xpath(driver,'/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[3]/div/div/div/a[1]').click()
        else:
            common.xpath(driver,'/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[3]/div/div/div/a[2]').click()
#########################################
## U148 = 'U148 Set Drum Refresh Mode'
    elif(mode == enum.U148):
        mode_val = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/input').get_attribute('value')
        if(mode_val != '3'): #Max value
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/div/a[1]').click()
        else:
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/div/a[2]').click()
        dew_val = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/input').get_attribute('value')
        if(dew_val != '3'): #Max value
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/a[1]').click()
        else:
            common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/a[2]').click()
##################################################
## U250 = 'U250 Set Maintenance Counter Preset'
## U251 = 'U251 Clear Maintenance Counter'
    elif(mode == enum.U250 or mode == enum.U251):
        if(mm_type == enum.TYPE_SETTING):
            ##
            ex = common.count(driver, '//*[@id="panel-holder"]/ul/li/div/div/input')
            print(str(ex))##
            cnt_a = common.xpath(driver, '//*[@id="panel-holder"]/ul/li[1]/div/div/input').get_attribute('value')
            ret = int(cnt_a) % 2
            if(ret == 0): #Increment
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/div/a[1]').click()
            else: #Decrement
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div/div/div/a[2]').click()

            cnt_b = common.xpath(driver, '//*[@id="panel-holder"]/ul/li[2]/div/div/input').get_attribute('value')
            ret = int(cnt_b) % 2
            if(ret == 0): #Increment
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/a[1]').click()
            else: #Decrement
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[2]/div/div/div/a[2]').click()

            cnt_c = common.xpath(driver, '//*[@id="panel-holder"]/ul/li[3]/div/div/input').get_attribute('value')
            ret = int(cnt_c) % 2
            if(ret == 0): #Increment
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[3]/div/div/div/a[1]').click()
            else: #Decrement
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[3]/div/div/div/a[2]').click()

            cnt_ht = common.xpath(driver, '//*[@id="panel-holder"]/ul/li[4]/div/div/input').get_attribute('value')
            ret = int(cnt_ht) % 2
            if(ret == 0): #Increment
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[4]/div/div/div/a[1]').click()
            else: #Decrement
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[4]/div/div/div/a[2]').click()

            cass1 = common.xpath(driver, '//*[@id="panel-holder"]/ul/li[5]/div/div/input').get_attribute('value')
            ret = int(cass1) % 2
            if(ret == 0): #Increment
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[5]/div/div/div/a[1]').click()
            else: #Decrement
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[5]/div/div/div/a[2]').click()

            cass2 = common.xpath(driver, '//*[@id="panel-holder"]/ul/li[6]/div/div/input').get_attribute('value')
            ret = int(cass2) % 2
            if(ret == 0): #Increment
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[5]/div/div/div/a[1]').click()
            else: #Decrement
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li[5]/div/div/div/a[2]').click()        
        #elif(mm_type == enum.TYPE_ACTION): #No custom inputs
################################################
## U474 = 'U474 Check LSU Cleaning Operation'
    elif(mode == enum.U474):
        if(mm_type == enum.TYPE_SETTING):
            val = common.xpath(driver, '//*[@id="panel-holder"]/ul/li/div/div/div/div/div/input').get_attribute('value')
            if(val != '5000'): # Maximum Value
                common.xpath(driver, '//*[@id="panel-holder"]/ul/li/div/div/div/div/div/div/a[1]').click()
            else:
                common.xpath(driver, '//*[@id="panel-holder"]/ul/li/div/div/div/div/div/div/a[2]').click()
        #elif(mm_type == enum.TYPE_ACTION): #No custom inputs
#########################################
## U464 = 'U464 Set ID Adjustment Mode'
    elif(mode == enum.U464):
        if(mm_type == enum.TYPE_SETTING):
            count = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/div/div[2]/div/div/input').get_attribute('value')
            if(count != '0'): # Decrement
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/div/div[2]/div/div/div/a[2]').click()
            else: # Increment
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/div/div[2]/div/div/div/a[1]').click()
            leaving_time = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/div/div[6]/div/div/input').get_attribute('value')
            if(leaving_time != '480'):# Increment
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/div/div[6]/div/div/div/a[1]').click()
            else: # Decrement
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/div/div[6]/div/div/div/a[2]').click()
            # Other items not yet included please add.
        elif(mm_type == enum.TYPE_ACTION):
            rb1 = common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/p[1]/label/span[1]').get_attribute('class')
            if(rb1 == 'icon-radio checked'):
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/p[2]/label').click()
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/div[2]/div/div/label').click()
            else:
                common.xpath(driver, '/html/body/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/ul/li/div/p[1]/label').click()
#########################################
## U600 = 'U600 Initialize: All Data'
## U601 = 'U601 Initialize: Keep Data'
    elif(mode == enum.U600 or mode == enum.U601):
        if(mm_type == enum.TYPE_ACTION):
            inp_val = common.xpath(driver, '//*[@id="panel-holder"]/ul/li/div[2]/div[1]/div/div/input').get_attribute('value')
            val = int(inp_val) % 2
            if(val == 0):
                common.xpath(driver, '//*[@id="panel-holder"]/ul/li/div[2]/div[1]/div/div/div/a[1]').click()
            else:
                common.xpath(driver, '//*[@id="panel-holder"]/ul/li/div[2]/div[1]/div/div/div/a[2]').click()
