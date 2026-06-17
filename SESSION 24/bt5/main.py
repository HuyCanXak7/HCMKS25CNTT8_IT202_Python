"""
===================================================================
TÀI LIỆU THIẾT KẾ LỚP BISTROTABLE
===================================================================

1. Class Attributes (Thuộc tính Lớp):
   - _vat_rate
   Ý nghĩa:
   Thuế VAT áp dụng chung cho toàn bộ nhà hàng.

2. Instance Attributes (Thuộc tính Đối tượng):

   Public:
   - capacity
     Sức chứa của bàn.

   Private:
   - __table_id
     Mã bàn.

   - __current_bill
     Tiền tạm tính hiện tại.

3. Methods (Các Phương thức):

   __init__(self, table_id, capacity)
   - Khởi tạo mã bàn.
   - Khởi tạo sức chứa.
   - Hóa đơn mặc định = 0.

   @property table_id
   - Cho phép đọc mã bàn.

   @property current_bill
   - Cho phép đọc tiền tạm tính.

   @property status
   - Tính động trạng thái bàn.
   - 0 -> Đang trống
   - >0 -> Có khách

   @property final_bill
   - Tính hóa đơn sau VAT.

   order_dish(self, amount)
   - Cộng tiền món ăn.

   cancel_dish(self, amount)
   - Giảm tiền hóa đơn.

   checkout(self)
   - Trả về tổng tiền cần thanh toán.
   - Reset hóa đơn về 0.

   @classmethod
   update_vat_rate(cls, new_rate)
   - Cập nhật VAT toàn hệ thống.

   @staticmethod
   is_valid_table_id(table_id)
   - Kiểm tra định dạng mã bàn.
===================================================================
"""


class BistroTable:
    _vat_rate = 0.08

    def __init__(self, table_id, capacity):
        self.__table_id = table_id
        self.capacity = capacity
        self.__current_bill = 0

    @property
    def table_id(self):
        return self.__table_id

    @property
    def current_bill(self):
        return self.__current_bill

    @property
    def status(self):
        if self.__current_bill == 0:
            return "Đang trống"
        return "Có khách"

    @property
    def final_bill(self):
        return int(
            self.__current_bill * (1 + BistroTable._vat_rate)
        )

    def order_dish(self, amount):
        if amount <= 0:
            print("Vui lòng nhập số tiền là một số nguyên dương!")
            return False

        self.__current_bill += amount
        return True

    def cancel_dish(self, amount):
        if amount <= 0:
            print("Vui lòng nhập số tiền là một số nguyên dương!")
            return False

        if amount > self.__current_bill:
            print(
                "Lỗi: Số tiền giảm trừ vượt quá giá trị hóa đơn hiện tại!"
            )
            return False

        self.__current_bill -= amount
        return True

    def checkout(self):
        total = self.final_bill
        self.__current_bill = 0
        return total

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls._vat_rate = new_rate

    @staticmethod
    def is_valid_table_id(table_id):
        table_id = table_id.upper()

        if not table_id.startswith("TB"):
            return False

        if len(table_id) < 3:
            return False

        return True


table_records = [
    BistroTable("TB01", 4),
    BistroTable("TB02", 2),
    BistroTable("TB03", 8)
]


def find_table(table_id):
    table_id = table_id.strip().upper()

    for table in table_records:
        if table.table_id == table_id:
            return table

    return None


def display_tables():
    print("\n--- SƠ ĐỒ BÀN ĂN RIKKEI BISTRO ---")

    for index, table in enumerate(table_records, start=1):
        print(
            f"{index}. Mã bàn: {table.table_id} | "
            f"Sức chứa: {table.capacity} người | "
            f"Tạm tính: {table.current_bill:,}đ | "
            f"Trạng thái: {table.status}"
        )

    print("----------------------------------")


def order_food():
    print("\n--- GỌI MÓN MỚI ---")

    table_id = input("Nhập mã bàn gọi món: ").strip().upper()

    if not BistroTable.is_valid_table_id(table_id):
        print("Mã bàn không hợp lệ!")
        return

    table = find_table(table_id)

    if not table:
        print("Không tìm thấy bàn!")
        return

    try:
        amount = int(input("Nhập giá tiền món ăn mới: "))
    except ValueError:
        print("Vui lòng nhập số tiền hợp lệ!")
        return

    if table.order_dish(amount):
        print(
            f">> Thành công: Đã ghi nhận món ăn "
            f"{amount:,}đ vào Bàn '{table.table_id}'."
        )

        print(
            f">> Số tiền tạm tính hiện tại của bàn: "
            f"{table.current_bill:,}đ."
        )


def cancel_food():
    print("\n--- HỦY MÓN / GIẢM TRỪ HÓA ĐƠN ---")

    table_id = input(
        "Nhập mã bàn cần hủy món: "
    ).strip().upper()

    table = find_table(table_id)

    if not table:
        print("Không tìm thấy bàn!")
        return

    try:
        amount = int(
            input("Nhập giá trị món muốn giảm trừ: ")
        )
    except ValueError:
        print("Vui lòng nhập số tiền hợp lệ!")
        return

    if table.cancel_dish(amount):
        print(
            f">> Thành công: Đã giảm trừ "
            f"{amount:,}đ khỏi Bàn "
            f"'{table.table_id}' do sự cố bếp."
        )

        print(
            f">> Số tiền tạm tính còn lại: "
            f"{table.current_bill:,}đ."
        )

        if table.current_bill == 0:
            print(
                f">> Bàn '{table.table_id}' hiện đã "
                f"chuyển về trạng thái Đang trống."
            )


def update_vat():
    print("\n--- CẬP NHẬT THUẾ SUẤT VAT TOÀN NHÀ HÀNG ---")

    print(
        f"[HỆ THỐNG] Thuế suất VAT hiện tại là: "
        f"{BistroTable._vat_rate * 100:.0f}% "
        f"({BistroTable._vat_rate})"
    )

    try:
        new_rate = float(
            input(
                "Nhập thuế suất VAT mới "
                "(ví dụ 0.1 cho 10%): "
            )
        )
    except ValueError:
        print("Tỷ lệ thuế không hợp lệ!")
        return

    if not 0 <= new_rate <= 0.2:
        print("Tỷ lệ thuế không hợp lệ!")
        return

    BistroTable.update_vat_rate(new_rate)

    print(
        f"\n>> Thông báo: Rikkei Bistro cập nhật "
        f"thuế suất VAT mới ở mức "
        f"{new_rate * 100:.0f}% thành công!"
    )


def checkout_table():
    print("\n--- THANH TOÁN HÓA ĐƠN ---")

    table_id = input(
        "Nhập mã bàn thanh toán: "
    ).strip().upper()

    table = find_table(table_id)

    if not table:
        print("Không tìm thấy bàn!")
        return

    if table.current_bill == 0:
        print(
            "Lỗi: Bàn này hiện đang trống, "
            "không có hóa đơn để thanh toán!"
        )
        return

    print(
        f"\n--- HÓA ĐƠN THANH TOÁN BÀN "
        f"{table.table_id} ---"
    )

    print(
        f"Số tiền món ăn: "
        f"{table.current_bill:,}đ"
    )

    print(
        f"Thuế suất VAT áp dụng: "
        f"{BistroTable._vat_rate * 100:.0f}%"
    )

    print(
        f"Tổng tiền cần thanh toán "
        f"(gồm thuế): {table.final_bill:,}đ"
    )

    print("-----------------------------------")

    table.checkout()

    print(
        f">> Thanh toán thành công! "
        f"Bàn '{table.table_id}' đã được dọn sạch "
        f"và chuyển sang trạng thái Đang trống."
    )


def main():
    while True:
        print("\n===== HỆ THỐNG ĐIỀU PHỐI BÀN ĂN - RIKKEI BISTRO =====")
        print("1. Hiển thị sơ đồ & Trạng thái bàn ăn")
        print("2. Gọi món mới")
        print("3. Hủy món / Giảm trừ hóa đơn")
        print("4. Cập nhật thuế suất VAT toàn nhà hàng")
        print("5. Thanh toán hóa đơn & Trả bàn trống")
        print("6. Thoát chương trình")
        print("=====================================================")

        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            display_tables()

        elif choice == "2":
            order_food()

        elif choice == "3":
            cancel_food()

        elif choice == "4":
            update_vat()

        elif choice == "5":
            checkout_table()

        elif choice == "6":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống "
                "điều phối bàn ăn Rikkei Bistro!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()