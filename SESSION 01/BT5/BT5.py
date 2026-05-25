print("Chào mừng đến Kiosk Khai Báo Y tế - Bệnh viện Sức Khỏe Vàng")
print("Xin vui lòng nhập thông tin theo hướng dẫn bên dưới.\n")

patient_name = input("Nhập họ tên bệnh nhân (Ví dụ: Nguyen Van A): ")
patient_id = input("Nhập mã bệnh nhân (Ví dụ: BN123): ")

try:
    body_temperature = float(input("Nhập nhiệt độ cơ thể °C (Ví dụ: 37.5): "))
except ValueError:
    print("Lỗi: Nhiệt độ phải là số thực (float).")
    exit()

try:
    heart_rate = int(input("Nhập nhịp tim (nhịp/phút, Ví dụ: 85): "))
except ValueError:
    print("Lỗi: Nhịp tim phải là số nguyên (int).")
    exit()

try:
    weight = float(input("Nhập cân nặng kg (Ví dụ: 65.5): "))
except ValueError:
    print("Lỗi: Cân nặng phải là số thực (float).")
    exit()

print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")
print(f"Họ tên bệnh nhân : {patient_name}")
print(f"Mã bệnh nhân     : {patient_id}")
print(f"Nhiệt độ cơ thể  : {body_temperature} °C")
print(f"Nhịp tim         : {heart_rate} nhịp/phút")
print(f"Cân nặng         : {weight} kg")
print("====================================")

print("\n===== LOG HỆ THỐNG (IT) =====")
print(f"patient_name     → {type(patient_name)}")
print(f"patient_id       → {type(patient_id)}")
print(f"body_temperature → {type(body_temperature)}")
print(f"heart_rate       → {type(heart_rate)}")
print(f"weight           → {type(weight)}")
print("================================")
