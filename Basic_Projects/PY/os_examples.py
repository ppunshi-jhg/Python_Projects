import os

print(os.listdir("."))
print(os.listdir("Basic_Projects")) #This will list the contents of the Basic_Projects directory
print(os.getcwd()) #This will print the current working directory
print(os.path.exists("Basic_Projects/test.py")) #This will check if the file exists
# os.makedirs("Basic_Projects/new_foolder", exist_ok=True)  #This will create a new folder if it does not exist
# os.remove("Basic_Projects/test.py")  #This will remove the file test.py
print(os.path.join("Basic_projects", "test2.py")) #This will join the two paths correctly