import os

def list_files_and_directories(directory):
    # Check if the directory exists
    if os.path.exists(directory):
        # List items in the directory
        dir_contents = os.listdir(directory)
        for item in dir_contents:
            print(item)
    else:
        print(f"The directory '{directory}' does not exist.")
