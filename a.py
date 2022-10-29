import os 

dir="logs"
print(dir)
main_dir=os.path.join(os.getcwd(),dir)
os.makedirs(main_dir,exist_ok=True)