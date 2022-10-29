import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Template:
    def __init__(self,project_name):
        self.project_name=project_name

    def create_template(self):
        logging.info(f"creating a project named {self.project_name}")
        self.project_files=[
            ".github/workflows",
            ".github/.gitkeep",
            f"src/{self.project_name}/utils/__init__.py",
            f"src/{self.project_name}/components/__init__.py",
            f"src/{self.project_name}/constants/__init__.py",
            f"src/{self.project_name}/pipeline/__init__.py",
            f"src/{self.project_name}/templates/__init__.py",
            f"src/{self.project_name}/entity/__init__.py",
            "config/config.yaml",
            "dvc.yaml",
            "params.yaml",
            "master_data_management.yaml",
            "requirements.txt",
            "setup.py",
            "Dockerfile",
            "notebook/consumer.ipynb",
            "documentation",
            "app.py"
            "webapp/templates"
            "webapp/css"
            ".gitignore",
            ".dockerignore",
            "app_exception/__init__.py"
        ]
        for filepath in self.project_files:
            file_dir,filename=os.path.split(Path(filepath))
            if file_dir!="":
                os.makedirs(file_dir,exist_ok=True)
                logging.info(f"directory {file_dir} created for file {filename}")
            if not os.path.exists(filepath) or os.path.getsize(filepath)==0:
                with open(filepath,"w") as file:
                    pass
                logging.info(f"created new file {filename} at {filepath}")
            else:
                logging.info(f"{filename} exists with current size: {os.path.getsize(filepath)}")

if __name__=="__main__":
    project_name="ConsumerComplaints"
    Template(project_name=project_name).create_template()