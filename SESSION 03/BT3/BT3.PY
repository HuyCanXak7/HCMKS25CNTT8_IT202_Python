print("=== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ ===")

for employee_number in range(1, 4):
    print(f"\n→ Đang nhập dữ liệu cho nhân viên số {employee_number}:")

    employee_id = input("Nhập Mã nhân viên: ")
    employee_name = input("Nhập Họ và tên: ")
    department = input("Nhập Phòng ban: ")

    if not employee_id.strip() or not employee_name.strip():
        print("CẢNH BÁO: Dữ liệu không hợp lệ!"
              "Mã nhân viên và Họ tên không được bỏ trống hoặc chỉ chứa khoảng trắng.")
        continue  

    print("\n--- PHIẾU HỒ SƠ NHÂN SỰ ĐIỆN TỬ ---")
    print(f"Mã nhân viên : {employee_id}")
    print(f"Họ và tên    : {employee_name}")
    print(f"Phòng ban    : {department}")
    print("-----------------------------------\n")

print("Đã hoàn tất khởi tạo hồ sơ cho 3 nhân viên!")
