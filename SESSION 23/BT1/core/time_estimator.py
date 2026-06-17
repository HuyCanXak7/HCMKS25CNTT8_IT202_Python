from datetime import datetime, timedelta


def predict_eta(departure_str, distance_km, speed=60):
    departure_time = datetime.strptime(
        departure_str,
        "%Y-%m-%d %H:%M:%S"
    )

    hours_needed = distance_km / speed

    eta = departure_time + timedelta(hours=hours_needed)

    return eta