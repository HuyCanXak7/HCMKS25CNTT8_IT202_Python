total_bill = int(input("nhập số tiền: "))
print("Tổng số tiền ban đầu: ", total_bill)
print("--- Hóa đơn thanh toán RIKKEI STORE ---")
if total_bill >= 500000:
    print("số tiền sau khi giảm giá 10%: ", total_bill * 0.9)
    print("tổng số tiền phải thanh toán: ", total_bill * 0.9)
else:
    print("số tiền không được giảm giá: ", total_bill)
    print("tổng số tiền phải thanh toán: ", total_bill)