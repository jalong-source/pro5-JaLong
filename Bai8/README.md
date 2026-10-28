# BÁO CÁO THỰC HÀNH TUẦN 8: JAVASCRIPT FUNDAMENTALS & TƯ DUY LOGIC AI-FIRST

> **Học phần:** 111101 · Thiết Kế Web — Đại học Lạc Hồng  
> **Sinh viên:** Gia Long (Ja Long)  
> **Thư mục bài tập:** `Bai8/`

---

## 📌 HOẠT ĐỘNG 1: "Hello JS Console" — Đối thoại với trình duyệt (30 phút)

### 1. Mã lệnh thực hành trực tiếp trên tab Console (F12)

```javascript
// 1. Khai báo biến với let và const
const myName = "Gia Long";       // Kiểu String (Chuỗi)
let myAge = 20;                 // Kiểu Number (Số)
const isStudent = true;         // Kiểu Boolean (Đúng/Sai)

console.log("Họ tên:", myName);
console.log("Tuổi:", myAge);
console.log("Là sinh viên:", isStudent);

// 2. Thực hiện các phép toán cơ bản (+, -, *, /, %)
let a = 25;
let b = 5;

console.log("Tổng a + b =", a + b);     // 30
console.log("Hiệu a - b =", a - b);     // 20
console.log("Tích a * b =", a * b);     // 125
console.log("Thương a / b =", a / b);   // 5
console.log("Chia lấy dư 27 % 5 =", 27 % 5); // 2
```

---

### 2. Vibe Coding: Giải thích "Tại sao khi cộng '10' + 20 trong JS lại ra '1020' mà không phải 30?"

* **Bản chất vấn đề:**  
  Trong JavaScript, toán tử cộng (`+`) là một toán tử đa năng:
  1. **Phép cộng số học (Addition):** Được kích hoạt khi **cả hai vế** đều là kiểu `Number`. Ví dụ: `10 + 20 = 30`.
  2. **Phép nối chuỗi (String Concatenation):** Được kích hoạt khi **có ít nhất một trong hai vế** là kiểu `String`.

* **Cơ chế Ép kiểu ngầm định (Type Coercion):**  
  Khi thực hiện `'10' + 20`, toán hạng bên trái `'10'` là kiểu chuỗi (String). Trình thông dịch JavaScript ưu tiên biến đổi số `20` thành chuỗi `"20"`. Phép toán trở thành:
  $$\text{"10"} + \text{"20"} = \text{"1020"}$$

* **Cách khắc phục để tính ra kết quả 30:**  
  Cần chủ động ép chuỗi `'10'` về kiểu số trước khi thực hiện phép tính:
  ```javascript
  Number('10') + 20;     // 30 (Cách chuẩn)
  parseInt('10') + 20;   // 30 (Lấy số nguyên)
  +'10' + 20;            // 30 (Dùng toán tử unary plus)
  ```

---

## 📌 HOẠT ĐỘNG 2: "Logic Builder" — Máy tính mini / Kiểm tra xếp loại (45 phút)

### 1. Mã nguồn JavaScript hoàn chỉnh (Sử dụng `prompt()`, `if-else`, `alert()`)

```javascript
function kiemTraDiem() {
  // 1. Nhận giá trị nhập từ người dùng
  let input = prompt("Nhập điểm số của bạn (từ 0 đến 10):");

  // Xử lý khi người dùng nhấn "Hủy" hoặc không nhập gì
  if (input === null || input.trim() === "") {
    alert("Bạn đã hủy thao tác hoặc chưa nhập điểm!");
    return;
  }

  // Chuyển đổi dữ liệu chuỗi sang số thực
  let score = parseFloat(input);

  // 2. Kiểm tra dữ liệu có hợp lệ hay không
  if (isNaN(score) || score < 0 || score > 10) {
    alert("Điểm không hợp lệ! Vui lòng nhập số thực từ 0 đến 10.");
    return;
  }

  // 3. Cấu trúc rẽ nhánh if - else if - else xếp loại học tập
  let rank = "";
  let feedback = "";

  if (score > 8.0) {
    rank = "Giỏi 🌟";
    feedback = "Chúc mừng bạn đạt kết quả xuất sắc!";
  } else if (score > 6.5) {
    rank = "Khá 👍";
    feedback = "Làm tốt lắm, tiếp tục phát huy nhé!";
  } else if (score >= 5.0) {
    rank = "Trung bình (Đạt) 👏";
    feedback = "Chúc mừng bạn đã đạt!";
  } else {
    rank = "Yếu 📚";
    feedback = "Rất tiếc, hãy cố gắng hơn ở lần sau!";
  }

  // 4. Hiển thị thông báo bằng alert() và log vào Console
  let resultMsg = `Điểm số của bạn: ${score}\nXếp loại: ${rank}\nĐánh giá: ${feedback}`;
  alert(resultMsg);
  console.log(resultMsg);
}

// Gọi hàm để chạy
kiemTraDiem();
```

---

## 📌 HOẠT ĐỘNG 3: "AI Logic Explainer" (30 phút)

Dưới đây là 3 ca lỗi logic thực tế mà lập trình viên mới bắt đầu với JavaScript thường gặp, kèm theo phân tích luồng chạy (step-by-step trace):

### Case 1: Lỗi đảo lộn thứ tự điều kiện trong chuỗi `if-else`

```javascript
// ❌ ĐOẠN MÃ LỖI:
let diem = 9.5;

if (diem >= 5.0) {
  console.log("Trung bình");
} else if (diem > 8.0) {
  console.log("Giỏi");
}
// Kết quả in ra: "Trung bình" (Dù 9.5 phải là Giỏi)
```

* **🤖 AI giải thích luồng chạy từng bước:**
  1. Biến `diem` nhận giá trị số thực `9.5`.
  2. Trình thông dịch kiểm tra điều kiện `if` đầu tiên: `diem >= 5.0`.
  3. Biểu thức `9.5 >= 5.0` trả về giá trị `true`.
  4. Khối lệnh bên trong `if` được kích hoạt ngay lập tức: In ra `"Trung bình"`.
  5. Vì nhánh `if` đã thỏa mãn, JavaScript bỏ qua toàn bộ nhánh `else if (diem > 8.0)` phía sau.
* **✔ Cách sửa:** Khi so sánh theo ngưỡng lớn dần, luôn đặt điều kiện có độ chặt chẽ cao nhất lên đầu (từ lớn xuống bé: `> 8.0` trước, rồi mới tới `> 6.5`, `>= 5.0`).

---

### Case 2: Cạm bẫy so sánh lỏng lẻo (`==`) so với nghiêm ngặt (`===`)

```javascript
// ❌ ĐOẠN MÃ GÂY BỐI RỐI:
console.log(0 == "");     // Kết quả: true
console.log(0 == "0");    // Kết quả: true
console.log("" == "0");   // Kết quả: false
```

* **🤖 AI giải thích luồng chạy từng bước:**
  * `0 == ""` ra `true`: Toán tử `==` tự động ép chuỗi rỗng `""` về số `0`. Mà `0 == 0` là `true`.
  * `0 == "0"` ra `true`: Chuỗi `"0"` bị ép kiểu về số `0`. `0 == 0` là `true`.
  * `"" == "0"` ra `false`: Cả hai vế đều là chuỗi, nên JS không ép kiểu mà so sánh ký tự. Chuỗi rỗng độ dài bằng 0, chuỗi `"0"` có ký tự mã ASCII `48`, khác nhau nên trả về `false`.
* **✔ Quy chuẩn thực tế:** Luôn sử dụng toán tử so sánh nghiêm ngặt `===` (so sánh cả giá trị và kiểu dữ liệu) để kiểm soát triệt để logic: `0 === ""` sẽ trả về `false`.

---

### Case 3: Lỗi quên ép kiểu khi nhận dữ liệu từ `prompt()`

```javascript
// ❌ ĐOẠN MÃ LỖI:
let a = prompt("Nhập số a:"); // Người dùng nhập: 5
let b = prompt("Nhập số b:"); // Người dùng nhập: 10
let tong = a + b;
alert("Tổng là: " + tong);    // Ra "510" thay vì 15!
```

* **🤖 AI giải thích:**  
  Hàm `prompt()` luôn trả về giá trị kiểu chuỗi (`String`). Do đó biến `a` là `"5"` và biến `b` là `"10"`. Toán tử `+` thực hiện nối hai chuỗi lại thành `"510"`.
* **✔ Cách sửa:** Sử dụng `parseFloat()` hoặc `Number()`:
  ```javascript
  let tong = parseFloat(a) + parseFloat(b); // Kết quả: 15
  ```



---

# 📚 BÀI TẬP TỰ RÈN LUYỆN TẠI NHÀ (HOMEWORK TUẦN 8)

> **File giao diện tương tác trực tiếp:** [homework.html](file:///Users/jalong/Mon%20Thiet%20Ke%20Web/pro5-JaLong/Bai8/homework.html)

---

## 🟢 Bài 1: Chuyển đổi tiền tệ đơn giản (USD ➔ VND)

### Đề bài:
Viết mã JS cho phép nhập số lượng USD và tính ra số tiền VND tương ứng (giả sử tỉ giá 25.000). Kết quả hiện ra console.

### Mã nguồn JavaScript:
```javascript
function doiTienUSD() {
  const TI_GIA = 25000;
  let usd = parseFloat(prompt("Nhập số tiền USD cần đổi:"));

  if (isNaN(usd) || usd < 0) {
    console.log("Số tiền USD không hợp lệ!");
    alert("Số tiền USD không hợp lệ!");
    return;
  }

  let vnd = usd * TI_GIA;
  let ketQua = `${usd} USD = ${vnd.toLocaleString('vi-VN')} VNĐ`;
  console.log(ketQua);
  alert(ketQua);
}

doiTienUSD();
```

---

## 🟢 Bài 2: Kiểm tra số chẵn / số lẻ

### Đề bài:
Nhập một số bất kỳ từ bàn phím. Thông báo cho người dùng biết đó là số chẵn hay số lẻ.

### Mã nguồn JavaScript:
```javascript
function kiemTraChanLe() {
  let input = prompt("Nhập một số nguyên bất kỳ:");
  if (input === null || input.trim() === "") return;

  let n = parseInt(input);
  if (isNaN(n)) {
    alert("Vui lòng nhập một số hợp lệ!");
    return;
  }

  // Sử dụng toán tử chia lấy dư % 2
  if (n % 2 === 0) {
    console.log(`Số ${n} là số chẵn.`);
    alert(`Số ${n} là SỐ CHẴN.`);
  } else {
    console.log(`Số ${n} là số lẻ.`);
    alert(`Số ${n} là SỐ LẺ.`);
  }
}

kiemTraChanLe();
```

---

## 🟢 Bài 3: Tính chỉ số BMI cơ bản

### Đề bài:
Nhập chiều cao (m) và cân nặng (kg). Tính $BMI = \text{cân nặng} / (\text{chiều cao} \times \text{chiều cao})$ và in ra kết quả.

### Mã nguồn JavaScript:
```javascript
function tinhBMI() {
  let chieuCao = parseFloat(prompt("Nhập chiều cao của bạn (mét - ví dụ: 1.70):"));
  let canNang = parseFloat(prompt("Nhập cân nặng của bạn (kg - ví dụ: 65):"));

  if (isNaN(chieuCao) || isNaN(canNang) || chieuCao <= 0 || canNang <= 0) {
    alert("Chiều cao và cân nặng phải là số dương hợp lệ!");
    return;
  }

  let bmi = canNang / (chieuCao * chieuCao);
  let status = "";
  if (bmi < 18.5) status = "Gầy (Thiếu cân)";
  else if (bmi < 24.9) status = "Bình thường (Cân đối)";
  else if (bmi < 29.9) status = "Tiền béo phì (Thừa cân)";
  else status = "Béo phì";

  let msg = `BMI: ${bmi.toFixed(2)} - Tình trạng: ${status}`;
  console.log(msg);
  alert(msg);
}

tinhBMI();
```

---

## 🟢 Bài 4: Logic Đăng nhập (Mô phỏng)

### Đề bài:
Tạo 2 biến `username` và `password` cố định. Viết cấu trúc `if` kiểm tra nếu người dùng nhập đúng cả 2 thì hiện "Đăng nhập thành công", nếu sai 1 trong 2 thì hiện "Thông tin không chính xác".

### Mã nguồn JavaScript:
```javascript
function dangNhap() {
  const USER_NAME_CHUAN = "admin";
  const PASSWORD_CHUAN = "123456";

  let inputUser = prompt("Nhập username:");
  let inputPass = prompt("Nhập password:");

  // Sử dụng toán tử logic && (VÀ)
  if (inputUser === USER_NAME_CHUAN && inputPass === PASSWORD_CHUAN) {
    console.log("Đăng nhập thành công");
    alert("Đăng nhập thành công! Chào mừng bạn.");
  } else {
    console.log("Thông tin không chính xác");
    alert("Thông tin không chính xác!");
  }
}

dangNhap();
```

---

## 🟢 Bài 5: Máy tính giảm giá (Discount Calculator)

### Đề bài:
Nhập số tiền hóa đơn. Nếu số tiền > 500.000đ thì giảm giá 10%, ngược lại không giảm. Tính số tiền cuối cùng phải trả.

### Mã nguồn JavaScript:
```javascript
function tinhGiamGia() {
  let tongTien = parseFloat(prompt("Nhập tổng số tiền hóa đơn (VNĐ):"));

  if (isNaN(tongTien) || tongTien < 0) {
    alert("Số tiền hóa đơn không hợp lệ!");
    return;
  }

  let giamGia = 0;
  if (tongTien > 500000) {
    giamGia = tongTien * 0.10; // Giảm 10%
  }

  let thanhToan = tongTien - giamGia;
  let msg = `Hóa đơn gốc: ${tongTien.toLocaleString('vi-VN')} VNĐ\n` +
            `Giảm giá: ${giamGia.toLocaleString('vi-VN')} VNĐ\n` +
            `Số tiền cần thanh toán: ${thanhToan.toLocaleString('vi-VN')} VNĐ`;

  console.log(msg);
  alert(msg);
}

tinhGiamGia();
```

---

## 🟢 Bài 6: Phân loại tam giác (Kiểm tra tam giác đều)

### Đề bài:
Nhập vào 3 cạnh của một tam giác. Kiểm tra xem đó có phải là tam giác đều không (3 cạnh bằng nhau).

### Mã nguồn JavaScript:
```javascript
function kiemTraTamGiac() {
  let a = parseFloat(prompt("Nhập cạnh a:"));
  let b = parseFloat(prompt("Nhập cạnh b:"));
  let c = parseFloat(prompt("Nhập cạnh c:"));

  // 1. Kiểm tra cạnh dương hợp lệ
  if (isNaN(a) || isNaN(b) || isNaN(c) || a <= 0 || b <= 0 || c <= 0) {
    alert("Độ dài các cạnh phải là số dương hợp lệ!");
    return;
  }

  // 2. Kiểm tra bất đẳng thức tam giác
  if (a + b <= c || a + c <= b || b + c <= a) {
    alert("Ba cạnh này KHÔNG thể tạo thành một hình tam giác!");
    return;
  }

  // 3. Kiểm tra tam giác đều (cả 3 cạnh bằng nhau)
  if (a === b && b === c) {
    console.log("Đây là tam giác đều.");
    alert(`Ba cạnh (${a}, ${b}, ${c}) tạo thành: TAM GIÁC ĐỀU! 🔺`);
  } else {
    console.log("Không phải tam giác đều.");
    alert(`Ba cạnh (${a}, ${b}, ${c}) là tam giác nhưng KHÔNG PHẢI tam giác đều.`);
  }
}

kiemTraTamGiac();
```
