print("---- SMART TRIAGE KIOSK ----")

patient_name = input("Nhập họ tên bệnh nhân (Ví dụ: Nguyen Van A): ").strip()
try:
    patient_age = int(input("Nhập tuổi bệnh nhân (Ví dụ: 35): "))
    spo2_level = int(input("Nhập nồng độ oxy trong máu SpO2 (%) (Ví dụ: 97): "))
    heart_rate = int(input("Nhập nhịp tim (nhịp/phút, Ví dụ: 85): "))
except ValueError:
    print("LỖI: Tuổi, SpO2 và nhịp tim phải là số nguyên!")
    exit()

has_insurance = input("Bạn có thẻ BHYT không? (Vui lòng chỉ gõ 'yes' hoặc 'no'): ").strip().lower()

if not patient_name or patient_age < 0 or spo2_level < 0 or heart_rate < 0:
    print("LỖI: Dữ liệu nhập vào không hợp lệ!")
    exit()

if has_insurance not in ["yes", "no"]:
    print("LỖI: Câu trả lời BHYT không hợp lệ! Vui lòng nhập 'yes' hoặc 'no'.")
    exit()

if spo2_level < 90 or heart_rate > 120:
    triage = "BÁO ĐỘNG ĐỎ - Cấp cứu khẩn!"
elif 90 <= spo2_level <= 95 or 100 <= heart_rate <= 120:
    triage = "BÁO ĐỘNG VÀNG - Theo dõi sát!"
else:
    triage = "XANH - Khám thường."

base_fee = 500000
if patient_age < 6 or patient_age >= 80:
    fee = 0
elif has_insurance == "yes":
    fee = base_fee / 2
else:
    fee = base_fee

print("\n===== PHIẾU KHÁM BỆNH ĐIỆN TỬ =====")
print(f"Họ tên bệnh nhân : {patient_name}")
print(f"Tuổi             : {patient_age}")
print(f"SpO2             : {spo2_level}%")
print(f"Nhịp tim         : {heart_rate} nhịp/phút")
print(f"Phân luồng       : {triage}")
print(f"Viện phí tạm ứng : {fee} VNĐ")
print("====================================")

print("\n===== LOG HỆ THỐNG =====")
print(f"patient_name  → {type(patient_name)}")
print(f"patient_age   → {type(patient_age)}")
print(f"spo2_level    → {type(spo2_level)}")
print(f"heart_rate    → {type(heart_rate)}")
print(f"has_insurance → {type(has_insurance)}")
print("====================================")
