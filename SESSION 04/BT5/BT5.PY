total_revenue = 0
total_bill = 0
large_bill = 0

while True:
    i = int(input("Nhập số thứ tự khách hàng: "))
    bill_amount = int(input(f"Nhập giá trị hóa đơn thứ {i}: "))
    total_revenue += bill_amount
    total_bill += 1
    if bill_amount >= 1000000:
        large_bill += 1
    continue_input = input("Bạn có muốn nhập tiếp không? (C/K): ")
    if continue_input.upper() != "C":
        break
print("=== BÁO CÁO DANH THU CUỐI NGÀY RIKKEI STORE")
print("Tổng số hóa đơn đã xử lý:", total_bill)
print("Tổng doanh thu ngày hôm nay: ", total_revenue)
print("Số hóa đơn lớn hơn (>=1000000):", large_bill)
print("Tỷ lệ hóa đơn lớn đạt: ", large_bill / total_bill * 100 if total_bill > 0 else 0, "%", "trên tổng số đơn hàng")