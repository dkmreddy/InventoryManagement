from InventoryManagement.settings import PROJECT_ROOT
import logging
import os

handlerpath=os.path.realpath(os.path.join(PROJECT_ROOT,"Logging/LogFile.log"))
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler(handlerpath)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)
info_flag=1
warning_flag=2
error_flag=3

def LogInfo(sModuleInfo,sDetails,iLogLevel=1,sStatus=""):
    """
    1- info
    2 - warning
    3 - error
    """
    if iLogLevel == 1:
        logger.info(sModuleInfo + ' - ' + sDetails + '' + sStatus)
    elif iLogLevel == 2:
        logger.warning(sModuleInfo + ' - ' + sDetails + '' + sStatus)
    elif iLogLevel == 3:
        logger.error(sModuleInfo + ' - ' + sDetails + '' + sStatus)
    else:
        print "Unknown Log Level"
    

def PassMessasge(sModuleInfo,msg,level,debug=True):
    if debug:
        print msg
        LogInfo(sModuleInfo, msg, level)
    return msg

def getfileInfo(path):
    path=path.split("\\")
    return path[-2]+"/"+path[-1]+" : "