sender_name = ""
sender_phone = ""
pickup_address = ""
receiver_name = ""
receiver_phone = ""
delivery_address = ""
delivery_note = ""

while True:

    print("\n===== MENU =====")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn phải từ 1 đến 5")
        continue

    if choice == 1:

        sender_name = input("Nhập tên người gửi: ")
        sender_phone = input("Nhập SĐT người gửi: ")
        pickup_address = input("Nhập địa chỉ lấy hàng: ")
        receiver_name = input("Nhập tên người nhận: ")
        receiver_phone = input("Nhập SĐT người nhận: ")
        delivery_address = input("Nhập địa chỉ giao hàng: ")
        delivery_note = input("Nhập ghi chú giao hàng: ")

        fields = {
            "Tên người gửi": sender_name,
            "SĐT người gửi": sender_phone,
            "Địa chỉ lấy hàng": pickup_address,
            "Tên người nhận": receiver_name,
            "SĐT người nhận": receiver_phone,
            "Địa chỉ giao hàng": delivery_address,
            "Ghi chú giao hàng": delivery_note
        }

        empty_found = False

        for field_name, value in fields.items():
            if value.strip() == "":
                print(field_name, "không được bỏ trống")
                empty_found = True

        if empty_found:
            continue

        sender_name = sender_name.strip().title()
        receiver_name = receiver_name.strip().title()

        pickup_address = " ".join(pickup_address.strip().split())
        delivery_address = " ".join(delivery_address.strip().split())

        delivery_note = delivery_note.strip()

        print("\n===== BÁO CÁO =====")
        print("Tên người gửi:", sender_name)
        print("Tên người nhận:", receiver_name)
        print("Địa chỉ lấy hàng:", pickup_address)
        print("Địa chỉ giao hàng:", delivery_address)
        print("Ghi chú:", delivery_note)
        print("Độ dài ghi chú:", len(delivery_note))
        print("Số lượng từ:", len(delivery_note.split()))
        print("Ghi chú chữ thường:", delivery_note.lower())
        print("Ghi chú chữ hoa:", delivery_note.upper())

    elif choice == 2:

        order_code = input("Nhập mã đơn hàng: ")

        if order_code.strip() == "":
            print("Mã đơn hàng không được bỏ trống")
            continue

        order_code = order_code.strip().upper()
        order_code = "-".join(order_code.split())

        if not order_code.startswith("GRAB-"):
            order_code = "GRAB-" + order_code

        print("Mã đơn hàng chuẩn hóa:", order_code)

    elif choice == 3:

        phones = {
            "SĐT người gửi": sender_phone,
            "SĐT người nhận": receiver_phone
        }

        for title, phone in phones.items():

            if phone.strip() == "":
                print(title, "không được bỏ trống")
                continue

            if not phone.isdigit():
                print("Số điện thoại không hợp lệ")
                continue

            if len(phone) != 10:
                print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                continue

            hidden_phone = phone[:3] + "*****" + phone[-2:]

            print(title + ":", hidden_phone)

    elif choice == 4:

        if delivery_note.strip() == "":
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue

        old_keyword = input("Nhập từ khóa cần tìm: ")
        new_keyword = input("Nhập từ khóa thay thế: ")

        if old_keyword in delivery_note:

            count = delivery_note.count(old_keyword)

            new_note = delivery_note.replace(old_keyword, new_keyword)

            print("Số lần xuất hiện của từ khóa:", count)
            print("Ghi chú sau thay thế:", new_note)

        else:

            print("Không tìm thấy từ khóa")

    elif choice == 5:

        print("Thoát chương trình")
        break