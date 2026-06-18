from abc import ABC, abstractmethod

class Equipment(ABC):
    """Abstract Base Class cho mọi loại trang bị"""

    @abstractmethod
    def calculate_total_damage(self):
        pass


class Weapon(Equipment):
    """Vũ khí vật lý"""

    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + (self.upgrade_level * 10)

    def __gt__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể so sánh giữa các trang bị!")
            return False

        return (
            self.calculate_total_damage()
            > other.calculate_total_damage()
        )

    def __add__(self, other):
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp giữa các trang bị!")
            return None

        new_name = (
            f"Fusion({self.name} + {other.name})"
        )

        new_base_damage = (
            self.base_damage + other.base_damage
        )

        new_upgrade_level = (
            self.upgrade_level + other.upgrade_level
        )

        return Weapon(
            new_name,
            new_base_damage,
            new_upgrade_level
        )


class MagicMixin:
    """Mixin phép thuật"""

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"{self.name} đang phát sáng ma thuật!")


class MagicSword(Weapon, MagicMixin):
    """Kiếm ma thuật"""

    def __init__(
        self,
        name,
        base_damage,
        upgrade_level,
        magic_power
    ):
        Weapon.__init__(
            self,
            name,
            base_damage,
            upgrade_level
        )

        MagicMixin.__init__(
            self,
            magic_power
        )

    def calculate_total_damage(self):
        return (
            self.base_damage
            + (self.upgrade_level * 10)
            + self.magic_power
        )


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def input_positive_int(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Giá trị phải lớn hơn 0!")
                continue

            return value

        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")


def display_inventory(inventory):
    print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")

    if not inventory:
        print("Kho vũ khí hiện đang trống.")
        print(
            "Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3."
        )
        return

    print(
        f"{'STT':<5} | "
        f"{'Tên vũ khí':<30} | "
        f"{'Loại':<12} | "
        f"{'Cấp':<5} | "
        f"{'Sát thương tổng'}"
    )

    print("-" * 85)

    for index, item in enumerate(inventory, start=1):
        print(
            f"{index:<5} | "
            f"{item.name:<30} | "
            f"{type(item).__name__:<12} | "
            f"{item.upgrade_level:<5} | "
            f"{item.calculate_total_damage()}"
        )


def forge_weapon(inventory):
    print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")

    name = input("Nhập tên vũ khí: ")

    base_damage = input_positive_int(
        "Nhập sát thương gốc: "
    )

    upgrade_level = input_positive_int(
        "Nhập cấp cường hóa: "
    )

    weapon = Weapon(
        name,
        base_damage,
        upgrade_level
    )

    inventory.append(weapon)

    print("\n>> Rèn vũ khí vật lý thành công!")
    print(f"Tên vũ khí: {weapon.name}")
    print("Loại: Weapon")
    print(
        f"Cấp cường hóa: {weapon.upgrade_level}"
    )
    print(
        f"Sát thương tổng: "
        f"{weapon.calculate_total_damage()}"
    )


def forge_magic_sword(inventory):
    print("\n--- RÈN KIẾM MA THUẬT ---")

    name = input(
        "Nhập tên kiếm ma thuật: "
    )

    base_damage = input_positive_int(
        "Nhập sát thương gốc: "
    )

    upgrade_level = input_positive_int(
        "Nhập cấp cường hóa: "
    )

    magic_power = input_positive_int(
        "Nhập sức mạnh phép thuật: "
    )

    sword = MagicSword(
        name,
        base_damage,
        upgrade_level,
        magic_power
    )

    inventory.append(sword)

    print("\n>> Rèn kiếm ma thuật thành công!")
    print(f"Tên vũ khí: {sword.name}")
    print("Loại: MagicSword")
    print(
        f"Cấp cường hóa: {sword.upgrade_level}"
    )
    print(
        f"Sát thương gốc: {sword.base_damage}"
    )
    print(
        f"Sức mạnh phép thuật: "
        f"{sword.magic_power}"
    )
    print(
        f"Sát thương tổng: "
        f"{sword.calculate_total_damage()}"
    )


def compare_weapons(inventory):
    print("\n--- THẨM ĐỊNH VŨ KHÍ ---")

    if len(inventory) < 2:
        print(
            "Cần ít nhất 2 vũ khí trong kho để thẩm định!"
        )
        return

    weapon_1 = inventory[0]
    weapon_2 = inventory[1]

    print("\nVũ khí thứ nhất:")
    print(
        f"{weapon_1.name} | "
        f"Loại: {type(weapon_1).__name__} | "
        f"Sát thương: "
        f"{weapon_1.calculate_total_damage()}"
    )

    print("\nVũ khí thứ hai:")
    print(
        f"{weapon_2.name} | "
        f"Loại: {type(weapon_2).__name__} | "
        f"Sát thương: "
        f"{weapon_2.calculate_total_damage()}"
    )

    if weapon_1 > weapon_2:
        print(
            f"\nKết quả: "
            f"{weapon_1.name} mạnh hơn "
            f"{weapon_2.name}."
        )

    elif weapon_2 > weapon_1:
        print(
            f"\nKết quả: "
            f"{weapon_2.name} mạnh hơn "
            f"{weapon_1.name}."
        )

    else:
        print(
            "\nKết quả: Hai vũ khí có "
            "sức mạnh ngang nhau."
        )


def fuse_weapons(inventory):
    print("\n--- DUNG HỢP VŨ KHÍ ---")

    if len(inventory) < 2:
        print(
            "Cần ít nhất 2 vũ khí trong kho để dung hợp!"
        )
        return

    weapon_1 = inventory[0]
    weapon_2 = inventory[1]

    print(
        "Đang dung hợp 2 vũ khí đầu tiên trong kho..."
    )

    print(
        f"\nVũ khí 1: {weapon_1.name}"
        f" | Cấp: {weapon_1.upgrade_level}"
        f" | Sát thương: "
        f"{weapon_1.calculate_total_damage()}"
    )

    print(
        f"Vũ khí 2: {weapon_2.name}"
        f" | Cấp: {weapon_2.upgrade_level}"
        f" | Base Damage: "
        f"{weapon_2.base_damage}"
    )

    new_weapon = weapon_1 + weapon_2

    if new_weapon is None:
        return

    inventory.pop(0)
    inventory.pop(0)

    inventory.append(new_weapon)

    print("\n>> Dung hợp vũ khí thành công!")

    print(
        f"Đã xóa khỏi kho: {weapon_1.name}"
    )

    print(
        f"Đã xóa khỏi kho: {weapon_2.name}"
    )

    print(
        f"\nVũ khí mới: {new_weapon.name}"
    )

    print("Loại: Weapon")

    print(
        f"Cấp cường hóa: "
        f"{new_weapon.upgrade_level}"
    )

    print(
        f"Sát thương tổng: "
        f"{new_weapon.calculate_total_damage()}"
    )


# =====================================================
# MAIN PROGRAM
# =====================================================

inventory = []

while True:
    print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS =====")
    print("1. Xem kho vũ khí & Sát thương tổng")
    print("2. Rèn Vũ khí Vật lý")
    print("3. Rèn Kiếm Ma Thuật")
    print("4. Thẩm định vũ khí")
    print("5. Dung hợp vũ khí")
    print("6. Thoát game")
    print("========================================")

    choice = input(
        "Chọn chức năng (1-6): "
    )

    if choice == "1":
        display_inventory(inventory)

    elif choice == "2":
        forge_weapon(inventory)

    elif choice == "3":
        forge_magic_sword(inventory)

    elif choice == "4":
        compare_weapons(inventory)

    elif choice == "5":
        fuse_weapons(inventory)

    elif choice == "6":
        print(
            "Thoát Lò Rèn. Hẹn gặp lại Anh hùng!"
        )
        break

    else:
        print(
            "Lựa chọn không hợp lệ!"
        )