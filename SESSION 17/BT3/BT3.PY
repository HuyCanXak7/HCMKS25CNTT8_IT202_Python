import itertools

teams_list = []
match_schedule = []

def input_teams():
    global teams_list

    print("\n--- NHẬP DANH SÁCH ---")
    teams = input("Nhập các đội (cách nhau bởi dấu phẩy): ")

    teams = [team.strip().upper() for team in teams.split(",") if team.strip()]

    unique_teams = []
    for team in teams:
        if team not in unique_teams:
            unique_teams.append(team)

    teams_list = unique_teams

    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")

def create_schedule():
    global match_schedule

    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")

    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return

    matches = itertools.combinations(teams_list, 2)

    match_schedule = [f"{team1} vs {team2}" for team1, team2 in matches]

    for index, match in enumerate(match_schedule, start=1):
        print(f"{index}. {match}")

    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")

def generate_match_ids():
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    if not match_schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    for index, match in enumerate(match_schedule, start=1):
        team1, team2 = match.split(" vs ")

        code1 = f"{team1[:3]:X<3}"
        code2 = f"{team2[:3]:X<3}"

        match_id = f"M{index:02d}-{code1}-{code2}"

        print(f"Trận {index} ({match}) -> ID: {match_id}")

def main():
    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động")
        print("4. Đóng hệ thống")
        print("==============================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            input_teams()

        elif choice == "2":
            create_schedule()

        elif choice == "3":
            generate_match_ids()

        elif choice == "4":
            print("Đóng hệ thống. Hẹn gặp lại!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-4!")

main()