import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DRINK_MENU = {
    "P1": {
        "name": "Phin Sữa Đá",
        "price": 35000
    },
    "F1": {
        "name": "Freeze Trà Xanh",
        "price": 55000
    },
    "T1": {
        "name": "Trà Sen Vàng",
        "price": 45000
    }
}


class ItemNotFoundError(Exception):
    """Raised when drink code does not exist."""


class InvalidQuantityError(Exception):
    """Raised when quantity is invalid."""


def format_currency(amount):
    """
    Format currency with comma separator.

    Args:
        amount (int): Money amount.

    Returns:
        str: Formatted currency.
    """
    return f"{amount:,}"


def display_menu():
    """Display main menu."""
    print("\n========== HIGHLANDS MINI POS ==========")
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")
    print("========================================")


def view_menu():
    """Display drink menu."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")

    for code, item in DRINK_MENU.items():
        print(
            f"[{code}] - "
            f"{item['name']} - "
            f"{format_currency(item['price'])} VNĐ"
        )


def add_to_order(order, drink_code, quantity):
    """
    Add item to order.

    Args:
        order (list): Current order.
        drink_code (str): Drink code.
        quantity (int): Quantity.

    Raises:
        ItemNotFoundError
        InvalidQuantityError
    """
    drink_code = drink_code.strip().upper()

    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError(drink_code)

    if quantity <= 0:
        raise InvalidQuantityError(quantity)

    order.append(
        {
            "code": drink_code,
            "quantity": quantity
        }
    )

    logging.info(
        "Added %s of %s to order",
        quantity,
        drink_code
    )


def handle_add_to_order(order):
    """Handle add item process."""
    print("\n--- THÊM MÓN VÀO GIỎ ---")

    try:
        drink_code = input(
            "Nhập mã đồ uống: "
        )

        quantity = int(
            input("Nhập số lượng: ")
        )

        add_to_order(
            order,
            drink_code,
            quantity
        )

        code = drink_code.strip().upper()

        print(
            f"Đã thêm {quantity} x "
            f"{DRINK_MENU[code]['name']} "
            f"vào giỏ hàng."
        )

    except ValueError:
        logging.error(
            "ValueError - Invalid quantity input"
        )
        print(
            "Vui lòng nhập số lượng "
            "là một số nguyên!"
        )

    except ItemNotFoundError as error:
        logging.warning(
            "ItemNotFoundError - Code: %s",
            error
        )
        print(
            "Mã đồ uống không hợp lệ, "
            "vui lòng kiểm tra lại thực đơn!"
        )

    except InvalidQuantityError as error:
        logging.warning(
            "InvalidQuantityError - Quantity: %s",
            error
        )
        print("Số lượng phải lớn hơn 0!")


def calculate_total(order):
    """
    Calculate order total.

    Args:
        order (list): Current order.

    Returns:
        int: Total amount.
    """
    total = 0

    for item in order:
        code = item["code"]
        quantity = item["quantity"]

        total += (
            DRINK_MENU[code]["price"] *
            quantity
        )

    return total


def view_order(order):
    """
    Display current order.

    Args:
        order (list): Current order.
    """
    if not order:
        print(
            "Giỏ hàng trống, vui lòng "
            "chọn món (Chức năng 2)."
        )
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")

    print(
        "Mã SP | Tên đồ uống"
        "          | Đơn giá  | "
        "Số lượng | Thành tiền"
    )

    print("-" * 64)

    for item in order:
        code = item["code"]
        quantity = item["quantity"]

        name = DRINK_MENU[code]["name"]
        price = DRINK_MENU[code]["price"]

        subtotal = price * quantity

        print(
            f"{code:<5} | "
            f"{name:<20} | "
            f"{format_currency(price):<8} | "
            f"{quantity:<8} | "
            f"{format_currency(subtotal)} VNĐ"
        )

    print("-" * 64)

    total = calculate_total(order)

    print(
        f"Tổng tiền cần thanh toán: "
        f"{format_currency(total)} VNĐ"
    )


def checkout(order):
    """
    Process checkout.

    Args:
        order (list): Current order.
    """
    if not order:
        print(
            "Giỏ hàng trống, vui lòng "
            "chọn món (Chức năng 2)."
        )
        return

    total = calculate_total(order)

    print("\n--- THANH TOÁN ---")
    print(
        f"Tổng tiền cần thanh toán: "
        f"{format_currency(total)} VNĐ"
    )

    confirm = input(
        f"Xác nhận thanh toán "
        f"{format_currency(total)} VNĐ? (y/n): "
    ).strip().lower()

    if confirm == "y":
        logging.info(
            "Checkout successful"
        )

        order.clear()

        print("Thanh toán thành công.")
        print("Giỏ hàng đã được làm trống.")

    elif confirm == "n":
        print(
            "Đã hủy thao tác thanh toán. "
            "Quay lại menu chính."
        )

    else:
        print(
            "Lựa chọn không hợp lệ. "
            "Thanh toán đã bị hủy."
        )


def main():
    """Main program."""
    current_order = []

    while True:
        display_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        )

        if choice == "1":
            view_menu()

        elif choice == "2":
            handle_add_to_order(
                current_order
            )

        elif choice == "3":
            view_order(
                current_order
            )

        elif choice == "4":
            checkout(
                current_order
            )

        elif choice == "5":
            logging.info(
                "Cashier logged out. "
                "System shutdown."
            )

            print(
                "Đã thoát ca làm việc. "
                "Hẹn gặp lại!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ."
            )


if __name__ == "__main__":
    main()