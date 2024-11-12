import os

def search_file_by_name(directory, filename):
    # Check if the directory exists
    if exists:
        found = False
        # For each directory in the directory tree rooted at top (hint theres an os function you can replace [] with)
        for root, dirs, files in []:
            if filename in files:
                print(f"File '{filename}' found in '{root}'.")
                found = True
        # If you don't find the file, print a message
        if not_found:
            print(f"File '{filename}' not found in '{directory}'.")
    else:
        print(f"The directory '{directory}' does not exist.")
