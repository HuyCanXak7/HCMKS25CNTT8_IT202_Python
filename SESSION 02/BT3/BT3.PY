print("---- HỆ THỐNG PHÂN LUỒNG BỆNH NHÂN ----")

patient_name = input("Nhập họ và tên bệnh nhân: ").strip()
try:
    patient_age = int(input("Nhập tuổi bệnh nhân: "))
except ValueError:
    print("LỖI: Tuổi phải là số nguyên!")
    exit()

if not patient_name or patient_age < 0 or patient_age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    exit()

if patient_age < 6:
    priority = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif patient_age >= 80:
    priority = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    priority = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print(f"Tên bệnh nhân : {patient_name}")
print(f"Tuổi          : {patient_age}")
print(f"Kết quả       : {priority}")
