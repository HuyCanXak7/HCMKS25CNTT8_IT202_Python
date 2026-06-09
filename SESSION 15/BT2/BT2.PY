atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():
    """
    Hiển thị số dư tài khoản và tiền mặt ATM.

    Parameters:
        None

    Returns:
        None
    """
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(
        f"Tài khoản của bạn: "
        f"{user_account_balance:,} VND"
    )
    print(
        f"(Debug) Tiền mặt trong ATM: "
        f"{atm_vault_balance:,} VND"
    )


def deposit_money(amount):
    """
    Nạp tiền vào tài khoản.

    Parameters:
        amount (int): Số tiền cần nạp.

    Returns:
        bool: True nếu thành công.
    """
    global atm_vault_balance
    global user_account_balance

    user_account_balance += amount
    atm_vault_balance += amount

    return True


def check_withdrawal_rules(amount):
    """
    Kiểm tra điều kiện rút tiền.

    Parameters:
        amount (int): Số tiền cần rút.

    Returns:
        tuple:
        (status, total_deduction)
    """
    fee = 1100
    total_deduction = amount + fee

    if amount % 50000 != 0:
        return "INVALID_MULTIPLE", None

    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS", None

    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH", None

    return "OK", total_deduction


def execute_withdrawal(
        total_deduction,
        amount_to_dispense
):
    """
    Thực hiện giao dịch rút tiền.

    Parameters:
        total_deduction (int)
        amount_to_dispense (int)

    Returns:
        None
    """
    global atm_vault_balance
    global user_account_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense

    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")

    print(
        f"Bạn đã rút thành công "
        f"{amount_to_dispense:,} VND."
    )

    print(
        f"Số dư tài khoản còn lại: "
        f"{user_account_balance:,} VND."
    )


def input_positive_amount(message):
    """
    Nhập số tiền hợp lệ.

    Parameters:
        message (str)

    Returns:
        int
    """
    while True:

        try:
            amount = int(input(message))

            if amount <= 0:
                print("Số tiền không hợp lệ")
                continue

            return amount

        except ValueError:
            print("Số tiền không hợp lệ")


def main():
    """
    Chương trình chính.

    Parameters:
        None

    Returns:
        None
    """

    while True:

        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")

        choice = input(
            "Vui lòng chọn giao dịch (1-4): "
        )

        if choice == "1":

            display_balances()

        elif choice == "2":

            print("\n--- NẠP TIỀN ---")

            amount = input_positive_amount(
                "Nhập số tiền muốn nạp: "
            )

            if deposit_money(amount):

                print(
                    "Giao dịch thành công! "
                    f"Số dư tài khoản hiện tại: "
                    f"{user_account_balance:,} VND."
                )

        elif choice == "3":

            print("\n--- RÚT TIỀN ---")

            amount = input_positive_amount(
                "Nhập số tiền cần rút: "
            )

            status, total_deduction = (
                check_withdrawal_rules(amount)
            )

            if status == "INVALID_MULTIPLE":

                print(
                    "Số tiền rút phải là "
                    "bội số của 50,000"
                )

            elif status == "INSUFFICIENT_FUNDS":

                print(
                    "Giao dịch thất bại: "
                    "Số dư tài khoản không đủ."
                )

            elif status == "ATM_OUT_OF_CASH":

                print(
                    "Giao dịch thất bại: "
                    "Máy ATM không đủ tiền mặt "
                    "để phục vụ."
                )

            else:

                execute_withdrawal(
                    total_deduction,
                    amount
                )

        elif choice == "4":

            print(
                "Cảm ơn quý khách đã sử dụng dịch vụ!"
            )
            break

        else:

            print(
                "Lựa chọn không hợp lệ!"
            )


if __name__ == "__main__":
    main()