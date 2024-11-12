import os

def delete_file_or_directory(path):
    try:
        # Check if the file or directory exists
        if exists:
            # check if the path is a file or directory
            if is_file:
                # delete the file
                print(f"File '{path}' has been deleted.")
            elif is_dir:
                # delete the directory
                print(f"Directory '{path}' has been deleted.")
        else:
            print(f"The file or directory '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
