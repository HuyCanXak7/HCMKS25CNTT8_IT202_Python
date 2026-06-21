from abc import ABC, abstractmethod

# =========================
# Abstract Base Class
# =========================
class BaseProduct(ABC):
    warehouse_name = "Amazon Logistics"
    base_storage_fee = 5000

    def __init__(self, product_code, product_name):
        if not self.validate_product_code(product_code):
            raise ValueError("Invalid product code! Must be 10 characters starting with a letter.")
        self.product_code = product_code
        self.product_name = product_name.strip().upper()
        self.__stock_quantity = 0

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    @abstractmethod
    def import_stock(self, quantity):
        pass

    @abstractmethod
    def export_stock(self, quantity):
        pass

    def __add__(self, other):
        if isinstance(other, BaseProduct):
            return self.stock_quantity + other.stock_quantity
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BaseProduct):
            return self.stock_quantity < other.stock_quantity
        return NotImplemented

    @staticmethod
    def validate_product_code(product_code):
        return product_code[0].isalpha() and len(product_code) == 10

    @classmethod
    def update_warehouse_name(cls, new_name):
        cls.warehouse_name = new_name


# =========================
# Subclass: ColdStorageProduct
# =========================
class ColdStorageProduct(BaseProduct):
    def __init__(self, product_code, product_name, required_temperature):
        super().__init__(product_code, product_name)
        self.required_temperature = required_temperature

    def import_stock(self, quantity):
        self._BaseProduct__stock_quantity += quantity

    def export_stock(self, quantity):
        loss = quantity * 0.05
        total_deduction = quantity + loss
        if self.stock_quantity >= total_deduction:
            self._BaseProduct__stock_quantity -= total_deduction
            print(f"Xuất kho {quantity} đơn vị, hao hụt {loss:.2f}.")
        else:
            print("Không đủ tồn kho!")

    def apply_cooling_cost(self):
        cost = abs(self.required_temperature) * self.stock_quantity * 60
        return cost


# =========================
# Subclass: HazardousProduct
# =========================
class HazardousProduct(BaseProduct):
    def __init__(self, product_code, product_name, max_safety_limit):
        super().__init__(product_code, product_name)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        if self.stock_quantity + quantity > self.max_safety_limit:
            print("Nhập kho thất bại! Vượt hạn mức an toàn.")
        else:
            self._BaseProduct__stock_quantity += quantity

    def export_stock(self, quantity):
        if self.stock_quantity >= quantity:
            self._BaseProduct__stock_quantity -= quantity
        else:
            print("Không đủ tồn kho!")


# =========================
# Multiple Inheritance: HybridPremiumProduct
# =========================
class HybridPremiumProduct(ColdStorageProduct, HazardousProduct):
    def __init__(self, product_code, product_name, required_temperature, max_safety_limit):
        super().__init__(product_code, product_name, required_temperature)
        self.max_safety_limit = max_safety_limit

    def import_stock(self, quantity):
        if self.stock_quantity + quantity > self.max_safety_limit:
            print("Nhập kho thất bại! Vượt hạn mức an toàn.")
        else:
            super().import_stock(quantity)


# =========================
# Duck Typing
# =========================
def dispatch_to_carrier(carrier_agent, product, quantity):
    try:
        carrier_agent.ship_package(product, quantity)
        product.export_stock(quantity)
    except AttributeError:
        print("Đơn vị vận chuyển không hợp lệ!")


class FedExCarrier:
    def ship_package(self, product, quantity):
        print(f"[FedEx] Đang vận chuyển {quantity} đơn vị {product.product_name}...")


class DHLCarrier:
    def ship_package(self, product, quantity):
        print(f"[DHL] Đang vận chuyển {quantity} đơn vị {product.product_name}...")


# =========================
# CLI Menu
# =========================
def main():
    products = []
    current_product = None

    while True:
        print("\n===== AMAZON INVENTORY SIMULATOR PRO =====")
        print("1. Đăng ký mã hàng hóa mới")
        print("2. Xem thông tin & Kiểm tra MRO")
        print("3. Giao dịch Nhập / Xuất kho")
        print("4. Kiểm tra điều kiện bảo quản / Tính chi phí")
        print("5. Gộp lô hàng & So sánh tồn kho")
        print("6. Điều phối vận chuyển (Duck Typing)")
        print("7. Thoát chương trình")
        choice = input("Chọn chức năng (1-7): ")

        if choice == "1":
            print("--- CHỌN LOẠI SẢN PHẨM ---")
            print("1. Cold Storage Product")
            print("2. Hazardous Product")
            print("3. Hybrid Premium Product")
            type_choice = input("Chọn loại (1-3): ")
            code = input("Nhập mã sản phẩm (10 ký tự): ")
            name = input("Nhập tên sản phẩm: ")

            try:
                if type_choice == "1":
                    temp = int(input("Nhiệt độ bảo quản: "))
                    p = ColdStorageProduct(code, name, temp)
                elif type_choice == "2":
                    limit = int(input("Hạn mức an toàn: "))
                    p = HazardousProduct(code, name, limit)
                elif type_choice == "3":
                    temp = int(input("Nhiệt độ bảo quản: "))
                    limit = int(input("Hạn mức an toàn: "))
                    p = HybridPremiumProduct(code, name, temp, limit)
                else:
                    print("Loại không hợp lệ!")
                    continue
                products.append(p)
                current_product = p
                print("Đăng ký thành công!")
            except ValueError as e:
                print(e)

        elif choice == "2":
            if not current_product:
                print("Chưa có sản phẩm nào được chọn!")
            else:
                print("--- THÔNG TIN SẢN PHẨM ---")
                print("Loại:", type(current_product).__name__)
                print("Kho:", current_product.warehouse_name)
                print("Mã:", current_product.product_code)
                print("Tên:", current_product.product_name)
                print("Tồn kho:", current_product.stock_quantity)
                print("MRO:", [cls.__name__ for cls in type(current_product).mro()])

        elif choice == "3":
            if not current_product:
                print("Chưa có sản phẩm nào được chọn!")
            else:
                print("1. Nhập kho\n2. Xuất kho")
                act = input("Chọn giao dịch: ")
                qty = int(input("Số lượng: "))
                if act == "1":
                    current_product.import_stock(qty)
                elif act == "2":
                    current_product.export_stock(qty)

        elif choice == "4":
            if isinstance(current_product, ColdStorageProduct):
                cost = current_product.apply_cooling_cost()
                print("Chi phí làm lạnh:", cost, "VND")
            else:
                print("Sản phẩm này không hỗ trợ tính năng bảo quản lạnh.")

        elif choice == "5":
            if len(products) < 2 or not current_product:
                print("Cần ít nhất 2 sản phẩm để so sánh!")
            else:
                other = products[0] if products[0] != current_product else products[1]
                print("So sánh tồn kho:", current_product < other)
                print("Tổng tồn kho:", current_product + other)

        elif choice == "6":
            if not current_product:
                print("Chưa có sản phẩm nào được chọn!")
            else:
                print("1. FedEx\n2. DHL")
                carrier_choice = input("Chọn đối tác: ")
                qty = int(input("Số lượng vận chuyển: "))
                carrier = FedExCarrier() if carrier_choice == "1" else DHLCarrier()
                dispatch_to_carrier(carrier, current_product, qty)

        elif choice == "7":
            print("Cảm ơn đã sử dụng hệ thống!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
