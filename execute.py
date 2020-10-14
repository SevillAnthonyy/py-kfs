from selenium.webdriver.common.keys import Keys
import pyautogui
pyautogui.FAILSAFE = True


from lib import enum
from lib import console
from lib import common
from lib.kfs import kfs

print("Press Ctrl-C on the command line to terminate the autotest \n\n")

instance = common.setup(enum.settings)
kfs = kfs(instance)
try:
    while True:
        #print(str(run.getDriver())
        kfs.start()
        ###### START! Main execution
        ###### Code from here

        #kfs.backupdata_import()
        #kfs.panel_note()
   
        #kfs.fwupdate()
        #kfs.restart_network()
        #kfs.restart_device()
        #kfs.snapshots()
        #kfs.snapshots()
        
        ##Maintenance mode. Check lib/enum.py for the list of mnt mode to execute
        
        #kfs.mnt_mode(enum.U136, enum.TYPE_SETTING)
        #kfs.mnt_mode(enum.U147, enum.TYPE_SETTING)
        #kfs.mnt_mode(enum.U148, enum.TYPE_SETTING)
        kfs.mnt_mode(enum.U250, enum.TYPE_SETTING)
        #kfs.mnt_mode(enum.U251, enum.TYPE_SETTING)
        #kfs.mnt_mode(enum.U326, enum.TYPE_SETTING)
        #kfs.mnt_mode(enum.U327, enum.TYPE_SETTING)
        #kfs.mnt_mode(enum.U332, enum.TYPE_SETTING)
        #kfs.mnt_mode(enum.U464, enum.TYPE_ACTION)
        #kfs.mnt_mode(enum.U464, enum.TYPE_SETTING)
        #kfs.mnt_mode(enum.U474, enum.TYPE_ACTION)
        #kfs.mnt_mode(enum.U474, enum.TYPE_SETTING)
        
        #kfs.mnt_mode(enum.U601, enum.TYPE_ACTION)
        #kfs.mnt_mode(enum.U605, enum.TYPE_ACTION)
        #kfs.mnt_mode(enum.U903, enum.TYPE_ACTION)
        #kfs.mnt_mode(enum.U904, enum.TYPE_ACTION)
        #kfs.mnt_mode(enum.U910, enum.TYPE_ACTION)
        
        
        ##Maintenance mode adjustment settings
        #kfs.mnt_adjustment(enum.MA_LSU)
        #kfs.mnt_adjustment(enum.MA_CALIB)
        #kfs.mnt_adjustment(enum.MA_DRUM_REF)
        #kfs.mnt_adjustment(enum.MA_DEV_REF)
        
        
        #kfs.device_settings(enum.COMMON)
        kfs.device_settings(enum.COPY_DENSITY)
        #kfs.device_settings(enum.SCAN)
        #kfs.device_settings(enum.OUTPUT_DEFAULT)


        ###### Until here.
        ###### END Main execution
    

except KeyboardInterrupt:
    console.log("Terminated")
    input('Press any key to exit...')
    instance.quit()

except Exception as e:
    console.log("Exception has occured!")
    console.log(e)
    console.log("Refreshing....")
    instance.refresh()


