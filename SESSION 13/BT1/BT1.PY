cars = []
next_id = 1

while True:
    print("\n===== SMART PARKING SYSTEM =====")
    print("1. Check-in")
    print("2. Báo cáo tồn kho")
    print("3. Tìm kiếm xe")
    print("4. Check-out")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":
        plate = input("Nhập biển số xe: ").strip()

        if plate == "":
            print("ERR-01: Biển số không được để trống")
            continue

        exist = False
        for car in cars:
            if car["plate"] == plate:
                exist = True
                break

        if exist:
            print("ERR-02: Biển số đã tồn tại")
            continue

        while True:
            try:
                car_type = int(input("Loại xe (1-Xe máy, 2-Ô tô): "))
                if car_type == 1 or car_type == 2:
                    break
                print("ERR-03: Loại xe không hợp lệ")
            except:
                print("ERR-03: Loại xe không hợp lệ")

        while True:
            try:
                entry_time = int(input("Nhập giờ vào: "))
                break
            except:
                print("ERR-05: Giờ vào không hợp lệ")

        cars.append({
            "id": next_id,
            "plate": plate,
            "type": car_type,
            "entry_time": entry_time
        })

        next_id += 1
        print("Check-in thành công")

    elif choice == "2":
        if len(cars) == 0:
            print("ERR-06: Bãi xe hiện đang trống")
        else:
            print(f"{'ID':<5}{'Biển số':<15}{'Loại xe':<10}{'Giờ vào':<10}")

            for car in cars:
                if car["type"] == 1:
                    type_name = "Xe máy"
                else:
                    type_name = "Ô tô"

                print(f"{car['id']:<5}{car['plate']:<15}{type_name:<10}{car['entry_time']:<10}")

    elif choice == "3":
        plate = input("Nhập biển số cần tìm: ").strip()

        found = False

        for car in cars:
            if car["plate"] == plate:
                print(car)
                found = True
                break

        if found == False:
            print("ERR-04: Không tìm thấy xe")

    elif choice == "4":
        plate = input("Nhập biển số cần check-out: ").strip()

        found = False

        for car in cars:
            if car["plate"] == plate:
                found = True

                while True:
                    try:
                        exit_time = int(input("Nhập giờ ra: "))

                        if exit_time < car["entry_time"]:
                            print("ERR-07: Giờ ra phải lớn hơn hoặc bằng giờ vào")
                        else:
                            break
                    except:
                        print("ERR-08: Giờ ra không hợp lệ")

                parking_hours = exit_time - car["entry_time"]

                if car["type"] == 1:
                    fee = parking_hours * 5000
                else:
                    fee = parking_hours * 20000

                print("Phí gửi xe:", fee)

                cars.remove(car)
                print("Check-out thành công")
                break

        if found == False:
            print("ERR-04: Không tìm thấy xe")

    elif choice == "5":
        print("Thoát chương trình...")
        break

    else:
        print("ERR-09: Lựa chọn không hợp lệ")
        