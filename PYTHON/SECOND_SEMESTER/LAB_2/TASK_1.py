import os

def find_files_by_extension(directory, extension):
    try:
        if not os.path.isdir(directory):
            raise ValueError("The specified path is not a directory")
        result = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(extension.lower()):
                    result.append(os.path.join(root, file))
        if result:
            for file_path in result:
                print(file_path)
        else:
            print("No files with the specified extension were found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory = input("Enter the path to the directory: ").strip()
    extension = input("Enter the file extension (e.g., .txt): ").strip()
    find_files_by_extension(directory, extension)
