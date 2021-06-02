from Board import Board
from choice_player import THE_players


class Game():

    def __init__(self):  # two players and board
        self.player_turn = 0
        self.player1 = None
        self.player2 = None
        self.Curr_Player = None
        self.board = Board()

    def Run(self):
        Game_mode = int(input('''
        1- Human Vs Human
        2- Human Vs AI
        3- AI Vs Human
        4- AI VS AI
        You choice ? :
        '''))
        difficulty=''
        if Game_mode>1:
            difficulty=int(input('''
            1- for easy AI
            2- for moderate AI
            3- for Hard AI
            Your choice?
            '''))
        if Game_mode>1:
            self.player1, self.player2 = THE_players(Game_mode,difficulty)
        else:
            self.player1, self.player2 = THE_players(Game_mode)
            
        self.Curr_Player = self.player1
        print(self.player1.id, self.player2.id, self.Curr_Player.id)

        while not self.board.GameOver():

            print(f"player : {self.player_turn}")
            print(self.board)
            nextMove = self.Curr_Player.choice(self.board)
            print(nextMove)
            turn_end = self.board.Move(nextMove, self.player_turn)
            # change Btween players
            if turn_end:
                self.player_turn ^= 1
                if self.player_turn == 0:
                    self.Curr_Player = self.player1
                else:
                    self.Curr_Player = self.player2
        print(self.board)
        print(self.board.who_win())
        # Todo calc the sum to the nune zero side player
        # rais the winner player
        print('end')


if __name__ == "__main__":
    game = Game()
    game.Run()
