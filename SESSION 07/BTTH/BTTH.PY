raw_input = "   nGuyen vaN aN  ;  2004   "

menu = {}
print("===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
menu ['1'] = "Hiển thị chuỗi dữ liệu gốc"
menu ['2'] = "Chuẩn Hóa họ tên và tính tuổi"
menu ['3'] = "Tạo mã ID và Email tự động"
menu ['4'] = "Thoát chương trình"
while True:
    print("=======================================")
    for key in menu:
        print(key, ":", menu[key])
    choice = input("Nhập lựa chọn của bạn: ")
    if choice == '1':
        print("Chuỗi dữ liệu gốc:", raw_input)
    elif choice == '2':
        # Chuẩn hóa họ tên
        name_part = raw_input.split(';')[0].strip()
        name_parts = name_part.split()
        standardized_name = ' '.join([part.capitalize() for part in name_parts])
        
        # Tính tuổi
        birth_year = int(raw_input.split(';')[1].strip())
        current_year = 2024
        age = current_year - birth_year
        
        print("Họ tên chuẩn hóa:", standardized_name)
        print("Tuổi:", age)
    elif choice == '3':
        # Tạo mã ID và Email tự động
        name_part = raw_input.split(';')[0].strip()
        name_parts = name_part.split()
        
        # Mã ID: lấy chữ cái đầu của họ và tên, cộng với năm sinh
        id_code = name_parts[0][0].upper() + name_parts[-1][0].upper() + str(raw_input.split(';')[1].strip())
        
        # Email: lấy tên viết liền không dấu, cộng với năm sinh và "@example.com"
        email = ''.join(name_parts).lower() + str(raw_input.split(';')[1].strip()) + "@example.com"
        
        print("Mã ID tự động:", id_code)
        print("Email tự động:", email)
    elif choice == '4':
        print("Thoát chương trình. Hẹn gặp lại!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
