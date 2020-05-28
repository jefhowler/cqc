# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'

class Rat:
    """ A rat caught in a maze."""

    # Write your Rat methods here.
    def __init__(self, rat_sym, row, column):

        """
        (Rat, str, int, int) -> NoneType
        >>> rod = Rat(RAT_1_CHAR, 2, 3)
        >>> rod.rat_sym
        'J'
        >>> rod.row
        2
        >>> rod.column
        3
        >>> rod.num_sprouts_eaten
        0
        """

        self.rat_sym = rat_sym
        self.row = row
        self.column = column
        self.num_sprouts_eaten = 0

    def set_location(self, row, column):
        """
        (Rat, int, int) -> NoneType
        >>> rodney = Rat('R', 3, 4)
        >>> rodney.set_location(5, 6)
        >>> rodney.row
        5
        >>> rodney.column
        6

        """
        self.row = row
        self.column = column

    def eat_sprout(self):
        """
        (Rat) -> NoneType
        >>> rod = Rat('R', 2, 3)
        >>> rod.eat_sprout()
        >>> rod.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        (Rat) -> str
        >>> rod = Rat(RAT_1_CHAR, 2, 3)
        >>> rod.eat_sprout()
        >>> rod.eat_sprout()
        >>> str(rod)
        'J at (2, 3) ate 2 sprouts'
        """
        return self.rat_sym + ' at ({0}, {1}) ate {2} sprouts'.format(str(self.row), str(self.column), str(self.num_sprouts_eaten))


class Maze:
    """ A 2D maze. """


    # Write your Maze methods here.


    def __init__(self, maze_contents, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType
        >>> maze_1 = Maze(
                [
                    ['#', '#', '#', '#', '#', '#', '#'],
                    ['#', '.', '.', '.', '.', '.', '#'],
                    ['#', '.', '#', '#', '#', '.', '#'],
                    ['#', '.', '.', '@', '#', '.', '#'],
                    ['#', '@', '#', '.', '@', '.', '#'],
                    ['#', '#', '#', '#', '#', '#', '#']
                ], Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze_1.rat_1.row
        1
        >>> maze_1.rat_2.column
        4
        >>> maze_1.num_sprouts_left
        3
        """
        self.maze_contents = maze_contents
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0
        for list in self.maze_contents:
            for char in list:
                if char == SPROUT:
                    self.num_sprouts_left += 1

    def is_wall(self, row, column):
        """(Maze, int, int) -> bool
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
                           ['#', '.', '.', '.', '.', '.', '#'],
                           ['#', '.', '#', '#', '#', '.', '#'],
                           ['#', '.', '.', '@', '#', '.', '#'],
                           ['#', '@', '#', '.', '@', '.', '#'],
                           ['#', '#', '#', '#', '#', '#', '#']],
                          Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze_1.is_wall(0, 2)
        True
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
                           ['#', '.', '.', '.', '.', '.', '#'],
                           ['#', '.', '#', '#', '#', '.', '#'],
                           ['#', '.', '.', '@', '#', '.', '#'],
                           ['#', '@', '#', '.', '@', '.', '#'],
                           ['#', '#', '#', '#', '#', '#', '#']],
                          Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze_1.is_wall(1, 2)
        False
        """
        return self.maze_contents[row][column] == WALL

    def get_character(self, row, column):
        """
        (Maze, int, int) -> str
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
                           ['#', '.', '.', '.', '.', '.', '#'],
                           ['#', '.', '#', '#', '#', '.', '#'],
                           ['#', '.', '.', '@', '#', '.', '#'],
                           ['#', '@', '#', '.', '@', '.', '#'],
                           ['#', '#', '#', '#', '#', '#', '#']],
                          Rat('J', 1, 1), Rat('P', 1, 4))
        >>> maze_1.get_character(2, 3)
        '#'
        >>> maze_1.get_character(1, 4)
        'P'
        """
        if self.rat_1.row == row and self.rat_1.column == column:
            return RAT_1_CHAR
        elif self.rat_2.row == row and self.rat_2.column == column:
            return RAT_2_CHAR
        else:
            return self.maze_contents[row][column]

    def move(self, rat, vertical_change, horizontal_change):
        """
        (self, rat, int, int) -> Bool
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
                           ['#', '.', '.', '.', '.', '.', '#'],
                           ['#', '.', '#', '#', '#', '.', '#'],
                           ['#', '.', '.', '@', '#', '.', '#'],
                           ['#', '@', '#', '.', '@', '.', '#'],
                           ['#', '#', '#', '#', '#', '#', '#']],
                          Rat('J', 3, 1), Rat('P', 1, 4))
        >>> maze_1.move(Rat('J', 3, 1),DOWN, NO_CHANGE)
        True
        >>> maze_1.num_sprouts_left
        2
        >>> maze_1.rat_1.row
        4
        >>> maze_1.rat_1.column
        1
        >>> maze_1.move(Rat('J', 4, 1),NO_CHANGE, LEFT)
        False
        >>> rat.row
        4
        >>> rat.column
        1
        """
        if rat.rat_sym == self.rat_1.rat_sym:
            rat = self.rat_1
        elif rat.rat_sym == self.rat_2.rat_sym:
            rat = self.rat_2
        else:
            return 'your rat is unknown'
        new_row = rat.row + vertical_change
        new_column = rat.column + horizontal_change
        new_location = self.maze_contents[new_row][new_column]
        if self.is_wall(new_row, new_column):
            rat.row = rat.row
            rat.column = rat.column

        elif new_location == SPROUT:
            rat.eat_sprout()
            self.num_sprouts_left
            self.num_sprouts_left -= 1
            new_location = HALL
            rat.set_location(new_row, new_column)
            return True
        else:
            rat.set_location(new_row, new_column)
            return True

    def __str__(self):
        """
        (Maze) -> NoneType
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'],
                           ['#', '.', '.', '.', '.', '.', '#'],
                           ['#', '.', '#', '#', '#', '.', '#'],
                           ['#', '.', '.', '@', '#', '.', '#'],
                           ['#', '@', '#', '.', '@', '.', '#'],
                           ['#', '#', '#', '#', '#', '#', '#']],
                          Rat('J', 3, 1), Rat('P', 1, 4))
        >>> str(maze_1)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        rows_string = ''
        row_string = ''
        for row in self.maze_contents:
            for char in row:
                row_string += char
            row_string += '\n'
            rows_string += row_string
            row_string = ''
#        rows_string += str(self.rat_1) + '\n' + str(self.rat_2)
        return rows_string + str(self.rat_1) + '\n' + str(self.rat_2)
