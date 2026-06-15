# Dữ liệu thống kê
player_stats = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths


def process_player_kda(player_stats):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player in player_stats:
        name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(
                kills,
                deaths,
                assists
            )

            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda}")

        except ZeroDivisionError:
            print(f"{name}: KDA Hoàn hảo (Perfect Game)!")
            continue

        except ValueError:
            print(f"{name}: Lỗi dữ liệu không hợp lệ!")
            continue


process_player_kda(player_stats)