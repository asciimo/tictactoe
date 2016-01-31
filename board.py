# -*- coding: utf-8 -*-
class Board(object):
    """
    The board cells are numbered 0-8:
    0 | 1 | 2
    - - - - -
    3 | 4 | 5
    - - - - -
    6 | 7 | 8
    """
    cells = [
        None, None, None,
        None, None, None,
        None, None, None
    ]

    test_cells = [
        None, None, None,
        None, None, None,
        'X', 'X', 'X'
    ]

    def get_board_ascii(self):
        output = ''
        for (index, cell) in enumerate(self.cells):
            if cell == None:
                output += '   '
            else:
                output += ' ' + cell + ' '

            if ((index + 1) % 3) == 0:
                if index + 1 != 9:
                    output += "\n- - - - - -\n"
            else:
                output += "|"
        return output

    def get_cells(self):
        return self.cells

    def get_winner(self):
        victory_states = self.get_victory_states()

        for state in victory_states:
            cells = set(state)
            if len(cells) == 1:
                # There is only one value in the set of cells: None, X, or Y
                value = cells.pop()
                if value in ['X', 'Y']:
                    return value

        return None

    def is_a_draw(self):
        """ If there is no winner nor any empty cells, the game is a draw """
        return not self.get_winner() and None not in self.cells

    def get_victory_states(self):
        """
        Returns the current contents of the 8 possible victory configurations
        for X or O
        """
        victory_states = [
            # rows
            self.cells[0:3],
            self.cells[3:6],
            self.cells[6:9],

            # cols
            self.cells[0::3],
            self.cells[1::3],
            self.cells[2::3],

            # diags
            self.cells[0::4],
            [self.cells[2], self.cells[3], self.cells[8]]
        ]
        return victory_states

    def is_valid_move(self, index):
        """ A move is valid if it is to an existing, empty cell """
        return (0 <= int(index) < len(self.cells)) and self.cells[int(index)] == None

    def place_move(self, marker, index):
        self.cells[index] = marker;

    def is_clear(self):
        return len(set(self.cells)) == 1

    def get_board_diagram_ascii(self):
        return ''' 0 | 1 | 2
- - - - - -
 3 | 4 | 5
- - - - - -
 6 | 7 | 8
'''
