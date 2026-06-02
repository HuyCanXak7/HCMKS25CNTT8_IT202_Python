account_name = ""
video_title = ""
video_description = ""
hashtags = []

while True:
    print("\n===== MENU =====")
    print("1. Nhập dữ liệu và xem báo cáo")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")
    choice = input("Nhập lựa chọn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)
    if choice < 1 or choice > 5:
        print("Lựa chọn phải từ 1 đến 5")
        continue

    if choice == 1:

        account_name = input("Nhập tên tài khoản: ")

        if account_name.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        video_title = input("Nhập tiêu đề video: ")
        video_description = input("Nhập mô tả video: ")

        if video_description.strip() == "":
            print("Mô tả video không được rỗng")
            continue

        hashtag_input = input("Nhập hashtag (cách nhau bởi dấu phẩy): ")

        account_name = account_name.strip()
        video_title = video_title.strip().title()
        video_description = video_description.strip()

        hashtags = []

        for tag in hashtag_input.split(","):
            tag = tag.strip()
            if tag != "":
                hashtags.append(tag)

        print("\n===== BÁO CÁO =====")
        print("Tên tài khoản:", account_name)
        print("Tiêu đề:", video_title)
        print("Mô tả:", video_description)
        print("Độ dài mô tả:", len(video_description))
        print("Số lượng từ:", len(video_description.split()))
        print("Danh sách hashtag:", ", ".join(hashtags))
        print("Số lượng hashtag:", len(hashtags))
        print("Mô tả chữ thường:", video_description.lower())
        print("Mô tả chữ hoa:", video_description.upper())

    elif choice == 2:

        if account_name == "":
            account_name = input("Nhập tên tài khoản: ")

        if account_name.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        normalized_name = "@" + account_name.strip().lower()

        print("Tên ban đầu:", account_name)
        print("Tên chuẩn hóa:", normalized_name)

    elif choice == 3:

        hashtag = input("Nhập hashtag: ").strip()

        if hashtag == "":
            print("Hashtag không được rỗng")

        elif not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng #")

        elif " " in hashtag:
            print("Hashtag không được chứa khoảng trắng")

        elif len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự")

        else:

            valid = True

            for char in hashtag[1:]:

                if not(char.isalnum() or char == "_"):
                    valid = False
                    break

            if valid:
                print("Hashtag hợp lệ")
                hashtags.append(hashtag)
                print("Đã thêm vào danh sách hashtag")
            else:
                print("Hashtag chỉ chứa chữ, số hoặc dấu _")

    elif choice == 4:

        if video_description.strip() == "":
            print("Chưa có mô tả video")
            continue

        old_keyword = input("Nhập từ khóa cần tìm: ")
        new_keyword = input("Nhập từ khóa thay thế: ")

        if old_keyword in video_description:

            count = video_description.count(old_keyword)
            replaced_description = video_description.replace(old_keyword, new_keyword)

            print("Mô tả sau thay thế:", replaced_description)
            print("Số lần xuất hiện:", count)

        else:
            print("Không tìm thấy từ khóa")

    elif choice == 5:
        print("Thoát chương trình")
        break