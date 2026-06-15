
import logging

logging.basicConfig(
    filename="fantasy_league.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

players = [
    {
        "player_id": "T101",
        "name": "Faker",
        "market_value": 5000,
        "fan_tokens": 1500,
        "match_points": 0,
        "form_multiplier": 1.0
    },
    {
        "player_id": "GEN01",
        "name": "Chovy",
        "market_value": 4800,
        "fan_tokens": 800,
        "match_points": 500,
        "form_multiplier": 1.2
    },
    {
        "player_id": "DRX01",
        "name": "Deft",
        "market_value": 3000,
        "fan_tokens": 0,
        "match_points": 0,
        "form_multiplier": 0.8
    }
]


def find_player_by_id(players: list, player_id: str) -> int:
    """
    Tìm vị trí tuyển thủ theo ID.
    """
    player_id = player_id.strip().upper()

    for index, player in enumerate(players):
        if player.get("player_id", "").upper() == player_id:
            return index

    return -1


def get_investment_status(fan_tokens: int) -> str:
    """
    Trả về trạng thái đầu tư.
    """
    if fan_tokens == 0:
        return "Chưa có người đầu tư"
    elif fan_tokens <= 1000:
        return "Đang thu hút"
    return "Tuyển thủ Hot"


def display_market(players: list) -> None:
    """
    Hiển thị sàn giao dịch tuyển thủ.
    """
    logging.info("User viewed the player market.")

    if not players:
        print("Sàn giao dịch hiện chưa có tuyển thủ nào.")
        return

    print("\n--- SÀN GIAO DỊCH TUYỂN THỦ ---")

    print(
        f"{'ID':<10}"
        f"{'Tên tuyển thủ':<18}"
        f"{'Giá trị':<15}"
        f"{'Fan Token':<12}"
        f"{'Điểm trận':<12}"
        f"{'Hệ số':<10}"
        f"{'Trạng thái'}"
    )

    print("-" * 95)

    for player in players:
        player_id = player.get("player_id", "Unknown")
        name = player.get("name", "Unknown")
        market_value = player.get("market_value", 0)
        fan_tokens = player.get("fan_tokens", 0)
        match_points = player.get("match_points", 0)
        form_multiplier = player.get("form_multiplier", 1.0)

        status = get_investment_status(fan_tokens)

        print(
            f"{player_id:<10}"
            f"{name:<18}"
            f"{market_value:<15,}"
            f"{fan_tokens:<12,}"
            f"{match_points:<12,}"
            f"{form_multiplier:<10}"
            f"{status}"
        )


def invest_tokens(players: list) -> None:
    """
    Đầu tư fan token.
    """
    print("\n--- ĐẦU TƯ FAN TOKEN ---")

    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    index = find_player_by_id(players, player_id)

    if index == -1:
        print("Không tìm thấy tuyển thủ!")
        logging.warning(
            f"Invest failed - Player {player_id} not found"
        )
        return

    while True:
        try:
            amount = int(
                input("Nhập số token muốn đầu tư: ")
            )

            if amount <= 0:
                raise ValueError

            break

        except ValueError:
            print(
                "Số token phải là số nguyên dương. "
                "Vui lòng nhập lại."
            )
            logging.warning(
                "Invalid token input while investing"
            )

    players[index]["fan_tokens"] += amount

    print(
        f"\nThành công: Đã đầu tư {amount} token "
        f"vào tuyển thủ {player_id}."
    )

    print(
        f"Số Fan Token hiện tại của "
        f"{players[index]['name']}: "
        f"{players[index]['fan_tokens']:,}"
    )

    logging.info(
        f"Invested {amount} tokens into {player_id}"
    )


def calc_actual_withdrawal(amount: int) -> float:
    """
    Tính số token thực nhận sau phí 10%.
    """
    return amount * 0.9


def withdraw_tokens(players: list) -> None:
    """
    Rút vốn fan token.
    """
    print("\n--- RÚT VỐN FAN TOKEN ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    index = find_player_by_id(players, player_id)

    if index == -1:
        print("Không tìm thấy tuyển thủ!")
        return

    while True:
        try:
            amount = int(
                input("Nhập số token muốn rút: ")
            )

            if amount <= 0:
                raise ValueError

            break

        except ValueError:
            print(
                "Số token phải là số nguyên dương."
            )

    current_tokens = players[index]["fan_tokens"]

    if amount > current_tokens:
        print(
            "Không thể rút. "
            "Số token muốn rút vượt quá số "
            "Fan Token hiện có."
        )

        print(
            f"Fan Token hiện có của "
            f"{players[index]['name']}: "
            f"{current_tokens:,}"
        )

        logging.warning(
            "Withdraw failed - Amount exceeds current fan tokens"
        )
        return

    fee = amount * 0.1
    actual_received = calc_actual_withdrawal(amount)

    players[index]["fan_tokens"] -= amount

    print(
        f"\nThành công: Đã rút {amount} token "
        f"khỏi tuyển thủ {player_id}."
    )
    print(f"Phí giao dịch 10%: {fee} token")
    print(
        f"Số token thực nhận về ví: "
        f"{actual_received} token"
    )

    print(
        f"Fan Token còn lại của "
        f"{players[index]['name']}: "
        f"{players[index]['fan_tokens']:,}"
    )

    logging.info(
        f"Withdrawn {amount} tokens from "
        f"{player_id}. Actual received: "
        f"{actual_received}"
    )


def update_form(players: list) -> None:
    """
    Cập nhật hệ số phong độ.
    """
    print("\n--- CẬP NHẬT HỆ SỐ PHONG ĐỘ ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    index = find_player_by_id(players, player_id)

    if index == -1:
        print("Không tìm thấy tuyển thủ!")
        return

    while True:
        try:
            multiplier = float(
                input(
                    "Nhập hệ số phong độ mới "
                    "(0.5 - 2.5): "
                )
            )

            if not 0.5 <= multiplier <= 2.5:
                print(
                    "Hệ số phong độ chỉ được nằm "
                    "trong khoảng 0.5 đến 2.5."
                )
                continue

            break

        except ValueError:
            print(
                "Hệ số phong độ phải là số thực. "
                "Vui lòng nhập lại."
            )

    players[index]["form_multiplier"] = multiplier

    print(
        f"\nThành công: Đã cập nhật hệ số "
        f"phong độ cho "
        f"{players[index]['name']}."
    )

    print(f"Hệ số mới: x{multiplier}")

    logging.info(
        f"Updated form multiplier for "
        f"{player_id} to {multiplier}"
    )


def calculate_match_points(players: list) -> None:
    """
    Chấm điểm sau trận đấu.
    """
    print("\n--- CHẤM ĐIỂM SAU TRẬN ĐẤU ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    index = find_player_by_id(players, player_id)

    if index == -1:
        print("Không tìm thấy tuyển thủ!")
        return

    while True:
        try:
            base_points = float(
                input(
                    "Nhập điểm gốc của trận đấu: "
                )
            )

            if base_points < 0:
                raise ValueError

            break

        except ValueError:
            print(
                "Điểm phải là số không âm."
            )

    multiplier = players[index]["form_multiplier"]

    earned_points = base_points * multiplier

    players[index]["match_points"] += earned_points

    print(
        f"\n>> Tuyển thủ "
        f"{players[index]['name']} "
        f"nhận được {earned_points} điểm "
        f"(Hệ số x{multiplier})."
    )

    print(
        f"Tổng điểm: "
        f"{players[index]['match_points']}"
    )

    logging.info(
        f"Added {earned_points} match points "
        f"to {player_id}"
    )


def main():
    while True:
        print("\n===== HỆ THỐNG RIKKEI ESPORTS FANTASY =====")
        print("1. Xem Sàn Giao Dịch Tuyển Thủ")
        print("2. Đầu tư Fan Token")
        print("3. Rút vốn (Hoàn trả Token)")
        print("4. Biến động phong độ")
        print("5. Chấm điểm sau trận đấu")
        print("6. Thoát hệ thống")
        print("=" * 50)

        choice = input(
            "Chọn chức năng (1-6): "
        ).strip()

        if choice == "1":
            display_market(players)

        elif choice == "2":
            invest_tokens(players)

        elif choice == "3":
            withdraw_tokens(players)

        elif choice == "4":
            update_form(players)

        elif choice == "5":
            calculate_match_points(players)

        elif choice == "6":
            logging.info(
                "Fantasy League system shutdown."
            )
            print(
                "Đóng hệ thống Rikkei Esports Fantasy."
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")
            logging.warning(
                "Invalid menu choice selected"
            )


if __name__ == "__main__":
    main()