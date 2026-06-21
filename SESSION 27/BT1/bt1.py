from abc import ABC, abstractmethod


class BaseAccount(ABC):
    """
    Abstract Base Class cho mọi loại tài khoản
    """

    bank_name = "Vietcombank"

    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self._set_balance(balance)

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = " ".join(value.strip().upper().split())

    @property
    def balance(self):
        return self.__balance

    def _set_balance(self, value):
        self.__balance = value

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name

    def __add__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BaseAccount):

    def __init__(
        self,
        account_number,
        owner_name,
        interest_rate,
        balance=0
    ):
        super().__init__(
            account_number,
            owner_name,
            balance
        )
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self._set_balance(self.balance + amount)

    def withdraw(self, amount):
        fee = amount * 0.02
        total = amount + fee

        if total > self.balance:
            raise ValueError("Không đủ số dư")

        self._set_balance(self.balance - total)
        return fee

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self._set_balance(self.balance + interest)
        return interest


class CreditAccount(BaseAccount):

    def __init__(
        self,
        account_number,
        owner_name,
        credit_limit,
        balance=0
    ):
        super().__init__(
            account_number,
            owner_name,
            balance
        )

        self.credit_limit = credit_limit

    def deposit(self, amount):
        self._set_balance(self.balance + amount)

    def withdraw(self, amount):

        if self.balance - amount < -self.credit_limit:
            raise ValueError(
                "Vượt quá hạn mức thấu chi cho phép"
            )

        self._set_balance(self.balance - amount)


class DigitalPremiumMixin:

    def cashback_reward(self, amount):

        if amount > 5_000_000:
            return amount * 0.01

        return 0


class HybridAccount(
    SavingsAccount,
    DigitalPremiumMixin
):
    pass


class VNPayGateway:

    def execute_pay(self, account, amount):

        print(
            f"[VNPay] Kết nối tới tài khoản "
            f"{account.account_number}"
        )

        account.withdraw(amount)


class ViettelMoneyGateway:

    def execute_pay(self, account, amount):

        print(
            f"[Viettel Money] Kết nối tới tài khoản "
            f"{account.account_number}"
        )

        account.withdraw(amount)


def process_payment(
    payment_gateway,
    account,
    amount
):

    try:
        payment_gateway.execute_pay(
            account,
            amount
        )

        print(
            "Thanh toán thành công!"
        )

    except AttributeError:
        print(
            "Cổng thanh toán không hợp lệ hoặc chưa được tích hợp"
        )

    except Exception as error:
        print(error)


accounts = []
current_account = None


def create_account():

    global current_account

    print("\n1. Savings Account")
    print("2. Credit Account")
    print("3. Hybrid Account")

    choice = input(
        "Chọn loại tài khoản: "
    )

    account_number = input(
        "Nhập số tài khoản: "
    )

    if not BaseAccount.validate_account_number(
        account_number
    ):
        print(
            "Số tài khoản không hợp lệ!"
        )
        return

    owner_name = input(
        "Nhập tên chủ tài khoản: "
    )

    if choice == "1":

        interest_rate = float(
            input(
                "Lãi suất: "
            )
        )

        account = SavingsAccount(
            account_number,
            owner_name,
            interest_rate
        )

    elif choice == "2":

        limit = float(
            input(
                "Hạn mức tín dụng: "
            )
        )

        account = CreditAccount(
            account_number,
            owner_name,
            limit
        )

    elif choice == "3":

        interest_rate = float(
            input(
                "Lãi suất: "
            )
        )

        account = HybridAccount(
            account_number,
            owner_name,
            interest_rate
        )

    else:
        print("Lựa chọn không hợp lệ")
        return

    accounts.append(account)
    current_account = account

    print("Mở tài khoản thành công!")


def show_account():

    if current_account is None:
        print(
            "Chưa có tài khoản"
        )
        return

    print(
        f"\nLoại: "
        f"{type(current_account).__name__}"
    )

    print(
        f"Ngân hàng: "
        f"{current_account.bank_name}"
    )

    print(
        f"Số tài khoản: "
        f"{current_account.account_number}"
    )

    print(
        f"Chủ tài khoản: "
        f"{current_account.owner_name}"
    )

    print(
        f"Số dư: "
        f"{current_account.balance:,.0f}"
    )

    print("\nMRO:")

    for cls in type(current_account).mro():
        print(cls.__name__)


def transaction():

    if current_account is None:
        print(
            "Chưa có tài khoản"
        )
        return

    print("1. Nạp tiền")
    print("2. Rút tiền")

    choice = input(
        "Chọn: "
    )

    amount = float(
        input(
            "Số tiền: "
        )
    )

    try:

        if choice == "1":

            current_account.deposit(amount)

            if isinstance(
                current_account,
                HybridAccount
            ):
                cashback = (
                    current_account
                    .cashback_reward(amount)
                )

                if cashback > 0:
                    current_account.deposit(
                        cashback
                    )

                    print(
                        f"Cashback: "
                        f"{cashback:,.0f}"
                    )

        elif choice == "2":

            result = current_account.withdraw(
                amount
            )

            if isinstance(
                current_account,
                SavingsAccount
            ):
                print(
                    f"Phí rút: "
                    f"{result:,.0f}"
                )

        print(
            f"Số dư: "
            f"{current_account.balance:,.0f}"
        )

    except Exception as error:
        print(error)


def apply_interest():

    if current_account is None:
        print(
            "Chưa có tài khoản"
        )
        return

    if isinstance(
        current_account,
        (SavingsAccount, HybridAccount)
    ):

        interest = (
            current_account
            .apply_interest()
        )

        print(
            f"Lãi nhận được: "
            f"{interest:,.0f}"
        )

    else:
        print(
            "Tài khoản không hỗ trợ lãi suất"
        )


def compare_accounts():

    if len(accounts) < 2:
        print(
            "Cần ít nhất 2 tài khoản"
        )
        return

    for i, acc in enumerate(accounts):
        print(
            f"{i}. "
            f"{acc.owner_name}"
        )

    index = int(
        input(
            "Chọn tài khoản: "
        )
    )

    other = accounts[index]

    try:

        if current_account < other:
            print(
                "A nhỏ hơn B"
            )
        else:
            print(
                "A không nhỏ hơn B"
            )

        print(
            f"Tổng số dư: "
            f"{current_account + other:,.0f}"
        )

    except TypeError:
        print(
            "So sánh không hợp lệ"
        )


def payment():

    if current_account is None:
        print(
            "Chưa có tài khoản"
        )
        return

    print("1. VNPay")
    print("2. Viettel Money")

    choice = input(
        "Chọn cổng: "
    )

    amount = float(
        input(
            "Số tiền: "
        )
    )

    if choice == "1":
        gateway = VNPayGateway()
    else:
        gateway = ViettelMoneyGateway()

    process_payment(
        gateway,
        current_account,
        amount
    )


def main():

    while True:

        print("\n===== MENU =====")
        print("1. Mở tài khoản")
        print("2. Xem thông tin")
        print("3. Giao dịch")
        print("4. Tính lãi")
        print("5. So sánh")
        print("6. Thanh toán")
        print("7. Thoát")

        choice = input(
            "Chọn: "
        )

        if choice == "1":
            create_account()

        elif choice == "2":
            show_account()

        elif choice == "3":
            transaction()

        elif choice == "4":
            apply_interest()

        elif choice == "5":
            compare_accounts()

        elif choice == "6":
            payment()

        elif choice == "7":
            break

        else:
            print(
                "Lựa chọn không hợp lệ"
            )


if __name__ == "__main__":
    main()
