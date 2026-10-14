# Bài tập Buổi 2 · Bản sắc cá nhân

Trang giới thiệu cá nhân tập trung vào cấu trúc Semantic HTML5 và thông tin cơ bản phục vụ SEO. Nội dung lấy từ portfolio hiện có trong workspace; trang mẫu giao diện cụ thể không được đính kèm, nên đây là bản dựng độc lập thay vì bản sao pixel-perfect.

## Chạy trang

Mở `index.html` trực tiếp hoặc chạy từ thư mục gốc repository:

```sh
python3 -m http.server 8002 --directory BaitapBuoi2
```

Truy cập `http://localhost:8002`.

## Cấu trúc semantic

- `header` chứa thương hiệu và `nav` điều hướng.
- `main` chứa nội dung chính; `section` được đặt tên bằng heading và `aria-labelledby`.
- `article` dùng cho từng dự án độc lập; `aside` dành cho ghi chú bổ sung.
- `figure` và `figcaption` nhóm ảnh chân dung với chú thích.
- `footer` chứa thông tin học phần và điều hướng trở về đầu trang.
- `title`, `meta description`, `lang="vi"`, alt ảnh và liên kết bỏ qua điều hướng hỗ trợ SEO/accessibility cơ bản.

## Tự kiểm tra

- [ ] Nội dung vẫn có thứ tự hợp lý khi tắt CSS.
- [ ] Heading đi theo cấp bậc, không chọn cấp chỉ vì kích thước.
- [ ] Tất cả `href` trỏ đến ID có thật.
- [ ] Ảnh chân dung tải từ `assets/gia-long.jpg` và có alt phù hợp.
- [ ] Kiểm tra trên desktop và mobile; chạy HTML qua W3C Nu HTML Checker.

## Prompt tham khảo

Prompt đã lưu tại `prompt.txt`. Hãy cập nhật lại prompt theo ảnh giao diện thật và thông tin chính xác của bạn trước khi nộp.
