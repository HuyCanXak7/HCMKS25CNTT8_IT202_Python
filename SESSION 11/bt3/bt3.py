def normalize_product_id(product_id):
    return product_id.strip().upper()

def find_product_index_by_id(product_list, product_id):
    for index, product in enumerate(product_list):
        if product.get("product_id") == product_id:
            return index
    return None

def display_product_list(product_list):
    if not product_list:
        print("Danh sách sản phẩm hiện đang trống.")
        return

    print("Danh sách sản phẩm hiện tại:")
    for idx, product in enumerate(product_list, start=1):
        print(
            f"{idx}. Mã SP: {product['product_id']} | Tên: {product['product_name']} | Giá: {product['price']} | Số lượng: {product['quantity']}"
        )

def input_positive_int(prompt):
    raw_value = input(prompt).strip()
    if not raw_value.isdigit():
        return None
    value = int(raw_value)
    if value <= 0:
        return None
    return value

def add_product(product_list):
    raw_id = input("Nhập mã sản phẩm: ")
    product_id = normalize_product_id(raw_id)
    if not product_id:
        print("Mã sản phẩm bị trùng")
        return

    if find_product_index_by_id(product_list, product_id) is not None:
        print("Mã sản phẩm bị trùng")
        return

    product_name = input("Nhập tên sản phẩm: ").strip()
    price = input_positive_int("Nhập giá sản phẩm: ")
    quantity = input_positive_int("Nhập số lượng sản phẩm: ")

    if price is None or quantity is None:
        print("Giá/Số lượng không hợp lệ")
        return

    new_product = {
        "product_id": product_id,
        "product_name": product_name,
        "price": price,
        "quantity": quantity,
    }
    product_list.append(new_product)
    print("Thêm sản phẩm thành công")


def update_product(product_list):
    raw_id = input("Nhập mã sản phẩm cần cập nhật: ")
    product_id = normalize_product_id(raw_id)
    index = find_product_index_by_id(product_list, product_id)

    if index is None:
        print("Không tìm thấy mã sản phẩm cần cập nhật!")
        return

    product = product_list[index]
    product_name = input("Nhập tên sản phẩm: ").strip()
    price = input_positive_int("Nhập giá sản phẩm: ")
    quantity = input_positive_int("Nhập số lượng sản phẩm: ")

    if price is None or quantity is None:
        print("Giá/Số lượng không hợp lệ")
        return

    product["product_name"] = product_name
    product["price"] = price
    product["quantity"] = quantity
    print("Cập nhật sản phẩm thành công")


def delete_product(product_list):
    raw_id = input("Nhập mã sản phẩm cần xóa: ")
    product_id = normalize_product_id(raw_id)
    index = find_product_index_by_id(product_list, product_id)

    if index is None:
        print("Không tìm thấy mã sản phẩm cần xoá!")
        return

    del product_list[index]
    print("Xóa sản phẩm thành công")


def show_menu():
    print("===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")


def main():
    product_list = [
        {
            "product_id": "SP001",
            "product_name": "Áo polo nam",
            "price": 299000,
            "quantity": 20,
        },
        {
            "product_id": "SP002",
            "product_name": "Quần kaki nam",
            "price": 399000,
            "quantity": 15,
        },
        {
            "product_id": "SP003",
            "product_name": "Váy công sở nữ",
            "price": 459000,
            "quantity": 10,
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
            add_product(product_list)
        elif choice == 3:
            update_product(product_list)
        elif choice == 4:
            delete_product(product_list)
        elif choice == 5:
            print("Thoát chương trình.")
            break


if __name__ == "__main__":
    main()
