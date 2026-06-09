
students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]


def display_menu():
    """Hiển thị menu chính"""
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")


def validate_score(score_input):
    """Kiểm tra điểm có hợp lệ hay không"""
    try:
        score = float(score_input)

        if 0 <= score <= 10:
            return True

        return False

    except ValueError:
        return False


def input_score(subject):
    """Nhập điểm hợp lệ"""
    while True:
        score_input = input(f"Nhập điểm {subject}: ")

        if validate_score(score_input):
            return float(score_input)

        print("Điểm không hợp lệ, phải là số từ 0 đến 10")


def find_student_by_id(student_list, student_id):
    """Tìm học viên theo mã"""
    for index, student in enumerate(student_list):
        if student["student_id"] == student_id:
            return index

    return -1


def display_students(student_list):
    """Hiển thị danh sách học viên"""

    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    print("\n===== DANH SÁCH HỌC VIÊN =====")

    for index, student in enumerate(student_list, start=1):
        print(
            f"{index}. Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Toán: {student['math_score']} | "
            f"Anh: {student['english_score']}"
        )


def add_student(student_list):
    """Thêm học viên mới"""

    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()

        if find_student_by_id(student_list, student_id) != -1:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
            continue

        break

    while True:
        name = input("Nhập tên học viên: ").strip().title()

        if name == "":
            print("Tên học viên không được để trống!")
            continue

        break

    math_score = input_score("Toán")
    english_score = input_score("Anh")

    student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }

    student_list.append(student)

    print("Thêm học viên thành công!")


def update_score(student_list):
    """Cập nhật điểm học viên"""

    student_id = input(
        "Nhập mã học viên cần cập nhật: "
    ).strip().upper()

    index = find_student_by_id(student_list, student_id)

    if index == -1:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    print("Nhập điểm mới")

    student_list[index]["math_score"] = input_score("Toán")
    student_list[index]["english_score"] = input_score("Anh")

    print("Cập nhật điểm thành công!")


def get_rank(average_score):
    """Xếp loại học lực"""

    if average_score >= 8:
        return "Giỏi"

    if average_score >= 6.5:
        return "Khá"

    if average_score >= 5:
        return "Trung bình"

    return "Yếu"


def evaluate_students(student_list):
    """Đánh giá học lực"""

    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
        return

    print("\n===== KẾT QUẢ ĐÁNH GIÁ =====")

    for student in student_list:

        average = (
            student["math_score"]
            + student["english_score"]
        ) / 2

        rank = get_rank(average)

        print(
            f"Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"ĐTB: {average:.2f} | "
            f"Xếp loại: {rank}"
        )

while True:

    display_menu()

    choice = input("Chọn chức năng (1-5): ").strip()

    if choice == "1":
        display_students(students)

    elif choice == "2":
        add_student(students)

    elif choice == "3":
        update_score(students)

    elif choice == "4":
        evaluate_students(students)

    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")