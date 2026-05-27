branch_count = int(input("Nhập số lượng chi nhánh: "))
for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}:")
    for class_number in range(1, 3):
        while True:
            student_count = int(input(f"Nhập số học viên đi học của lớp {class_number}: "))
            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue
            if student_count == 0:
                print(f"Chi nhánh {branch} - Lớp {class_number}: ""Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
                break
            if student_count >= 20:
                print(f"Chi nhánh {branch} - Lớp {class_number}: ""Lớp học ổn định")
            else:
                print(f"Chi nhánh {branch} - Lớp {class_number}: ""Lớp cần được nhắc nhở theo dõi")
            break