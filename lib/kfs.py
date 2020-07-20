import time
from . import console
from . import snapshots_
from . import restart_device_
from . import restart_network_
from . import import_

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
