from datetime import datetime


def find_patient_index(records, patient_id):
    patient_id = patient_id.strip().upper()

    for index, record in enumerate(records):
        if record.startswith(patient_id + "-"):
            return index

    return -1


def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")

    for index, record in enumerate(records, start=1):
        data = record.split("-")

        print(
            f"{index}. [{data[0]}] {data[1]:<20} | "
            f"Năm sinh: {data[2]} | "
            f"Chẩn đoán: {data[3]}"
        )

    print("--------------------------------------------------------------------------")


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if find_patient_index(records, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    name = name.strip().replace("-", " ").title()

    current_year = datetime.now().year

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if birth_year.isdigit():
            birth_year = int(birth_year)

            if 1900 <= birth_year <= current_year:
                break

        print("Năm sinh không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = diagnosis.strip().replace("-", " ").capitalize()

    record = f"{patient_id}-{name}-{birth_year}-{diagnosis}"

    records.append(record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print(record)


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"Không tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    data = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ")
    new_diagnosis = new_diagnosis.strip().replace("-", " ").capitalize()

    data[3] = new_diagnosis

    records[index] = "-".join(data)

    print("\nCập nhật chẩn đoán thành công!")


def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    current_year = datetime.now().year

    children = 0
    adult = 0
    elderly = 0

    for record in records:
        data = record.split("-")

        age = current_year - int(data[2])

        if age < 16:
            children += 1
        elif age <= 60:
            adult += 1
        else:
            elderly += 1

    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adult} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


def main():
    patient_records = [
        "BN001-Nguyen Van A-1985-Viem Phoi",
        "BN002-Tran Thi B-1990-Sot Xuat Huyet",
        "BN003-Le Van C-2015-Viem Phe Quan"
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("==================================================")

        try:
            choice = int(input("Chọn chức năng (1-5): "))

            if choice == 1:
                display_records(patient_records)

            elif choice == 2:
                add_patient(patient_records)

            elif choice == 3:
                update_diagnosis(patient_records)

            elif choice == 4:
                generate_age_report(patient_records)

            elif choice == 5:
                print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")

        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


main()