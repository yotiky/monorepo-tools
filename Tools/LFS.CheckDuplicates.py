def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def extract_hashes(lines):
    return [line.split()[0] for line in lines if line.strip()]

def check_duplicates(file_path, output_file):
    lines = read_file(file_path)
    hashes = extract_hashes(lines)
    
    seen = set()
    duplicates = set()
    
    for hash in hashes:
        if hash in seen:
            duplicates.add(hash)
        else:
            seen.add(hash)
    
    if duplicates:
        print(f"Found {len(duplicates)} duplicate hashes.")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("Duplicate hashes:\n")
            for hash in duplicates:
                file.write(hash + '\n')
    else:
        print("No duplicate hashes found.")

# ファイルパスを指定
merged_file_path = 'lfs-files.plugin.txt'
output_file_path = 'duplicate_hashes.txt'

check_duplicates(merged_file_path, output_file_path)