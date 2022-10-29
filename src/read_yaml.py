import os
import sys
sys.path.append(os.getcwd())
from application_loggings.logger import logging
import yaml

class READYAML(object):
    def __init__(self):
        pass
    def read_yaml(self,config_path):
        try:
            logging.info("Reading yaml file")
            with open(config_path) as yaml_file:
                yaml_data=yaml.safe_load(yaml_file)
            logging.info("Yaml file read successfully")
            return yaml_data
        except Exception as e:
            logging.info("Error while reading yaml file")
            raise e


if __name__ == "__main__":
    config_path="dvc.yaml"
    yaml_data=READYAML().read_yaml(config_path)
        