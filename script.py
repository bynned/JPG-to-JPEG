import os

def rename_files_in_folder(folder_path):
    # List all the files in the given folder
    files = os.listdir(folder_path)
    
    # Filter for files that end with .jpg
    jpg_files = [f for f in files if f.endswith('.jpg')]
    
    # Rename each file
    for file in jpg_files:
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, file[:-4] + '.jpeg')
        os.rename(old_path, new_path)
        print(f'Renamed {old_path} to {new_path}')

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder: ")
    rename_files_in_folder(folder_path)