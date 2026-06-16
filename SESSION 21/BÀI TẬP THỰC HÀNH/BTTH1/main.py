import logging
logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.DEBUG,
    format=''
)

balance = 0 

def Deposit():
    global balance
    print("\n--- NẠP TIỀN VÀO VÍ ---")
    try:
        amount = int(input("Nhập số tiền cần nạp: "))
        if amount <= 0:
            print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
            logging.error(f"InvalidAmountError: Attempted to process {amount} VND.")
            return
        balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")
        print(f"Số dư hiện tại: {balance:,} VND")
        logging.info(f"Deposit successful: +{amount} VND. Current Balance: {balance}")
    except ValueError:
        print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
        logging.error("ValueError: Invalid numeric input for deposit.")
        

    

header = """========== VÍ MOMO GIẢ LẬP ==========

1. Nạp tiền vào ví

2. Chuyển tiền

3.  Xem số dư hiện tại

4. Thoát chương trình 

==============================================="""


while True:
    print(header)
    user_choice = input("Nhập lựa chọn của bạn: ")
    if user_choice == '4':
        break
    elif user_choice == '1':
        Deposit()
    