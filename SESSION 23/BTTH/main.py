from hrm_package.attendance_logic import (
    clock_in,
    clock_out
)

from hrm_package.time_calc import (
    evaluate_flex_time as evaluate
)

from hrm_package.ui_display import (
    display_records
)

attendance_book = [
    {
        "id": "NV01",
        "name": "Nguyễn Văn A",
        "times": (
            "08:30",
            "17:30"
        )
    },
    {
        "id": "NV02",
        "name": "Trần Thị B",
        "times": (
            "09:30",
            None
        )
    },
    {
        "id": "NV03",
        "name": "Lê Văn C",
        "times": (
            "10:15",
            "19:15"
        )
    }
]


def show_menu():

    print(
        "\n=== HỆ THỐNG CHẤM CÔNG "
        "RIKKEI (FLEX-TIME) ==="
    )

    print(
        "1. Xem bảng chấm công ngày"
    )

    print(
        "2. Chấm công Vào (Clock-in)"
    )

    print(
        "3. Chấm công Ra (Clock-out)"
    )

    print(
        "4. Đánh giá vi phạm"
    )

    print(
        "5. Thoát chương trình"
    )

    print("=" * 49)


def main():

    while True:

        show_menu()

        try:

            choice = int(
                input(
                    "Chọn chức năng (1-5): "
                )
            )

            if choice == 1:

                display_records(
                    attendance_book
                )

            elif choice == 2:

                clock_in(
                    attendance_book
                )

            elif choice == 3:

                clock_out(
                    attendance_book
                )

            elif choice == 4:

                evaluate(
                    attendance_book
                )

            elif choice == 5:

                print(
                    "Thoát chương trình..."
                )

                break

            else:

                print(
                    "Vui lòng chọn từ 1-5."
                )

        except ValueError:

            print(
                "Vui lòng nhập số!"
            )


if __name__ == "__main__":
    main()