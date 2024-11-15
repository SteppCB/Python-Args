from e1_list_dir import list_files_and_directories
from e2_delete_dir import delete_file_or_directory
from e3_rename_dir import rename_file_or_directory
from e4_search_dir import search_file_by_name
import argparse

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="File and directory manipulation script")
    parser.add_argument("directory", help="The target directory for the action")
    parser.add_argument("--list", action="store_true", help="List files and directories")
    parser.add_argument("--delete", help="Delete a file or directory")
    parser.add_argument("--rename", nargs=2, metavar=("OLD_NAME", "NEW_NAME"), help="Rename a file or directory")
    parser.add_argument("--search", help="Search for a file by name")

    # Parse the arguments
    args = parser.parse_args()

    if args.list:
        list_files_and_directories(args.directory)
    elif args.delete:
        delete_file_or_directory(args.delete)
    elif args.rename:
        rename_file_or_directory(args.rename[0], args.rename[1])
    elif args.search:
        search_file_by_name(args.directory, args.search)
    else:
        print("No valid action specified. Use --help for more information.")

if __name__ == "__main__":
    main()
