# Prompt Log - Tuần 5

Dưới đây là nhật ký các prompt đã sử dụng để tạo và tinh chỉnh các hiệu ứng CSS:

## Bài 1: Floating Action Button (FAB)
- **Prompt gốc:** "Hãy tạo một nút tròn cố định ở góc dưới bên phải màn hình. Sử dụng CSS Animation để tạo hiệu ứng 'phập phồng' (pulse) co giãn liên tục và mượt mà. Nút có màu xanh, đổ bóng và biểu tượng nằm chính giữa."
- **Tinh chỉnh:** "Làm cho hiệu ứng pulse mượt hơn bằng cách điều chỉnh thời gian duration lên 1.5s và dùng ease-in-out."

## Bài 2: Card Flip Effect
- **Prompt gốc:** "Tạo hiệu ứng lật thẻ (Card Flip) bằng CSS. Khi hover vào thẻ, nó sẽ xoay 180 độ theo trục Y để hiện mặt sau. Đảm bảo hiệu ứng có chiều sâu 3D và mượt mà."
- **Tinh chỉnh:** "Thêm bóng đổ cho thẻ và làm cho mặt sau có màu nền khác biệt. Chỉnh transition thành 0.6s."

## Bài 3: Typing Effect
- **Prompt gốc:** "Hãy viết mã CSS tạo hiệu ứng máy đánh chữ (Typing effect) cho một thẻ h1. Chữ sẽ xuất hiện dần dần từ trái sang phải, kèm theo con trỏ nhấp nháy ở cuối dòng chữ. Không sử dụng JavaScript."
- **Tinh chỉnh:** "Điều chỉnh số steps() trong animation sao cho khớp với số lượng ký tự của chuỗi văn bản để chữ hiện ra đều đặn hơn."

## Bài 4: Parallax Background
- **Prompt gốc:** "Hướng dẫn cách tạo hiệu ứng Parallax đơn giản cho một Section bằng CSS. Khi cuộn trang, ảnh nền phải giữ cố định hoặc di chuyển chậm hơn nội dung phía trên. Hãy đảm bảo ảnh hiển thị tốt trên cả Desktop và Mobile."
- **Tinh chỉnh:** "Đảm bảo background-size là cover và background-position là center. Thêm một lớp phủ (overlay) tối màu để chữ dễ đọc hơn."

## Bài 5: Modern Hamburger Menu
- **Prompt gốc:** "Tạo hiệu ứng chuyển đổi biểu tượng Hamburger (3 gạch) thành dấu X bằng CSS Transition. Khi tôi thêm class 'active' vào container, thanh trên cùng xoay 45 độ, thanh giữa biến mất, và thanh dưới xoay -45 độ."
- **Tinh chỉnh:** "Chỉnh origin xoay (transform-origin) và căn chỉnh lại vị trí để khi tạo thành dấu X thì 2 thanh giao nhau ngay chính giữa."

## Bài 6: Skill Bar Animation
- **Prompt gốc:** "Viết CSS cho các thanh tiến trình (Progress bars) hiển thị kỹ năng. Khi trang được tải, các thanh này sẽ chạy từ 0% đến mức phần trăm cụ thể (ví dụ 80%) trong vòng 2 giây với hiệu ứng mượt mà."
- **Tinh chỉnh:** "Thêm hiệu ứng ease-out để thanh chạy chậm dần khi gần đến đích. Thêm con số phần trăm xuất hiện cùng lúc."
