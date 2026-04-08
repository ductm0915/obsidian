# Antigravity — LLM Wiki

Kho kiến thức cá nhân theo mô hình LLM Wiki. LLM xây dựng và duy trì một wiki có liên kết chéo từ các nguồn thô — kiến thức tích lũy theo thời gian thay vì phải tổng hợp lại từ đầu mỗi lần.

## Bắt đầu phiên làm việc

**Đọc `SCHEMA.md` trước tiên.** File này định nghĩa toàn bộ: cấu trúc wiki, format trang, quy ước đặt tên, và quy trình cho ingest / query / lint.

## Thao tác nhanh

| Lệnh | Mô tả | Workflow |
|---|---|---|
| `/ingest raw/path/to/file.md` | Nạp nguồn mới vào wiki | `.agents/workflows/ingest.md` |
| `/query` | Tra cứu từ wiki | `.agents/workflows/query.md` |
| `/lint` | Kiểm tra sức khỏe wiki | `.agents/workflows/lint.md` |

## Cấu trúc

| Thư mục | Vai trò | Quy tắc |
|---|---|---|
| `raw/` | Tài liệu nguồn gốc | Bất biến — không bao giờ sửa |
| `wiki/` | Wiki do LLM tạo và duy trì | LLM toàn quyền |
| `SCHEMA.md` | Quy ước wiki | Co-evolve cùng người dùng |
| `.agents/workflows/` | Workflow chi tiết cho từng thao tác | Đọc trước khi thực hiện |

## File quan trọng

- `wiki/index.md` — Danh mục toàn bộ wiki (đọc để điều hướng)
- `wiki/log.md` — Lịch sử thao tác (chỉ append, không sửa)
- `wiki/overview.md` — Tổng quan hiện tại
