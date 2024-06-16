

import os

print("The CWD is: ", os.getcwd()) #C:\Projects VS Code\repository\first_repo

# os.chdir("C:\Projects VS Code\repository\first_repo\self_education")

# print("The new CWD is: ", os.getcwd())

os.mkdir("New_directory")
if os.path.exists("New_directory"):
    print("The directory exists.")

print("The CWD is: ", os.getcwd())



    