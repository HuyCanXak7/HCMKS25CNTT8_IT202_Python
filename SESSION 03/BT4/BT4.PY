print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")
while True:
    try:
        num_employees = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    except ValueError:
        print("[LỖI] Dữ liệu không hợp lệ! Vui lòng nhập một số nguyên.")
        continue

    if num_employees <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
    else:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {num_employees} nhân sự mới!")
        break 
print("--- CHƯƠNG TRÌNH KẾT THÚC ---")
