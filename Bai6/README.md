# Bài tập Buổi 6 · Animation & Smart Components

Portfolio dự án mẫu thực hành hai tương tác: hiệu ứng reveal khi cuộn bằng AOS và bộ lọc dự án theo Web/Mobile. Nội dung gồm sáu ý tưởng minh họa, không phải sáu sản phẩm đã phát hành.

## Chạy trang

Mở `index.html` hoặc chạy server từ thư mục gốc repository:

```sh
python3 -m http.server 8006 --directory BaitapBuoi6
```

Truy cập `http://localhost:8006`. AOS và Google Fonts được tải từ CDN; bộ lọc vẫn chạy bằng JavaScript thuần. Nếu script AOS không tải, mã bỏ thuộc tính `data-aos` để nội dung không bị ẩn.

## Tương tác

- Nút **Tất cả**, **Web**, **Mobile** lọc theo `data-category`.
- `aria-pressed` phản ánh nút đang chọn; vùng `role="status"` thông báo số thẻ còn hiển thị.
- Các phần hero, project card và phần giới thiệu có `data-aos`, `data-aos-duration` hoặc `data-aos-delay`.
- Cài đặt `prefers-reduced-motion` tắt AOS và giảm chuyển động trong CSS.

## Tự kiểm tra

- [ ] Chọn từng bộ lọc và xác nhận số lượng lần lượt 6, 3, 3.
- [ ] Dùng Tab/Enter/Space để thao tác bộ lọc.
- [ ] Kiểm tra ở màn hình mobile; xác nhận trang không tràn ngang.
- [ ] Chặn CDN AOS và xác nhận nội dung vẫn hiện.
- [ ] Chạy HTML qua W3C Nu HTML Checker.

## Prompt log

Các prompt khởi tạo và kiểm tra được lưu trong `prompt.txt`. Hãy cập nhật nếu có prompt khác được dùng trong quá trình làm bài.
