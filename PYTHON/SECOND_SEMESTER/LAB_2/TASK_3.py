import os
import shutil

def move_and_archive_images(src, dst):
    try:
        if not os.path.isdir(src):
            raise ValueError("Путь src не является директорией")
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
        print(f"Архив создан по пути: {archive_path}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    src = input("Введите путь до директории src: ").strip()
    dst = input("Введите путь до директории dst: ").strip()
    move_and_archive_images(src, dst)
