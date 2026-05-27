def main():
    total_revenue  = 0
    count_target = 0
    target_revenue = []

    for i in range(1, 8):
        while True:
            try:
                value = int(input(f"Ngày {i}: "))
                break
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập số nguyên.")

        target_revenue.append(value)
        total_revenue += value
        if value >= 5000000:
            count_target += 1

    average = total_revenue / 7

    print("BÁO CÁO DOANH THU TUẦN")
    print("Tổng doanh thu tuần:", total_revenue)
    print("Doanh thu trung bình mỗi ngày:", average)
    print("Số ngày đạt doanh thu mục tiêu (>=5,000,000):", count_target)
