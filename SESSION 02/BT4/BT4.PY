print("---- MODULE SÀNG LỌC TIỀN PHẪU THUẬT ----")

try:
    age = int(input("Nhập tuổi bệnh nhân: "))
    systolic_bp = int(input("Nhập huyết áp tâm thu (mmHg): "))
    blood_sugar = int(input("Nhập đường huyết (mg/dL): "))
except ValueError:
    print("Dữ liệu nhập vào không hợp lệ (phải là số nguyên).")
    exit()

if age < 0 or systolic_bp < 0 or blood_sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ (không được âm).")
    exit()

if age < 75:
    if 90 <= systolic_bp <= 140:
        if blood_sugar < 150:
            print("KẾT QUẢ: ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
        else:
            print("TỪ CHỐI PHẪU THUẬT - Đường huyết cao")
    else:
        print("TỪ CHỐI PHẪU THUẬT - Huyết áp không an toàn")
else:
    print("TỪ CHỐI PHẪU THUẬT - Tuổi quá cao")
