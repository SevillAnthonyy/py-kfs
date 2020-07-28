import time
from . import console
from . import snapshots_
from . import restart_device_
from . import restart_network_
from . import import_
from . import fwupdate_
from . import mnt_mode_
from . import mnt_adjustment_

def snapshots(driver, count):
    console.log('> Executing snapshots')
    snapshots_.execute(driver, count)

def restart_device(driver, count):
    console.log('> Executing device restart')
    restart_device_.execute(driver, count)

def restart_network(driver, count):
    console.log('> Executing network restart')
    restart_network_.execute(driver, count)

def backupdata_import(driver, count):
    console.log('> Executing network restart')
    import_.execute(driver, count)

def fwupdate(driver, count):
    console.log('> Executing firmware update')
    fwupdate_.execute(driver, count)

def mnt_mode(driver, count, mode):
    console.log('> Executing maintenance mode')
    mnt_mode_.execute(driver, count, mode)

def mnt_adjustment(driver, count, settings, mode):
    console.log('> Executing maintenance adjustment settings')
    mnt_adjustment_.execute(driver, count, settings, mode)
