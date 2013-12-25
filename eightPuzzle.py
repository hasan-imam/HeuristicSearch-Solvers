#Look for <<<...>>> tags in this file. These tags indicate changes in the 
#file to implement the required routines. Some mods have been made some others
#you have to make. Don't miss addressing each <<<...>>> tag in the file!


'''
8-Puzzle STATESPACE 

<<<8-Puzzle: 
State Space Representation: 
State space is represented as an array of 9 integers where the integer values 
equal the value of the containing tiles. If the value is 0, it means there is 
no tile in this block. The indexing starts from top-left corner and ends at the 
bottom-right corner. Index of the blank tile is also stored for ease of access.

Name of the states are defined by <tile number> -> <last movement direction>.
So the state that was reached by moving #4 left (from some other state) will 
have the name (or action value) '4->left'. This is equivalent to saying 'blank->right'
>>>8-Puzzle:

'''
from search import *

class eightPuzzle(StateSpace):

    StateSpace.n = 0
    
    def __init__(self, action, gval, state, parent = None):
        """state is supplied as a list of 9 numbers in the range [0-8]
           generate an eightPuzzle state. Create an eightPuzzle state
           object.
        
           The 9 numbers in state specify the position of the tiles in the puzzle from the
           top left corner, row by row, to the bottom right corner. E.g.:

           [2, 4, 5, 0, 6, 7, 8, 1, 3] represents the puzzle configuration

           |-----------|
           | 2 | 4 | 5 |
           |-----------|
           |   | 6 | 7 |
           |-----------|
           | 8 | 1 | 3 |
           |-----------|
           
           """
        StateSpace.__init__(self, action, gval, parent)
#<<<8-Puzzle: build your state representation from the passed data below
        self.state = state[:] # list of 9 numbers specifying tiles positions 
        self.empty = self.state.index(0) # index of the empty element
#>>>8-Puzzle: build your state representation from the passed data above

    def successors(self) :
        """Implemention of the actions of the 8-puzzle search space.
           Given the empty block, we can perform valid move-to-empty block 
           on the neighbouring tiles. Special case when the empty block is 
           adjacent to a wall. Must not return a state equal to self as this 
           is a null transition. 
           """
#<<<8-Puzzle: Your successor state function code below
#   IMPORTANT. The list of successor states returned must be in the ORDER
#   Move blank down move, move blank up, move blank right, move blank left
#   (with some successors perhaps missing if they are not available
#   moves from the current state, but the remaining ones in this  
#   order!)
        States = list() # list of successor states
        if (self.empty < 6): # can move a tile up
            newState = self.state[:]
            newState[self.empty] = newState[self.empty + 3]
            newState[self.empty + 3] = 0
            States.append(eightPuzzle(str(self.empty + 3) + "->up", self.gval + 1, newState, self))
        if (self.empty > 2): # can move a tile down
            newState = self.state[:]
            newState[self.empty] = newState[self.empty - 3]
            newState[self.empty - 3] = 0
            States.append(eightPuzzle(str(self.empty - 3) + "->down", self.gval + 1, newState, self))
        if (self.empty % 3 != 2): # can move a tile left
            newState = self.state[:]
            newState[self.empty] = newState[self.empty + 1]
            newState[self.empty + 1] = 0
            States.append(eightPuzzle(str(self.empty + 1) + "->left", self.gval + 1, newState, self))
        if (self.empty % 3 != 0): # can move a tile right
            newState = self.state[:]
            newState[self.empty] = newState[self.empty - 1]
            newState[self.empty - 1] = 0
            States.append(eightPuzzle(str(self.empty - 1) + "->right", self.gval + 1, newState, self))
        return States
#>>>8-Puzzle: Your successor state function code above
    
    def hashable_state(self) :
#<<<8-Puzzle: your hashable_state implementation below
        hash_value = 0
        for j in enumerate(self.state):
            hash_value = hash_value * 10 + j[1]
        return hash_value
#>>>8-Puzzle: your hashable_state implementation above

    def print_state(self):
#         if self.parent:
#             print "Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index)
#         else:
#             print "Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval)
#         print "|-------------|"
#         line = ""
#         for i,j in enumerate(self.state):
#             line = line + "| " + str(j) + " |"
#             if (i % 3 == 2):
#                 line = line + "\n"
#         print line + "|-------------|"
        return None        

#<<<8-Puzzle: below you will place your implementation of the misplaced 
#tiles heuristic and the manhattan distance heuristic
#You can alter any of the routines below to aid in your implementation. 
#However, mark all changes between 
#<<<8-Puzzle ... and >>>8-Puzzle tags.
#>>>8-Puzzle

eightPuzzle.goal_state = False

def eightPuzzle_set_goal(state):
    '''set the goal state to be state. Here state is a list of 9
       numbers in the same format as eightPuzzle.___init___'''
    eightPuzzle.goal_state = state
#<<<8-Puzzle: store additional information if wanted below

#>>>8-Puzzle: store additional information if wanted above

def eightPuzzle_goal_fn(state):
#Assume that the goal is a fully specified state.
#<<<8-Puzzle: your implementation of the goal test function below
    for i,j in zip(state.state, state.goal_state):
        if (i != j):
            return False
    return True
#>>>8-Puzzle: your implementation of the goal test function above

def h0(state):
    #a null heuristic (always returns zero)
    return 0

def h_misplacedTiles(state):
    '''Given a state returns the number of
    tiles (NOT INCLUDING THE BLANK!) in that state that are
    not in their goal position'''
    h = 0
    for i,j in zip(state.state, state.goal_state):
        # Count all misplaced tiles except blank (0)
        if (j != 0 and i != j):
            h = h + 1
    return h
    
def h_MHDist(state):
    '''Given a state returns the sum of the manhattan distances of each 
    tile (NOT INCLUDING THE BLANK), the distance each tile is from its 
    goal configuration. The manhattan distance of a tile that is currently 
    in row i column j and that has to be in row i" j" in the goal is 
    defined to be abs(i - i") + abs(j - j")'''
    h = 0
    for i,j in zip(state.state, state.goal_state):
        if (j != 0 and i != j):
            h = h + abs(state.goal_state.index(i)//3 - state.state.index(i)//3) \
                + abs(state.goal_state.index(i)%3 - state.state.index(i)%3)
    return h
#>>>8-Puzzle: your implementation of this function above

#<<<8-Puzzle: Make sure the sample code below works when it is uncommented

# se = SearchEngine('astar', 'none')
# s0 = eightPuzzle("START", 0, [1, 0, 2, 3, 4, 5, 6, 7, 8])
# eightPuzzle_set_goal([0, 1, 2, 3, 4, 5, 6, 7, 8])

# print '1'
# se.search(s0, eightPuzzle_goal_fn, h0)

# print '2'
# se.search(s0, eightPuzzle_goal_fn, h_misplacedTiles)

# print '3'
# s1 = eightPuzzle("START", 0, [8, 7, 6, 0, 4, 1, 2, 5, 3])
# se.search(s1, eightPuzzle_goal_fn, h_MHDist)

# print '4'
# se.set_strategy('astar', 'full')
# se.search(s1, eightPuzzle_goal_fn, h_MHDist)

## Note that this problem can take a long time...30 seconds of CPU on my mac-mini.
# print '5'
# se.search(s1, eightPuzzle_goal_fn, h_misplacedTiles)


#>>>8-Puzzle: Make sure the sample code above works when it is uncommented


