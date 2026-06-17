import random

from utils.player_utils import find_player

rewards = [
    "Potion",
    "Iron Sword",
    "Magic Scroll",
    "100 Gold",
    "Mana Stone"
]

shop_items = {
    "Potion": 50,
    "Iron Sword": 200,
    "Magic Book": 300,
    "Mana Stone": 150
}


def open_treasure_chest(records):

    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input(
        "Nhập mã người chơi mở rương: "
    )

    player_index = find_player(
        records,
        player_id
    )

    if player_index == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[player_index]

    reward = random.choice(rewards)

    print(
        f">> Người chơi {player['name']} "
        f"đã mở rương!"
    )

    print(
        f">> Phần thưởng nhận được: "
        f"{reward}"
    )

    if reward == "100 Gold":
        player["gold"] += 100

        print(
            ">> Nhận thêm 100 vàng!"
        )

    else:
        player["inventory"].append(reward)

        print(
            f">> Đã thêm {reward} "
            f"vào túi đồ."
        )


def buy_item(records):

    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    player_id = input(
        "Nhập mã người chơi: "
    )

    player_index = find_player(
        records,
        player_id
    )

    if player_index == -1:
        print("Không tìm thấy người chơi!")
        return

    item_name = input(
        "Nhập tên vật phẩm muốn mua: "
    ).strip()

    if item_name not in shop_items:
        print(
            "Vật phẩm không tồn tại "
            "trong cửa hàng!"
        )
        return

    player = records[player_index]

    item_price = shop_items[item_name]

    if player["gold"] < item_price:
        print(
            "Không đủ vàng để mua "
            "vật phẩm này!"
        )
        return

    player["gold"] -= item_price

    player["inventory"].append(item_name)

    print(
        f">> Mua thành công "
        f"{item_name}!"
    )

    print(
        f">> Số vàng còn lại: "
        f"{player['gold']}"
    )