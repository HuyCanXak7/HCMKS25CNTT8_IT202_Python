shop_name = ""
product_name = ""
product_description = ""
category = ""
keywords = []
discount_codes = []

while True:

    print("\n===== MENU =====")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")

    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn phải từ 1 đến 5")
        continue

    if choice == 1:

        shop_name = input("Nhập tên shop: ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        product_name = input("Nhập tên sản phẩm: ")
        product_description = input("Nhập mô tả sản phẩm: ")

        if product_description.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue

        category = input("Nhập danh mục sản phẩm: ")
        keyword_input = input("Nhập từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ")

        shop_name = shop_name.strip()
        product_name = product_name.strip().title()
        product_description = product_description.strip()
        category = category.strip().lower()

        keywords = []

        for keyword in keyword_input.split(","):
            keyword = keyword.strip()

            if keyword != "":
                keywords.append(keyword)

        print("\n===== BÁO CÁO =====")
        print("Tên shop:", shop_name)
        print("Tên sản phẩm:", product_name)
        print("Mô tả sản phẩm:", product_description)
        print("Độ dài mô tả:", len(product_description))
        print("Danh mục:", category)
        print("Danh sách từ khóa:", ", ".join(keywords))
        print("Số lượng từ khóa:", len(keywords))
        print("Mô tả chữ thường:", product_description.lower())
        print("Mô tả chữ hoa:", product_description.upper())

    elif choice == 2:

        if shop_name == "":
            shop_name = input("Nhập tên shop: ")

        if shop_name.strip() == "":
            print("Tên shop không được bỏ trống")
            continue

        normalized_shop = shop_name.strip().lower()
        normalized_shop = "-".join(normalized_shop.split())

        if not normalized_shop.startswith("shop-"):
            normalized_shop = "shop-" + normalized_shop

        print("Tên shop ban đầu:", shop_name)
        print("Tên shop chuẩn hóa:", normalized_shop)

    elif choice == 3:

        code = input("Nhập mã giảm giá: ").strip()

        if code == "":
            print("Mã giảm giá không được rỗng")

        elif " " in code:
            print("Mã giảm giá không được chứa khoảng trắng")

        elif len(code) < 6 or len(code) > 12:
            print("Mã giảm giá phải từ 6 đến 12 ký tự")

        elif code != code.upper():
            print("Mã giảm giá phải viết hoa toàn bộ")

        elif not code.isalnum():
            print("Mã giảm giá chỉ được chứa chữ và số")

        elif not code.startswith("SALE"):
            print("Mã giảm giá phải bắt đầu bằng SALE")

        else:

            print("Mã giảm giá hợp lệ")

            discount_codes.append(code)

            print("Danh sách mã giảm giá:", ", ".join(discount_codes))

    elif choice == 4:

        if product_description.strip() == "":
            print("Chưa có mô tả sản phẩm")
            continue

        old_keyword = input("Nhập từ khóa cần tìm: ")
        new_keyword = input("Nhập từ khóa thay thế: ")

        if old_keyword in product_description:

            count = product_description.count(old_keyword)

            replaced_description = product_description.replace(old_keyword, new_keyword)

            print("Số lần xuất hiện của từ khóa:", count)
            print("Mô tả sau khi thay thế:", replaced_description)

        else:

            print("Không tìm thấy từ khóa")

    elif choice == 5:

        print("Thoát chương trình")
        break