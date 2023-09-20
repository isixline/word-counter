import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)
        encoding = result['encoding']
    return encoding

def extract_english_text(file_path):
    encoding = detect_encoding(file_path)
    with open(file_path, 'r', encoding=encoding) as file:
        lines = file.readlines()

    english_texts = []

    for line in lines:
        if line.startswith('Dialogue:'):
            parts = line.split(',', 9)
            text = parts[9].strip()

            # 判断文本是否包含英文字母
            if any(char.isalpha() for char in text):
                # 提取英文部分
                english_text = text.split('}')[-1]
                english_texts.append(english_text)

    return english_texts

def save_to_txt(subtitles, file_path):
    output_file = file_path.replace('.ass', '_english.txt')

    with open(output_file, 'w', encoding='utf-8') as file:
        for subtitle in subtitles:
            file.write(f'{subtitle}\n')

def process_file(file_path):
    english_texts = extract_english_text(file_path)
    save_to_txt(english_texts, file_path)

if __name__ == '__main__':
    import sys

    file_path = sys.argv[1]
    process_file(file_path)

