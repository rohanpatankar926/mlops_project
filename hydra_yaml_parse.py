from omegaconf import DictConfig
import hydra

@hydra.main(config_path="MongoDbConfig", config_name="config")
def something(config: DictConfig):
    print("the data iam fetching from yaml file using hydra")
    print(f"The mongodb uri is {config.mongoDbCredentials.database}")

if __name__=="__main__":
    data=something()
    something()