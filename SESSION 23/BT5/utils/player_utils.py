def find_player(records, player_id):
    player_id = player_id.strip().upper()

    for index, player in enumerate(records):
        if player["player_id"] == player_id:
            return index

    return -1