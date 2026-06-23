class Student:
    def __init__(self, student_id, name, theory_score, practice_score, project_score):
        self.student_id = student_id
        self.name = name
        self.theory_score = theory_score
        self.practice_score = practice_score
        self.project_score = project_score
        self.final_score = 0
        self.academic_rank = ""
        self.calculate_final_score()
        self.classify_academic_rank()

    def calculate_final_score(self):
        self.final_score = (self.theory_score * 0.2+ self.practice_score * 0.3+ self.project_score * 0.5)

    def classify_academic_rank(self):
        if self.final_score < 5:
            self.academic_rank = "Yếu"
        elif self.final_score < 7:
            self.academic_rank = "Trung bình"
        elif self.final_score < 8.5:
            self.academic_rank = "Khá"
        else:
            self.academic_rank = "Giỏi"


class StudentManager:
    def __init__(self):
        self.students = []

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def input_score(self, message):
        while True:
            try:
                score = float(input(message))

                if 0 <= score <= 10:
                    return score

                print("Điểm phải nằm trong khoảng từ 0 đến 10!")

            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

    def add_student(self):
        student_id = input("Nhập mã sinh viên: ").strip()

        if not student_id:
            print("Mã sinh viên không được để trống!")
            return

        if self.find_student_by_id(student_id):
            print("Mã sinh viên đã tồn tại!")
            return

        name = input("Nhập họ tên: ").strip()

        if not name:
            print("Họ tên không được để trống!")
            return

        theory_score = self.input_score("Nhập điểm lý thuyết: ")
        practice_score = self.input_score("Nhập điểm thực hành: ")
        project_score = self.input_score("Nhập điểm đồ án: ")

        student = Student(
            student_id,
            name,
            theory_score,
            practice_score,
            project_score,
        )

        self.students.append(student)

        print("Thêm sinh viên thành công!")

    def show_all(self):
        if not self.students:
            print("Danh sách sinh viên trống!")
            return
        print('-'*80)
        print(
            f"|{'Mã SV':<6}|"
            f"{'Họ tên':<20}|"
            f"{'LT':<6}|"
            f"{'TH':<6}|"
            f"{'ĐA':<6}|"
            f"{'Tổng kết':<8}|"
            f"{'Học lực':<10}|"
        )
        print('-'*80)

        for student in self.students:
            print(
                f"|{student.student_id:6}|"
                f"{student.name:<20}|"
                f"{student.theory_score:<6}|"
                f"{student.practice_score:<6}|"
                f"{student.project_score:<6}|"
                f"{student.final_score:<8.1f}|"
                f"{student.academic_rank:<10}|"
            )

    def update_student(self):
        student_id = input("Nhập mã sinh viên cần cập nhật: ").strip()

        student = self.find_student_by_id(student_id)

        if student is None:
            print("Không tìm thấy sinh viên!")
            return

        student.theory_score = self.input_score(
            "Nhập điểm lý thuyết mới: "
        )
        student.practice_score = self.input_score(
            "Nhập điểm thực hành mới: "
        )
        student.project_score = self.input_score(
            "Nhập điểm đồ án mới: "
        )

        student.calculate_final_score()
        student.classify_academic_rank()

        print("Cập nhật thành công!")

    def delete_student(self):
        student_id = input("Nhập mã sinh viên cần xóa: ").strip()

        student = self.find_student_by_id(student_id)

        if student is None:
            print("Không tìm thấy sinh viên!")
            return

        confirm = input(
            "Bạn có chắc muốn xóa sinh viên này không? (Y/N): "
        )

        if confirm.lower() == "y":
            self.students.remove(student)
            print("Xóa thành công!")
        else:
            print("Đã hủy thao tác!")

    def search_student(self):
        keyword = input("Nhập tên cần tìm: ").strip().lower()

        found = False

        for student in self.students:
            if keyword in student.name.lower():
                found = True
                print(
                    f"{student.student_id} | "
                    f"{student.name} | "
                    f"{student.final_score:.2f} | "
                    f"{student.academic_rank}"
                )

        if not found:
            print("Không tìm thấy sinh viên phù hợp!")


feature = StudentManager()

menu = """
================ MENU ================
1. Hiển thị danh sách sinh viên
2. Thêm sinh viên mới
3. Cập nhật thông tin sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên theo tên
6. Thoát
======================================
"""

while True:
    print(menu)

    choice = input("Nhập lựa chọn của bạn: ")

    if choice == "1":
        feature.show_all()

    elif choice == "2":
        feature.add_student()

    elif choice == "3":
        feature.update_student()

    elif choice == "4":
        feature.delete_student()

    elif choice == "5":
        feature.search_student()

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống quản lý học tập!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")