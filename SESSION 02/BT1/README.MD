Phân tích lỗi trong code cũ:
print("---- EMERGENCY TRIAGE SYSTEM ----")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

Luồng thực thi từ trên xuống dưới:
Trong Python, khi dùng if - elif - else, chương trình sẽ kiểm tra điều kiện theo thứ tự từ trên xuống. Nếu một điều kiện đúng, nó sẽ chạy khối lệnh đó và bỏ qua các khối bên dưới.

# Hệ thống phân loại ưu tiên
if heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")

Điều kiện >100 đặt trước >120. Khi nhịp tim là 135, nó thỏa mãn >100 trước, nên khối RED không bao giờ được xét đến.