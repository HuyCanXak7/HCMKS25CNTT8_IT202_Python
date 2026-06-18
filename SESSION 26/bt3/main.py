from abc import ABC, abstractmethod


class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name

        # Edge Case: HP hoặc ATK <= 0
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + (self.calculate_skill_damage() * 1.5)

    def __add__(self, other):
        if isinstance(other, Champion):
            return (
                self.get_combat_power()
                + other.get_combat_power()
            )

        if isinstance(other, (int, float)):
            return (
                self.get_combat_power()
                + other
            )

        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return (
                other
                + self.get_combat_power()
            )

        return NotImplemented

    def __gt__(self, other):
        if not isinstance(other, Champion):
            return NotImplemented

        return (
            self.get_combat_power()
            > other.get_combat_power()
        )


class Warrior(Champion):
    def __init__(
        self,
        champion_id,
        name,
        base_hp,
        base_atk,
        shield_bonus
    ):
        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk
        )

        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return (
            self.base_atk * 2
            + self.shield_bonus
        )


class Mage(Champion):
    def __init__(
        self,
        champion_id,
        name,
        base_hp,
        base_atk,
        ability_power
    ):
        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk
        )

        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return (
            self.base_atk
            * self.ability_power
        )


def find_champion_by_id(
    champion_pool,
    champion_id
):
    for champion in champion_pool:
        if champion.champion_id == champion_id:
            return champion

    return None


def display_champion_pool(
    champion_pool
):
    print(
        "\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---"
    )

    print(
        f"{'Mã':<8}"
        f"{'Tên tướng':<22}"
        f"{'Hệ':<12}"
        f"{'HP':<8}"
        f"{'ATK':<8}"
        f"{'Chỉ số riêng':<20}"
        f"{'Chiến lực':<12}"
    )

    print("-" * 90)

    for champion in champion_pool:

        if isinstance(champion, Warrior):
            champion_type = "Warrior"
            special_stat = (
                f"Armor: {champion.shield_bonus}"
            )

        else:
            champion_type = "Mage"
            special_stat = (
                f"Mana: {champion.ability_power}"
            )

        print(
            f"{champion.champion_id:<8}"
            f"{champion.name:<22}"
            f"{champion_type:<12}"
            f"{champion.base_hp:<8}"
            f"{champion.base_atk:<8}"
            f"{special_stat:<20}"
            f"{champion.get_combat_power():.0f}"
        )

    print("-" * 90)


def add_new_champion(
    champion_pool
):
    print("\n--- THÊM QUÂN CỜ MỚI ---")
    print("1. Warrior")
    print("2. Mage")

    champion_type = input(
        "Chọn hệ tướng: "
    )

    champion_id = input(
        "Nhập mã tướng: "
    ).strip().upper()

    # Edge Case: Trùng mã
    if find_champion_by_id(
        champion_pool,
        champion_id
    ):
        print(
            "Mã tướng đã tồn tại!"
        )
        return

    name = input(
        "Nhập tên tướng: "
    )

    try:
        hp = int(input("Nhập HP: "))
        atk = int(input("Nhập ATK: "))
    except ValueError:
        print("Dữ liệu không hợp lệ!")
        return

    if champion_type == "1":

        try:
            armor = int(
                input("Nhập Armor: ")
            )
        except ValueError:
            print("Armor không hợp lệ!")
            return

        champion = Warrior(
            champion_id,
            name,
            hp,
            atk,
            armor
        )

        champion_pool.append(
            champion
        )

        print(
            "\nThêm tướng Warrior thành công!"
        )

    elif champion_type == "2":

        try:
            ability_power = float(
                input(
                    "Nhập Ability Power: "
                )
            )
        except ValueError:
            print(
                "Ability Power không hợp lệ!"
            )
            return

        champion = Mage(
            champion_id,
            name,
            hp,
            atk,
            ability_power
        )

        champion_pool.append(
            champion
        )

        print(
            "\nThêm tướng Mage thành công!"
        )

    else:
        print("Lựa chọn không hợp lệ!")
        return

    print(
        f"Mã: {champion.champion_id}"
        f" | Tên: {champion.name}"
        f" | Chiến lực: "
        f"{champion.get_combat_power():.0f}"
    )


def compare_champions(
    champion_pool
):
    print(
        "\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---"
    )

    first_id = input(
        "Nhập mã tướng thứ nhất: "
    ).strip().upper()

    second_id = input(
        "Nhập mã tướng thứ hai: "
    ).strip().upper()

    champion_1 = find_champion_by_id(
        champion_pool,
        first_id
    )

    champion_2 = find_champion_by_id(
        champion_pool,
        second_id
    )

    if champion_1 is None:
        print(
            f"Mã tướng {first_id} "
            f"không hợp lệ!"
        )
        return

    if champion_2 is None:
        print(
            f"Mã tướng {second_id} "
            f"không hợp lệ!"
        )
        return

    print("\nThông tin so sánh:")

    print(
        f"{champion_1.champion_id}"
        f" - {champion_1.name}"
        f" | Chiến lực: "
        f"{champion_1.get_combat_power():.0f}"
    )

    print(
        f"{champion_2.champion_id}"
        f" - {champion_2.name}"
        f" | Chiến lực: "
        f"{champion_2.get_combat_power():.0f}"
    )

    if champion_1 > champion_2:
        print(
            f"\nKết quả: "
            f"{champion_1.champion_id}"
            f" - {champion_1.name}"
            f" mạnh hơn "
            f"{champion_2.champion_id}"
            f" - {champion_2.name}"
        )

    elif champion_2 > champion_1:
        print(
            f"\nKết quả: "
            f"{champion_2.champion_id}"
            f" - {champion_2.name}"
            f" mạnh hơn "
            f"{champion_1.champion_id}"
            f" - {champion_1.name}"
        )

    else:
        print(
            "\nHai tướng có sức mạnh ngang nhau."
        )


def calculate_team_power(
    champion_pool
):
    print(
        "\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH ---"
    )

    champion_ids = input(
        "Nhập danh sách mã tướng "
        "(cách nhau bằng dấu phẩy): "
    )

    champion_ids = [
        champion_id.strip().upper()
        for champion_id
        in champion_ids.split(",")
    ]

    selected_team = []

    for champion_id in champion_ids:

        champion = find_champion_by_id(
            champion_pool,
            champion_id
        )

        if champion is None:
            print(
                f"Mã tướng "
                f"{champion_id} "
                f"không hợp lệ, bỏ qua!"
            )
            continue

        selected_team.append(
            champion
        )

    if not selected_team:
        print(
            "Không có tướng hợp lệ."
        )
        return

    print("\nDanh sách đội hình:")

    for index, champion in enumerate(
        selected_team,
        start=1
    ):
        print(
            f"{index}. "
            f"{champion.champion_id}"
            f" - {champion.name}"
            f" | Chiến lực: "
            f"{champion.get_combat_power():.0f}"
        )

    # Sử dụng Operator Overloading
    total_power = sum(selected_team)

    print(
        f"\nTổng chiến lực đội hình: "
        f"{total_power:.0f}"
    )


def main():

    champion_pool = [
        Warrior(
            "WAR01",
            "Rikkei Knight",
            1200,
            300,
            150
        ),
        Warrior(
            "WAR02",
            "Steel Guardian",
            1500,
            250,
            200
        ),
        Mage(
            "MAG01",
            "Rikkei Wizard",
            800,
            500,
            2.0
        )
    ]

    while True:

        print(
            "\n===== RIKKEI RPG AUTO-BATTLER ====="
        )
        print(
            "1. Hiển thị bể tướng"
        )
        print(
            "2. Thêm quân cờ mới"
        )
        print(
            "3. So sánh 2 quân cờ"
        )
        print(
            "4. Tính tổng chiến lực đội hình"
        )
        print(
            "5. Thoát chương trình"
        )

        choice = input(
            "Chọn chức năng (1-5): "
        )

        if choice == "1":
            display_champion_pool(
                champion_pool
            )

        elif choice == "2":
            add_new_champion(
                champion_pool
            )

        elif choice == "3":
            compare_champions(
                champion_pool
            )

        elif choice == "4":
            calculate_team_power(
                champion_pool
            )

        elif choice == "5":
            print(
                "\nCảm ơn bạn đã sử dụng "
                "Rikkei RPG "
                "- Auto-Battler Manager!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ!"
            )


if __name__ == "__main__":
    main()