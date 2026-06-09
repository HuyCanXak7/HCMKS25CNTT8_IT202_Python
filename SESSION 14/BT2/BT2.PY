# Tổng điểm hiện tại của khách hàng
total_points = 100

# Hàm cộng điểm thưởng
def add_reward_points(current_points, points_earned):
    print("Đã cộng thêm", points_earned, "điểm.")
    return current_points + points_earned

# Khách mua hàng được thưởng 50 điểm
total_points = add_reward_points(total_points, 50)

# In kết quả
print("Tổng điểm hiện tại của khách hàng:", total_points)