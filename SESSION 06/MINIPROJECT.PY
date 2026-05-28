laptop = 0
phone = 0
tablet = 0
while True:
    print("\n===== MENU QUẢN LÝ KHO =====")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    choice = input("Vui lòng chọn chức năng (1-5): ")

    if choice == "1":
        print("\n--- Báo cáo tồn kho ---")
        for name, qty in [("Laptop", laptop), ("Phone", phone), ("Tablet", tablet)]:
            print(f"{name} ({qty}): {'*' * qty}")

    elif choice == "2":
        print("\n--- Nhập kho ---")
        item = input("Chọn mặt hàng (1-Laptop, 2-Phone, 3-Tablet): ")

        while True:
            try:
                qty = int(input("Nhập số lượng cần thêm: "))
                if qty < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                else:
                    break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")

        if item == "1":
            laptop += qty
        elif item == "2":
            phone += qty
        elif item == "3":
            tablet += qty
        else:
            print("Mặt hàng không hợp lệ!")

    elif choice == "3":
        print("\n--- Xuất kho ---")
        item = input("Chọn mặt hàng (1-Laptop, 2-Phone, 3-Tablet): ")

        while True:
            try:
                qty = int(input("Nhập số lượng cần xuất: "))
                if qty < 0:
                    print("Số lượng không hợp lệ, vui lòng nhập lại!")
                else:
                    break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")

        if item == "1":
            if qty <= laptop:
                laptop -= qty
            else:
                print("Không đủ hàng!")
        elif item == "2":
            if qty <= phone:
                phone -= qty
            else:
                print("Không đủ hàng!")
        elif item == "3":
            if qty <= tablet:
                tablet -= qty
            else:
                print("Không đủ hàng!")
        else:
            print("Mặt hàng không hợp lệ!")

    elif choice == "4":
        print("\n--- Cảnh báo tồn kho thấp ---")
        if laptop < 10:
            print(f"[CẢNH BÁO] Laptop sắp hết (Chỉ còn {laptop} sản phẩm)")
        if phone < 10:
            print(f"[CẢNH BÁO] Phone sắp hết (Chỉ còn {phone} sản phẩm)")
        if tablet < 10:
            print(f"[CẢNH BÁO] Tablet sắp hết (Chỉ còn {tablet} sản phẩm)")

    elif choice == "5":
        print("Thoát chương trình. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
