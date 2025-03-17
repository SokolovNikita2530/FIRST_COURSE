import os
import shutil
import tempfile

def get_total_size_from_archive(archive_path):
    try:
        if not os.path.isfile(archive_path):
            raise ValueError("Указанный путь не является файлом")
        temp_dir = tempfile.mkdtemp()
        shutil.unpack_archive(archive_path, temp_dir)
        total_size = 0
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
        shutil.rmtree(temp_dir)
        print(f"Суммарный размер файлов: {total_size} байт")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    archive_path = input("Введите путь до заархивированной директории: ").strip()
    get_total_size_from_archive(archive_path)
