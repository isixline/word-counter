from count import process_file as count_process_file
from filtrate import process_file as filtrate_process_file
from merge import merge_csv
from dotenv import load_dotenv
import sys
import os

# 加载 .env 文件
load_dotenv()

def process_file(file_path):
    output_file_path = count_process_file(file_path)
    white_list_file_path = os.getenv('WHITE_LIST_FILE_PATH')
    output_file_path = filtrate_process_file(output_file_path, white_list_file_path)
    word_list_file_path = os.getenv('WORD_LIST_FILE_PATH')
    merge_csv(output_file_path, word_list_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    process_file(file_path)
