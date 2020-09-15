from . import config

settings = {
    'BROWSER':          1,              # 1 = Chrome / 2 = Firefox
    'KFS_SERVER':       'https://kfs-as01-userweb.cloudapp.net/',
    'KFS_USERNAME':     config.KFS_USER,
    'KFS_PASSWORD':     config.KFS_PW,
    'SERIAL_NUMBER':    'Z3Z7500006'
    # 2V6: Z3Z7500006
    # 2L6: NPB3400044
    # 2V5: ZZV7300008
}

#TODO: MM settings that are dependent to device settings. E.G Cassettes / Mono Colored MFPs, etc

## Maintenance mode
TYPE_SETTING = 'setting'
TYPE_ACTION  = 'action'

## MM Type has actions & settings
U464 = 'U464 Set ID Adjustment Mode'            #OK
U474 = 'U474 Check LSU Cleaning Operation'      #OK

## MM Type settings only
U136 = 'U136 Set Toner Near End Detection'      #OK
U147 = 'U147 Set Toner Apply Mode'              #OK
U148 = 'U148 Set Drum Refresh Mode'             #OK
U250 = 'U250 Set Maintenance Counter Preset'    #OK - To confirm, firmware extensions cass1 cass2
U251 = 'U251 Clear Maintenance Counter'         #OK - To confirm, firmware extensions cass1 cass2

## MM Type actions only
U600 = 'U600 Initialize: All Data'              #OK
U601 = 'U601 Initialize: Keep Data'             #OK
U605 = 'U605 Clear Data'                        #OK

U903 = 'U903 Clear Paper Misfeed Counter'       #OK
U904 = 'U904 Clear Service Call Counter'        #OK
U906 = 'U906 Reset Disable Function Mode'       #NG
U910 = 'U910 Clear Coverage Data'               #OK

MM_CUSTOM_INPUTS = [U136, U147, U148, U250, U251, U464, U474, U600, U601]

## Maintenance adjustment settings
MA_LSU          = 'Laser scanner cleaning'
MA_CALIB        = 'Calibration'
MA_DRUM_REF     = 'Drum refresh'
MA_DEV_REF      = 'Developer refresh'


#Device Settings
COMMON         = 'common'
COPY_DENSITY   = 'copy density'
COPY_FEED      = 'copy feed'
DATE_AND_TIME  = 'date and time'
EMAIL_ADD      = 'email address'
EMAIL_REPORT   = 'email report'
EMAIL_SMTP     = 'email smtp'
ENHANCED_WSD   = 'enahnced wsd'
FAX_REPORT     = 'fax report'
IPV4           = 'ipv4'
MEDIA_INPUT    = 'media input'
MEDIA_TYPE     = 'media type'
OUTPUT         = 'output'
OUTPUT_DEFAULT = 'output default'
POWER_OFF      = 'power off'
SCAN           = 'scan'
SECURITY       = 'security'
SLEEP          = 'sleep'
TIMER          = 'timer'
WEEKLY_TIMER   = 'weekly timer'
