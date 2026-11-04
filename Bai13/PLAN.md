# KẾ HOẠCH DỰ ÁN PBL — TUẦN 13: PLANNING & PROTOTYPING
## Đề tài: LHU Student Portal — Hệ thống Quản lý Học vụ & Lộ trình Học tập Thông minh

> **Lớp:** Thiết kế Web 111101 · Trường Đại học Lạc Hồng (LHU)  
> **Nhóm thực hiện:** Scrum Team Vibe Devs  
> **Scrum Master:** Trần Gia Long  
> **Phương pháp triển khai:** Project-Based Learning (PBL) kết hợp Agile/Scrum Sprint 1

---

### 1. Phân tích bài toán thực tế (Driving Question)
* **Vấn đề:** Sinh viên LHU hiện nay cần một giao diện tập trung để tra cứu nhanh tiến độ học tập, tự tính GPA tích lũy, kiểm tra điều kiện cảnh báo học vụ và mô phỏng đăng ký môn học trực quan.
* **Giải pháp:** Xây dựng cổng thông tin **LHU Student Portal** với giao diện hiện đại chuẩn màu sắc LHU (Xanh lam & Trắng), chia module theo cấu trúc tách biệt giữa Dữ liệu (`data.js`), Giao diện (`ui.js`) và Logic (`app.js`).

---

### 2. Danh sách User Stories (Product Backlog - Sprint 1)
1. **US01 (UI/UX):** Là một sinh viên, tôi muốn xem giao diện Dashboard tổng quan với thanh điều hướng (Sidebar/Navbar) đồng nhất để dễ dàng chuyển đổi các phân hệ.
2. **US02 (Data Contract):** Là nhà phát triển, tôi muốn cấu trúc dữ liệu sinh viên và môn học được chuẩn hóa trong file `data.js` để nhóm phối hợp không bị đè code.
3. **US03 (Progress Bar):** Là một sinh viên, tôi muốn xem thanh tiến độ hoàn thành tín chỉ và biểu đồ cột trực quan bằng CSS thuần.
4. **US04 (Wireframing):** Là đội ngũ Scrum, chúng tôi muốn có bản vẽ khung giao diện (Wireframe) để thống nhất bố cục trước khi bước vào Sprint 2.
5. **US05 (Repository Standard):** Là đội ngũ Scrum, chúng tôi tuân thủ cấu trúc kho lưu trữ Phụ lục 3 với các nhánh `develop`, `feature/planning-core-ui`.

---

### 3. Phân chia vai trò nhóm (Scrum Roles & Module)
* **Dev 1 (UI/UX Designer):** Trần Gia Long — Phụ trách Layout tổng thể, Sidebar, Navbar, CSS Variables (`style.css`, `index.html`).
* **Dev 2 (Data Logic):** Thành viên A — Phụ trách cấu trúc `data.js`, hàm tính toán GPA và tín chỉ.
* **Dev 3 (Feature Master):** Thành viên B — Phụ trách liên kết sự kiện DOM, render danh sách môn học và wireframe.
