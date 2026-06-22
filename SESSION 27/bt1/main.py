from abc import ABC, abstractmethod

class BaseAccount(ABC):
    bank_name = "Vietcombank"

    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @staticmethod 
    def validate_account_number(account_number):
        if len(account_number) != 10:
            raise ValueError("Lỗi số tài khoản phải đủ 10 chữ số")

    @classmethod 
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name

    @abstractmethod
    def deposit(self, amount): pass

    @abstractmethod
    def with_draw(self, amount): pass

    def __add__(self, other):
        return self.balance + other.balance

    def __lt__(self, other):
        return self.balance < other.balance


class SavingsAccount(BaseAccount):
    def __init__(self, interest_rate):
        super().__init__()

        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.__balance += amount

    def with_draw(self, amount):
        self.__balance -= amount + amount * 0.02

    def apply_interest(self):
        interest = self.__balance * self.interest_rate

        self.__balance += interest


class CreditAccount(BaseAccount):
    def __init__(self, credit_limit):
        super().__init__()

        self.credit_limit = credit_limit
        
    def deposit(self, amount):
        self.__balance += amount
        
    def with_draw(self, amount):
        self.__balance -= amount


class DigitalPremiumMixin:
    def cashback_reward(self, amount):
        if amount > 5000000:
            return amount * 0.01

        return 0


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    def __init__(self, interest_rate):
        super().__init__(interest_rate)
        
header = """===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====
1. Mở tài khoản mới (Chọn loại tài khoản)
2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)
3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng (Đa hình)
4. Tích lũy / Áp dụng lãi suất định kỳ
5. Kiểm tra tính năng gộp tài khoản & So sánh (Overloading)
6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)
7. Thoát chương trình
=============================================="""
while True:
    print(header)
    choice = (input("Chọn chức năng (1-7): "))
    if choice == '7':
        print("Thoát chương trình... ")
        break