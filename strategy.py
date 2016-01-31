
class Strategy(object):

    def move(self, Board):
        """
        The stragegy prefers
        1. The center square and squares adjacent to it on its first move.
        2. After that, it tries to fill rows, columns, and diagonals that have Os in them.
        3. If it can't find any candidates, it pics a random empty cell
        """
        victory_states = Board.get_victory_states()

        if Board.is_clear():
            return 4;

        if self.block_opponent(victory_states):
            return True

        # Win; look for rows, cols, diags that have 2 Os in them
        if self.winning_move(victory_states):
            return True

        # Look for rows, cols, diags that have 1 O in them already
        if self.road_to_victory(victory_states):
            return True

        # Pick an open corner
        if self.corner(victory_states):
            return True

        # Pick a random empty cell
        if self.random(victory_states):
            return True

        return False

    def block_opponent(self, victory_states):
        """ Block oppnent's win; look for rows, cols, diags that have 2 Xs in them """
