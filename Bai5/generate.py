import os

base_dir = "/Users/jalong/web-vip-pro/BaitapBuoi5"

files = {
    "week5_prompts.md": """# Prompt Log - Tuần 5

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
""",
    "Bai1-FAB/index.html": """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài 1 - Floating Action Button</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <h1>Bài 1: Floating Action Button (FAB)</h1>
    <p>Cuộn trang hoặc nhìn xuống góc phải bên dưới để thấy nút FAB với hiệu ứng phập phồng (pulse).</p>

    <a href="#" class="fab">
        <i class="fab fa-facebook-messenger"></i>
    </a>
</body>
</html>""",
    "Bai1-FAB/style.css": """body {
    font-family: Arial, sans-serif;
    padding: 2rem;
    height: 150vh; /* Để có thể scroll */
    background-color: #f4f7f6;
}

.fab {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 60px;
    height: 60px;
    background-color: #0084ff;
    color: white;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
    text-decoration: none;
    box-shadow: 0 4px 10px rgba(0, 132, 255, 0.4);
    animation: pulse 1.5s ease-in-out infinite;
    z-index: 1000;
}

@keyframes pulse {
    0% {
        transform: scale(1);
        box-shadow: 0 0 0 0 rgba(0, 132, 255, 0.7);
    }
    50% {
        transform: scale(1.1);
        box-shadow: 0 0 0 15px rgba(0, 132, 255, 0);
    }
    100% {
        transform: scale(1);
        box-shadow: 0 0 0 0 rgba(0, 132, 255, 0);
    }
}""",
    "Bai2-CardFlip/index.html": """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài 2 - Card Flip Effect</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="card-container">
        <div class="card">
            <div class="card-front">
                <img src="https://via.placeholder.com/150" alt="Avatar" class="avatar">
                <h2>Nguyễn Văn A</h2>
                <p>Web Developer</p>
            </div>
            <div class="card-back">
                <h2>Liên hệ</h2>
                <div class="social-links">
                    <a href="#"><i class="fab fa-facebook"></i> Facebook</a>
                    <a href="#"><i class="fab fa-github"></i> GitHub</a>
                    <a href="#"><i class="fas fa-envelope"></i> Email</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>""",
    "Bai2-CardFlip/style.css": """body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #e0e5ec;
}

.card-container {
    perspective: 1000px;
}

.card {
    width: 300px;
    height: 400px;
    position: relative;
    transition: transform 0.6s;
    transform-style: preserve-3d;
    cursor: pointer;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    border-radius: 15px;
}

.card-container:hover .card {
    transform: rotateY(180deg);
}

.card-front, .card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
}

.card-front {
    background-color: white;
    color: #333;
}

.avatar {
    border-radius: 50%;
    width: 120px;
    height: 120px;
    object-fit: cover;
    margin-bottom: 20px;
    border: 4px solid #f0f0f0;
}

.card-front h2 { margin: 0 0 10px; }
.card-front p { margin: 0; color: #777; }

.card-back {
    background-color: #2c3e50;
    color: white;
    transform: rotateY(180deg);
}

.social-links {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-top: 20px;
    width: 100%;
}

.social-links a {
    color: white;
    text-decoration: none;
    font-size: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px;
    background: rgba(255,255,255,0.1);
    border-radius: 8px;
    transition: background 0.3s;
}

.social-links a:hover {
    background: rgba(255,255,255,0.2);
}""",
    "Bai3-Typing/index.html": """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài 3 - Typing Effect</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="typing-container">
        <h1 class="typing-text">Tôi là một Web Developer...</h1>
    </div>
</body>
</html>""",
    "Bai3-Typing/style.css": """body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color: #1a1a1a;
    font-family: 'Courier New', Courier, monospace;
    color: #00ff00;
}

.typing-container {
    display: inline-block;
}

.typing-text {
    overflow: hidden; /* Ẩn phần chữ chưa được gõ */
    white-space: nowrap; /* Giữ chữ trên một dòng */
    border-right: 3px solid #00ff00; /* Con trỏ nhấp nháy */
    margin: 0 auto;
    font-size: 2.5rem;
    letter-spacing: 2px;
    /* steps(27) vì "Tôi là một Web Developer..." có khoảng 27 ký tự */
    animation:
        typing 3.5s steps(27, end),
        blink-caret .75s step-end infinite;
}

@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

@keyframes blink-caret {
    from, to { border-color: transparent }
    50% { border-color: #00ff00; }
}""",
    "Bai4-Parallax/index.html": """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài 4 - Parallax Image</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <section class="normal-section">
        <h2>Cuộn xuống để xem hiệu ứng Parallax</h2>
        <p>Đây là nội dung bình thường trước phần parallax.</p>
    </section>

    <section class="parallax-section">
        <div class="parallax-content">
            <h2>Hiệu ứng Parallax Background</h2>
            <p>Ảnh nền cuộn chậm hơn nội dung.</p>
        </div>
    </section>

    <section class="normal-section">
        <h2>Nội dung tiếp theo</h2>
        <p>Trang web vẫn tiếp tục sau phần parallax. Hãy cuộn lên và cuộn xuống để cảm nhận độ sâu.</p>
    </section>
</body>
</html>""",
    "Bai4-Parallax/style.css": """body, html {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

.normal-section {
    height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    padding: 20px;
    text-align: center;
}

.parallax-section {
    position: relative;
    height: 80vh;
    display: flex;
    justify-content: center;
    align-items: center;

    /* Thiết lập Parallax */
    background-image: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

.parallax-section::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: rgba(0, 0, 0, 0.5); /* Lớp phủ làm tối ảnh */
}

.parallax-content {
    position: relative;
    z-index: 1;
    color: white;
    text-align: center;
}

.parallax-content h2 {
    font-size: 3rem;
    margin-bottom: 10px;
}

.parallax-content p {
    font-size: 1.5rem;
}""",
    "Bai5-Hamburger/index.html": """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài 5 - Modern Hamburger Menu</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="menu-container">
        <h2>Click vào biểu tượng Menu</h2>
        <div class="hamburger" id="hamburger-menu">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
        </div>
    </div>

    <script>
        const hamburger = document.getElementById('hamburger-menu');
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
        });
    </script>
</body>
</html>""",
    "Bai5-Hamburger/style.css": """body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
    background-color: #f0f2f5;
    font-family: sans-serif;
}

.menu-container {
    text-align: center;
}

.hamburger {
    width: 40px;
    height: 30px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    cursor: pointer;
    margin: 30px auto;
}

.bar {
    width: 100%;
    height: 4px;
    background-color: #333;
    border-radius: 4px;
    transition: all 0.4s ease;
    transform-origin: left center;
}

/* Khi có class active */
.hamburger.active .bar:nth-child(1) {
    transform: rotate(45deg);
    width: 42px; /* Điều chỉnh độ dài cho vừa dấu X */
}

.hamburger.active .bar:nth-child(2) {
    opacity: 0;
    transform: translateX(20px);
}

.hamburger.active .bar:nth-child(3) {
    transform: rotate(-45deg);
    width: 42px;
}""",
    "Bai6-SkillBar/index.html": """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bài 6 - Skill Bar Animation</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="skills-container">
        <h2>Kỹ năng của tôi</h2>

        <div class="skill-box">
            <div class="skill-info">
                <span>HTML</span>
                <span>90%</span>
            </div>
            <div class="progress-bg">
                <!-- Sử dụng CSS custom properties (variables) để truyền giá trị đích -->
                <div class="progress-bar" style="--target-width: 90%; background-color: #e34c26;"></div>
            </div>
        </div>

        <div class="skill-box">
            <div class="skill-info">
                <span>CSS</span>
                <span>85%</span>
            </div>
            <div class="progress-bg">
                <div class="progress-bar" style="--target-width: 85%; background-color: #264de4;"></div>
            </div>
        </div>

        <div class="skill-box">
            <div class="skill-info">
                <span>JavaScript</span>
                <span>75%</span>
            </div>
            <div class="progress-bg">
                <div class="progress-bar" style="--target-width: 75%; background-color: #f0db4f;"></div>
            </div>
        </div>
    </div>
</body>
</html>""",
    "Bai6-SkillBar/style.css": """body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    background-color: #2c3e50;
    font-family: Arial, sans-serif;
    color: white;
}

.skills-container {
    width: 100%;
    max-width: 500px;
    background: #34495e;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

h2 {
    text-align: center;
    margin-bottom: 30px;
}

.skill-box {
    margin-bottom: 25px;
}

.skill-info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 8px;
    font-weight: bold;
}

.progress-bg {
    width: 100%;
    height: 12px;
    background-color: #1a252f;
    border-radius: 10px;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    width: 0; /* Khởi tạo bằng 0 */
    border-radius: 10px;
    /* Sử dụng biến var(--target-width) được truyền từ HTML */
    animation: fillBar 2s ease-out forwards;
}

@keyframes fillBar {
    from {
        width: 0;
    }
    to {
        width: var(--target-width);
    }
}"""
}

for filepath, content in files.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Đã tạo xong tất cả các file cho Bài tập tuần 5!")
