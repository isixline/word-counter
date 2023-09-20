import sys
import mimetypes
from extract_text import ass_extract_text, pdf_extract_text

def process_unknown(mime):
    # 输出“暂不支持”
    print("暂不支持 ", mime)

def process_file(file_path):
    mime, _ = mimetypes.guess_type(file_path)
    if mime is not None:
        if mime == 'application/pdf':
            pdf_extract_text.process_file(file_path, 5)  # 调用pdf-extract-text.py中的process_file
        elif mime == 'audio/aac' and file_path.endswith('.ass'):
            ass_extract_text.process_file(file_path)  # 调用ass-extract-text.py中的process_file
        else:
            process_unknown(mime)
    else:
        process_unknown(file_path)

if __name__ == "__main__":
    file_path = sys.argv[1]
    process_file(file_path)

