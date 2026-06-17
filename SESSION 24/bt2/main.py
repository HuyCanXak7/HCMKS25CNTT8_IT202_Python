class MemberCard:

    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = 0
        self.points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


card1 = MemberCard("Le Van C", 100)

print(f"Điểm ban đầu: {card1.points}")

# Thử gán điểm âm
card1.points = -50

print(f"Điểm sau khi gán -50: {card1.points}")

# Thử gán chuỗi
card1.points = "mot tram"

print(f"Điểm sau khi gán chuỗi: {card1.points}")

# Kiểm tra voucher trực tiếp từ Class
result = MemberCard.is_eligible_for_voucher(250000)

print(f"\nKhách hàng: {card1.customer_name}")
print(f"Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250000 có được tặng Voucher không? {result}")