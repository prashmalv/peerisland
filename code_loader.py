import os

def load_code_from_directory(directory, extensions=(".java", ".sql", ".xml", ".md")):
    """
    Reads all files recursively from the given directory that match the given extensions.
    Returns a list of dictionaries containing file paths and contents.
    """
    code_files = []

    for root, _, files in os.walk(directory):
        print(f"Scanning: {root}")
        for file in files:
            print(f"Found file: {file}")
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        code_files.append({
                            "path": file_path,
                            "content": f.read()
                        })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return code_files

# Test (optional)
if __name__ == "__main__":
    test_dir = r"C:\Codebase\codeEval\sakillaCode\SakilaProject"
    files = load_code_from_directory(test_dir)
    print(f"Loaded {len(files)} files")
    for f in files[:3]:  # Show first 3 files
        print(f"\n📄 {f['path']}\n---\n{f['content'][:300]}...\n")

