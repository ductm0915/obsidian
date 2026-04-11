---
title: "Specialty Pipeline (PPV)"
type: concept
created: 2026-04-11
updated: 2026-04-11
sources:
  - "[[ppv-pro-program]]"
tags:
  - ppv
  - productivity
  - workflows
  - notion
  - systems
---

# Specialty Pipeline (PPV)

Một database riêng trong [[ppv-system]] để quản lý luồng các **mini-project lặp lại với tần suất cao** — tách khỏi [[gpr-framework]] để tránh làm flood system với hàng chục mini-project nhỏ.

---

## Vấn đề cần giải quyết

[[gpr-framework]] được thiết kế cho goals, projects, routines có trọng lượng. Khi bạn có hoạt động lặp lại tần suất cao (ví dụ: sản xuất content mỗi tuần), mỗi lần là một mini-project riêng, nếu đưa tất cả vào GPR thì:

- Projects database bị flood → khó thấy projects thật sự
- Too small to set up formally in GPR
- But too important and complex to just track as single actions

---

## Tiêu chí sử dụng Specialty Pipeline

Sử dụng specialty pipeline khi hoạt động đáp ứng cả 3 tiêu chí:

| Tiêu chí | Mô tả |
|---|---|
| **Tần suất cao** | ≥ 2 lần/tháng (có thể hàng tuần) |
| **Nhiều bước** | 3+ tasks mỗi instance |
| **Cấu trúc tương đồng** | Các instance có cùng quy trình |

> Volume là yếu tố quyết định — không phải chỉ vì nó recurring. Nếu chỉ có 1–2 lần/tháng, GPR vẫn xử lý được.

**Giới hạn:** Chỉ nên có **1–2 specialty pipelines** trong hệ thống — nhiều hơn = thêm complexity không cần thiết.

---

## Ví dụ thực tế

- **Content Pipeline** — video, newsletter, bài viết; mỗi tuần có 2–5 pieces đang sản xuất
- **Client Pipeline** — onboarding, deliverables, check-ins cho mỗi khách hàng
- **Podcast Pipeline** — episodes từ idea → script → recording → edit → publish
- **Sales Pipeline** — leads từ prospect → proposal → close → onboarding

---

## Cấu trúc Content Pipeline (ví dụ cụ thể)

### Channels Database
Phân loại content theo kênh (YouTube, Newsletter, X, LinkedIn...). Mỗi channel là một category của pipeline.

### Ideas / Next Up Queue
- **Ideas:** Capture mọi idea mà chưa commit sản xuất
- **Next Up:** Những pieces đã được chọn để đưa vào production

### Production Pipeline (Board View)
Kanban board với các stages tùy chỉnh. Ví dụ cho video:
```
Idea → Research → Script → Recording → Editing → Ready to Post → Published
```
- Mỗi stage có thể assign owner (team member)
- Drag-and-drop để advance qua stages

### Calendar System
- **Scheduled date** — ngày dự định publish
- **Actual publish date** — ngày thực tế
- Publishing calendar view để nhìn tổng quan theo tháng

### Archive
Lưu trữ completed content — không xóa, giữ để phân tích performance và tái sử dụng.

---

## Tích hợp với Action Items Database

Ba phương pháp kết nối Content Pipeline với [[focus-zone]] Actions:

1. **Direct relational link** — link action trực tiếp từ content item; đơn giản nhất, phù hợp khi mỗi content chỉ có 1–2 actions
2. **Auto-create tasks** — tạo multiple tasks tự động từ template khi content item được tạo
3. **Inline tasks** — track tasks trong page của content item, không dùng relational link

---

## Tích hợp với [[neurobits]]

Ideas có thể được capture trước trong Neurobits, sau đó chuyển sang pipeline khi sẵn sàng sản xuất. Neurobits là "ideas holding area" — pipeline là "production queue."

---

## Specialty Pipeline vs. GPR Routine

| | GPR Routine | Specialty Pipeline |
|---|---|---|
| **Khi nào dùng** | Recurring behavior (exercise, weekly review) | High-freq multi-step production |
| **Granularity** | Single action level | Multi-step project level |
| **Volume** | Thấp | Cao (2+ instances/tuần) |
| **Tracking** | Yes/No completion | Stage progression |

---

## Liên quan

- [[ppv-system]]
- [[gpr-framework]]
- [[focus-zone]]
- [[neurobits]]
- [[ppv-pro-program]]
