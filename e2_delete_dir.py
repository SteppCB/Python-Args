import os
import shutil  # For removing directories

def delete_file_or_directory(path):
    try:
        # Check if the file or directory exists
        if os.path.exists(path):
            # Check if the path is a file or directory
            if os.path.isfile(path):
                os.remove(path)  # Delete the file
                print(f"File '{path}' has been deleted.")
            elif os.path.isdir(path):
                shutil.rmtree(path)  # Delete the directory
                print(f"Directory '{path}' has been deleted.")
        else:
            print(f"The file or directory '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
