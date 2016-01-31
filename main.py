import sys
import board
import strategy

class Game(object):

    Board = None
    Strategy = None

    running = False

    def __init__(self):
        self.Board = board.Board()
        self.Strategy = Strategy()

    def start(self):
        """ Start the main game loop. User is X, Computer is O """
        self.running = True
        while(self.running):
            self.draw_board()
            user_input = self.get_user_input()
            self.check_for_quit(user_input)
            self.apply_user_move(user_input)
            self.check_for_victory()
            self.apply_computer_move(self.Strategy.move(self.Board))
            self.check_for_victory()

    def draw_board(self):
        self.Board.draw()

    def get_user_input(self):
        return raw_input('Q)uit ').strip()

    def check_for_quit(self, user_input):
        if(user_input == 'Q'):
            sys.exit()

    def apply_user_move(self, input):
        """ Validate the user's move and update the board """
        if self.Board.is_valid_move(input):
            self.Board.place_move('X', input)

    def apply_computer_move(self, input):
        self.Board.place_move('Y', input)

    def check_for_victory(self):
        if self.Board.has_victory_state():
            print "Someone won!"
            sys.exit()

    def stop(self):
        """ Cause the main game loop to stop """
        self.running = False
        print('Quitting')


Game = Game()
Game.start()
