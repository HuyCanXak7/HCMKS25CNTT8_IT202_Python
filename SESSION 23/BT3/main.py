from core.logistics import (
    show_flight
)

from core.manager import (
    add_flight
)

from utils.time_helper import (
    calculate_eta
)

from utils.file_helper import (create_log_folder)


flights = [
    {
        "flight_id": "RA001",
        "passengers": 154,
        "depart_time":
            "2026-06-15 08:00:00",
        "duration_min": 120
    },
    {
        "flight_id": "RA002",
        "passengers": 85,
        "depart_time":
            "2026-06-15 13:30:00",
        "duration_min": 45
    }
]


def show_menu():

    print(
        "\n===== HỆ THỐNG "
        "ĐIỀU HÀNH BAY "
        "RIKKEI AVIATION ====="
    )

    print(
        "1. Hiển thị lịch trình "
        "và Thống kê hậu cần"
    )

    print(
        "2. Tiếp nhận "
        "chuyến bay mới"
    )

    print(
        "3. Tính thời gian "
        "hạ cánh dự kiến (ETA)"
    )

    print(
        "4. Khởi tạo thư mục "
        "lưu trữ log hệ thống"
    )

    print(
        "5. Thoát chương trình"
    )

    print("=" * 50)


while True:

    show_menu()

    try:
        choice = int(
            input(
                "Nhập lựa chọn của bạn: "
            )
        )

        if choice == 1:

            show_flight(flights)

        elif choice == 2:

            add_flight(flights)

        elif choice == 3:

            print(
                "\n----- TÍNH TOÁN "
                "THỜI GIAN HẠ CÁNH "
                "(ETA) -----"
            )

            flight_id = input(
                "Nhập mã chuyến bay "
                "cần tính: "
            )

            calculate_eta(
                flight_id,
                flights
            )

        elif choice == 4:

            create_log_folder()

        elif choice == 5:

            print(
                "Cảm ơn kỹ sư đã sử dụng "
                "hệ thống!"
            )

            break

        else:

            print(
                "Vui lòng nhập từ 1-5."
            )

    except ValueError:

        print(
            "Lựa chọn không hợp lệ. "
            "Vui lòng nhập số từ 1-5."
        )