import colorama as clr

from data.students import (
    student_records
)

from reports.report_generator import (
    display_student_scores,
    export_learning_report
)

from utils.random_utils import (
    generate_assignment_code
)

from utils.string_utils import (
    normalize_student_names
)

clr.init()


def main():

    while True:

        print(
            "\n===== HỆ THỐNG TIỆN ÍCH "
            "HỌC TẬP RIKKEI ACADEMY ====="
        )

        print(
            "1. Xem danh sách sinh viên "
            "và điểm trung bình"
        )

        print(
            "2. Chuẩn hóa tên sinh viên"
        )

        print(
            "3. Sinh mã bài tập ngẫu nhiên"
        )

        print(
            "4. Xuất báo cáo học tập"
        )

        print(
            "5. Thoát chương trình"
        )

        try:

            choice = int(
                input(
                    "Chọn chức năng (1-5): "
                )
            )

            if choice == 1:

                display_student_scores(
                    student_records
                )

            elif choice == 2:

                normalize_student_names(
                    student_records
                )

            elif choice == 3:

                print(
                    "\n--- SINH MÃ BÀI TẬP ---"
                )

                print(
                    "Mã bài tập của bạn là:",
                    generate_assignment_code()
                )

            elif choice == 4:

                print(
                    "\n--- XUẤT BÁO CÁO "
                    "HỌC TẬP ---"
                )

                export_learning_report(
                    student_records
                )

            elif choice == 5:

                print(
                    "Cảm ơn bạn đã sử dụng "
                    "hệ thống!"
                )

                break

            else:

                print(
                    "Chức năng không hợp lệ. "
                    "Vui lòng chọn từ 1 đến 5."
                )

        except ValueError:

            print(
                "Chức năng không hợp lệ. "
                "Vui lòng chọn từ 1 đến 5."
            )


if __name__ == "__main__":
    main()