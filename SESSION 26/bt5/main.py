from abc import ABC, abstractmethod


class Companion(ABC):
    """
    Abstract Base Class cho mọi sinh vật đồng hành
    """

    def __init__(self, name, level=1, **kwargs):
        self.name = name
        self.level = level

    def __add__(self, other):
        """
        Lai tạo sinh vật
        Chỉ cho phép cùng loại
        """

        if not isinstance(other, Companion):
            raise TypeError(
                "Chỉ có thể lai tạo 2 sinh vật cùng loài!"
            )

        if type(self) != type(other):
            raise TypeError(
                "Chỉ có thể lai tạo 2 sinh vật cùng loài!"
            )

        new_name = f"{self.name} {other.name}"
        new_level = max(self.level, other.level) + 1

        if isinstance(self, Dragon):
            return Dragon(
                new_name,
                bonus_atk=self.bonus_atk + other.bonus_atk,
                bonus_speed=self.bonus_speed + other.bonus_speed,
                level=new_level
            )

        if isinstance(self, Pet):
            return Pet(
                new_name,
                bonus_atk=self.bonus_atk + other.bonus_atk,
                level=new_level
            )

        if isinstance(self, Mount):
            return Mount(
                new_name,
                bonus_speed=self.bonus_speed + other.bonus_speed,
                level=new_level
            )

    @abstractmethod
    def unleash_skill(self):
        pass


class Pet(Companion):

    def __init__(
        self,
        name,
        bonus_atk,
        level=1,
        **kwargs
    ):
        super().__init__(
            name=name,
            level=level,
            **kwargs
        )
        self.bonus_atk = bonus_atk

    def unleash_skill(self):
        print(
            f">> {self.name} gầm gừ: "
            f"Tấn công kẻ thù, gây "
            f"{self.bonus_atk} sát thương!"
        )


class Mount(Companion):

    def __init__(
        self,
        name,
        bonus_speed,
        level=1,
        **kwargs
    ):
        super().__init__(
            name=name,
            level=level,
            **kwargs
        )
        self.bonus_speed = bonus_speed

    def unleash_skill(self):
        print(
            f">> {self.name} hí vang: "
            f"Tăng tốc độ di chuyển thêm "
            f"{self.bonus_speed} điểm!"
        )


class Dragon(Pet, Mount):

    def __init__(
        self,
        name,
        bonus_atk,
        bonus_speed,
        level=1
    ):
        super().__init__(
            name=name,
            level=level,
            bonus_atk=bonus_atk,
            bonus_speed=bonus_speed
        )

        self.bonus_speed = bonus_speed

    def unleash_skill(self):
        print(f">> {self.name} thị uy:")
        print(
            f"   - Tấn công kẻ thù, gây "
            f"{self.bonus_atk} sát thương!"
        )
        print(
            f"   - Tăng tốc độ di chuyển thêm "
            f"{self.bonus_speed} điểm!"
        )


def display_companions(companions):
    if not companions:
        print("Đội hình hiện đang trống!")
        return

    print("\n===== ĐỘI HÌNH SINH VẬT =====")

    for index, companion in enumerate(
        companions,
        start=1
    ):
        if isinstance(companion, Dragon):
            print(
                f"{index}. [Dragon] "
                f"{companion.name} | "
                f"Cấp: {companion.level} | "
                f"Atk: +{companion.bonus_atk} | "
                f"Speed: +{companion.bonus_speed}"
            )

        elif isinstance(companion, Pet):
            print(
                f"{index}. [Pet] "
                f"{companion.name} | "
                f"Cấp: {companion.level} | "
                f"Atk: +{companion.bonus_atk}"
            )

        elif isinstance(companion, Mount):
            print(
                f"{index}. [Mount] "
                f"{companion.name} | "
                f"Cấp: {companion.level} | "
                f"Speed: +{companion.bonus_speed}"
            )


if __name__ == "__main__":

    print("===== TEST BẪY 1 =====")

    try:
        test = Companion("Test")
    except TypeError as e:
        print("Đã chặn thành công:", e)

    print("\n===== TEST LAI TẠO PET =====")

    p1 = Pet(
        "Sói Trắng",
        bonus_atk=50
    )

    p2 = Pet(
        "Sói Đen",
        bonus_atk=60
    )

    p3 = p1 + p2

    print(
        f"Tên: {p3.name}"
    )

    print(
        f"Level: {p3.level}"
    )

    print(
        f"Atk: {p3.bonus_atk}"
    )

    print("\n===== TEST BẪY 2 =====")

    m1 = Mount(
        "Ngựa",
        bonus_speed=10
    )

    try:
        result = p1 + m1
    except TypeError as e:
        print("Đã chặn:", e)

    try:
        result = p1 + 100
    except TypeError as e:
        print("Đã chặn:", e)

    print("\n===== TEST DRAGON =====")

    d1 = Dragon(
        "Rồng Lửa",
        bonus_atk=500,
        bonus_speed=200
    )

    print(
        f"Tên: {d1.name}"
    )

    print(
        f"Atk: {d1.bonus_atk}"
    )

    print(
        f"Speed: {d1.bonus_speed}"
    )

    print("\n===== TEST ĐA HÌNH =====")

    equipped = [
        p3,
        m1,
        d1
    ]

    for companion in equipped:
        companion.unleash_skill()