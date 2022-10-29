# modules import libraries
import logging
import os
from datetime import datetime
# ------------------------------------------------

# ------------------------------------------------
# Path: application_loggings/logger.py

#variable initialization
LOG_DIR="logs"
MAIN_DIR_LOGS=os.path.join(os.getcwd(),LOG_DIR) #joined a path with current working directory

os.makedirs(MAIN_DIR_LOGS,exist_ok=True) #create a directory if it does not exist

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}" #current time stamp
file_name = f"log_{CURRENT_TIME_STAMP}.log" #file name with current time stamp

log_file_path = os.path.join(LOG_DIR, file_name) #joined a path with current working directory
 
logging.basicConfig(filename=log_file_path,
                    filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.NOTSET) #class to configure logging