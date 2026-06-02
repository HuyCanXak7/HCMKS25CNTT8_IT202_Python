order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice < 1 or choice > 4:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    if choice == 1:

        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")

            for i in range(len(order_list)):
                print(f"{i + 1}. {order_list[i]}")

    elif choice == 2:

        new_order = input("Nhập mã đơn hàng mới: ").strip().upper()

        order_list.append(new_order)

        print("Đã thêm đơn hàng thành công.")

    elif choice == 3:

        delete_order = input("Nhập mã đơn hàng cần xóa: ").strip().upper()

        if delete_order in order_list:

            order_list.remove(delete_order)

            print("Xóa đơn hàng thành công.")

        else:

            print("Không tìm thấy mã đơn hàng cần xóa!")

    elif choice == 4:

        print("Thoát chương trình.")
        break