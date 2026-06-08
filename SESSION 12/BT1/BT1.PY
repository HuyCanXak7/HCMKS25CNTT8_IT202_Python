cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:
    print("\n==============================")
    print("SHOPEE CART MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")

    choice = input("Mời bạn chọn chức năng (1-5): ")

    if choice == "1":
        print("\n----- CHI TIẾT GIỎ HÀNG -----")

        total_number = 0
        total_money = 0

        print("STT | Mã SP | Tên sản phẩm | SL | Đơn giá | Thành tiền")

        stt = 1

        for item in cart_items:
            thanh_tien = item["number"] * item["price"]

            print(
                stt,
                "|",
                item["id"],
                "|",
                item["name"],
                "|",
                item["number"],
                "|",
                format(item["price"], ","),
                "|",
                format(thanh_tien, ",")
            )

            total_number += item["number"]
            total_money += thanh_tien

            stt += 1

        print("--------------------------------------")
        print("Tổng số lượng sản phẩm:", total_number)
        print("Tổng tiền thanh toán:", format(total_money, ","))

    elif choice == "2":
        ma_sp = input("Nhập mã sản phẩm: ")
        ten_sp = input("Nhập tên sản phẩm: ")

        try:
            so_luong = int(input("Nhập số lượng: "))
            don_gia = int(input("Nhập đơn giá: "))

            if so_luong <= 0 or don_gia < 0:
                print("Lỗi! Số lượng hoặc đơn giá không hợp lệ.")
                continue

            tim_thay = False

            for item in cart_items:
                if item["id"] == ma_sp:
                    item["number"] += so_luong
                    tim_thay = True
                    print("Đã cộng dồn số lượng sản phẩm.")
                    break

            if tim_thay == False:
                new_product = {
                    "id": ma_sp,
                    "name": ten_sp,
                    "number": so_luong,
                    "price": don_gia
                }

                cart_items.append(new_product)

                print("Thêm sản phẩm thành công.")

        except:
            print("Dữ liệu nhập không hợp lệ.")

    elif choice == "3":
        ma_sp = input("Nhập mã sản phẩm cần cập nhật: ")

        try:
            so_luong_moi = int(input("Nhập số lượng mới: "))

            if so_luong_moi <= 0:
                print("Số lượng phải lớn hơn 0.")
                continue

            tim_thay = False

            for item in cart_items:
                if item["id"] == ma_sp:
                    item["number"] = so_luong_moi
                    tim_thay = True
                    print("Cập nhật thành công.")
                    break

            if tim_thay == False:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

        except:
            print("Dữ liệu nhập không hợp lệ.")

    elif choice == "4":
        ma_sp = input("Nhập mã sản phẩm cần xóa: ")

        tim_thay = False

        for item in cart_items:
            if item["id"] == ma_sp:
                cart_items.remove(item)
                tim_thay = True
                print("Xóa sản phẩm thành công.")
                break

        if tim_thay == False:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "5":
        print("Thoát chương trình...")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")