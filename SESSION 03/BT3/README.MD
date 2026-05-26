Input:
Mã nhân viên STR
Họ và tên nhân viên STR
Phòng ban công tác STR
Output:
dữ liệu hợp lệ: In ra Phiếu Hồ sơ Nhân sự Điện tử với đầy đủ thông tin
Nếu dữ liệu không hợp lệ in ra cảnh báo lỗi màu đỏ và không in phiếu

Giải pháp:Dùng vòng lặp for chạy đúng 3 lần 
Pseudocode
Khởi tạo vòng lặp chạy 3 lần:
    Nhập mã nhân viên
    Nhập họ tên nhân viên
    Nhập phòng ban

    Nếu mã nhân viên hoặc họ tên rỗng hoặc chỉ chứa khoảng trắng:
        In cảnh báo lỗi
        Tiếp tục sang nhân viên tiếp theo

    Ngược lại:
        In Phiếu Hồ sơ Nhân sự Điện tử với thông tin đã nhập

Kết thúc vòng lặp → In thông báo hoàn tất

