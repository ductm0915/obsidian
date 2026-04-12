import sys
from docx import Document

def doc_file_docx(file_path):
    try:
        doc = Document(file_path)
        toan_bo_text = ""
        for para in doc.paragraphs:
            text = para.text.strip()
            if text:
                toan_bo_text += text + "\n"
        return toan_bo_text
    except Exception as e:
        return f"Lỗi khi đọc file {file_path}: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = " ".join(sys.argv[1:])
        print(f"--- BẮT ĐẦU ĐỌC FILE: {file_path} ---")
        content = doc_file_docx(file_path)
        print(content)
        print("--- KẾT THÚC ---")
    else:
        print("Vui lòng cung cấp tên file. Ví dụ: python3 read_docx.py ten_file.docx")
