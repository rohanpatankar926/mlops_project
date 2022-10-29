import sys
import os
sys.path.append(os.getcwd())
from application_loggings.logger import logging


class Something(object):
    def __init__(self):
        logging.info("This is a constructor class")
        print("This is constructor")
        logging.info("Constructor class ended")

    def funct(self):
        logging.info("This is a function")
        print("This is a function")
        logging.info("Function ended")

if __name__ == "__main__":
    logging.info("This is main")
    s=Something()
    s.funct()
    logging.info("Main ended")