rooms = int(input("Số lượng phòng học cần kiểm tra: "))
seats_per_room = int(input("Số lượng ghế trong mỗi phòng: "))
seats_per_row = int(input("Số ghế trên mỗi hàng của mỗi phòng: "))

if rooms <= 0:
    print("Số lượng phòng học không hợp lệ!")
elif seats_per_room <= 0:
    print("Số lượng ghế trong mỗi phòng không hợp lệ!")
elif seats_per_row <= 0:
    print("Số ghế trên mỗi hàng không hợp lệ!")
elif seats_per_room > 10 or seats_per_row > 10:
    print("Số lượng ghế trong mỗi phòng hoặc số ghế trên mỗi hàng không hợp lệ!")
elif seats_per_row > seats_per_room:
    print("Số ghế trên mỗi hàng không thể lớn hơn tổng số ghế trong phòng!")
else:
    for room in range(1, rooms + 1):
        print(f"Phòng {room}:")
        remaining = seats_per_room
        while remaining > 0:
            row_seats = min(seats_per_row, remaining)
            print("*" * row_seats)
            remaining -= row_seats
        print()