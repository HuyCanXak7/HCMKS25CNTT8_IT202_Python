student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]


def find_student(records, student_id):
    """
    Tìm học viên theo mã
    """
    for index, student in enumerate(records):
        if student["student_id"] == student_id:
            return index

    return -1


def get_status(current_points):
    """
    Xác định trạng thái thành viên
    """
    if current_points < 500:
        return "Cần tích lũy thêm"

    if current_points <= 1500:
        return "Thành viên tiềm năng"

    return "Thành viên ưu tú"


def input_positive_integer(message):
    """
    Nhập số nguyên dương
    """
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Vui lòng nhập số nguyên dương!")

        except ValueError:
            print("Vui lòng nhập số nguyên dương!")


def input_multiplier():
    """
    Nhập hệ số hợp lệ
    """
    while True:
        try:
            multiplier = float(
                input(
                    "Nhập hệ số nhân mới (1.0 - 3.0): "
                )
            )

            if 1.0 <= multiplier <= 3.0:
                return multiplier

            print(
                "Hệ số nhân không hợp lệ. "
                "Chỉ chấp nhận số từ 1.0 đến 3.0"
            )

        except ValueError:
            print(
                "Hệ số nhân không hợp lệ. "
                "Chỉ chấp nhận số từ 1.0 đến 3.0"
            )


def display_statements(records):
    """
    Hiển thị sao kê điểm
    """
    print("\n--- SAO KÊ ĐIỂM SỐ ---")

    for index, student in enumerate(records, start=1):

        status = get_status(
            student["current_points"]
        )

        print(
            f"{index}. "
            f"Mã: {student['student_id']} | "
            f"Tên: {student['name']} | "
            f"Hiện có: {student['current_points']} | "
            f"Đã tiêu: {student['spent_points']} | "
            f"Hoàn trả: {student['refunded_points']} | "
            f"Hệ số: x{student['multiplier']} | "
            f"Trạng thái: {status}"
        )

    print("----------------------")


def redeem_rewards(records):
    """
    Đổi điểm lấy quà
    """
    student_id = input(
        "Nhập mã học viên đổi quà: "
    ).strip().upper()

    index = find_student(
        records,
        student_id
    )

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    points = input_positive_integer(
        "Nhập số điểm cần tiêu: "
    )

    if points > records[index]["current_points"]:
        print(
            "Số dư điểm không đủ để "
            "thực hiện giao dịch!"
        )
        return

    records[index]["current_points"] -= points
    records[index]["spent_points"] += points

    print(
        f">> Giao dịch thành công! "
        f"'{records[index]['name']}' "
        f"đã tiêu {points} điểm. "
        f"Số dư còn lại: "
        f"{records[index]['current_points']} điểm."
    )


def appeal_score(records):
    """
    Hoàn điểm
    """
    student_id = input(
        "Nhập mã học viên cần phúc khảo: "
    ).strip().upper()

    index = find_student(
        records,
        student_id
    )

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    refund_points = input_positive_integer(
        "Nhập số điểm hoàn lại: "
    )

    if refund_points > records[index]["spent_points"]:
        print(
            "Không thể hoàn số điểm lớn hơn "
            "tổng điểm đã tiêu!"
        )
        return

    records[index]["current_points"] += refund_points
    records[index]["spent_points"] -= refund_points
    records[index]["refunded_points"] += refund_points

    print(
        f">> Hoàn điểm thành công! "
        f"'{records[index]['name']}' "
        f"được cộng lại {refund_points} điểm."
    )


def activate_multiplier(records):
    """
    Kích hoạt hệ số
    """
    student_id = input(
        "Nhập mã học viên nhận hệ số: "
    ).strip().upper()

    index = find_student(
        records,
        student_id
    )

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    multiplier = input_multiplier()

    records[index]["multiplier"] = multiplier

    print(
        f">> Đã kích hoạt hệ số "
        f"x{multiplier} cho học viên "
        f"'{records[index]['name']}'."
    )


def grade_assignment(records):
    """
    Chấm bài và cộng điểm
    """
    student_id = input(
        "Nhập mã học viên vừa nộp bài: "
    ).strip().upper()

    index = find_student(
        records,
        student_id
    )

    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return

    base_points = input_positive_integer(
        "Nhập số điểm gốc đạt được: "
    )

    multiplier = records[index]["multiplier"]

    earned_points = int(
        base_points * multiplier
    )

    records[index]["current_points"] += earned_points

    print(
        f">> Hệ số hiện tại của "
        f"'{records[index]['name']}' "
        f"là x{multiplier}."
    )

    print(
        f">> Điểm thực nhận: "
        f"{earned_points}."
    )

    print(
        f">> Đã cộng {earned_points} điểm "
        f"vào tài khoản!"
    )


def display_menu():
    print("\n===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
    print("1. Hiển thị sao kê điểm số")
    print("2. Đổi điểm lấy phần thưởng")
    print("3. Phúc khảo bài thi (Hoàn điểm)")
    print("4. Kích hoạt (Hệ số nhân điểm)")
    print("5. Chấm bài (thêm điểm)")
    print("6. Thoát chương trình")
    print("=====================================================")


def main():

    while True:

        display_menu()

        choice = input(
            "Chọn chức năng (1-6): "
        )

        if choice == "1":
            display_statements(
                student_records
            )

        elif choice == "2":
            redeem_rewards(
                student_records
            )

        elif choice == "3":
            appeal_score(
                student_records
            )

        elif choice == "4":
            activate_multiplier(
                student_records
            )

        elif choice == "5":
            grade_assignment(
                student_records
            )

        elif choice == "6":
            print(
                "Cảm ơn bạn đã sử dụng hệ thống!"
            )
            break

        else:
            print(
                "Lựa chọn không hợp lệ!"
            )


if __name__ == "__main__":
    main()