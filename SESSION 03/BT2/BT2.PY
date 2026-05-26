print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("→ Đang xử lý nhân viên số", employee_number, "—")
    working_days = int(input("Nhập số ngày công trong tháng: "))
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        continue

    bonus_amount = working_days * 200000
    print("→ Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VND tiền thưởng!")
    print("———————————————\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")
