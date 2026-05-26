print("---- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ----")
total_budget = 0
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    salary = int(input(" Nhập mức lương (VND): "))
    total_budget += salary
print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VND")
