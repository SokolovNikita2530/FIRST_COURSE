import os
import shutil
import tempfile

def get_total_size_from_archive(archive_path):
    try:
        if not os.path.isfile(archive_path):
            raise ValueError("The specified path is not a file")
        temp_dir = tempfile.mkdtemp()
        shutil.unpack_archive(archive_path, temp_dir)
        total_size = 0
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
        shutil.rmtree(temp_dir)
        print(f"Total size of files: {total_size} bytes")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    archive_path = input("Enter the path to the archive: ").strip()
    get_total_size_from_archive(archive_path)
