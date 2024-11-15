import os

def search_file_by_name(directory, filename):
    # Check if the directory exists
    if os.path.exists(directory):
        found = False
        # Traverse the directory tree
        for root, dirs, files in os.walk(directory):
            if filename in files:
                print(f"File '{filename}' found in '{root}'.")
                found = True
                break
        if not found:
            print(f"File '{filename}' not found in '{directory}'.")
    else:
        print(f"The directory '{directory}' does not exist.")
