import os

def find_files_by_extension():
    try:
        folder_path = input("Enter the path to the folder: ")
        extension = input("Enter file extension (e.g., .jpg): ").lower()

        if not os.path.isdir(folder_path):
            raise NotADirectoryError("Provided path is not a directory.")

        print(f"Files with extension {extension}:")
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(extension):
                    print(os.path.join(root, file))
    except Exception as e:
        print(f"Error: {e}")

find_files_by_extension()
