import pymongo
from pymongo import MongoClient
from read_yaml import ReadYaml
import json

class MongoDb:
        def __init__(self,config_path:str="config.yaml" ):
                self.config=ReadYaml().read_params(config_path)
        
        def load_data(self):
                try:
                    self.myClient=pymongo.MongoClient(self.config["mongoDbCredentials"]["uri"])
                    self.database=self.myClient[self.config["mongoDbCredentials"]["database"]]
                    self.col=self.database[self.config["mongoDbCredentials"]["collection"]]
                    with open(self.config["Data"]["json_data"]) as json_data:
                        json_data_=json.loads(json_data.read())
                    self.DummyData = json_data_ 
                    self.load_data = self.col.insert_one(self.DummyData)
                    return f"Data Loaded successfully at {self.load_data}"
                except Exception as e:
                    raise e

if __name__=="__main__":
        MongoDb().load_data()
