import yaml
from yaml import safe_load
import logging

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)

class ReadYaml:    
    def read_params(self, config_path):
        try:
            logging.info(f"Reading all parameters from config_path")
            with open(config_path) as file:
                self.config = safe_load(file)
                logging.info(f"Parameters Readed from config_path Successfully !!!")
                return self.config
        except Exception as e:
            logging.warning("Something happened",e)
            raise e