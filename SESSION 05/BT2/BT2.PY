branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

print("\n-------------- Kết quả --------------")
for branch in range(1, branch_count + 1):
    total_students = 0
    for class_ in range(1, class_count + 1):
        students = int(input(f"Nhập số lượng học sinh của chi nhánh {branch}, lớp {class_}: "))
        total_students += students
    print(f"Chi nhánh {branch}: {total_students} học viên")