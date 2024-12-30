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
        print(f"Found {len(duplicates)} duplicate hashes in {file_path}.")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("Duplicate hashes:\n")
            for hash in duplicates:
                file.write(hash + '\n')
    else:
        print(f"No duplicate hashes found in {file_path}.")

# ファイルパスを指定
file_paths = ['lfs-files.plugin.txt', 'lfs-files.arts.txt', 'lfs-files.monorepo.txt']
output_file_paths = ['duplicate_hashes_p.txt', 'duplicate_hashes_a.txt', 'duplicate_hashes_m.txt']

for file_path, output_file_path in zip(file_paths, output_file_paths):
    check_duplicates(file_path, output_file_path)