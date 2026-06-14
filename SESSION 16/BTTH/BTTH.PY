def find_blood_bag(inventory, blood_id):
    blood_id = blood_id.strip().upper()

    for index, blood in enumerate(inventory):
        if blood.startswith(blood_id + "-"):
            return index

    return -1


def display_inventory(inventory):
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return

    total_volume = 0

    print("\n--- DANH SÁCH KHO MÁU ---")
    print(f"{'Mã Túi':<8}|{'Người Hiến':<20}|{'Nhóm Máu':<10}|{'Thể Tích':<10}|{'Ngày Hết Hạn'}")
    print("-" * 70)

    for blood in inventory:
        data = blood.split("-")

        blood_id = data[0]
        donor = data[1]
        blood_type = data[2]

        if data[3] == "":
            blood_type += "-"
            volume = int(data[4])
            expiry = data[5]
        else:
            volume = int(data[3])
            expiry = data[4]

        total_volume += volume

        print(
            f"{blood_id:<8}|"
            f"{donor:<20}|"
            f"{blood_type:<10}|"
            f"{str(volume) + ' ml':<10}|"
            f"{expiry}"
        )

    print("-" * 70)
    print(f"Tổng thể tích máu trong kho: {total_volume} ml.")


def add_blood_bag(inventory):
    print("\n--- NHẬP TÚI MÁU MỚI ---")

    blood_id = input("Nhập mã túi máu mới: ").strip().upper()

    if blood_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    if find_blood_bag(inventory, blood_id) != -1:
        print(f"Lỗi: Mã túi máu {blood_id} đã tồn tại! Vui lòng nhập mã khác.")
        return

    donor = input("Nhập tên người hiến: ").strip().title()

    if donor == "":
        print("Lỗi: Tên người hiến không được để trống!")
        return

    blood_type = input("Nhập nhóm máu: ").strip().upper()

    try:
        volume = int(input("Nhập thể tích (ml): "))

        if volume <= 0:
            print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
            return

    except ValueError:
        print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()

    new_blood = "-".join([
        blood_id,
        donor,
        blood_type,
        str(volume),
        expiry
    ])

    inventory.append(new_blood)

    print(f"\nThành công: Đã nhập túi máu {blood_id} vào kho!")


def update_expiry(inventory):
    print("\n--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")

    blood_id = input("Nhập mã túi máu cần cập nhật: ").strip().upper()

    if blood_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag(inventory, blood_id)

    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    new_expiry = input("Nhập ngày hết hạn mới: ").strip()

    data = inventory[index].split("-")

    data[-1] = new_expiry

    inventory[index] = "-".join(data)

    print(f"Thành công: Đã cập nhật ngày hết hạn cho túi máu {blood_id}!")


def remove_blood_bag(inventory):
    print("\n--- XUẤT / HỦY TÚI MÁU ---")

    blood_id = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()

    if blood_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    index = find_blood_bag(inventory, blood_id)

    if index == -1:
        print(f"Lỗi: Không tìm thấy túi máu {blood_id} trong kho!")
        return

    inventory.pop(index)

    print(f"Thành công: Đã xuất túi máu {blood_id} khỏi kho!")


def main():
    blood_inventory = [
        "BL001-Nguyen Van A-O+-250-31/12/2026",
        "BL002-Tran Thi B-A--350-15/11/2026",
        "BL003-Le Van C-AB+-250-20/10/2026"
    ]

    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
        print("1. Xem danh sách túi máu trong kho")
        print("2. Nhập túi máu mới")
        print("3. Gia hạn / Sửa ngày hết hạn")
        print("4. Xuất / Hủy túi máu")
        print("5. Thoát chương trình")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_inventory(blood_inventory)

        elif choice == "2":
            add_blood_bag(blood_inventory)

        elif choice == "3":
            update_expiry(blood_inventory)

        elif choice == "4":
            remove_blood_bag(blood_inventory)

        elif choice == "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


main()