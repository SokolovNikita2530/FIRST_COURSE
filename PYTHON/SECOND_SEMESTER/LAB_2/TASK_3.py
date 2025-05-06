import os
import shutil
import zipfile

def move_images_and_zip():
    try:
        src = input("Enter path to source folder: ")
        dst = input("Enter path to destination folder: ")

        if not os.path.isdir(src):
            raise NotADirectoryError("Source path is not a directory.")
        if not os.path.exists(dst):
            os.makedirs(dst)

        image_exts = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'}

        for root, _, files in os.walk(src):
            for file in files:
                if os.path.splitext(file)[1].lower() in image_exts:
                    src_path = os.path.join(root, file)
                    shutil.move(src_path, os.path.join(dst, file))

        zip_path = dst + '.zip'
        shutil.make_archive(dst, 'zip', dst)
        print(f"Images moved and archived to: {zip_path}")
    except Exception as e:
        print(f"Error: {e}")

move_images_and_zip()
