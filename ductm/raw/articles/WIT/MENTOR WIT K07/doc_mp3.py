import os
import sys

# Kiểm tra thư viện AI Whisper
try:
    import whisper
except ImportError:
    print("🤖 Hệ thống AI đang được cài đặt. Vui lòng đợi chút nhé hoặc báo lại cho tôi nếu có lỗi...")
    sys.exit(1)

def transcribe_audio(file_path):
    print(f"\n[!!!] Đang tải não bộ AI (chỉ mất chút thời gian ở lần chạy đầu tiên)...")
    # Dùng model 'base' gọn nhẹ nhưng đọc tiếng Việt khá tốt
    model = whisper.load_model("base")
    
    print(f"\n[!!!] Đang lắng nghe file: {file_path}")
    print("⏳ Quá trình này sẽ mất một lúc tuỳ thuộc vào độ dài của bài nói. Bạn có thể đi uống nước và quay lại sau!\n")
    
    # Whisper sẽ tự nhận diện ngôn ngữ và bóc băng
    result = model.transcribe(file_path, language="vi")
    
    # Lưu kết quả ra file Text để bạn dễ đọc
    txt_path = file_path + ".txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
        
    return result["text"], txt_path

def main():
    while True:
        print("\n" + "=" * 60)
        print("     🧠 CHƯƠNG TRÌNH AI BÓC BĂNG ÂM THANH (MP3/M4A) SANG CHỮ")
        print("=" * 60)
        
        # Lấy danh sách file audio
        files = [f for f in os.listdir('.') if f.lower().endswith(('.mp3', '.wav', '.m4a'))]
        files.sort()
        
        if not files:
            print("\n❌ Không tìm thấy file âm thanh (.mp3, .wav, .m4a) nào trong thư mục này.")
            print("Bạn hãy copy file âm thanh vào thư mục MENTOR WIT K07 và chạy lại nhé.")
            break
            
        print("Danh sách các file âm thanh:")
        for i, f in enumerate(files):
            print(f"  [{i + 1}] {f}")
        print("  [0] THOÁT")
        print("=" * 60)
        
        choice = input("👉 Mời bạn nhập số của file muốn dịch ra chữ (vd: 1) hoặc 0 để thoát: ")
        choice = choice.strip()
        
        if choice == '0':
            print("Tạm biệt!")
            break
            
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                file_path = files[idx]
                text, txt_file = transcribe_audio(file_path)
                
                print("\n" + "=" * 60)
                print(f"✅ HOÀN TẤT BÓC BĂNG! Toàn bộ chữ đã được lưu vào file:")
                print(f"➡️  {txt_file}")
                print("=" * 60)
                print("\nTRÍCH ĐOẠN ĐẦU TIÊN CỦA FILE:\n")
                print(text[:800] + "...\n")
                
                input("Nhấn Enter để quay lại danh sách chọn file...")
            else:
                print("❌ Số bạn chọn không nằm trong danh sách!")
        except ValueError:
            print("❌ Vui lòng chỉ nhập số hợp lệ.")

if __name__ == "__main__":
    main()
