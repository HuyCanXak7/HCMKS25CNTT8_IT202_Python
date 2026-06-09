# Hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    # Tính tổng tiền sau khi áp dụng giảm giá và phí ship
    total_after_fees = price - (price * discount) + shipping_fee
    print("Đã tính xong tổng tiền (trước phí đóng gói):", total_after_fees)
    # Trả về giá trị đã tính để có thể sử dụng bên ngoài hàm
    return total_after_fees

# Đơn hàng mua áo thun: Giá 100000, giảm giá 10% (0.1), phí ship 15000
# Gọi hàm để tính tiền
# Hàm chỉ cần nhận các giá trị cần thiết cho việc tính toán
order_total = calculate_final_price(100000, 0.1, 15000)

# Hệ thống cộng thêm 5000 phí đóng gói vào tổng tiền đơn hàng
# order_total bây giờ đã có giá trị là kết quả trả về từ hàm
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)

