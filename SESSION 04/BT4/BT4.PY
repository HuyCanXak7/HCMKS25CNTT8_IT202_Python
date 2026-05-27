import random 
secret_number = random.randint(1, 100)
for i in range(1,6):
    guess = int(input("Nhập số bạn đoán: "))
    if guess < secret_number:
        print("Số bạn đoán quá nhỏ.")
    elif guess > secret_number:
        print("Số bạn đoán quá lớn.")
    else:
        print("Chúc mừng! Bạn đã đoán đúng số bí mật.")
        break
else:
    print("Bạn đã hết số lần đoán. Số bí mật là:", secret_number)
