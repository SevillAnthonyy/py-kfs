from selenium.webdriver.common.keys import Keys
import pyautogui
pyautogui.FAILSAFE = False

import config
from lib import console
from lib import common
from lib import kfs



COUNT = 1
settings = {
    'KEEP_SCREEN_ALIVE' :True,
    'BROWSER':          2,              # 1 = Chrome / 2 = Firefox
    'KFS_SERVER':       'https://kfs-integ15-userweb.cloudapp.net/',
    'KFS_USERNAME':     config.KFS_USER,
    'KFS_PASSWORD':     config.KFS_PW,
    'SERIAL_NUMBER':    'NPB3400044',
               
}

print("Press Ctrl-C on the command line to terminate the autotest \n\n")
instance = common.setup(settings)
try:
    while True:
        console.log('@@ AUTOTEST START! COUNT: '+ str(COUNT))
        # START! Main execution
        # Code from here
        kfs.snapshots(instance, COUNT)
        kfs.restart_network(instance, COUNT)
        kfs.restart_device(instance, COUNT)
        #kfs.backupdata_import(instance, COUNT)

        # Until here.
        # END Main execution
        COUNT = COUNT + 1
        if(settings['KEEP_SCREEN_ALIVE'] == True):
           pyautogui.move(0, 0, duration=1)
except KeyboardInterrupt:
    console.log("Terminated")
    pass


input('Press any key to exit...')
instance.quit()



    

