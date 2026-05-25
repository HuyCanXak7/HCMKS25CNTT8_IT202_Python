Thiết kế kiến trúc & Luồng dữ liệu:
patient_name: Họ và tên bệnh nhân (string)

patient_age: Tuổi bệnh nhân (int)

spo2_level: Nồng độ oxy trong máu (%) (int)

heart_rate: Nhịp tim (bpm) (int)

has_insurance: Có thẻ BHYT không? (string, chỉ nhận "yes" hoặc "no")
Luồng chương trình (pseudocode):

Code
START
→ Nhập họ tên, tuổi, SpO2, nhịp tim, BHYT
→ Kiểm tra dữ liệu rác (tên trống, tuổi âm, SpO2 hoặc nhịp tim âm)
   Nếu lỗi → In cảnh báo và kết thúc
→ Phân luồng y khoa:
   Nếu SpO2 < 90 hoặc nhịp tim > 120 → RED
   Elif SpO2 từ 90–95 hoặc nhịp tim 100–120 → YELLOW
   Else → GREEN
→ Tính viện phí:
   Nếu tuổi < 6 hoặc tuổi ≥ 80 → phí = 0
   Elif có BHYT = yes → phí = 250000
   Else → phí = 500000
→ In Phiếu Khám Bệnh Điện Tử (thông tin + phân luồng + viện phí)
→ In Log hệ thống (tên biến + kiểu dữ liệu)
END
Thiết kế câu hỏi input() thân thiện:

"Nhập họ tên bệnh nhân (Ví dụ: Nguyen Van A): "

"Nhập tuổi bệnh nhân (Ví dụ: 35): "

"Nhập nồng độ oxy trong máu SpO2 (%) (Ví dụ: 97): "

"Nhập nhịp tim (nhịp/phút, Ví dụ: 85): "

"Bạn có thẻ BHYT không? (Vui lòng chỉ gõ 'yes' hoặc 'no'): "