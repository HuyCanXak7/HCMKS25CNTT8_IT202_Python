print("=== CHƯƠNG TRÌNH QUẢN LÝ CHẤM CÔNG NHÂN VIÊN ===")

while True:
    try:
        num_employees = int(input("Nhập số lượng nhân viên cần quản lý: "))
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
        continue

    for i in range(1, num_employees + 1):
        print(f"\n→ Nhân viên số {i}:")
        name = input("Nhập tên nhân viên: ")
        
        try:
            working_days = int(input("Nhập số ngày đi làm: "))
        except ValueError:
            print("Lỗi: Vui lòng nhập số nguyên cho ngày công!")
            continue

        print("\n--- THÔNG TIN NHÂN VIÊN ---")
        print(f"Tên: {name}")
        print(f"Số ngày đi làm: {working_days}")

        if working_days < 20:
            print("Đánh giá: Cần cải thiện chuyên cần")
        else:
            print("Đánh giá: Nhân viên chuyên cần tốt")
        print("---------------------------\n")

    choice = input("Bạn có muốn tiếp tục? (y/n): ").lower()
    if choice == "n":
        print("Chương trình kết thúc. Cảm ơn bạn đã sử dụng!")
        break
