order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:

    print("\n===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Gán tài xế cho đơn hàng")
    print("3. Cập nhật trạng thái giao hàng")
    print("4. Hủy đơn hàng")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
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

        order_code = input("Nhập mã đơn hàng: ").strip().upper()

        found = False

        for i in range(len(order_list)):

            code, status = order_list[i].split(" - ")

            if code == order_code:

                found = True

                if status == "PENDING":

                    order_list[i] = code + " - ASSIGNED"
                    print("Gán tài xế thành công.")

                else:

                    print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")

                break

        if not found:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == 3:

        order_code = input("Nhập mã đơn hàng: ").strip().upper()

        found = False

        for i in range(len(order_list)):

            code, status = order_list[i].split(" - ")

            if code == order_code:

                found = True

                if status == "ASSIGNED":

                    order_list[i] = code + " - DELIVERING"
                    print("Cập nhật trạng thái thành DELIVERING.")

                elif status == "DELIVERING":

                    order_list[i] = code + " - COMPLETED"
                    print("Cập nhật trạng thái thành COMPLETED.")

                elif status == "PENDING":

                    print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")

                elif status == "COMPLETED":

                    print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")

                elif status == "CANCELLED":

                    print("Đơn hàng đã bị hủy, không thể cập nhật.")

                break

        if not found:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == 4:

        order_code = input("Nhập mã đơn hàng cần hủy: ").strip().upper()

        found = False

        for i in range(len(order_list)):

            code, status = order_list[i].split(" - ")

            if code == order_code:

                found = True

                if status == "PENDING" or status == "ASSIGNED":

                    order_list[i] = code + " - CANCELLED"
                    print("Hủy đơn hàng thành công.")

                elif status == "DELIVERING":

                    print("Đơn hàng đang được giao, không thể hủy.")

                elif status == "COMPLETED":

                    print("Đơn hàng đã hoàn tất, không thể hủy.")

                elif status == "CANCELLED":

                    print("Đơn hàng đã được hủy trước đó.")

                break

        if not found:
            print("Không tìm thấy mã đơn hàng.")

    elif choice == 5:

        print("Thoát chương trình")
        break