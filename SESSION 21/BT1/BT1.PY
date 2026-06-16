import logging
import re


logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid."""


class InsufficientBalanceError(Exception):
    """Raised when wallet balance is insufficient."""


class Wallet:
    """Represent a MoMo wallet."""

    HIGH_VALUE_THRESHOLD = 10_000_000

    def __init__(self):
        """Initialize wallet with zero balance."""
        self.balance = 0

    def deposit(self, amount):
        """
        Deposit money into wallet.

        Args:
            amount (int): Amount to deposit.

        Raises:
            InvalidAmountError: If amount <= 0.
        """
        if amount <= 0:
            raise InvalidAmountError(
                f"Attempted to process {amount} VND."
            )

        self.balance += amount

        logging.info(
            "Deposit successful: +%s VND. Current Balance: %s",
            amount,
            self.balance
        )

    def transfer(self, phone, amount):
        """
        Transfer money to another user.

        Args:
            phone (str): Receiver phone number.
            amount (int): Amount to transfer.

        Raises:
            InvalidAmountError: If amount <= 0.
            InsufficientBalanceError: If balance not enough.
        """
        if amount <= 0:
            raise InvalidAmountError(
                f"Attempted to process {amount} VND."
            )

        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Attempted to transfer {amount} VND "
                f"with balance {self.balance} VND."
            )

        if amount >= self.HIGH_VALUE_THRESHOLD:
            logging.warning(
                "High value transaction detected: %s VND to %s",
                amount,
                phone
            )

        self.balance -= amount

        logging.info(
            "Transfer successful: -%s VND to %s. "
            "Current Balance: %s",
            amount,
            phone,
            self.balance
        )

    def get_balance(self):
        """
        Return current balance.

        Returns:
            int: Wallet balance.
        """
        logging.info(
            "Balance checked. Current Balance: %s",
            self.balance
        )

        return self.balance


def format_currency(amount):
    """
    Format amount with comma separator.

    Args:
        amount (int): Amount.

    Returns:
        str: Formatted amount.
    """
    return f"{amount:,}"


def input_amount(action):
    """
    Get valid amount from user.

    Args:
        action (str): Transaction type.

    Returns:
        int: Valid amount.
    """
    while True:
        try:
            amount = int(
                input(f"Nhập số tiền cần {action}: ")
            )
            return amount

        except ValueError:
            logging.error(
                "ValueError: Invalid numeric input for %s.",
                action
            )
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")


def validate_phone(phone):
    """
    Validate Vietnamese phone number.

    Args:
        phone (str): Phone number.

    Returns:
        bool: Validation result.
    """
    return bool(re.fullmatch(r"\d{10}", phone))


def deposit_money(wallet):
    """Handle deposit transaction."""
    print("\n--- NẠP TIỀN VÀO VÍ ---")

    amount = input_amount("nạp")

    try:
        wallet.deposit(amount)

        print(
            f"\nNạp tiền thành công: "
            f"+{format_currency(amount)} VND"
        )
        print(
            f"Số dư hiện tại: "
            f"{format_currency(wallet.balance)} VND"
        )

    except InvalidAmountError as error:
        logging.error(
            "InvalidAmountError: %s",
            error
        )
        print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")


def transfer_money(wallet):
    """Handle transfer transaction."""
    print("\n--- CHUYỂN TIỀN ---")

    while True:
        phone = input(
            "Nhập số điện thoại người nhận: "
        )

        if validate_phone(phone):
            break

        print("Lỗi: Số điện thoại phải gồm 10 chữ số.")

    amount = input_amount("chuyển")

    try:
        wallet.transfer(phone, amount)

        print(
            f"\nChuyển tiền thành công tới số điện thoại "
            f"{phone}."
        )
        print(
            f"Số tiền đã chuyển: "
            f"{format_currency(amount)} VND"
        )
        print(
            f"Số dư còn lại: "
            f"{format_currency(wallet.balance)} VND"
        )

    except InvalidAmountError as error:
        logging.error(
            "InvalidAmountError: %s",
            error
        )
        print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")

    except InsufficientBalanceError as error:
        logging.error(
            "InsufficientBalanceError: %s",
            error
        )
        print(
            "\nGiao dịch thất bại: "
            "Số dư của bạn không đủ."
        )
        print(
            f"Số dư hiện tại: "
            f"{format_currency(wallet.balance)} VND"
        )


def show_balance(wallet):
    """Display wallet balance."""
    print("\n--- SỐ DƯ VÍ MOMO ---")

    balance = wallet.get_balance()

    print(
        f"Số dư hiện tại: "
        f"{format_currency(balance)} VND"
    )


def display_menu():
    """Display application menu."""
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("=====================================")


def main():
    """Main application."""
    wallet = Wallet()

    while True:
        display_menu()

        choice = input(
            "Chọn chức năng (1-4): "
        )

        if choice == "1":
            deposit_money(wallet)

        elif choice == "2":
            transfer_money(wallet)

        elif choice == "3":
            show_balance(wallet)

        elif choice == "4":
            logging.info("System shutdown")
            print(
                "\nCảm ơn bạn đã sử dụng dịch vụ."
            )
            break

        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()