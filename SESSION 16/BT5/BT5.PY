def find_patient_index(patients, er_id):
    er_id = er_id.strip().upper()

    for index, patient in enumerate(patients):
        if patient.startswith(er_id + "|"):
            return index

    return -1


def extract_vital_value(vital_string):
    return float(vital_string.split(":")[1])


def display_dashboard(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("--- BẢNG THEO DÕI CA CẤP CỨU ------------------------------------")

    for index, patient in enumerate(patients, start=1):
        data = patient.split("|")

        hr = data[2].split(":")[1]
        temp = data[3].split(":")[1]

        print(
            f"{index}. [{data[0]}] {data[1]} | "
            f"Nhịp tim: {hr} bpm | "
            f"Nhiệt độ: {temp} °C"
        )

    print("-----------------------------------------------------------------")


def admit_patient(patients):
    print("--- TIẾP NHẬN CA CẤP CỨU MỚI ---")

    er_id = input("Nhập mã ER: ").strip().upper()

    if er_id == "":
        print("Mã ER không được để trống!")
        return

    if find_patient_index(patients, er_id) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()

    if name == "":
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        try:
            hr = int(input("Nhập nhịp tim HR: "))

            if hr > 0:
                break

            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

        except ValueError:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

    while True:
        try:
            temp = float(input("Nhập nhiệt độ TEMP: "))

            if temp >= 36.5:
                break

            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

        except ValueError:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

    patient = f"{er_id}|{name}|HR:{hr}|TEMP:{temp}"

    patients.append(patient)

    print("\nTiếp nhận ca cấp cứu mới thành công!")
    print(patient)


def update_vitals(patients):
    print("--- CẬP NHẬT LẠI SINH HIỆU ---")

    er_id = input("Nhập mã ER cần cập nhật: ").strip().upper()

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    data = patients[index].split("|")

    print(f"Tìm thấy bệnh nhân: {data[1]}")
    print(f"Sinh hiệu hiện tại: {data[2]} | {data[3]}")
    print("Bạn muốn cập nhật:")
    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")

    choice = input("Chọn loại sinh hiệu: ")

    if choice == "1":
        try:
            new_hr = int(input("Nhập nhịp tim mới: "))

            if new_hr <= 0:
                raise ValueError

            data[2] = f"HR:{new_hr}"

            patients[index] = "|".join(data)

            print("\nCập nhật nhịp tim thành công!")

        except ValueError:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

    elif choice == "2":
        try:
            new_temp = float(input("Nhập nhiệt độ mới: "))

            if new_temp < 36.5:
                raise ValueError

            data[3] = f"TEMP:{new_temp}"

            patients[index] = "|".join(data)

            print("\nCập nhật nhiệt độ thành công!")

        except ValueError:
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")


def trigger_red_alert(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    critical_count = 0

    for patient in patients:
        data = patient.split("|")

        hr = extract_vital_value(data[2])
        temp = extract_vital_value(data[3])

        if hr > 100 or temp >= 39.0:
            critical_count += 1

    if critical_count == 0:
        print("--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
        return

    print("!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")

    stt = 1

    for patient in patients:
        data = patient.split("|")

        hr = extract_vital_value(data[2])
        temp = extract_vital_value(data[3])

        if hr > 100 or temp >= 39.0:
            print(
                f"{stt}. [{data[0]}] {data[1]} | "
                f"HR: {int(hr)} bpm | "
                f"TEMP: {temp} °C | "
                f"CẦN XỬ LÝ KHẨN CẤP"
            )

            stt += 1

    print("-----------------------------------------------------")
    print(f"Tổng số ca nguy kịch: {critical_count}")


def discharge_patient(patients):
    print("--- XUẤT VIỆN / CHUYỂN KHOA ---")

    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip().upper()

    if er_id == "":
        print("Mã ER không được để trống!")
        return

    index = find_patient_index(patients, er_id)

    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    patient_name = patients[index].split("|")[1]

    patients.pop(index)

    print(f"Đã chuyển khoa thành công cho bệnh nhân {patient_name}!")


def main():
    er_patients = [
        "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
        "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
        "ER03|Le Van Cuong|HR:130|TEMP:38.2"
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
        print("1. Bảng theo dõi bệnh nhân")
        print("2. Tiếp nhận ca cấp cứu mới")
        print("3. Cập nhật lại sinh hiệu")
        print("4. BÁO ĐỘNG ĐỎ Lọc bệnh nhân nguy kịch")
        print("5. Xuất viện / Chuyển khoa")
        print("6. Thoát chương trình")
        print("=================================================")

        try:
            choice = int(input("Chọn chức năng (1-6): "))

            if choice == 1:
                display_dashboard(er_patients)

            elif choice == 2:
                admit_patient(er_patients)

            elif choice == 3:
                update_vitals(er_patients)

            elif choice == 4:
                trigger_red_alert(er_patients)

            elif choice == 5:
                discharge_patient(er_patients)

            elif choice == 6:
                print("Kết thúc ca trực. Tạm biệt!")
                break

            else:
                print("Lựa chọn không hợp lệ!")

        except ValueError:
            print("Lựa chọn không hợp lệ!")


main()