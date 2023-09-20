import PyPDF2
import os
import sys

def extract_text_from_pdf(pdf_path, start_page, end_page):
    pdf_text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_num in range(start_page, min(end_page, len(pdf_reader.pages))):
                page = pdf_reader.pages[page_num]
                pdf_text += page.extract_text()
        
        return pdf_text
    except Exception as e:
        print(f"提取文本时出现错误：{str(e)}")
        return None

def save_text_to_file(text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"文本已保存至 {output_path}")
    except Exception as e:
        print(f"保存文本时出现错误：{str(e)}")

def process_file(pdf_path, split_every):
    output_dir = os.path.dirname(pdf_path)
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    num_pages = len(pdf_reader.pages)
    
    if split_every and split_every > 0:
        for i in range(0, num_pages, split_every):
            pdf_text = extract_text_from_pdf(pdf_path, i, i+split_every)
            if pdf_text is not None:
                output_subdir = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}-txt")
                os.makedirs(output_subdir, exist_ok=True)
                output_path = os.path.join(output_subdir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_pages_{i+1}-{i+split_every}.txt")
                save_text_to_file(pdf_text, output_path)
    else:
        pdf_text = extract_text_from_pdf(pdf_path, 0, num_pages)
        if pdf_text is not None:
            output_subdir = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}-txt")
            os.makedirs(output_subdir, exist_ok=True)
            output_path = os.path.join(output_subdir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_pages_1-{num_pages}.txt")
            save_text_to_file(pdf_text, output_path)

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    split_every = int(sys.argv[2]) if len(sys.argv) == 3 else None
    process_file(pdf_path, split_every)
