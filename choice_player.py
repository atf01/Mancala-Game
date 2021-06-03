from Players import Human_player, AI_player


def THE_players(Game_mode):
    if Game_mode == 1:
        print('Human _ Human Mode')
        Player_1, Player_2 = Human_player(0), Human_player(1)

    elif Game_mode == 2:
        print('Human _ Ai Mode')
        Player_1, Player_2 = Human_player(0), AI_player(1,2)

    elif Game_mode == 3:
        print('Ai _ Human Mode')
        Player_1, Player_2 = AI_player(0,2), Human_player(1)

    elif Game_mode == 4:
        print('Ai _ Ai Mode')
        Player_1, Player_2 = AI_player(0, 3), AI_player(1,4)
    return Player_1, Player_2

# test
# if __name__ == "__main__":
#   Player_1, Player_2 = THE_players(4)
#   print(type(Player_1))
#   print(type(Player_2))
