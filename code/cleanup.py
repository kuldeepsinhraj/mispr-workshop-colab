import shutil 

for folder in ["be", "esp", "md"]:
    try:
        shutil.rmtree(folder)
    except Exception as e:
        print(e) 