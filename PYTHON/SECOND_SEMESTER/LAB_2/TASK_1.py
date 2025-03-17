import os

def find_files_by_extension(directory, extension):
    try:
        if not os.path.isdir(directory):
            raise ValueError("Указанный путь не является директорией")
        result = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(extension.lower()):
                    result.append(os.path.join(root, file))
        if result:
            for file_path in result:
                print(file_path)
        else:
            print("Файлы с указанным расширением не найдены.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    directory = input("Введите путь до директории: ").strip()
    extension = input("Введите расширение файлов (например, .txt): ").strip()
    find_files_by_extension(directory, extension)
