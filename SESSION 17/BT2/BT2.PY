import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]


def display_labels(products):
    print("\n--- DANH SÁCH TEM NHÃN ---")

    template = "Mã: {code:<10} | Tên: {name:<20} | Giá: {price} VND | Rating: {rating}*"

    for product in products:
        try:
            code, name, price, rating = product.split("-")

            data = {
                "code": code,
                "name": name,
                "price": f"{int(price):,}",
                "rating": rating
            }

            print(template.format_map(data))

        except ValueError:
            product_id = product.split("-")[0]
            print(f"Bỏ qua sản phẩm {product_id} do sai cấu trúc dữ liệu")
        except Exception:
            product_id = product.split("-")[0]
            print(f"Bỏ qua sản phẩm {product_id} do sai cấu trúc dữ liệu")


def sort_products(products):
    try:

        def sort_key(product):
            parts = product.split("-")

            if len(parts) != 4:
                raise ValueError

            price = parts[2]
            rating = parts[3]

            if not price.isdigit():
                raise ValueError

            return (-float(rating), int(price))

        valid_products = []
        invalid_products = []

        for product in products:
            try:
                sort_key(product)
                valid_products.append(product)
            except:
                invalid_products.append(product)

        valid_products.sort(key=sort_key)

        products.clear()
        products.extend(valid_products)

        print("\n--- SẮP XẾP SẢN PHẨM ---")
        print("Đã sắp xếp thành công! Cập nhật danh sách:")

        for index, product in enumerate(products, start=1):
            print(f"{index}. {product}")

        for product in invalid_products:
            product_id = product.split("-")[0]
            print(f"Bỏ qua sản phẩm {product_id} do sai cấu trúc dữ liệu")

    except Exception as error:
        print("Có lỗi xảy ra:", error)


def calculate_total_value(products):
    prices = []

    for product in products:
        try:
            parts = product.split("-")

            if len(parts) != 4:
                raise ValueError

            price = parts[2]

            if not price.isdigit():
                raise ValueError

            prices.append(int(price))

        except:
            product_id = product.split("-")[0]
            print(f"Bỏ qua sản phẩm {product_id} do sai cấu trúc dữ liệu")

    total = functools.reduce(lambda acc, x: acc + x, prices, 0)

    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND.")


def main():
    while True:
        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm")
        print("2. Sắp xếp sản phẩm thông minh")
        print("3. Tính tổng giá trị kho hàng")
        print("4. Đóng hệ thống")
        print("================================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            display_labels(product_list)

        elif choice == "2":
            sort_products(product_list)

        elif choice == "3":
            calculate_total_value(product_list)

        elif choice == "4":
            print("Đóng hệ thống. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1-4.")


main()