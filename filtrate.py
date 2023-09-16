import csv
import os
import sys
from spellchecker import SpellChecker

def load_whitelist(whitelist_path):
    with open(whitelist_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        whitelist = {row[0].lower() for row in reader}
    return whitelist

def load_spellchecker():
    return SpellChecker()

def is_spelled_correctly(spellchecker, word):
    return word in spellchecker

def filtrate_csv(csv_file_path, whitelist, spellchecker):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader if row['Word'].lower() not in whitelist]

    for row in rows:
        if is_spelled_correctly(spellchecker, row['Word']):
            yield row

def process_file(input_file):
    whitelist_path = 'white-list.csv'
    whitelist = load_whitelist(whitelist_path)
    spellchecker = load_spellchecker()

    base_name = os.path.splitext(os.path.basename(input_file))[0]

    # 使用相同的文件路径来覆盖原文件
    result_csv_file_path = input_file

    filtered_rows = list(filtrate_csv(input_file, whitelist, spellchecker))

    with open(result_csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Word', 'Frequency']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in filtered_rows:
            writer.writerow(row)

    print(f"过滤完成，结果已保存到 {result_csv_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filtrate.py <csv_file_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]

    if not os.path.isfile(csv_file_path):
        print(f"Error: 文件 '{csv_file_path}' 不存在.")
        sys.exit(1)

    process_file(csv_file_path)
