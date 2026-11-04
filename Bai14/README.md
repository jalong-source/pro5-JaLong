# ĐỒ ÁN NHÓM: LHU STUDENT PORTAL (HỆ THỐNG QUẢN LÝ HỌC VỤ & LỘ TRÌNH HỌC TẬP)
## Học phần 111101 · Thiết Kế Web — Đại học Lạc Hồng (LHU)

### 1. Thông tin nhóm dự án
* **Tên nhóm:** Vibe Devs (Scrum Team LHU)
* **Thành viên & Phân vai:**
  * **Trần Gia Long (Scrum Master / UI-UX Lead):** Điều phối Sprint, thiết kế cấu trúc thư mục, Semantic Layout, CSS System (`index.html`, `style.css`, `portal.html`).
  * **Thành viên A (Data & Pure Logic Developer):** Xây dựng hợp đồng dữ liệu `data.js`, thuật toán quy đổi điểm hệ 4 và hàm `tinhGPA()` trong `logic.js`.
  * **Thành viên B (Feature Master & DOM Interaction):** Xử lý giỏ hàng đăng ký môn học, kiểm soát giới hạn tín chỉ <= 25, bộ lọc tìm kiếm môn và cảnh báo học vụ.

---

### 2. Mô tả bài toán & Giải pháp thực tế
* **Chủ đề 2.1:** Hệ thống Quản lý Học vụ (Student Portal) - Trường Đại học Lạc Hồng.
* **Vấn đề giải quyết:** Hỗ trợ sinh viên LHU theo dõi kết quả học tập trực quan, tự động tính điểm GPA hệ 4, cảnh báo học vụ sớm (GPA < 2.0) và thực hiện đăng ký môn học theo thời gian thực không tải lại trang.

---

### 3. Cấu trúc mã nguồn chuẩn (Repository Standard - Phụ lục 3)
```
Bai14/
├── index.html            # Trang mục lục điều hướng Tuần 14
├── portal.html           # Website hoàn chỉnh sản phẩm LHU Student Portal
├── hoatdong1.html        # Daily Stand-up & Agile DoD Checklist
├── hoatdong2.html        # JavaScript Vibe Logic (Tính GPA & Cảnh báo học vụ)
├── hoatdong3.html        # Đóng gói sản phẩm & Hướng dẫn phát hành
├── style.css             # Hệ thống Design System CSS Variables
├── data.js               # Hợp đồng dữ liệu chung (Shared Data Contract)
├── logic.js              # Các hàm xử lý tính toán thuần túy (Pure Functions)
├── README.md             # Giới thiệu đồ án & hướng dẫn
└── prompt_log.md         # Nhật ký Prompt Vibe Coding
```

---

### 4. Top 5 Prompts đắt giá nhất điều khiển AI trong dự án
1. *"Hãy đóng vai chuyên gia Agile Scrum, giúp nhóm chia dự án LHU Student Portal thành 5 User Stories rõ ràng cho Sprint 1 & Sprint 2."*
2. *"Viết hàm JavaScript tính điểm trung bình tích lũy GPA dựa trên mảng môn học, quy đổi thang điểm 10 sang thang điểm 4 theo học chế tín chỉ LHU."*
3. *"Hãy viết mã kiểm tra: Nếu GPA < 2.0 thì tự động hiển thị thông báo Cảnh báo học vụ màu đỏ nổi bật."*
4. *"Xây dựng tính năng giỏ hàng môn học bằng JavaScript: Thêm/Xóa môn học, tự động tính học phí và ngăn chặn nếu tổng tín chỉ vượt quá 25."*
5. *"Refactor lại toàn bộ code JS thành mô hình tách biệt: data.js (dữ liệu), logic.js (hàm thuần túy) và controller DOM để tránh xung đột khi làm việc nhóm."*

---

### 5. Hướng dẫn chạy sản phẩm
* Mở trực tiếp file `portal.html` trên bất kỳ trình duyệt nào (Chrome, Edge, Safari).
* Tương tác tìm kiếm môn học, tính GPA hoặc click chọn đăng ký môn để xem cập nhật thời gian thực.
