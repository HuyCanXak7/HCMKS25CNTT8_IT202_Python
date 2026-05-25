Input:
Họ và tên bệnh nhân STR
Tuổi bệnh nhân INT 

Giải pháp:
Dùng cấu trúc if-elif-else để phân loại ưu tiên theo tuổi
START
→ Nhập tên bệnh nhân
→ Nhập tuổi bệnh nhân
→ Kiểm tra:
   - Nếu tên rỗng hoặc toàn khoảng trắng → LỖI
   - Nếu tuổi < 0 hoặc > 150 → LỖI
→ Nếu hợp lệ:
   - Nếu tuổi < 6 → ƯU TIÊN: Bệnh nhi
   - Elif tuổi ≥ 80 → ƯU TIÊN: Người cao tuổi
   - Else → KHÁM THƯỜNG
→ In phiếu khám bệnh điện tử
END
