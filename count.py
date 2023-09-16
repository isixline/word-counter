import re
import csv
import os
import sys

def count_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.lower()
    text = re.sub(r'[^a-z ]', ' ', text)
    words = text.split()

    word_count = {}
    for word in words:
        if len(word) > 1:  # Exclude single-letter words
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

def process_file(file_path):
    result = count_words_from_file(file_path)

    # 按频次从高到低排序
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    # 输出到CSV文件
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_directory = 'temp'
    os.makedirs(output_directory, exist_ok=True)
    csv_file_name = os.path.join(output_directory, f"{base_name}-words.csv")
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Word', 'Frequency']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for word, count in sorted_result:
            writer.writerow({'Word': word, 'Frequency': count})

    print(f"结果已保存到 {csv_file_name}")
    return csv_file_name

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    process_file(file_path)
