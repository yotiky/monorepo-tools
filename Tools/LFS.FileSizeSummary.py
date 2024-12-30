import subprocess
import re
import argparse

# コマンドライン引数の処理
parser = argparse.ArgumentParser(description='Git LFS file size summary')
parser.add_argument('--all', action='store_true', help='Include all files in the repository')
args = parser.parse_args()

# Git LFSファイルリストを取得
command = ['git', 'lfs', 'ls-files', '-l', '-s']
if args.all:
    command.append('--all')

result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
lines = result.stdout.splitlines()

# サイズカテゴリの初期化
small = 0      # < 1MB
medium = 0     # 1MB - 10MB
large = 0      # 10MB - 100MB
very_large = 0 # > 100MB
over_50mb_files = [] # > 50MBのファイルリスト
total_size = 0 # 合計サイズ
total_count = 0 # 合計ファイル数

# ファイルサイズを読み込み、カテゴリごとにカウント
for line in lines:
    match = re.search(r'\((\d+(\.\d+)?)\s*(KB|MB|GB)\)', line)
    if match:
        size = float(match.group(1))
        unit = match.group(3)

        # サイズをバイトに変換
        if unit == 'KB':
            size *= 1024
        elif unit == 'MB':
            size *= 1024 * 1024
        elif unit == 'GB':
            size *= 1024 * 1024 * 1024

        total_size += size
        total_count += 1

        if size < 1 * 1024 * 1024:
            small += 1
        elif size < 10 * 1024 * 1024:
            medium += 1
        elif size < 100 * 1024 * 1024:
            large += 1
        else:
            very_large += 1

        if size > 50 * 1024 * 1024:
            over_50mb_files.append((line, size))

# 結果を表示
print(f"Total size: {total_size / (1024 * 1024):.2f} MB")
print(f"Total count: {total_count}")
print(f"Small (<1MB): {small}")
print(f"Medium (1MB-10MB): {medium}")
print(f"Large (10MB-100MB): {large}")
print(f"Very Large (>100MB): {very_large}")

# 50MBを超えるファイルの数を表示
print(f"Files over 50MB: {len(over_50mb_files)}")

# 50MBを超えるファイルの上位10個を表示
over_50mb_files.sort(key=lambda x: x[1], reverse=True)
print("Top 10 files over 50MB:")
for file, size in over_50mb_files[:10]:
    print(file)