from datetime import datetime


def parse_and_inspect_date(date_str):
    try:
        return datetime.strptime(
            date_str,
            "%Y-%m-%d"
        )

    except ValueError:
        print(
            f"[WARNING] Ngày không hợp lệ: "
            f"{date_str}"
        )
        return None