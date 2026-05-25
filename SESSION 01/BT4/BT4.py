def nhap_du_lieu():
    ma_bn = input("Nhập mã bệnh nhân: ")
    try:
        nhiet_do = float(input("Nhập nhiệt độ cơ thể (°C): "))
    except ValueError:
        print("Lỗi: Nhiệt độ phải là số thực (ví dụ: 37.5)")
        return
    
    try:
        nhip_tim = int(input("Nhập nhịp tim (nhịp/phút): "))
    except ValueError:
        print("Lỗi: Nhịp tim phải là số nguyên (ví dụ: 85)")
        return

    print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
    print(f"Mã bệnh nhân: {ma_bn}")
    print(f"Nhiệt độ cơ thể: {nhiet_do} độ C")
    print(f"⇒ Kiểu dữ liệu hệ thống ghi nhận: {type(nhiet_do)}")
    print(f"Nhịp tim: {nhip_tim} nhịp/phút")
    print(f"⇒ Kiểu dữ liệu hệ thống ghi nhận: {type(nhip_tim)}")
    print("-------------------------------------")
    print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")

if __name__ == "__main__":
    nhap_du_lieu()
