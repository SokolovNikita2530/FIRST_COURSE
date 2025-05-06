import os
import re

def collect_unique_imports():
    try:
        folder_path = input("Enter path to the folder: ")

        if not os.path.isdir(folder_path):
            raise NotADirectoryError("Provided path is not a directory.")

        import_lines = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py"):
                    with open(os.path.join(root, file), encoding='utf-8') as f:
                        for line in f:
                            if re.match(r'^\s*(import|from)\s+', line):
                                import_lines.append(line.strip())

        combined = {}
        direct_imports = set()

        for line in import_lines:
            if line.startswith("import "):
                direct_imports.add(line)
            elif line.startswith("from "):
                parts = re.split(r'\s+', line)
                if len(parts) >= 4 and parts[2] == "import":
                    module = parts[1]
                    symbols = parts[3].split(',')
                    if module not in combined:
                        combined[module] = set()
                    combined[module].update(s.strip() for s in symbols)

        result_lines = sorted(direct_imports)
        for module, symbols in sorted(combined.items()):
            result_lines.append(f"from {module} import {', '.join(sorted(symbols))}")

        with open("combined_imports.py", "w", encoding='utf-8') as f:
            for line in result_lines:
                f.write(line + '\n')

        print("Combined import statements written to 'combined_imports.py'.")
    except Exception as e:
        print(f"Error: {e}")

collect_unique_imports()
