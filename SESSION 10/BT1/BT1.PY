cart = [
    {"code": "P001", "name": "Dien thoai iPhone 15", "quantity": 1, "unit_price": 25000000},
    {"code": "P002", "name": "Op lung Silicon", "quantity": 2, "unit_price": 150000},
]

menu = True
while menu:
    print("==========================================")
    print("SHOPEE CART MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("==========================================")
    input_user = input("Vui lòng chọn chức năng (1-5): ")
    if input_user == "1":
        print("Bạn đã chọn chức năng 1: Xem chi tiết giỏ hàng & Tính tổng tiền")
        print("\n--- CHI TIẾT GIỎ HÀNG ---")
        print("STT | Mã SP | Tên Sản Phẩm                | SL | Đơn Giá       | Thành Tiền")
        print("-------------------------------------------------------------------------")
        total_quantity = 0
        total_amount = 0
        for index, item in enumerate(cart, start=1):
            line_total = item["quantity"] * item["unit_price"]
            total_quantity += item["quantity"]
            total_amount += line_total
            print(f"{index:<3} | {item['code']:<4} | {item['name']:<25} | {item['quantity']:<2} | {item['unit_price']:>13,}đ | {line_total:>13,}đ")

        print("-------------------------------------------------------------------------")
        print(f"=> Tổng số lượng sản phẩm trong giỏ: {total_quantity}")
        print(f"=> TỔNG TIỀN THANH TOÁN {total_amount:,}đ\n")
    elif input_user == "2":
        print("Bạn đã chọn chức năng 2: Thêm sản phẩm mới / Cộng dồn số lượng")
        code = input("Nhập Mã sản phẩm: ").strip()
        name = input("Nhập Tên sản phẩm: ").strip()
        try:
            quantity = int(input("Nhập Số lượng: ").strip())
            unit_price = int(input("Nhập Đơn giá: ").strip())
        except ValueError:
            print("Số lượng và Đơn giá phải là số nguyên. Vui lòng thử lại.")
            continue

        if not code or not name:
            print("Mã sản phẩm và Tên sản phẩm không được để trống. Vui lòng thử lại.")
            continue

        if quantity <= 0 or unit_price <= 0:
            print("Số lượng và Đơn giá phải lớn hơn 0. Vui lòng thử lại.")
            continue

        found = False
        for item in cart:
            if item["code"].lower() == code.lower():
                item["quantity"] += quantity
                print(f"Mã {code} đã tồn tại. Đã cộng dồn số lượng mới vào giỏ hàng.")
                found = True
                break

        if not found:
            cart.append({
                "code": code,
                "name": name,
                "quantity": quantity,
                "unit_price": unit_price,
            })
            print(f"Đã thêm sản phẩm mới {code} vào giỏ hàng.")
    elif input_user == "3":
        print("Bạn đã chọn chức năng 3: Cập nhật số lượng sản phẩm")
        code = input("Nhập Mã sản phẩm cần cập nhật: ").strip()
        try:
            new_quantity = int(input("Nhập Số lượng mới: ").strip())
        except ValueError:
            print("Số lượng phải là số nguyên. Vui lòng thử lại.")
            continue

        if new_quantity <= 0:
            print("Số lượng phải lớn hơn 0. Vui lòng thử lại.")
            continue

        updated = False
        for item in cart:
            if item["code"].lower() == code.lower():
                item["quantity"] = new_quantity
                print(f"Đã cập nhật số lượng sản phẩm {code} thành {new_quantity}.")
                updated = True
                break
        if not updated:
            print(f"Không tìm thấy sản phẩm có mã {code}.")
    elif input_user == "4":
        print("Bạn đã chọn chức năng 4: Xóa sản phẩm khỏi giỏ hàng")
        code = input("Nhập Mã sản phẩm cần xóa: ").strip()
        removed = False
        for item in cart:
            if item["code"].lower() == code.lower():
                cart.remove(item)
                print(f"Đã xóa sản phẩm có mã {code} khỏi giỏ hàng.")
                removed = True
                break
        if not removed:
            print(f"Không tìm thấy sản phẩm có mã {code}.")
    elif input_user == "5":
        print("Bạn đã chọn chức năng 5: Thoát chương trình")
        menu = False
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
