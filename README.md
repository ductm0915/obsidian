# Antigravity

Kho kiến thức cá nhân sử dụng Obsidian + LLM. Mục tiêu: biến tài liệu thô (sách, video transcript, bài viết) thành hệ thống wiki có liên kết chéo, dễ tra cứu và phát triển theo thời gian.

## Cách hoạt động

1. **Nạp tài liệu** — Bỏ file gốc (PDF, transcript, bài viết) vào thư mục `raw/`
2. **LLM xử lý** — LLM đọc tài liệu, trích xuất ý chính, tạo trang wiki tương ứng
3. **Wiki tự liên kết** — Các khái niệm, nhân vật, chủ đề được liên kết chéo bằng `[[wikilinks]]` của Obsidian
4. **Tra cứu** — Hỏi bất kỳ câu hỏi nào, LLM tổng hợp câu trả lời từ toàn bộ wiki

## Cấu trúc thư mục

```
├── raw/                         # Tài liệu gốc (không chỉnh sửa)
│   ├── articles/                # Bài viết, video transcript
│   ├── books/                   # Sách PDF
│   └── assets/                  # Hình ảnh, file đính kèm
│
├── wiki/                        # Wiki do LLM tạo và duy trì
│   ├── index.md                 # Danh mục tổng — liệt kê tất cả trang wiki
│   ├── overview.md              # Tổng quan toàn bộ kiến thức
│   ├── log.md                   # Nhật ký thao tác (nạp, truy vấn, bảo trì)
│   ├── sources/                 # Tóm tắt từng nguồn tài liệu
│   ├── entities/                # Nhân vật, tổ chức, công cụ, sản phẩm
│   ├── concepts/                # Khái niệm, framework, mô hình tư duy
│   ├── topics/                  # Bài phân tích sâu theo chủ đề
│   └── analyses/                # Kết quả truy vấn, so sánh, báo cáo
│
├── .agents/workflows/           # Quy trình LLM (ingest, query, lint)
└── SCHEMA.md                    # Quy ước wiki — LLM đọc file này mỗi phiên
```

## Giải thích từng phần

### `raw/` — Tài liệu gốc

Nơi lưu trữ tất cả tài liệu nguồn. File trong đây **không bao giờ bị chỉnh sửa** — chỉ đọc.

- `articles/` — Video transcript đã format thành markdown, bài viết web
- `books/` — Sách dạng PDF
- `assets/` — Hình ảnh, file đính kèm

### `wiki/` — Wiki do LLM tạo

Toàn bộ nội dung trong đây do LLM tạo và cập nhật. Mỗi trang có frontmatter YAML (title, type, created, updated, sources, tags) và sử dụng `[[wikilinks]]` để liên kết chéo.

| Thư mục | Chứa gì | Ví dụ |
|---|---|---|
| `sources/` | Mỗi tài liệu gốc có 1 trang tóm tắt | `hormozi-no-bs-business-2026.md` |
| `entities/` | Nhân vật, tổ chức, công cụ | `alex-hormozi.md`, `school-platform.md` |
| `concepts/` | Khái niệm, framework | `scale-framework.md`, `value-equation.md` |
| `topics/` | Phân tích sâu theo chủ đề | `sales.md`, `brand-building.md` |
| `analyses/` | Kết quả so sánh, báo cáo | Truy vấn đã lưu lại |

### `SCHEMA.md` — Quy ước wiki

File quy ước mà LLM đọc đầu mỗi phiên làm việc. Định nghĩa cấu trúc trang, quy tắc đặt tên, và các quy trình (nạp tài liệu, truy vấn, kiểm tra sức khỏe wiki).

### `.agents/workflows/` — Quy trình LLM

Chứa hướng dẫn chi tiết cho 3 quy trình chính:

- **Ingest** — Nạp tài liệu mới: đọc → tạo trang source → trích xuất entities & concepts → cập nhật index
- **Query** — Truy vấn: đọc index → tìm trang liên quan → tổng hợp câu trả lời
- **Lint** — Kiểm tra sức khỏe: tìm link hỏng, trang mồ côi, mâu thuẫn, thiếu liên kết

## Cách sử dụng

### Nạp tài liệu mới

1. Bỏ file vào `raw/articles/` hoặc `raw/books/`
2. Yêu cầu LLM: *"Ingest file này"*
3. LLM tự động tạo/cập nhật các trang wiki tương ứng

### Tra cứu kiến thức

Hỏi trực tiếp, ví dụ:
- *"Tóm tắt framework SCALE của Hormozi"*
- *"So sánh phương pháp bán hàng của Hormozi và Jeremy Miner"*
- *"Liệt kê tất cả concepts liên quan đến sales"*

### Kiểm tra wiki

Yêu cầu: *"Lint wiki"* — LLM sẽ kiểm tra link hỏng, trang thiếu liên kết, mâu thuẫn nội dung.

## Mở bằng Obsidian

Mở thư mục gốc của repo này bằng Obsidian để xem wiki dưới dạng graph view với các liên kết chéo trực quan.
