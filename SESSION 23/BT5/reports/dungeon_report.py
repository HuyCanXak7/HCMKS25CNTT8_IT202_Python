from operator import itemgetter
from datetime import datetime

from colorama import Fore


def get_status(hp):

    if hp <= 0:
        return "Đã gục ngã"

    if hp < 50:
        return "Nguy hiểm"

    if hp < 100:
        return "Ổn định"

    return "Sung sức"


def display_players(records):

    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    print(
        "\n--- DANH SÁCH NGƯỜI CHƠI ---"
    )

    for index, player in enumerate(
        records,
        start=1
    ):

        print(
            f"{index}. "
            f"Mã: {player['player_id']} "
            f"| Tên: {player['name']} "
            f"| HP: {player['hp']} "
            f"| Mana: {player['mana']} "
            f"| Gold: {player['gold']} "
            f"| Level: {player['level']} "
            f"| Trạng thái: "
            f"{get_status(player['hp'])}"
        )

    print("-" * 30)


def show_leaderboard(records):

    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    ranking = sorted(
        records,
        key=itemgetter(
            "level",
            "gold",
            "hp"
        ),
        reverse=True
    )

    print(
        "\n--- BẢNG XẾP HẠNG "
        "NGƯỜI CHƠI ---"
    )

    for index, player in enumerate(
        ranking,
        start=1
    ):

        print(
            f"{index}. "
            f"{player['name']} "
            f"| Level: {player['level']} "
            f"| Gold: {player['gold']} "
            f"| HP: {player['hp']}"
        )

    print("-" * 30)


def export_player_report(records):

    report_time = datetime.now()

    with open(
        "dungeon_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            f"THỜI GIAN: "
            f"{report_time}\n\n"
        )

        for player in records:

            file.write(
                f"{player['player_id']} - "
                f"{player['name']} - "
                f"Level {player['level']}\n"
            )

    print(
        Fore.GREEN +
        ">> Đã xuất báo cáo "
        "dungeon_report.txt"
    )