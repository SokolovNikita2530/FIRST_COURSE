import os
import re

def collect_unique_imports(directory):
    try:
        if not os.path.isdir(directory):
            raise ValueError("Указанный путь не является директорией")
        import_dict = {}
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            line = line.strip()
                            if line.startswith('import '):
                                modules = re.findall(r'import\s+(.+)', line)
                                for mod in modules:
                                    for part in mod.split(','):
                                        part = part.strip()
                                        if part:
                                            import_dict.setdefault(part, set())
                            elif line.startswith('from '):
                                match = re.match(r'from\s+(\S+)\s+import\s+(.+)', line)
                                if match:
                                    module, items = match.groups()
                                    items_list = [item.strip() for item in items.split(',')]
                                    import_dict.setdefault(module, set()).update(items_list)
        output_lines = []
        for module, items in import_dict.items():
            if items:
                line = f"from {module} import {', '.join(sorted(items))}"
            else:
                line = f"import {module}"
            output_lines.append(line)
        with open('collected_imports.py', 'w', encoding='utf-8') as f_out:
            f_out.write('\n'.join(sorted(output_lines)))
        print("Файл collected_imports.py успешно создан.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    directory = input("Введите путь до директории: ").strip()
    collect_unique_imports(directory)
