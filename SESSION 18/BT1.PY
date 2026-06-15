def display_orders(orders):
    if not orders:
        print("\nERR-02: Danh sách đơn hàng trống!")
        return

    print("\n{:<10} {:<25} {:>15} {:<10}".format(
        "Ma HD", "Ten Dai Ly", "Gia Tri", "Trang Thai"
    ))
    print("-" * 65)

    for order in orders:
        print("{:<10} {:<25} {:>15,} {:<10}".format(
            order["id"],
            order["name"],
            order["price"],
            order["status"]
        ))


def input_non_empty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Du lieu khong duoc de trong!")


def input_positive_price():
    while True:
        try:
            price = int(input("Nhap gia tri don hang: "))
            if price > 0:
                return price
            print("Gia tri phai lon hon 0!")
        except ValueError:
            print("Vui long nhap so nguyen hop le!")


def add_order(orders):
    print("\n=== TAO MOI DON HANG ===")

    order_id = input_non_empty("Nhap ma don hang: ")

    for order in orders:
        if order["id"].lower() == order_id.lower():
            print("ERR-01: Ma don hang da ton tai!")
            return

    agency_name = input_non_empty("Nhap ten dai ly: ")
    price = input_positive_price()

    new_order = {
        "id": order_id,
        "name": agency_name,
        "price": price,
        "status": "Unpaid"
    }

    orders.append(new_order)
    print("Them moi don hang thanh cong!")


def update_payment_status(orders):
    print("\n=== CAP NHAT THANH TOAN ===")

    order_id = input_non_empty("Nhap ma don hang: ")

    for order in orders:
        if order["id"].lower() == order_id.lower():

            if order["status"] == "Paid":
                print("ERR-04: Don hang da duoc thanh toan truoc do!")
                return

            order["status"] = "Paid"
            print("Cap nhat trang thai thanh toan thanh cong!")
            return

    print("ERR-03: Khong tim thay ma don hang!")


def calculate_revenue(orders):
    total_revenue = 0

    for order in orders:
        if order["status"] == "Paid":
            total_revenue += order["price"]

    discount_percent = 5 if total_revenue >= 100_000_000 else 0
    discount_amount = total_revenue * discount_percent / 100

    return total_revenue, discount_percent, discount_amount


def show_revenue_report(orders):
    revenue, discount_percent, discount_amount = calculate_revenue(orders)

    print("\n=== BAO CAO DOANH THU ===")
    print(f"Tong doanh thu thuc te: {revenue:,.0f} VND")
    print(f"Ty le chiet khau: {discount_percent}%")
    print(f"Tien chiet khau: {discount_amount:,.0f} VND")


def show_menu():
    print("\n========== QUAN LY DON HANG ==========")
    print("1. Xem danh sach don hang")
    print("2. Tao moi don hang")
    print("3. Cap nhat trang thai thanh toan")
    print("4. Tinh tong doanh thu & chiet khau")
    print("5. Thoat")
    print("======================================")


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
        show_menu()

        try:
            choice = int(input("Nhap lua chon: "))
        except ValueError:
            print("Vui long nhap so tu 1 den 5!")
            continue

        if choice == 1:
            display_orders(orders)

        elif choice == 2:
            add_order(orders)

        elif choice == 3:
            update_payment_status(orders)

        elif choice == 4:
            show_revenue_report(orders)

        elif choice == 5:
            print("Cam on ban da su dung chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()