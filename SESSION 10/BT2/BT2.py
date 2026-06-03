playlist = []
def show_menu():
    print("========== MENU QUẢN LÝ DANH SÁCH PHÁT ==========")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và Trích xuất danh sách")
    print("5. Thoát chương trình")
    print("===============================================")


def view_playlist():
    if len(playlist) == 0:
        print("Danh sách phát hiện đang trống!")
        return
    print("\n--- DANH SÁCH PHÁT ---")
    i = 1
    for song in playlist:
        print(str(i) + ". " + song)
        i += 1
    print("Tổng số bài hát: " + str(len(playlist)))


def add_song():
    print("\n--- THÊM BÀI HÁT ---")
    print("1. Thêm vào cuối danh sách")
    print("2. Chèn vào vị trí cụ thể")
    choice = input("Nhập lựa chọn: ").strip()
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
        return
    choice = int(choice)
    song_name = input("Nhập tên bài hát: ").strip()
    if song_name == "":
        print("Tên bài hát không được để trống.")
        return
    if choice == 1:
        playlist.append(song_name)
        print("Đã thêm bài hát '" + song_name + "' vào cuối danh sách.")
        print("Số lượng bài hát hiện tại: " + str(len(playlist)))
    elif choice == 2:
        pos = input("Nhập vị trí cần chèn: ").strip()
        if not pos.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            return
        pos = int(pos)
        if pos < 1 or pos > len(playlist) + 1:
            print("Vị trí không hợp lệ.")
            return
        playlist.insert(pos - 1, song_name)
        print("Đã chèn bài hát '" + song_name + "' vào vị trí " + str(pos) + ".")
        print("Số lượng bài hát hiện tại: " + str(len(playlist)))
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")


def delete_song():
    if len(playlist) == 0:
        print("Danh sách phát hiện đang trống!")
        return
    print("\n--- XÓA BÀI HÁT ---")
    print("1. Xóa theo tên bài hát")
    print("2. Xóa theo số thứ tự")
    choice = input("Nhập lựa chọn: ").strip()
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
        return
    choice = int(choice)
    if choice == 1:
        song_name = input("Nhập tên bài hát cần xóa: ").strip()
        if song_name in playlist:
            playlist.remove(song_name)
            print("Đã xóa bài hát '" + song_name + "' khỏi danh sách.")
        else:
            print("Không tìm thấy bài hát trong danh sách phát.")
    elif choice == 2:
        pos = input("Nhập số thứ tự bài hát cần xóa: ").strip()
        if not pos.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            return
        pos = int(pos)
        if pos < 1 or pos > len(playlist):
            print("Vị trí không hợp lệ.")
            return
        removed = playlist.pop(pos - 1)
        print("Đã xóa bài hát '" + removed + "' khỏi danh sách.")
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")


def sort_extract():
    if len(playlist) == 0:
        print("Danh sách phát hiện đang trống!")
        return
    print("\n--- SẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH ---")
    print("1. Sắp xếp danh sách phát theo bảng chữ cái A-Z")
    print("2. Hiển thị 3 bài hát đầu tiên")
    choice = input("Nhập lựa chọn: ").strip()
    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
        return
    choice = int(choice)
    if choice == 1:
        playlist.sort()
        print("Danh sách đã được sắp xếp theo bảng chữ cái A-Z.")
        view_playlist()
    elif choice == 2:
        print("\n--- 3 BÀI HÁT ĐẦU TIÊN ---")
        max_show = 3
        if len(playlist) < 3:
            max_show = len(playlist)
        i = 0
        while i < max_show:
            print(str(i + 1) + ". " + playlist[i])
            i += 1
        print("Tổng số bài hát trong danh sách: " + str(len(playlist)))
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")


def main():
    while True:
        show_menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()
        if not choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
            continue
        choice = int(choice)
        if choice == 1:
            add_song()
        elif choice == 2:
            view_playlist()
        elif choice == 3:
            delete_song()
        elif choice == 4:
            sort_extract()
        elif choice == 5:
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")


main()
