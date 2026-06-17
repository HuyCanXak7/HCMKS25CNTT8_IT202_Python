class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.title()
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if new_price > 0:
            self.__base_price = new_price
            print("Cập nhật giá gốc thành công!")
        else:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return int(
            self.__base_price +
            self.__base_price * MenuItem.service_charge
        )

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_code):
        if len(item_code) != 4:
            return False

        if not item_code[:2].isalpha():
            return False

        if not item_code[:2].isupper():
            return False

        if not item_code[2:].isdigit():
            return False

        return True


menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]


def find_item(item_id):
    for item in menu_db:
        if item.item_id == item_id:
            return item
    return None


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái")
    print("4. Điều chỉnh giá gốc")
    print("5. Cập nhật phụ phí dịch vụ")
    print("6. Thoát")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")

        for index, item in enumerate(menu_db, start=1):
            status = (
                "Đang bán"
                if item.is_available
                else "Hết hàng"
            )

            print(
                f"{index}. Mã: {item.item_id} "
                f"| Tên: {item.item_name} "
                f"| Trạng thái: {status} "
                f"| Giá niêm yết: "
                f"{item.calculate_selling_price():,} VNĐ"
            )

    elif choice == "2":
        print("\n--- THÊM MÓN MỚI ---")

        item_id = input("Nhập mã món: ").strip()

        if not MenuItem.is_valid_item_id(item_id):
            print("Mã món không hợp lệ!")
            print(
                "Mã món phải gồm 2 chữ cái in hoa "
                "và 2 chữ số. Ví dụ: CF01."
            )
            continue

        if find_item(item_id):
            print("Mã món đã tồn tại!")
            continue

        item_name = input("Nhập tên món: ")

        try:
            base_price = int(
                input("Nhập giá gốc: ")
            )

            if base_price <= 0:
                print("Giá phải lớn hơn 0!")
                continue

            new_item = MenuItem(
                item_id,
                item_name,
                base_price
            )

            menu_db.append(new_item)

            print("Thêm món mới thành công!")

        except ValueError:
            print("Giá không hợp lệ!")

    elif choice == "3":
        print("\n--- CẬP NHẬT TRẠNG THÁI ---")

        item_id = input(
            "Nhập mã món cần cập nhật: "
        ).strip()

        item = find_item(item_id)

        if not item:
            print("Không tìm thấy món!")
            continue

        item.toggle_availability()

        status = (
            "ĐANG BÁN"
            if item.is_available
            else "HẾT HÀNG"
        )

        print(
            f">> Đã cập nhật "
            f"{item.item_name} thành {status}!"
        )

    elif choice == "4":
        print("\n--- ĐIỀU CHỈNH GIÁ ---")

        item_id = input(
            "Nhập mã món cần đổi giá: "
        ).strip()

        item = find_item(item_id)

        if not item:
            print("Không tìm thấy món!")
            continue

        try:
            new_price = int(
                input("Nhập giá tiền mới: ")
            )

            item.base_price = new_price

        except ValueError:
            print("Giá không hợp lệ!")

    elif choice == "5":
        print(
            "\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ ---"
        )

        print(
            f"Phụ phí hiện tại: "
            f"{MenuItem.service_charge * 100:.0f}%"
        )

        try:
            new_rate = float(
                input(
                    "Nhập phụ phí mới "
                    "(Ví dụ 0.1): "
                )
            )

            MenuItem.update_service_charge(
                new_rate
            )

            print(
                "Cập nhật phụ phí dịch vụ thành công!"
            )

        except ValueError:
            print("Dữ liệu không hợp lệ!")

    elif choice == "6":
        print(
            "Cảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!"
        )
        break

    else:
        print("Lựa chọn không hợp lệ!")