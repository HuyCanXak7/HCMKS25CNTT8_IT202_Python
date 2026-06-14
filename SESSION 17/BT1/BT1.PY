raw_logs = []
processed_logs = []


def load_and_clean_logs():
    """
    Nhập và làm sạch dữ liệu log thô.
    """
    global raw_logs

    print("\n--- NẠP DỮ LIỆU LOG ---")

    log_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")

    remove_chars = str.maketrans("", "", "!@#$")

    cleaned_text = log_input.translate(remove_chars)

    raw_logs = [log.strip() for log in cleaned_text.split(";") if log.strip()]

    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")


def filter_danger_logs():
    """
    Lọc các log chứa ERROR hoặc CRITICAL.
    """
    global processed_logs

    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    print("\n--- LỌC CẢNH BÁO ---")

    processed_logs = [
        log for log in raw_logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]

    if len(processed_logs) == 0:
        print("Không tìm thấy cảnh báo nguy hiểm.")
        return

    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")

    for log in processed_logs:
        print(f"- {log}")


def mask_ip_logs():
    """
    Mã hóa địa chỉ IP trong log nguy hiểm.
    """
    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    if len(processed_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 2")
        return

    print("\n--- MÃ HÓA IP ---")

    masked_logs = []

    for log in processed_logs:
        words = log.split()

        for i in range(len(words)):
            if "." in words[i]:
                ip_parts = words[i].split(".")

                if len(ip_parts) == 4:
                    words[i] = ".".join(ip_parts[:2] + ["*", "*"])

        masked_logs.append(" ".join(words))

    print("Báo cáo log an toàn:")

    for index, log in enumerate(masked_logs, start=1):
        print(f"{index}. {log}")

    return masked_logs


def main():
    """
    Hàm điều khiển menu chính.
    """
    while True:
        print("\n============= SECURITY LOG ANALYZER =============")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            load_and_clean_logs()

        elif choice == "2":
            filter_danger_logs()

        elif choice == "3":
            mask_ip_logs()

        elif choice == "4":
            print("Đóng hệ thống thành công!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1-4!")


main()