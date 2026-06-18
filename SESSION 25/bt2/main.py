class NetflixAccount:
    """
    Netflix Account Manager
    """

    # Class Attributes
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email

        # Private Attributes
        self.__password = ""
        self.__plan = "Basic"

        self.profiles = []

    @property
    def password(self):
        """
        Chỉ hiển thị mật khẩu đã được che.
        """
        return "********"

    @password.setter
    def password(self, new_password):
        """
        Kiểm tra độ dài mật khẩu.
        """
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    @property
    def plan(self):
        """
        Read-only property.
        Chỉ cho phép đọc gói cước.
        """
        return self.__plan

    @staticmethod
    def validate_email(email):
        """
        Kiểm tra email hợp lệ.
        """
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        """
        Thay đổi giới hạn profile toàn hệ thống.
        """
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        """
        Thêm profile mới.
        """
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print(
                "Đã đạt giới hạn số lượng Profile trên tài khoản này"
            )
            return

        self.profiles.append(profile_name)
        print("Thêm Profile thành công!")

    def upgrade_plan(self, new_plan):
        """
        Nâng cấp gói cước.
        """
        valid_plans = [
            "Basic",
            "Standard",
            "Premium"
        ]

        if new_plan not in valid_plans:
            print("Gói cước không hợp lệ")
            return

        self.__plan = new_plan
        print(f"Đã nâng cấp lên gói {new_plan}")

    def display_info(self):
        """
        Hiển thị thông tin tài khoản.
        """
        print("\n===== ACCOUNT INFORMATION =====")
        print(f"Platform: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Plan: {self.plan}")
        print(f"Profiles: {self.profiles}")
        print(
            f"Max Profiles Allowed: "
            f"{NetflixAccount.max_profiles}"
        )


def main():
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Register New Account")
        print("2. View Account")
        print("3. Add Profile")
        print("4. Upgrade Plan")
        print("5. Update Netflix Policy")
        print("6. Exit")
        print("==================================")

        choice = input("Choose (1-6): ")

        # Register
        if choice == "1":
            print("\n--- REGISTER ACCOUNT ---")

            while True:
                email = input("Enter email: ")

                if NetflixAccount.validate_email(email):
                    break

                print(
                    "Email không hợp lệ, vui lòng chứa ký tự '@' và '.'"
                )

            account = NetflixAccount(email)

            while True:
                try:
                    password = input("Enter password: ")
                    account.password = password
                    break

                except ValueError as error:
                    print(error)

            current_account = account

            print("Đăng ký tài khoản thành công!")

        # View Account
        elif choice == "2":
            if current_account is None:
                print(
                    "Vui lòng đăng ký tài khoản trước "
                    "(Chức năng 1)"
                )
                continue

            current_account.display_info()

        # Add Profile
        elif choice == "3":
            if current_account is None:
                print(
                    "Vui lòng đăng ký tài khoản trước "
                    "(Chức năng 1)"
                )
                continue

            profile_name = input(
                "Enter profile name: "
            )

            current_account.add_profile(profile_name)

        # Upgrade Plan
        elif choice == "4":
            if current_account is None:
                print(
                    "Vui lòng đăng ký tài khoản trước "
                    "(Chức năng 1)"
                )
                continue

            print("\nAvailable Plans:")
            print("Basic")
            print("Standard")
            print("Premium")

            new_plan = input(
                "Choose new plan: "
            )

            current_account.upgrade_plan(new_plan)

        # Update Policy
        elif choice == "5":
            try:
                new_limit = int(
                    input(
                        "Enter new max profiles: "
                    )
                )

                if new_limit <= 0:
                    print(
                        "Giới hạn Profile phải lớn hơn 0"
                    )
                    continue

                NetflixAccount.update_max_profiles(
                    new_limit
                )

                print(
                    f"Đã cập nhật giới hạn "
                    f"Profile toàn hệ thống thành "
                    f"{new_limit}"
                )

            except ValueError:
                print("Dữ liệu không hợp lệ")

        # Exit
        elif choice == "6":
            print(
                "Cảm ơn bạn đã sử dụng "
                "Netflix Account Manager!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()