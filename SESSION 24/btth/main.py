class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available


menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]


def display_menu():
    print("\n--- DANH SÁCH ĐỒ UỐNG ---\n")
    print("Mã món | Tên món | Giá bán | Trạng thái")
    print("-" * 60)

    for drink in menu:
        status = "Đang bán" if drink.is_available else "Ngừng bán"

        print(
            f"{drink.code:<7} | "
            f"{drink.name:<20} | "
            f"{drink.price:<8} | "
            f"{status}"
        )


def add_drink():
    code = input("Nhập mã món: ").strip().upper()

    for drink in menu:
        if drink.code == code:
            print("Mã món đã tồn tại trong hệ thống!")
            return

    name = input("Nhập tên món: ").strip()

    try:
        price = int(input("Nhập giá bán: "))

        if price <= 0:
            print("Giá bán không hợp lệ!")
            return

    except ValueError:
        print("Giá bán không hợp lệ!")
        return

    menu.append(Drink(code, name, price))

    print(f"Thành công: Đã thêm món {name} vào thực đơn!")


def update_status():
    code = input(
        "Nhập mã món cần cập nhật: "
    ).strip().upper()

    for drink in menu:
        if drink.code == code:
            drink.toggle_available()

            status = (
                "Đang bán"
                if drink.is_available
                else "Ngừng bán"
            )

            print(f"Đã cập nhật trạng thái món {code}.")
            print(f"Trạng thái hiện tại: {status}")
            return

    print("Không tìm thấy món có mã này!")


def main():
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
        print("1. Xem danh sách đồ uống")
        print("2. Thêm đồ uống mới")
        print("3. Cập nhật trạng thái kinh doanh")
        print("4. Thoát chương trình")
        print("=" * 46)

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            add_drink()

        elif choice == "3":
            update_status()

        elif choice == "4":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống quản lý "
                "thực đơn Rikkei Coffee!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()