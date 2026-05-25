print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân: ")
weight = (input("Nhập cân nặng (kg): "))

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Tên bệnh nhân:", name_patient)
print("Cân nặng:", weight, "kg")

print("CẢNH BÁO - kiểu dữ liệu đang lưu là :", type(weight))

hàm input dùng để nhập dữ liệu 
nguyên nhân sai: do thiếu kiểu dữ liệu float cho weight nên mặt định là string