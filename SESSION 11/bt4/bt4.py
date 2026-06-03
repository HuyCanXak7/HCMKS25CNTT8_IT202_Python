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
    for index, product in enumerate(product_list, start=1):
        status = get_stock_status(product["quantity"])
        print(
            f"{index}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | Giá: {product['price']} | Tồn kho: {product['quantity']} | Đã bán: {product['sold']} | Trạng thái: {status}"
        )


def input_positive_integer(prompt):
    raw_value = input(prompt).strip()
    if not raw_value.isdigit():
        return None
    value = int(raw_value)
    if value <= 0:
        return None
    return value


def sell_product(product_list):
    raw_id = input("Nhập mã sản phẩm khách muốn mua: ")
    product_id = normalize_product_id(raw_id)
    product = find_product_by_id(product_list, product_id)

    if product is None:
        print("Không tìm thấy sản phẩm cần bán/Nhập kho")
        return

    quantity = input_positive_integer("Nhập số lượng khách mua: ")
    if quantity is None:
        print("Số lượng mua/Nhập kho không hợp lệ")
        return

    if quantity > product["quantity"]:
        print("Số lượng trong kho không đủ để bán")
        return

    product["quantity"] -= quantity
    product["sold"] += quantity
    total_price = product["price"] * quantity
    print(f"Thanh toán: {total_price}")


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


def report_revenue(product_list):
    revenue_items = []
    total_revenue = 0
    max_sold = 0
    best_seller = None

    for product in product_list:
        sold = product.get("sold", 0)
        if sold > 0:
            revenue = product["price"] * sold
            revenue_items.append((product["product_name"], sold, revenue))
            total_revenue += revenue
            if sold > max_sold:
                max_sold = sold
                best_seller = product["product_name"]

    if total_revenue == 0:
        print("Chưa có doanh thu phát sinh.")
        return

    print("===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
    for index, (name, sold, revenue) in enumerate(revenue_items, start=1):
        print(f"{index}. {name} | Đã bán: {sold} | Doanh thu: {revenue}")

    print()
    print(f"Tổng doanh thu: {total_revenue}")
    print(f"Sản phẩm bán chạy nhất: {best_seller}")


def show_menu():
    print("===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")


def main():
    product_list = [
        {
            "product_id": "SP001",
            "product_name": "Áo polo nam",
            "price": 299000,
            "quantity": 20,
            "sold": 5,
        },
        {
            "product_id": "SP002",
            "product_name": "Quần kaki nam",
            "price": 399000,
            "quantity": 8,
            "sold": 3,
        },
        {
            "product_id": "SP003",
            "product_name": "Váy công sở nữ",
            "price": 459000,
            "quantity": 3,
            "sold": 7,
        },
    ]

    while True:
        show_menu()
        choice = input("Chọn chức năng: ").strip()

        if not choice.isdigit() or int(choice) not in range(1, 6):
            print('"Lựa chọn không hợp lệ", vui lòng nhập lại!')
            continue

        choice = int(choice)

        if choice == 1:
            display_product_list(product_list)
        elif choice == 2:
            sell_product(product_list)
        elif choice == 3:
            import_stock(product_list)
        elif choice == 4:
            report_revenue(product_list)
        elif choice == 5:
            print("Thoát chương trình.")
            break


if __name__ == "__main__":
    main()
