def show_orders(orders):
    print("\n--- DANH SÁCH ĐƠN HÀNG ĐẠI LÝ ---")

    if len(orders) == 0:
        print("Danh sách đơn hàng đang rỗng!")
        return

    print(f"{'MÃ ĐƠN':<8} | {'TÊN ĐẠI LÝ':<20} | {'GIÁ TRỊ (VND)':<15} | {'TRẠNG THÁI'}")
    print("-" * 70)

    for order in orders:
        print(
            f"{order['id']:<8} | "
            f"{order['name']:<20} | "
            f"{order['price']:<15,} | "
            f"{order['status']}"
        )

    print("-" * 70)


def add_order(orders):
    print("\n--- TẠO MỚI ĐƠN HÀNG ---")

    while True:
        order_id = input("Nhập mã đơn hàng: ").strip()

        if order_id == "":
            print("Mã đơn hàng không được để trống!")
            continue

        duplicate = False

        for order in orders:
            if order["id"] == order_id:
                duplicate = True
                break

        if duplicate:
            print("ERR-01: Mã đơn hàng đã tồn tại!")
            return

        break

    while True:
        agency_name = input("Nhập tên đại lý: ").strip()

        if agency_name == "":
            print("Tên đại lý không được để trống!")
        else:
            break

    while True:
        try:
            price = int(input("Nhập giá trị đơn hàng: "))

            if price <= 0:
                print("Giá trị đơn hàng phải lớn hơn 0!")
                continue

            break

        except ValueError:
            print("Vui lòng nhập số nguyên!")

    new_order = {
        "id": order_id,
        "name": agency_name,
        "price": price,
        "status": "Unpaid"
    }

    orders.append(new_order)

    print("Tạo đơn hàng thành công!")


def main():

    orders = [
        {
            "id": "HD01",
            "name": "Dai ly Hoang Long",
            "price": 45000000,
            "status": "Paid"
        },
        {
            "id": "HD02",
            "name": "Tap hoa Minh Thu",
            "price": 15000000,
            "status": "Unpaid"
        }
    ]

    while True:

        print("\n" + "=" * 40)
        print("QUẢN LÝ ĐƠN HÀNG - AGENT ORDER")
        print("=" * 40)
        print("1. Xem danh sách đơn hàng hiện có")
        print("2. Tạo mới đơn hàng đại lý")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & chiết khấu")
        print("5. Thoát chương trình")

        try:
            user_choice = int(input("Mời chọn chức năng (1-5): "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 5!")
            continue

        if user_choice == 1:
            show_orders(orders)

        elif user_choice == 2:
            add_order(orders)

        elif user_choice == 3:
            print("Chức năng 3 đang phát triển")

        elif user_choice == 4:
            print("Chức năng 4 đang phát triển")

        elif user_choice == 5:
            print("Đang thoát chương trình...")
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


main()