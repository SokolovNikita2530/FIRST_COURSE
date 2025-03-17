import os
import shutil

def move_and_archive_images(src, dst):
    try:
        if not os.path.isdir(src):
            raise ValueError("The src path is not a directory")
        if not os.path.isdir(dst):
            os.makedirs(dst)
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
        for root, _, files in os.walk(src):
            for file in files:
                if os.path.splitext(file)[1].lower() in image_extensions:
                    src_file_path = os.path.join(root, file)
                    dst_file_path = os.path.join(dst, file)
                    shutil.move(src_file_path, dst_file_path)
        archive_path = shutil.make_archive(dst, 'zip', dst)
        print(f"Archive created at: {archive_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    src = input("Enter the path to the src directory: ").strip()
    dst = input("Enter the path to the dst directory: ").strip()
    move_and_archive_images(src, dst)
