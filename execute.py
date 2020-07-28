from selenium.webdriver.common.keys import Keys
import pyautogui
pyautogui.FAILSAFE = False

import config
from lib import enum
from lib import console
from lib import common
from lib import kfs



COUNT = 1
settings = {
    'BROWSER':          2,              # 1 = Chrome / 2 = Firefox
    'KFS_SERVER':       'https://kfs-as01-userweb.cloudapp.net/',
    'KFS_USERNAME':     config.KFS_USER,
    'KFS_PASSWORD':     config.KFS_PW,
    'SERIAL_NUMBER':    'Z2J7400003'
               
}

print("Press Ctrl-C on the command line to terminate the autotest \n\n")
instance = common.setup(settings)
try:
    while True:
        console.log('@@ AUTOTEST START! COUNT: '+ str(COUNT))
        ###### START! Main execution
        ###### Code from here
        
        #kfs.snapshots(instance, COUNT)
        #kfs.fwupdate(instance, COUNT)
        #kfs.restart_network(instance, COUNT)
        #kfs.restart_device(instance, COUNT)

        ##Maintenance mode. Check lib/enum.py for the list of mnt mode to execute
        #kfs.mnt_mode(instance, COUNT, enum.U474)
        #kfs.mnt_mode(instance, COUNT, enum.U903)
        
        ##Maintenance mode adjustment settings
        kfs.mnt_adjustment(instance, COUNT, settings, enum.MA_LSU)
        kfs.mnt_adjustment(instance, COUNT, settings, enum.MA_CALIB)
        kfs.mnt_adjustment(instance, COUNT, settings, enum.MA_DRUM_REF)
        kfs.mnt_adjustment(instance, COUNT, settings, enum.MA_DEV_REF)
        
        #kfs.backupdata_import(instance, COUNT)

        ###### Until here.
        ###### END Main execution
        COUNT = COUNT + 1
        
except KeyboardInterrupt:
    console.log("Terminated")
    pass


input('Press any key to exit...')
instance.quit()



    

