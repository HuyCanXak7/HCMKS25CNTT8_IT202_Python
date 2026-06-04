cart = [
    {"code": "P001", "name": "Dien thoai iPhone 15", "quantity": 1, "unit_price": 25000000},
    {"code": "P002", "name": "Op lung Silicon", "quantity": 2, "unit_price": 150000},
]

print("Bạn đã chọn tính năng xem chi tiết giỏ hàng & Tính tổng tiền")
print("\n--- Chi tiết giỏ hàng ---")

header = f"{'STT':<3}|{'Mã':<4}|{'Tên sản phẩm':<20}|{'SL':<2}|{'Đơn giá':>11}|{'Thành tiền':>12}|"
print(header)
print("-"*65)

total_quantity = 0
total_amount = 0

for index, item in enumerate(cart, start=1):
    line_total = item["quantity"] * item["unit_price"]
    total_quantity += item["quantity"]
    total_amount += line_total
    print(f"{index:<3}|{item['code']:<4}|{item['name']:<20}|"f"{item['quantity']:<2}|{item['unit_price']:>10,}đ|{line_total:>12,}đ")

print("-"*65)
print(f"Tổng số lượng: {total_quantity}")
print(f"Tổng tiền: {total_amount:>12,}đ")