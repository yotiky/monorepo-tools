def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_to_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)

def extract_hashes(lines):
    return [line.split()[0] for line in lines if line.strip()]

def compare_files(file1, merged_file, output_file):
    list1 = read_file(file1)
    merged_list = read_file(merged_file)

    combined_hashes = sorted(extract_hashes(list1))
    merged_hashes_sorted = sorted(extract_hashes(merged_list))

    if combined_hashes == merged_hashes_sorted:
        print("The files have been merged correctly.")
    else:
        print("The files have not been merged correctly.")
        combined_set = set(combined_hashes)
        merged_set = set(merged_hashes_sorted)
        
        missing_in_merged = combined_set - merged_set
        extra_in_merged = merged_set - combined_set
        
        with open(output_file, 'w', encoding='utf-8') as file:
            if missing_in_merged:
                file.write("Hashes missing in merged file:\n")
                for hash in missing_in_merged:
                    file.write(hash + '\n')
                print(f"Missing hashes count: {len(missing_in_merged)}")
            
            if extra_in_merged:
                file.write("\nExtra hashes in merged file:\n")
                for hash in extra_in_merged:
                    file.write(hash + '\n')
                print(f"Extra hashes count: {len(extra_in_merged)}")

# ファイルパスを指定
file1_path = 'ModuleA.txt'
merged_file_path = 'monorepo.txt'
output_file_path = 'discrepancies.txt'

compare_files(file1_path, merged_file_path, output_file_path)