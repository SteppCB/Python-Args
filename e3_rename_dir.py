import os

def rename_file_or_directory(old_path, new_name):
    try:
        # Check if the file or directory exists
        if os.path.exists(old_path):
            # Get the directory of the old path and join it with the new name
            directory = os.path.dirname(old_path)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)  # Rename the file or directory
            print(f"Renamed '{old_path}' to '{new_path}'.")
        else:
            print(f"The file or directory '{old_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
