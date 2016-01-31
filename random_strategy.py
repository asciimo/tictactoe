# -*- coding: utf-8 -*-
import sys
import random
import strategy

class RandomStrategy(strategy.Strategy):
    """
    This strategy chooses a move randomly
    """
    def move(self, Board):
        cells = Board.get_cells()
        # Compile a list of the indexes of empty Board cells
        empty_cells = []
        for (index, cell) in enumerate(cells):
            if cell == None:
                empty_cells.append(index)
        if len(empty_cells) > 0:
            # Pick a random cell
            return random.choice(empty_cells)

        sys.exit("The board is full. ¯\_(ツ)_/¯")
