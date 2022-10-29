from read_yaml import READYAML
import os
import sys
sys.path.append(os.getcwd())
from application_loggings.logger import logging


class ReadValFromYaml(object):
    def __init__(self):
        pass

    def read_val_from_yaml(self,config_path):
        self.config=READYAML().read_yaml(config_path)
        data=self.config["xmas-fifth-day"]["partridges"]["count"]
        print(data)
        return data

if __name__ == "__main__":
    config_path="dvc.yaml"
    ReadValFromYaml().read_val_from_yaml(config_path)