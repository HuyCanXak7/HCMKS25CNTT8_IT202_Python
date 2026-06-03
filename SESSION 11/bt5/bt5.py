# Hệ thống quản lý giao dịch bán hàng Yody
# File: SESSION 11/bt5/bt5.py


def normalize_product_id(product_id):
    return product_id.strip().upper()


def find_product_by_id(product_list, product_id):
    for product in product_list:
        if product.get("product_id") == product_id:
            return product
    return None


def get_stock_status(quantity):
    if quantity == 0:
        return "Hết hàng"
    if quantity <= 5:
        return "Sắp hết hàng"
    return "Còn hàng"


def display_product_list(product_list):
    if not product_list:
        print("Danh sách sản phẩm hiện đang trống.")
        return

    print("Danh sách sản phẩm hiện tại:")
    for idx, p in enumerate(product_list, start=1):
        status = get_stock_status(p["quantity"])
        print(f"{idx}. Mã SP: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']} | Tồn kho: {p['quantity']} | Đã bán: {p['sold']} | Đổi trả: {p['returned']} | Giảm giá: {p['discount']}% | Trạng thái: {status}")


def input_positive_integer(prompt):
    raw = input(prompt).strip()
    if not raw.isdigit():
        return None
    value = int(raw)
    if value <= 0:
        return None
    return value


def calculate_price_after_discount(price, discount_percent):
    return price * (100 - discount_percent) / 100


def sell_product(product_list):
    raw_id = input("Nhập mã sản phẩm khách muốn mua: ")
    product_id = normalize_product_id(raw_id)
    product = find_product_by_id(product_list, product_id)

    if product is None:
        print("Không tìm thấy sản phẩm cần bán")
        return

    quantity = input_positive_integer("Nhập số lượng khách mua: ")
    if quantity is None:
        print("Số lượng mua/Nhập kho không hợp lệ")
        return

    if quantity > product["quantity"]:
        print("Số lượng trong kho không đủ để bán")
        return

    price_after = calculate_price_after_discount(product["price"], product.get("discount", 0))
    total = price_after * quantity

    # Cập nhật số lượng
    product["quantity"] -= quantity
    product["sold"] += quantity

    # Hiển thị tổng tiền (làm tròn nếu cần)
    if total.is_integer():
        total_display = int(total)
    else:
        total_display = round(total, 2)

    print(f"Tổng tiền: {total_display}")


def process_return(product_list):
    raw_id = input("Nhập mã sản phẩm khách muốn đổi/trả: ")
    product_id = normalize_product_id(raw_id)
    product = find_product_by_id(product_list, product_id)

    if product is None:
        print("Không tìm thấy sản phẩm cần đổi trả")
        return

    quantity = input_positive_integer("Nhập số lượng đổi/trả: ")
    if quantity is None:
        print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
        return

    if quantity > product.get("sold", 0):
        print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
        return

    price_after = calculate_price_after_discount(product["price"], product.get("discount", 0))
    refund = price_after * quantity

    # Cập nhật số liệu
    product["sold"] -= quantity
    product["quantity"] += quantity
    product["returned"] += quantity

    if refund.is_integer():
        refund_display = int(refund)
    else:
        refund_display = round(refund, 2)

    print(f"Số tiền hoàn lại: {refund_display}")


def apply_discount(product_list):
    raw_id = input("Nhập mã sản phẩm cần áp dụng giảm giá: ")
    product_id = normalize_product_id(raw_id)
    product = find_product_by_id(product_list, product_id)

    if product is None:
        print("Không tìm thấy sản phẩm cần áp dụng giảm giá")
        return

    raw_discount = input("Nhập phần trăm giảm giá: ").strip()
    if not raw_discount.isdigit():
        print("Phần trăm giảm giá không hợp lệ")
        return

    discount = int(raw_discount)
    if discount < 0 or discount > 70:
        print("Phần trăm giảm giá không hợp lệ")
        return

    product["discount"] = discount
    print("Áp dụng giảm giá thành công")


def import_stock(product_list):
    raw_id = input("Nhập mã sản phẩm cần nhập thêm: ")
    product_id = normalize_product_id(raw_id)
    product = find_product_by_id(product_list, product_id)

    if product is None:
        print("Không tìm thấy sản phẩm cần bán/Nhập kho")
        return

    quantity = input_positive_integer("Nhập số lượng nhập thêm: ")
    if quantity is None:
        print("Số lượng mua/Nhập kho không hợp lệ")
        return

    product["quantity"] += quantity
    print("Nhập hàng thành công")


def show_menu():
    print("===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")


def main():
    product_list = [
        {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20, "sold": 5, "returned": 1, "discount": 0},
        {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 8, "sold": 3, "returned": 0, "discount": 10},
        {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 3, "sold": 7, "returned": 1, "discount": 15},
    ]

    while True:
        show_menu()
        choice = input("Chọn chức năng: ").strip()
        if not choice.isdigit() or int(choice) not in range(1, 7):
            print('"Lựa chọn không hợp lệ", vui lòng nhập lại!')
            continue

        choice = int(choice)
        if choice == 1:
            display_product_list(product_list)
        elif choice == 2:
            sell_product(product_list)
        elif choice == 3:
            process_return(product_list)
        elif choice == 4:
            apply_discount(product_list)
        elif choice == 5:
            import_stock(product_list)
        elif choice == 6:
            print("Thoát chương trình.")
            break


if __name__ == "__main__":
    main()
