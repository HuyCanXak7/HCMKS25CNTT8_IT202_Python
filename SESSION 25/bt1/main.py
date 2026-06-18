class BankAccount:
    # Class Attributes
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__account_name = account_name.strip().upper()
        self.__balance = 0

    # Property chỉ đọc số dư
    @property
    def balance(self):
        return self.__balance

    # Property tên tài khoản
    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        if not new_name.strip():
            print("Tên tài khoản không được để trống")
            return

        self.__account_name = new_name.strip().upper()

    @property
    def account_number(self):
        return self.__account_number

    # Static Method
    @staticmethod
    def validate_account_number(account_number):
        return (
            account_number.isdigit()
            and len(account_number) == 10
        )

    # Class Method
    @classmethod
    def update_transaction_fee(cls, new_fee):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            return False

        cls.transaction_fee = new_fee
        return True

    # Instance Methods
    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total = amount + BankAccount.transaction_fee

        if self.__balance < total:
            print(
                "Giao dịch thất bại. "
                "Số dư không đủ để thanh toán số tiền và phí giao dịch"
            )
            return False

        self.__balance -= total
        return True

    def display_info(self):
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.__account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VND")
        print(
            f"Phí giao dịch: "
            f"{BankAccount.transaction_fee:,} VND"
        )


def main():
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật Tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống")
        print("6. Thoát chương trình")
        print("==========================================")

        choice = input("Chọn chức năng (1-6): ")

        # Chức năng 1
        if choice == "1":
            print("\n--- MỞ TÀI KHOẢN MỚI ---")

            while True:
                account_number = input(
                    "Nhập số tài khoản 10 chữ số: "
                )

                if BankAccount.validate_account_number(
                    account_number
                ):
                    break

                print("Số tài khoản không hợp lệ!")
                print("Số tài khoản phải gồm đúng 10 chữ số.")

            account_name = input(
                "Nhập tên chủ tài khoản: "
            )

            current_account = BankAccount(
                account_number,
                account_name
            )

            print("Mở tài khoản thành công!")
            print(
                f"Số tài khoản: "
                f"{current_account.account_number}"
            )
            print(
                f"Tên chủ tài khoản: "
                f"{current_account.account_name}"
            )

        # Chức năng 2
        elif choice == "2":
            print("\n--- THÔNG TIN TÀI KHOẢN ---")

            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print(
                    "Vui lòng mở tài khoản "
                    "ở Chức năng 1 trước."
                )
                continue

            current_account.display_info()

        # Chức năng 3
        elif choice == "3":
            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")

            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print(
                    "Vui lòng mở tài khoản "
                    "ở Chức năng 1 trước."
                )
                continue

            print("1. Nạp tiền")
            print("2. Rút tiền")

            transaction_choice = input(
                "Chọn loại giao dịch (1-2): "
            )

            try:
                amount = int(
                    input("Nhập số tiền giao dịch: ")
                )
            except ValueError:
                print("Số tiền không hợp lệ")
                continue

            if transaction_choice == "1":
                if current_account.deposit(amount):
                    print(
                        f"Nạp tiền thành công: "
                        f"+{amount:,} VND"
                    )
                    print(
                        f"Số dư mới: "
                        f"{current_account.balance:,} VND"
                    )

            elif transaction_choice == "2":
                if current_account.withdraw(amount):
                    print(
                        f"Rút tiền thành công: "
                        f"-{amount:,} VND"
                    )
                    print(
                        f"Phí giao dịch: "
                        f"{BankAccount.transaction_fee:,} VND"
                    )
                    print(
                        f"Số dư mới: "
                        f"{current_account.balance:,} VND"
                    )

        # Chức năng 4
        elif choice == "4":
            print(
                "\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---"
            )

            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print(
                    "Vui lòng mở tài khoản "
                    "ở Chức năng 1 trước."
                )
                continue

            new_name = input("Nhập tên mới: ")

            old_name = current_account.account_name

            current_account.account_name = new_name

            if old_name != current_account.account_name:
                print(
                    "Cập nhật thành công. "
                    f"Tên mới: "
                    f"{current_account.account_name}"
                )

        # Chức năng 5
        elif choice == "5":
            print(
                "\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---"
            )

            print(
                f"Phí giao dịch hiện tại: "
                f"{BankAccount.transaction_fee:,} VND"
            )

            try:
                new_fee = int(
                    input("Nhập phí giao dịch mới: ")
                )
            except ValueError:
                print("Phí giao dịch không hợp lệ")
                continue

            if BankAccount.update_transaction_fee(
                new_fee
            ):
                print(
                    "Đã cập nhật phí giao dịch "
                    f"toàn hệ thống thành "
                    f"{new_fee:,} VND"
                )
            else:
                print(
                    f"Phí giao dịch hiện tại vẫn là "
                    f"{BankAccount.transaction_fee:,} VND"
                )

        # Chức năng 6
        elif choice == "6":
            print(
                "Cảm ơn bạn đã sử dụng "
                "Vietcombank Digibank!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()