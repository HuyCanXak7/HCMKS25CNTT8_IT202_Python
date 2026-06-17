import colorama as clr

from data.players import player_records

from reports.dungeon_report import (
    display_players,
    show_leaderboard,
    export_player_report
)

from utils.item_utils import (
    open_treasure_chest,
    buy_item
)

from utils.battle_utils import (
    fight_monster
)

clr.init()


def show_menu():

    print(
        "\n===== RIKKEI DUNGEON "
        "- PYTHON MODULE ADVENTURE ====="
    )

    print(
        "1. Hiển thị danh sách người chơi"
    )

    print(
        "2. Mở rương báu ngẫu nhiên"
    )

    print(
        "3. Mua vật phẩm trong cửa hàng"
    )

    print(
        "4. Chiến đấu với quái vật"
    )

    print(
        "5. Xem bảng xếp hạng người chơi"
    )

    print(
        "6. Thoát chương trình"
    )

    print("=" * 52)


def main():

    while True:

        show_menu()

        try:

            choice = int(
                input(
                    "Chọn chức năng (1-6): "
                )
            )

            if choice == 1:

                display_players(
                    player_records
                )

            elif choice == 2:

                open_treasure_chest(
                    player_records
                )

            elif choice == 3:

                buy_item(
                    player_records
                )

            elif choice == 4:

                fight_monster(
                    player_records
                )

            elif choice == 5:

                show_leaderboard(
                    player_records
                )

            elif choice == 6:

                export_player_report(
                    player_records
                )

                print(
                    "\nCảm ơn bạn đã tham gia "
                    "Rikkei Dungeon!"
                )

                break

            else:

                print(
                    "Chức năng không hợp lệ."
                )

        except ValueError:

            print(
                "Vui lòng nhập số từ 1-6."
            )


if __name__ == "__main__":
    main()