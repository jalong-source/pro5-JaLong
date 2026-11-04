// Pure Functions (Dev 2 - Data Logic) - Tuần 14
// Quy đổi thang điểm 10 sang thang điểm 4 theo chuẩn học chế tín chỉ LHU
function quyDoiHe4(diem10) {
  if (diem10 >= 8.5) return 4.0; // A
  if (diem10 >= 7.0) return 3.0; // B
  if (diem10 >= 5.5) return 2.0; // C
  if (diem10 >= 4.0) return 1.0; // D
  return 0.0;                    // F
}

// Xếp loại học lực theo GPA hệ 4
function xepLoaiHocLuc(gpa4) {
  if (gpa4 >= 3.6) return { loai: "Xuất sắc", badge: "badge-excellent", warning: false };
  if (gpa4 >= 3.2) return { loai: "Giỏi", badge: "badge-good", warning: false };
  if (gpa4 >= 2.5) return { loai: "Khá", badge: "badge-fair", warning: false };
  if (gpa4 >= 2.0) return { loai: "Trung bình", badge: "badge-average", warning: false };
  return { loai: "Yếu / Kém", badge: "badge-warning", warning: true };
}

// Tính điểm trung bình tích lũy (GPA) hệ 4 có trọng số tín chỉ
function tinhGPA(courses) {
  if (!courses || courses.length === 0) return { gpa4: 0, totalCredits: 0, passedCourses: 0, failedCourses: 0 };
  
  let tongDiemNhanTinChi = 0;
  let tongTinChi = 0;
  let passed = 0;
  let failed = 0;

  courses.forEach(c => {
    const d4 = quyDoiHe4(c.grade10);
    tongDiemNhanTinChi += (d4 * c.credits);
    tongTinChi += c.credits;
    if (c.grade10 >= 4.0) passed++;
    else failed++;
  });

  const gpa4 = tongTinChi > 0 ? (tongDiemNhanTinChi / tongTinChi).toFixed(2) : 0;
  return {
    gpa4: parseFloat(gpa4),
    totalCredits: tongTinChi,
    passedCourses: passed,
    failedCourses: failed
  };
}

// Tìm kiếm và lọc môn học
function timKiemMonHoc(courses, query, category = "ALL") {
  const q = query.trim().toLowerCase();
  return courses.filter(c => {
    const matchName = c.name.toLowerCase().includes(q) || c.id.toLowerCase().includes(q);
    const matchCat = (category === "ALL") || (c.category === category);
    return matchName && matchCat;
  });
}
