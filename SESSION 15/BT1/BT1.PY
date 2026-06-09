inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")

def process_sale(quantity):
    global inventory_stock

    if quantity <= 0:
        print("Số lượng sản phẩm phải lớn hơn 0")
        return False

    if quantity > inventory_stock:
        print("Lỗi! Số lượng vượt quá tồn kho.")
        print(f"Số lượng trong kho là: {inventory_stock}")
        return False

    inventory_stock -= quantity
    return True

def calculate_final_price(quantity, price):
    global total_revenue

    total_temp = quantity * price

    if total_temp >= 1000:
        discount = total_temp * 0.1
    else:
        discount = 0

    vat = (total_temp - discount) * 0.08
    total_bill = total_temp - discount + vat

    total_revenue += total_bill

    return total_temp, discount, vat, total_bill

while True:
    print("========== TECHSTORE MANAGEMENT SYSTEM ==========")
    print("1. Nhập thêm hàng vào kho")
    print("2. Bán hàng (Tính toán hóa đơn)")
    print("3. Xem báo cáo tổng quan")
    print("4. Thoát chương trình")
    print("=================================================")

    user_choice = input("Chọn chức năng (1-4): ")

    if user_choice == '4':
        print("Đang thoát chương trình...")
        break

    elif user_choice == '1':
        print("--- NHẬP HÀNG ---")
        amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
        add_stock(amount)

    elif user_choice == '2':
        print("--- BÁN HÀNG ---")

        quantity = int(input("Nhập số lượng mua: "))

        if process_sale(quantity):
            price = int(input("Nhập đơn giá: "))

            total_temp, discount, vat, total_bill = calculate_final_price(quantity, price)

            print("-> Hóa đơn chi tiết:")
            print(f"Số lượng: {quantity} | Đơn giá: {price}")
            print(f"Tạm tính: {total_temp}")
            print(f"Giảm giá(10%): {discount}")
            print(f"Thuế VAT: {vat}")
            print(f"Tổng thanh toán: {total_bill}")
            print("Đã bán thành công!")

    elif user_choice == '3':
        print("--- BÁO CÁO ---")
        print(f"Tồn kho hiện tại: {inventory_stock}")
        print(f"Tổng doanh thu: {total_revenue}")

    else:
        print("Lựa chọn không hợp lệ!")
        