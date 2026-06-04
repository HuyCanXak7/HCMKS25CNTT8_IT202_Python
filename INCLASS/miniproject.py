parking_lot = []
car_id_counter = 1

while True:
    print("="*62)
    print("             Quản Lý Bãi Xe - SMART PARKING                   ")
    print("="*62)
    print("""
          1. thêm xe mới vào bãi
          2. hiển thị danh sách xe trong bãi
          3. xóa xe khỏi bãi (khi xe ra)
          4. thoát chương trình
          """)
    option = input("Chọn (1-4): ")
    if option == "4":
        print("Thoát chương trình")
        break

    if option == "1":
        vehicle_type = input("Loại xe: ")
        owner_name = input("Chủ xe: ")

        if vehicle_type and owner_name:
            parking_lot.append({"id": car_id_counter, "type": vehicle_type, "owner": owner_name})
            print("Đã thêm xe ID", car_id_counter)
            car_id_counter += 1
        else:
            print("Không được để trống!")

    elif option == "2":
        if not parking_lot:
            print("Bãi xe đang trống")
        else:
            print(f"{'ID':<5} | {'Loại xe':<20} | {'Chủ xe':<22}")
            print("-" * 50)
            for car in parking_lot:
                print(f"{car['id']:<5} | {car['type']:<20} | {car['owner']:<22}")

    elif option == "3":
        remove_input = input("Nhập ID xe cần xóa: ")
        if remove_input.isdigit():
            remove_id = int(remove_input)
            found = False
            for car in parking_lot:
                if car["id"] == remove_id:
                    parking_lot.remove(car)
                    print(f"Đã xóa xe ID {remove_id}")
                    found = True
                    break
            if not found:
                print("ID không tồn tại trong bãi xe")
        else:
            print("Vui lòng nhập số ID hợp lệ")
