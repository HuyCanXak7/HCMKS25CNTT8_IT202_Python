
bill_pay = []
bill_day = int(input("Nhập số lượng hóa đơn trong ca:"))
for i in range(1, bill_day + 1):
    bill_amount = int(input(f"Nhập số tiền hóa đơn thứ {i}: "))
    bill_pay.append(bill_amount)
print("=== kết quả kiểm toán ca RIKKEI STORE ===")
print("Hóa đơn có giá trị cao nhất là: ", max(bill_pay))
print ("Hóa đơn có giá trị thấp nhất là: ", min(bill_pay))
