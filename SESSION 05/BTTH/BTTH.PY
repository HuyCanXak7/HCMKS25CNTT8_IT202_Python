so_nv = int(input("Nhập số lượng nhân viên: "))
for i in range(1, so_nv + 1):
    print(f"\n--- Nhân viên {i} ---")
    ten = input("Nhập tên nhân viên: ")
    ngay_lam = int(input("Nhập số ngày làm việc (0-22): "))
    if ngay_lam < 0 or ngay_lam > 22:
        print("Dữ liệu không hợp lệ")
        continue
    if ngay_lam == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
    print("Biểu đồ ngày làm việc:")

    for j in range(1): 
        for k in range(ngay_lam): 
            print("*", end="")
    print()
    if ngay_lam >= 18:
        print("Làm việc chăm chỉ")
    elif ngay_lam < 10:
        print("Làm việc ít")
    else:
        print("Làm việc bình thường")