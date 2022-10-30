import os, sys, subprocess
from configs import USER_ROOT
with open("../requirements.txt", "r") as file:
    for line in file.readlines():
        requirement = line
        if ".git" in line:
            repo = line.split(".git")[0].split("/")[-1]
            requirement = str(os.path.join(USER_ROOT, repo))+"\n"
        
        print(requirement)
        # implement pip as a subprocess:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
        requirement])
