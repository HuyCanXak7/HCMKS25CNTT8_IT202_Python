from datetime import datetime as dt


def evaluate_flex_time(attendance_book):

    print("\n--- ĐÁNH GIÁ VI PHẠM ---")

    for employee in attendance_book:

        clock_in_time = employee["times"][0]
        clock_out_time = employee["times"][1]

        if clock_out_time is None:
            print(
                f"{employee['id']} - "
                f"Chưa chấm công ra."
            )
            continue

        start_time = dt.strptime(
            clock_in_time,
            "%H:%M"
        )

        end_time = dt.strptime(
            clock_out_time,
            "%H:%M"
        )

        max_time = dt.strptime(
            "10:00",
            "%H:%M"
        )

        if start_time > max_time:

            print(
                f"{employee['id']} - "
                f"Vi phạm: Đến muộn quá "
                f"90 phút."
            )

            continue

        working_hours = (
            end_time - start_time
        ).seconds / 3600

        if working_hours < 9:

            print(
                f"{employee['id']} - "
                f"Vi phạm: Về sớm, "
                f"chưa hoàn thành đủ "
                f"9 tiếng bù giờ."
            )

        else:

            print(
                f"{employee['id']} - "
                f"Hợp lệ: Hoàn thành "
                f"ca làm việc."
            )