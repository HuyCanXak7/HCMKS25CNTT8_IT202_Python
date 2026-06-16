# Dữ liệu từ API: (Tên, Số trận, MMR)
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def calculate_bonus(matches, mmr):
    return (matches * 10) + (int(mmr) * 0.5)


def process_bonus(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        try:
            name = record[0]
            matches = record[1]
            mmr = record[2]

            bonus = calculate_bonus(matches, mmr)

            print(f"Tuyển thủ {name} nhận được {bonus} RP")

        except IndexError:
            print(f"{record[0]}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue

        except ValueError:
            print(f"{record[0]}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue


process_bonus(player_records)