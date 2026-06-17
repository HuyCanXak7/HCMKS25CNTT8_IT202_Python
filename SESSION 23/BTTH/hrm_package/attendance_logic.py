def clock_in(attendance_book):
    employee_id = input("Nhập mã nhân viên: ").strip().upper()

    for employee in attendance_book:
        if employee["id"] == employee_id:
            print("Mã nhân viên đã tồn tại!")
            return

    employee_name = input("Nhập tên nhân viên: ").strip()
    clock_in_time = input("Nhập giờ vào (HH:MM): ").strip()

    attendance_book.append(
        {
            "id": employee_id,
            "name": employee_name,
            "times": (clock_in_time, None)
        }
    )

    print(
        f"Thành công: Đã ghi nhận "
        f"{employee_id} chấm công vào lúc "
        f"{clock_in_time}!"
    )


def clock_out(attendance_book):
    employee_id = input(
        "Nhập mã nhân viên: "
    ).strip().upper()

    clock_out_time = input(
        "Nhập giờ ra (HH:MM): "
    ).strip()

    for employee in attendance_book:

        if employee["id"] == employee_id:

            clock_in_time = employee["times"][0]

            employee["times"] = (
                clock_in_time,
                clock_out_time
            )

            print(
                f"Đã ghi nhận giờ ra "
                f"{clock_out_time}"
            )
            return

    print("Không tìm thấy nhân viên!")