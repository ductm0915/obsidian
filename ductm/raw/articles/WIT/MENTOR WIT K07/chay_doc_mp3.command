#!/bin/bash
# Di chuyển đến thư mục chứa file chạy hiện tại
cd "$(dirname "$0")"

# Kích hoạt môi trường ảo
source doc_venv/bin/activate

# Chạy trình AI bóc băng audio
python doc_mp3.py
