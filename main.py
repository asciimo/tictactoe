# -*- coding: utf-8 -*-
import sys
import re
import board
import random_strategy

class Game(object):
    """
    This is the main game resource, responsible for handling the game loop,
    user input, computer moves, and victory status.
    """
    Board = None
    Strategy = None

    running = False

    def __init__(self):
        self.Board = board.Board()
        self.Strategy = random_strategy.RandomStrategy()

    def start(self):
        """ Start the main game loop. User is X, Computer is O """
        self.running = True
        while(self.running):
            self.draw_board()

            user_input = self.get_user_input()

            if not self.check_for_valid_input(user_input):
                print "Invalid input. Please try again."
                continue

            if self.check_for_quit(user_input):
                print "Thanks for playing!"
                sys.exit()

            if self.check_for_help(user_input):
                continue

            if not self.apply_user_move(user_input):
                print "That is an invalid move."
                continue

            self.check_for_victory()
            self.check_for_draw()
            self.apply_computer_move(self.Strategy.move(self.Board))
            self.check_for_victory()
            self.check_for_draw()

    def draw_board(self):
        print self.Board.get_board_ascii()

    def get_user_input(self):
        return raw_input('0-8 H)elp Q)uit: ').strip()

    def check_for_valid_input(self, user_input):
        """ Check to make sure the raw input is valid. Moves are validated later """
        valid_pattern = '^[0-8,h,H,q,Q]$'
        return re.match(valid_pattern, user_input)

    def check_for_quit(self, user_input):
        if(user_input in ['Q', 'q']):
            return True

    def check_for_help(self, user_input):
        if(user_input in ['H', 'h']):
            print 'Choose the number corresponding to your desired move:'
            print self.Board.get_board_diagram_ascii()
            return True

    def apply_user_move(self, input):
        """ Validate the user's move and update the board """
        cell_index = int(input)
        if self.Board.is_valid_move(cell_index):
            self.Board.place_move('X', cell_index)
            return True
        return False

    def apply_computer_move(self, input):
        cell_index = int(input)
        self.Board.place_move('O', cell_index)

    def check_for_victory(self):
        if self.Board.get_winner() != None:
            # Show the board before exiting
            print self.Board.get_board_ascii()
            print self.Board.get_winner() + ' won!'
            sys.exit()

    def check_for_draw(self):
        if self.Board.is_a_draw() == True:
            # Show the board before exiting
            print self.Board.get_board_ascii()
            print "It's a darw!"
            sys.exit()

    def stop(self):
        """ Cause the main game loop to stop """
        self.running = False
        print('Quitting')


Game = Game()
Game.start()
