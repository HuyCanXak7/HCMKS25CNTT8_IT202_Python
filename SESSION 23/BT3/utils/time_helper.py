from datetime import (
    datetime,
    timedelta
)


def calculate_eta(
    flight_id,
    flight_list
):

    found_flight = None

    for flight in flight_list:
        if (
            flight["flight_id"]
            == flight_id.upper()
        ):
            found_flight = flight
            break

    if not found_flight:
        print(
            "Không tìm thấy chuyến bay!"
        )
        return

    depart_time = datetime.strptime(
        found_flight["depart_time"],
        "%Y-%m-%d %H:%M:%S"
    )

    eta = depart_time + timedelta(
        minutes=
        found_flight["duration_min"]
    )

    print(
        f"-> Chuyến bay "
        f"{found_flight['flight_id']} "
        f"cất cánh lúc: "
        f"{found_flight['depart_time']}"
    )

    print(
        f"-> Thời gian hạ cánh "
        f"dự kiến (ETA): "
        f"{eta}"
    )