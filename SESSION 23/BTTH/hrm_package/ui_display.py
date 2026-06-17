from tabulate import tabulate


def display_records(attendance_book):

    table_data = []

    for employee in attendance_book:

        clock_out_time = employee["times"][1]

        if clock_out_time is None:
            clock_out_time = "[Đang làm việc]"

        table_data.append(
            [
                employee["id"],
                employee["name"],
                employee["times"][0],
                clock_out_time
            ]
        )

    print("\n--- BẢNG CHẤM CÔNG ---")

    print(
        tabulate(
            table_data,
            headers=[
                "Mã NV",
                "Tên Nhân Viên",
                "Giờ Vào",
                "Giờ Ra"
            ],
            tablefmt="grid"
        )
    )