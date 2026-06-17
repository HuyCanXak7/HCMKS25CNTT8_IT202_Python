import random

from utils.player_utils import find_player

monsters = [
    {
        "name": "Bug Python",
        "damage": 20,
        "reward_gold": 100
    },
    {
        "name": "Import Error",
        "damage": 35,
        "reward_gold": 150
    },
    {
        "name": "Module Not Found",
        "damage": 50,
        "reward_gold": 250
    }
]


def fight_monster(records):

    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input(
        "Nhập mã người chơi chiến đấu: "
    )

    player_index = find_player(
        records,
        player_id
    )

    if player_index == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[player_index]

    if player["hp"] <= 0:
        print(
            "Người chơi đã gục ngã, "
            "không thể tiếp tục chiến đấu!"
        )
        return

    monster = random.choice(monsters)

    print(
        f">> Quái vật xuất hiện: "
        f"{monster['name']}"
    )

    player["hp"] -= monster["damage"]

    print(
        f">> {player['name']} "
        f"bị mất "
        f"{monster['damage']} HP."
    )

    if player["hp"] > 0:

        player["gold"] += monster["reward_gold"]

        print(
            f">> Chiến thắng! "
            f"Bạn nhận được "
            f"{monster['reward_gold']} vàng."
        )

        print(
            f">> HP còn lại: "
            f"{player['hp']}"
        )

    else:

        player["hp"] = 0

        print(
            ">> Bạn đã bị đánh bại!"
        )