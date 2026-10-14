# Buổi 1 · Biệt thự Web

Bài thực hành khởi động của học phần **111101 · Thiết kế Web**. Landing page “Hello World” giúp nhóm làm quen môi trường, Git/GitHub và cách chia việc trên các nhánh riêng.

## Thành viên và dự án nhóm

- Chủ đề nhóm: `[Điền chủ đề được bốc thăm]`
- Leader: `[Tên thành viên]`
- Member A: `[Tên thành viên]`
- Member B: `[Tên thành viên]`
- Repository nhóm: `[Dán URL GitHub sau khi tạo]`
- GitHub Project: `[Dán URL bảng Kanban sau khi tạo]`

## Chạy trang

Mở `index.html` trực tiếp hoặc chạy server trong thư mục gốc repository:

```sh
python3 -m http.server 8000 --directory BaitapBuoi1
```

Mở `http://localhost:8000` trên trình duyệt. Nút “Gửi lời chào” là ví dụ tương tác JavaScript nhỏ.

## Kiểm tra môi trường

- [ ] VS Code và Git đã cài đặt.
- [ ] Cài các AI extension theo hướng dẫn của giảng viên (Gemini Assist Code, GitHub Copilot Chatbot, Google Anti-Gravity/Vibe Code nếu được yêu cầu).
- [ ] Đăng nhập GitHub trong VS Code.
- [ ] Cấu hình thông tin commit cho tài khoản của mình:

```sh
git config --global user.name "Tên của bạn"
git config --global user.email "email-github-của-bạn"
git config --global --get user.name
git config --global --get user.email
```

- [ ] AI hỗ trợ tạo mã Hello World và trang hiển thị thành công trong trình duyệt.

## Thử thách Git nhanh

Mỗi thành viên nên thao tác bằng tài khoản Git riêng để lịch sử commit thể hiện đúng người tham gia.

1. Leader tạo repository nhóm trên GitHub, push landing page ban đầu lên `main`.
2. Leader tạo nhánh tích hợp `develop` từ `main` và push nhánh:

```sh
git switch -c develop
git push -u origin develop
```

3. Member A và Member B clone repository, track `origin/develop`, rồi tạo nhánh cá nhân:

```sh
git clone [URL-REPOSITORY]
cd [TEN-REPOSITORY]
git fetch origin
git switch --track origin/develop
git switch -c feature/member-a-yard
```

Member B dùng tên `feature/member-b-yard`. Hai thành viên làm phần sân của mình; để mô phỏng conflict, cả hai cùng sửa đúng phần tử `#shared-conflict-line` trong `index.html` theo nội dung khác nhau.

4. Member A commit và gửi Pull Request vào `develop`; Leader review rồi merge trước. Member B đã tạo nhánh từ `develop` trước khi Member A merge, sau đó cập nhật nhánh của mình để Git báo conflict:

```sh
git switch feature/member-b-yard
git fetch origin
git merge origin/develop
```

5. Mở `index.html` trong VS Code, dùng nút chọn thay đổi để kết hợp ý của hai thành viên. Đảm bảo đã xóa các dấu `<<<<<<<`, `=======`, `>>>>>>>`; sau đó kiểm tra trang, commit kết quả và gửi Pull Request vào `develop`.

Đoạn dùng để thực hành là phần tử `#shared-conflict-line`. Ví dụ nội dung cuối sau khi kết hợp: “Sân trước có lối đi và bồn hoa; sân sau là góc nghỉ ngơi dưới tán cây.”

## Dự án xuyên suốt và Kanban

Tạo Organization/repository chung theo phân công của nhóm hoặc giảng viên. Trong GitHub Projects, tạo board dạng Kanban với các cột **To Do**, **In Progress**, **Review**, **Done**. Tạo và giao ít nhất ba task đầu tiên; ví dụ:

| Task | Người nhận | Trạng thái |
| --- | --- | --- |
| Tạo semantic skeleton và README dự án | Leader | To Do |
| Xây section giới thiệu/chủ đề | Member A | To Do |
| Xây section nội dung thứ hai và kiểm tra responsive | Member B | To Do |

Thay tên, task và trạng thái theo chủ đề thực tế. Link repository và Project ở phần đầu README cần được nhóm điền sau khi tạo; workspace này không tự tạo Organization hay board trên GitHub.

## Cấu trúc

```text
BaitapBuoi1/
├── README.md
├── prompt.txt
├── index.html
├── assets/
│   └── README.md
├── css/
│   └── style.css
└── js/
    └── app.js
```

## Checklist nộp bài

- [ ] Hoàn thiện cấu trúc và push lên nhánh `develop` của repository nhóm.
- [ ] Điền URL repository và GitHub Project ở README.
- [ ] Board có đủ To Do, In Progress, Review, Done và ít nhất ba task được giao.
- [ ] Lịch sử commit có đóng góp từ Leader, Member A và Member B.
- [ ] Đã tạo conflict có chủ đích, giải quyết và kiểm tra trang sau khi merge.
- [ ] `prompt.txt` lưu prompt đã dùng; cập nhật lại nếu nhóm dùng thêm prompt.
