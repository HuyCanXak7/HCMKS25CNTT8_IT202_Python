Input:
age INT
systolic_bp INT
blood_sugar INT
Output:
if (-) > Dữ liệu nhập vào không hợp lệ

Giải pháp 2: Nested If (điều kiện lồng nhau)
python
if age < 75:
    if 90 <= systolic_bp <= 140:
        if blood_sugar < 150:
            print("ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
        else:
            print("TỪ CHỐI PHẪU THUẬT - Đường huyết cao")
    else:
        print("TỪ CHỐI PHẪU THUẬT - Huyết áp không an toàn")
else:
    print("TỪ CHỐI PHẪU THUẬT - Tuổi quá cao")
