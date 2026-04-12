#!/bin/bash
# Di chuyển đến thư mục chứa file chạy hiện tại
cd "$(dirname "$0")"

# Kích hoạt môi trường ảo (virtual environment)
source doc_venv/bin/activate

# Chạy mã nguồn Python
python chon_file.py
