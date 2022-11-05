import pymongo
from pymongo import MongoClient
from read_yaml import ReadYaml
import json
import hydra
from omegaconf import DictConfig

# class MongoDb:
#         def __init__(self):
#             pass

#         @hydra.main(config_path="config", config_name="config")
#         def load_data(config: DictConfig):
#                 try:
#                     self.myClient=pymongo.MongoClient(config.mongoDbCredentials.uri)
#                     self.database=self.myClient[config.mongoDbCredentials.database]
#                     self.col=self.database[config.mongoDbCredentials.collection]
#                     with open(config.Data.json_data) as json_data:
#                         json_data_=json.loads(json_data.read())
#                     self.DummyData = json_data_ 
#                     self.load_data = self.col.insert_one(self.DummyData)
#                     return f"Data Loaded successfully at {self.load_data}"
#                 except Exception as e:
#                     raise e


@hydra.main(config_path="config", config_name="config")
def load_data(config: DictConfig):
                try:
                    myClient=pymongo.MongoClient(config.mongoDbCredentials.uri)
                    database=myClient[config.mongoDbCredentials.database]
                    col=database[config.mongoDbCredentials.collection]
                    with open(config.Data.json_data) as json_data:
                        json_data_=json.loads(json_data.read())
                    DummyData = json_data_ 
                    load_data = col.insert_one(DummyData)
                    return f"Data Loaded successfully at {load_data}"
                except Exception as e:
                    raise e

if __name__=="__main__":
        load_data()