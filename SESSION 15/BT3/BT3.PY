available_seats = 50
flight_revenue = 0.0

BASE_PRICE = 2000.0
MAX_CAPACITY = 50


def calculate_ticket_cost(quantity, seat_class):
    """
    Tính tổng chi phí vé máy bay.

    Parameters:
        quantity (int): Số lượng vé.
        seat_class (int): 1 = Economy, 2 = Business.

    Returns:
        float: Tổng tiền sau khi cộng phí dịch vụ.
    """

    if seat_class == 1:
        ticket_price = BASE_PRICE
    else:
        ticket_price = BASE_PRICE * 1.5

    subtotal = ticket_price * quantity
    service_fee = subtotal * 0.05

    return subtotal + service_fee


def book_tickets(quantity, seat_class, total_cost):
    """
    Xử lý đặt vé.
    """
    global available_seats
    global flight_revenue

    if quantity > available_seats:
        print(
            f"Rất tiếc, chuyến bay chỉ còn "
            f"{available_seats} chỗ trống."
        )
        return False

    available_seats -= quantity
    flight_revenue += total_cost

    if seat_class == 1:
        class_name = "Economy"
        unit_price = BASE_PRICE
    else:
        class_name = "Business"
        unit_price = BASE_PRICE * 1.5

    subtotal = unit_price * quantity
    service_fee = subtotal * 0.05

    print("\n-> Xác nhận đặt chỗ:")
    print(
        f"Số lượng: {quantity} | "
        f"Hạng: {class_name}"
    )
    print(f"Tạm tính: ${subtotal:.1f}")
    print(f"Phí dịch vụ (5%): ${service_fee:.1f}")
    print(f"Tổng thanh toán: ${total_cost:.1f}")

    print(
        f"Đặt vé thành công! "
        f"Ghế trống còn lại: {available_seats}"
    )

    return True


def cancel_tickets(quantity):
    """
    Xử lý hủy vé và hoàn tiền.
    """
    global available_seats
    global flight_revenue

    if available_seats + quantity > MAX_CAPACITY:
        print(
            "Lỗi: Số lượng vé hủy vượt quá "
            "số vé đã bán ra."
        )
        return None

    refund_amount = quantity * BASE_PRICE * 0.8

    available_seats += quantity
    flight_revenue -= refund_amount

    print(
        f"Hủy vé thành công. "
        f"Hệ thống đã hoàn lại: "
        f"${refund_amount:.1f} "
        f"(80% giá cơ bản)."
    )

    print(
        f"Ghế trống hiện tại: "
        f"{available_seats}"
    )

    return refund_amount


def display_flight_status():
    """
    Hiển thị báo cáo tình trạng chuyến bay.

    Report Format:
    - Sức chứa tối đa
    - Ghế đã đặt
    - Ghế trống
    - Tổng doanh thu
    """

    booked_seats = MAX_CAPACITY - available_seats

    print("\n--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_CAPACITY}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(
        f"Tổng doanh thu hiện tại: "
        f"${flight_revenue:.1f}"
    )


def input_positive_integer(message):
    """
    Nhập số nguyên dương.
    """
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print(
                    "Giá trị phải lớn hơn 0."
                )
                continue

            return value

        except ValueError:
            print(
                "Vui lòng nhập số hợp lệ."
            )


def input_ticket_class():
    """
    Nhập hạng vé hợp lệ.
    """
    while True:

        seat_class = input(
            "Chọn hạng vé "
            "(1: Economy, 2: Business): "
        )

        if seat_class in ("1", "2"):
            return int(seat_class)

        print(
            "Hạng vé không hợp lệ."
        )


def main():

    while True:

        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("=============================================")

        choice = input(
            "Chọn chức năng (1-4): "
        )

        if choice == "1":

            print("\n--- ĐẶT VÉ MÁY BAY ---")

            quantity = input_positive_integer(
                "Nhập số lượng vé: "
            )

            seat_class = input_ticket_class()

            total_cost = calculate_ticket_cost(
                quantity,
                seat_class
            )

            book_tickets(
                quantity,
                seat_class,
                total_cost
            )

        elif choice == "2":

            print(
                "\n--- HỦY VÉ & HOÀN TIỀN ---"
            )

            quantity = input_positive_integer(
                "Nhập số lượng vé muốn hủy: "
            )

            cancel_tickets(quantity)

        elif choice == "3":

            display_flight_status()

        elif choice == "4":

            print(
                "Đóng hệ thống thành công!"
            )
            print(
                "Cảm ơn bạn đã sử dụng SkyBooking."
            )

            break

        else:

            print(
                "Lựa chọn không hợp lệ!"
            )


if __name__ == "__main__":
    main()