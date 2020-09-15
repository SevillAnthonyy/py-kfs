from . import config

settings = {
    'BROWSER':          1,              # 1 = Chrome / 2 = Firefox
    'KFS_SERVER':       'https://kfs-as01-userweb.cloudapp.net/',
    'KFS_USERNAME':     config.KFS_USER,
    'KFS_PASSWORD':     config.KFS_PW,
    'SERIAL_NUMBER':    'Z3Z7500006'
    # 2V6: Z3Z7500006
    # 2L6: NPB3400044
    # 2V6: NPB3400044
    # 2L6: Z3Z7500006
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
COMMON         = 'Common'                   #OK
COPY_DENSITY   = 'Copy Density'             #OK
COPY_FEED      = 'Copy Feed'                #OK
DATE_AND_TIME  = 'Date and Time'            #OK
EMAIL_ADD      = 'Email Address'            #OK
EMAIL_REPORT   = 'Email Report'             #OK
EMAIL_SMTP     = 'Email SMTP'               #OK
ENHANCED_WSD   = 'Enhanced WSD'             #OK
FAX_REPORT     = 'FAX Advance Report'       #OK
IPV4           = 'IPV4'                     #NG
MEDIA_INPUT    = 'Media Input'              #OK
MEDIA_TYPE     = 'Media Type'               #OK
OUTPUT         = 'Output'                   #OK
OUTPUT_DEFAULT = 'Output Default'           #OK
POWER_OFF      = 'Power Off'                #NG
SCAN           = 'Scan'                     #OK
SLEEP_LEVEL    = 'Sleep Level'              #OK
SECURITY       = 'Security'                 #OK
TIMER          = 'Timer'                    #OK
WEEKLY_TIMER   = 'Weekly Timer'             #OK
