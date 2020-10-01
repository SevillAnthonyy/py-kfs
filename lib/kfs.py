import time
from . import console
from . import snapshots_
from . import restart_device_
from . import restart_network_
from . import import_
from . import fwupdate_
from . import mnt_mode_
from . import mnt_adjustment_
from . import panel_note_
from . import device_settings_

class kfs:
    def __init__(self, driver, count = 0, fail_count = 0):
        self.driver = driver
        self.count = count
        self.fail_count = fail_count

    def start(self):
        self.count = self.count + 1
        console.log('@@ AUTOTEST START! COUNT: '+ str(self.count))

    def snapshots(self):
        console.log('> Executing snapshots')
        snapshots_.execute(self.driver, self.count)

    def restart_device(self):
        console.log('> Executing device restart')
        restart_device_.execute(self.driver, self.count)

    def restart_network(self):
        console.log('> Executing network restart')
        restart_network_.execute(self.driver, self.count)

    def backupdata_import(self):
        console.log('> Executing import backup data')
        import_.execute(self.driver, self.count)

    def fwupdate(self):
        console.log('> Executing firmware update')
        fwupdate_.execute(self.driver, self.count)

    def mnt_mode(self, mode, mm_type):
        console.log('> Executing maintenance mode')
        mnt_mode_.execute(self.driver, self.count, mode, mm_type)

    def mnt_adjustment(self, mode):
        console.log('> Executing maintenance adjustment settings')
        mnt_adjustment_.execute(self.driver, self.count, mode)

    def panel_note(self):
        console.log('> Executing panel note')
        panel_note_.execute(self.driver, self.count)

    def device_settings(self, setting):
        console.log('> Executing device settings')
        device_settings_.execute(self.driver, self.count, setting)
