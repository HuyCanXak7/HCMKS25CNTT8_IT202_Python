class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()

        # Khai báo private attributes
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    def earn_points(self, bill_amount):
        earned = bill_amount // 10000

        self.__points += earned

        if self.__points >= 100:
            self.__tier = "VIP"

        return earned

    def redeem_points(self, points_to_use):
        if points_to_use <= 0:
            print("Số điểm phải lớn hơn 0!")
            return

        if points_to_use > self.__points:
            print("Không thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {self.__points}")
            return

        self.__points -= points_to_use

        discount = points_to_use * MemberCard.point_value_vnd

        print(f"Đã trừ {points_to_use} điểm.")
        print(
            f"Khách hàng được giảm giá "
            f"{discount:,} VNĐ vào hóa đơn!"
        )

        if self.__points < 100:
            self.__tier = "Standard"

        print(f"Số điểm còn lại: {self.__points}")
        print(f"Hạng thẻ hiện tại: {self.__tier}")

    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value

    @staticmethod
    def is_valid_card_id(card_id):
        if len(card_id) != 4:
            return False

        if not card_id.startswith("RC"):
            return False

        if not card_id[2:].isdigit():
            return False

        return True


cards_database = [
    MemberCard("RC01", "Nguyen Van A"),
    MemberCard("RC02", "Tran Thi B")
]

cards_database[0].earn_points(1500000)
cards_database[1].earn_points(200000)


def find_card(card_id):
    for card in cards_database:
        if card.card_id == card_id:
            return card
    return None


while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng")
    print("4. Khách dùng điểm")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- DANH SÁCH THẺ ---")

        for index, card in enumerate(cards_database, start=1):
            print(
                f"{index}. Mã: {card.card_id} | "
                f"Tên: {card.name} | "
                f"Điểm: {card.points} | "
                f"Hạng: {card.tier}"
            )

    elif choice == "2":
        print("\n--- ĐĂNG KÝ THẺ MỚI ---")

        card_id = input("Nhập mã thẻ: ").strip()

        if not MemberCard.is_valid_card_id(card_id):
            print("Mã thẻ không hợp lệ!")
            continue

        if find_card(card_id):
            print("Mã thẻ đã tồn tại!")
            continue

        name = input("Nhập tên khách hàng: ")

        new_card = MemberCard(card_id, name)
        cards_database.append(new_card)

        print("Đăng ký thành công!")

    elif choice == "3":
        print("\n--- TÍCH ĐIỂM ---")

        card_id = input("Nhập mã thẻ: ").strip()

        card = find_card(card_id)

        if not card:
            print("Không tìm thấy thẻ!")
            continue

        bill_amount = int(input("Nhập tổng tiền hóa đơn: "))

        earned = card.earn_points(bill_amount)

        print(f"Tích thành công {earned} điểm.")
        print(f"Tổng điểm: {card.points}")
        print(f"Hạng thẻ: {card.tier}")

    elif choice == "4":
        print("\n--- ĐỔI ĐIỂM ---")

        card_id = input("Nhập mã thẻ: ").strip()

        card = find_card(card_id)

        if not card:
            print("Không tìm thấy thẻ!")
            continue

        points_to_use = int(input("Nhập số điểm muốn dùng: "))

        card.redeem_points(points_to_use)

    elif choice == "5":
        print("\n--- CẬP NHẬT TỶ GIÁ ---")

        new_value = int(
            input("Nhập tỷ giá mới cho 1 điểm: ")
        )

        MemberCard.update_point_value(new_value)

        print("Cập nhật thành công!")
        print(
            f"1 điểm = "
            f"{MemberCard.point_value_vnd:,} VNĐ"
        )

    elif choice == "6":
        print(
            "Cảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!"
        )
        break

    else:
        print("Lựa chọn không hợp lệ!")