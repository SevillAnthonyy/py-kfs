from selenium.webdriver.common.keys import Keys
import pyautogui
pyautogui.FAILSAFE = True


from lib import enum
from lib import console
from lib import common
from lib import kfs

COUNT = 1

print("Press Ctrl-C on the command line to terminate the autotest \n\n")
instance = common.setup(enum.settings)
try:
    while True:
        console.log('@@ AUTOTEST START! COUNT: '+ str(COUNT))
        ###### START! Main execution
        ###### Code from here

        #kfs.backupdata_import(instance, COUNT)
        #kfs.panel_note(instance, COUNT)
        #kfs.snapshots(instance, COUNT)
        #kfs.fwupdate(instance, COUNT)
        #kfs.restart_network(instance, COUNT)
        #kfs.restart_device(instance, COUNT)

        ##Maintenance mode. Check lib/enum.py for the list of mnt mode to execute
        
        #kfs.mnt_mode(instance, COUNT, enum.U136, enum.TYPE_SETTING)
        #kfs.mnt_mode(instance, COUNT, enum.U147, enum.TYPE_SETTING)
        #kfs.mnt_mode(instance, COUNT, enum.U148, enum.TYPE_SETTING)
        #kfs.mnt_mode(instance, COUNT, enum.U250, enum.TYPE_SETTING)
        #kfs.mnt_mode(instance, COUNT, enum.U251, enum.TYPE_SETTING)
        kfs.mnt_mode(instance, COUNT, enum.U326, enum.TYPE_SETTING)
        #kfs.mnt_mode(instance, COUNT, enum.U327, enum.TYPE_SETTING)
        #kfs.mnt_mode(instance, COUNT, enum.U332, enum.TYPE_SETTING)
        kfs.mnt_mode(instance, COUNT, enum.U464, enum.TYPE_ACTION)
        #kfs.mnt_mode(instance, COUNT, enum.U464, enum.TYPE_SETTING)
        #kfs.mnt_mode(instance, COUNT, enum.U474, enum.TYPE_ACTION)
        #kfs.mnt_mode(instance, COUNT, enum.U474, enum.TYPE_SETTING)
        
        #kfs.mnt_mode(instance, COUNT, enum.U601, enum.TYPE_ACTION)
        #kfs.mnt_mode(instance, COUNT, enum.U605, enum.TYPE_ACTION)
        #kfs.mnt_mode(instance, COUNT, enum.U903, enum.TYPE_ACTION)
        #kfs.mnt_mode(instance, COUNT, enum.U904, enum.TYPE_ACTION)
        #kfs.mnt_mode(instance, COUNT, enum.U910, enum.TYPE_ACTION)
        
        
        ##Maintenance mode adjustment settings
        #kfs.mnt_adjustment(instance, COUNT, enum.MA_LSU)
        #kfs.mnt_adjustment(instance, COUNT, enum.MA_CALIB)
        #kfs.mnt_adjustment(instance, COUNT, enum.MA_DRUM_REF)
        #kfs.mnt_adjustment(instance, COUNT, enum.MA_DEV_REF)
        
        

        #kfs.device_settings(instance, COUNT, enum.COPY_FEED)

        ###### Until here.
        ###### END Main execution
        COUNT = COUNT + 1
        
except KeyboardInterrupt:
    console.log("Terminated")
    pass


input('Press any key to exit...')
instance.quit()



    

