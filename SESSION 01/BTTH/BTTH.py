import random
print("HỆ THỐNG QUẢN LÝ BỆNH NHÂN - PHÒNG KHÁM TƯ NHÂN")
print("Vui lòng nhập thông tin bệnh nhân theo hướng dẫn.\n")

patient_name = input("Nhập tên bệnh nhân (Ví dụ: Nguyen Van A): ")
gender = input("Nhập giới tính (Nam/Nữ): ")

try:
    birth_year = int(input("Nhập năm sinh (Ví dụ: 1998): "))
except ValueError:
    print("Lỗi: Năm sinh phải là số nguyên.")
    exit()

phone_number = input("Nhập số điện thoại (Ví dụ: 0912345678): ")
email = input("Nhập email (Ví dụ: abc@gmail.com): ")
symptom = input("Nhập triệu chứng ban đầu (Ví dụ: Đau đầu): ")

try:
    fee = float(input("Nhập chi phí khám (Ví dụ: 250000): "))
except ValueError:
    print("Lỗi: Chi phí phải là số thực.")
    exit()

random_number = random.randint(100, 999)
patient_id = f"BN{birth_year}{random_number}"

print("\n--- THẺ BỆNH NHÂN ---")
print(f"Mã BN        : {patient_id}")
print(f"Tên          : {patient_name} ({type(patient_name)})")
print(f"Giới tính    : {gender} ({type(gender)})")
print(f"Năm sinh     : {birth_year} ({type(birth_year)})")
print(f"Điện thoại   : {phone_number} ({type(phone_number)})")
print(f"Email        : {email} ({type(email)})")
print(f"Triệu chứng  : {symptom} ({type(symptom)})")
print(f"Chi phí      : {fee} VND ({type(fee)})")
