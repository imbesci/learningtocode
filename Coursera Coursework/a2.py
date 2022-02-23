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
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col, num_sprouts_eaten=0):
        ''' (Rat, str, int, int, int) -> NoneType

        A constructor variable for the class rat including the one
        character name, row position, column positon and number of sprouts
        eaten (score) for the Rat.

        Precondition: len(self.name)== 1
        ''' 

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten

    def set_location(self, newrow, newcol):
        '''(Rat, int, int) -> NoneType
        Set the new location of the Rat on the board using new row and
        new column numbers'''

        self.row = newrow
        self.col = newcol
        
    def eat_sprout(self):
        '''(Rat) -> NoneType

         Increase the number of sprouts eaten by one'''
        
        self.num_sprouts_eaten += 1


    def __str__(self):
        '''(Rat) -> NoneType

        The print output format for class Rat'''

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol,
            self.row, self.col, self.num_sprouts_eaten)


    
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2, num_sprouts_left=0):
        '''(Maze, list of list of str, Rat, Rat, int) -> NoneType

        A constructor variable for a maze with length of the length of each
        list in mazeorder, and the width defined by the number of lists
        in mazeorder. Also contained is the location of both rat_1 and rat_2.
        '''

        self.maze = maze
        
        total = 0
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] == SPROUT:
                    total += 1

        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = total
    
    def is_wall(self, row, col):
        '''(Rat, int, int)-> bool

        Return the boolean if the location in the maze is a wall (#) when
        given the row and col coordinates.
        '''

        return self.maze[row][col] == WALL


    def get_character(self, row, col):
        '''(Maze, int, int) -> str

        Return the character at a particular position in the maze. If a rat is positioned
        at the specificied row and col, return the Rat letter.
        '''

        ##Check to see if a rat is there first

        if ((row, col) == (self.rat_1.row, self.rat_1.col)):
            return RAT_1_CHAR
            
        elif ((row, col) == (self.rat_2.row, self.rat_2.col)):
            return RAT_2_CHAR
                           
        #If no rats there, find the character

        s = self.maze[row][col]

        if s == WALL:
            return '#'
        elif s == HALL:
            return '.'
        elif s == SPROUT:
            return '@'
                
    def move(self, rat, rowchange, colchange):
        '''(Maze, Rat, int, int) -> bool

        Move the rat in the given rowchange and colchange directions. If a brussel sprout is present:
        Eat the brussel sprout, have the rat eat the SPROUT, mutate the sprout into a HALL, decrease the maze sprouts quantity by 1.
        If the directional change does not move the rat into a wall, return True.
        
        '''

        currentrow =  rat.row
        currentcol =  rat.col
        nextrow = currentrow + rowchange
        nextcol = currentcol + colchange
        char = self.get_character(nextrow, nextcol)

        if char == WALL:
            return False
        elif char == SPROUT:
            rat.eat_sprout()
            self.num_sprouts_left -= 1
            self.maze[nextrow][nextcol] = HALL
            rat.set_location(nextrow, nextcol)
            return True
        elif char == HALL:
            rat.set_location(nextrow, nextcol)
            return True

    def __str__(self):
        '''(Maze) -> str
        Configure the print function output for class Maze. '''

        maze2 = []

        for i in range(len(self.maze)):
            x = list(tuple(self.maze[i]))
            maze2.append(x)

        maze2[self.rat_1.row][self.rat_1.col] = RAT_1_CHAR
        maze2[self.rat_2.row][self.rat_2.col] = RAT_2_CHAR
        s= ''
        for i in range(len(maze2)):
            s = s + ''.join(maze2[i]) + '\n'
        
        return s + '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.rat_1.symbol, self.rat_1.row, self.rat_1.col, self.rat_1.num_sprouts_eaten) + '\n' + '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.rat_2.symbol, self.rat_2.row, self.rat_2.col, self.rat_2.num_sprouts_eaten)
