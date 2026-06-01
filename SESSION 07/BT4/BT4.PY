def process_registration(registration):
    parts = registration.split("|")
    if len(parts) != 4:
        print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
        return

    name = parts[0].strip().title()
    course = parts[1].strip().title()
    student_id = parts[2].strip().upper()
    email = parts[3].strip().lower()

    if "@" not in email:
        print("Email không hợp lệ. Bỏ qua phiếu này")
        return

    if len(student_id) < 5:
        print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
        return
    confirm_code = f"{student_id}_{course.upper().replace(' ', '-')}"

    print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
    print(f"Học viên: {name}")
    print(f"Khóa học: {course}")
    print(f"Mã học viên: {student_id}")
    print(f"Email: {email}")
    print(f"Mã xác nhận: {confirm_code}")


def main():
    try:
        n = int(input("Nhập số lượng phiếu đăng ký: "))
    except ValueError:
        print("Số lượng phiếu đăng ký không hợp lệ")
        return

    if n <= 0:
        print("Số lượng phiếu đăng ký không hợp lệ")
        return

    for i in range(n):
        registration = input(f"Nhập phiếu đăng ký {i+1}: ")
        process_registration(registration)
if __name__ == "__main__":
    main()
