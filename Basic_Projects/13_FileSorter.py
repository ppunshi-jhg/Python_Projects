import os
import shutil

def create_folder(path: str, extension: str) -> str:
    
    #Create a new folder with the name of the file extension
    folder_name: str = extension[1:].upper()
    folder_path: str = os.path.join(path, folder_name)
    
    #if the folder path doesnt exist, create it
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    return folder_path

def sort_files(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]
            
            if extension:
                target_folder: str = create_folder(source_path, extension)
                
                target_path: str = os.path.join(target_folder, filename)
                
                shutil.move(file_path, target_path)
                
def remove_empty_folders(source_path: str):
    
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        if not filenames and not sub_dir:
            os.rmdir(root_dir)
            
def main():
    user_input: str = input("Please enter the path to the folder you want to sort: ")
    
    if os.path.exists(user_input):
        print("Sorting files...")
        sort_files(user_input)
        print("Removing empty folders...")
        remove_empty_folders(user_input)
        print("Sorting complete.")
    else:
        print("The specified path does not exist. Please check the path and try again.")

if __name__ == "__main__":
    main()
    
