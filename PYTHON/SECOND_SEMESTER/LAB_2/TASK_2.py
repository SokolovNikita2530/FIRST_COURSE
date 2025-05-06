import os
import zipfile
import tempfile
import shutil

def get_total_size_in_zip():
    try:
        zip_path = input("Enter path to ZIP archive: ")

        if not zipfile.is_zipfile(zip_path):
            raise ValueError("Provided file is not a valid zip archive.")

        with tempfile.TemporaryDirectory() as tmpdir:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(tmpdir)

            total_size = 0
            for root, _, files in os.walk(tmpdir):
                for file in files:
                    full_path = os.path.join(root, file)
                    total_size += os.path.getsize(full_path)

            print(f"Total size of all files: {total_size} bytes")
    except Exception as e:
        print(f"Error: {e}")

get_total_size_in_zip()
