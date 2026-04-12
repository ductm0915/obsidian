import os
import sys

# Đảm bảo có thể import các thư viện
try:
    from docx import Document
    import fitz  # PyMuPDF
except ImportError:
    print("Thiếu thư viện! Vui lòng chạy lệnh: source doc_venv/bin/activate && pip install python-docx PyMuPDF")
    sys.exit(1)

def doc_docx(file_path):
    doc = Document(file_path)
    # Lấy ra các đoạn không phải chuỗi rỗng
    return "\n".join([para.text.strip() for para in doc.paragraphs if para.text.strip() != ""])

def doc_pdf(file_path):
    doc = fitz.open(file_path)
    # Ráp toàn bộ text của từng trang lại
    return "\n".join([page.get_text() for page in doc])

def main():
    while True:
        print("\n" + "=" * 50)
        print("          CHƯƠNG TRÌNH ĐỌC TÀI LIỆU MENTOR WIT K07")
        print("=" * 50)
        
        # Lấy danh sách file trong thư mục hiện tại
        files = [f for f in os.listdir('.') if f.endswith('.docx') or f.endswith('.pdf')]
        files.sort()
        
        if not files:
            print("Không tìm thấy file .docx hoặc .pdf nào trong thư mục này.")
            break
            
        print("Danh sách các tài liệu hiện có trong thư mục:")
        for i, f in enumerate(files):
            print(f"  [{i + 1}] {f}")
        print("  [0] THOÁT CHƯƠNG TRÌNH")
        print("=" * 50)
        
        choice = input("👉 Vui lòng nhập số của file bạn muốn đọc (hoặc 0 để thoát): ")
        choice = choice.strip()
        
        if choice == '0':
            print("Đã thoát chương trình. Tạm biệt!")
            break
            
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                file_path = files[idx]
                print(f"\n[!!!] BẮT ĐẦU ĐỌC NỘI DUNG FILE: {file_path}")
                print("-" * 60 + "\n")
                
                try:
                    if file_path.endswith('.docx'):
                        print(doc_docx(file_path))
                    else:
                        print(doc_pdf(file_path))
                except Exception as ex:
                    print(f"❌ Xảy ra lỗi khi cố lấy nội dung file: {ex}")
                    
                print("\n" + "-" * 60)
                print("✅ ĐÃ ĐỌC XONG.")
                input("\nNhấn Enter để quay lại danh sách chọn file...")
            else:
                print("❌ Số bạn nhập không có trong danh sách! Xin vui lòng nhập lại.")
        except ValueError:
            print("❌ Vui lòng chỉ nhập các chữ số hợp lệ.")

if __name__ == "__main__":
    main()
