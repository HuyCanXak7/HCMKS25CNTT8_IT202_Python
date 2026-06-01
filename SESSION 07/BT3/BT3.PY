# HNKS25CNTT1_Python_Session01_Ex01

raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

def parse_raw_data(raw_data):
    employees = []
    records = raw_data.split("|")
    for record in records:
        fields = record.strip().split(";")
        if len(fields) != 4:
            continue
        emp_id = fields[0].strip().upper()
        name = fields[1].strip().title()
        phone = fields[2].strip().replace("-", "")
        dept = fields[3].strip().upper()

        # xử lý số điện thoại
        if phone.isdigit():
            phone = "******" + phone[6:]
        else:
            phone = "Invalid Format"

        employees.append({
            "ID": emp_id,
            "Name": name,
            "Phone": phone,
            "Dept": dept
        })
    return employees

def print_report(employees):
    print(f"{'ID':<10}{'Name':<20}{'Phone':<20}{'Dept':<10}")
    print("-" * 60)
    for emp in employees:
        print(f"{emp['ID']:<10}{emp['Name']:<20}{emp['Phone']:<20}{emp['Dept']:<10}")

def search_employee(employees, emp_id):
    emp_id = emp_id.strip().upper()
    for emp in employees:
        if emp["ID"] == emp_id:
            print("Thông tin nhân viên:")
            print(f"ID: {emp['ID']}")
            print(f"Họ tên: {emp['Name']}")
            print(f"SĐT: {emp['Phone']}")
            print(f"Phòng ban: {emp['Dept']}")
            return
    print("Không tìm thấy nhân viên")

def main():
    employees = parse_raw_data(raw_data)
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
        print("1. Hiển thị chuỗi dữ liệu gốc")
        print("2. Chuẩn hóa dữ liệu và in báo cáo")
        print("3. Tìm kiếm nhân viên theo mã ID")
        print("4. Thoát chương trình")

        choice = input("Nhập lựa chọn: ")
        if not choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            continue

        choice = int(choice)
        if choice == 1:
            print("\nDữ liệu gốc:")
            print(raw_data)
        elif choice == 2:
            print("\nBáo cáo nhân sự:")
            print_report(employees)
        elif choice == 3:
            emp_id = input("Nhập mã nhân viên cần tìm: ")
            search_employee(employees, emp_id)
        elif choice == 4:
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    main()
