
"""
________________________________________________________________________________

    File        :   get_financial_class.py
    Author      :   Luis de la Barba
    Date        :   18-Jun-2021
    Purpose     :   Initializes the debuging functions
    Register    :
        Ref     Date            Author                  Description
--------------------------------------------------------------------------------
        01      18-Jun-2021     Luis de la Barba        File created
________________________________________________________________________________
"""

import logging
import os


# LEVELS:
#   1. NOTSET
#   2. DEBUG
#   3. INFO
#   4. WARNING
#   5. ERROR
#   6. CRITICAL

logging.getLogger('asyncio').setLevel(logging.WARNING) # Remove log mesage from the asyncio library

name_route      = 'files/'
name_debug_file = 'debug.log'

if not os.path.isdir(name_route):
    os.mkdir(name_route)

route_debug_file   = name_route + name_debug_file
f = open(route_debug_file,'a')
f.write("\n\n************************************************** \n")
f.write("                   NEW SESSION \n")
f.write("************************************************** \n")
f.close()
logging.basicConfig(level=logging.INFO, format='%(message)s')
fh = logging.FileHandler(route_debug_file)
fh.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s","%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)

class DEBUG_CLASS:
    log_display = None      # For displaying the data without registering in a file
    log_file    = None      # Logging data and write in a field
    def __init__(self, name):
        self.log_display    = logging.getLogger(name)
        self.log_file       = logging.getLogger(name)
        self.log_file.addHandler(fh)
        self.__name = name
    def changeLevelToInfo(self):
        self.log_file.setLevel(logging.INFO)
    def changeLevelToDebug(self):
        self.log_file.setLevel(logging.DEBUG)
        pass

if __name__ == "__main__":
    # Variables
    var = DEBUG_CLASS(__name__)
    shoot = var.log_file

    shoot.debug("Level 0 - This message is not shown")
    shoot.info("Level 1 - This message shows info appears on the cmd and also in the debug.log file")
    shoot.warning("Level 2 - This message shows a warning appears on the cmd and also in the debug.log file")
    shoot.error("Level 3 - This message shows an error appears on the cmd and also in the debug.log file")
    shoot.critical("Level 4 - This message is critical and appears on the cmd and also in the debug.log file")

    var.changeLevelToDebug()                # Call this function for showing debug messages
    shoot = var.log_file
    shoot.debug("Now the message appears, this is ideal for debugging processes")
