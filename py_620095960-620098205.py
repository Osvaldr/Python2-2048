import gui
import random
from copy import deepcopy

"""
2048 Game
Please read the comments to help clear up any confusion about what the purpose of the various variables are

Before submitting ensure to edit this comment block to include the ID numbers of both group members
Group Member:620095960
Group Member:620098205
"""
#Problem 1 - Give Representation
grid = [[0 for c in range(4)] for r in range(4)]

#Problem 2 - Returns List of Empty Slots
def empty_slots():
    return [(grid.index(i),c) for i in grid for c in range(4) if i[c]==0]

#Problem 3 - Returns a Random Empty Slot Position
def random_position():
    return random.choice(empty_slots())

#Problem 4 - Adds a random number to the Game Board
def add_random_number(game_board):
    r,c = random_position()
    key = "Tile number " + str(helper['count'])
    rand_num = gui.random_number()
    gui.put(game_board, key, rand_num,r,c)
    helper['count']+=1
    grid[r][c] = rand_num.value ## updates the slot value to appropriate number value
    return (r,c)

#Problem 5 - Returns the Unique Identifier for a given Slot Position with a Number
def find_identifier(game_board,r,c):
    for key in board.numbers.keys():
        if board.numbers[key] == (r,c):
            return key
     
# Values to represent the directions the tiles could move
UP= 1
DOWN = 2
RIGHT = 3
LEFT = 4

#Problem 6 - Updates the grid after a tile as been moved
def update_grid(r,c,d):
    if grid[r][c]!=0:
        if d == 1 and r!=0:
            if grid[r-1][c]==grid[r][c]:
                grid[r-1][c]+=grid[r][c]
                grid[r][c]=0
                return (r-1,c)
            elif grid[r-1][c]==0:
                grid[r-1][c]=grid[r][c]
                grid[r][c]=0
                return (r-1,c)
        elif d == 2 and r!=3:
            if grid[r+1][c]==grid[r][c]:
                grid[r+1][c]+=grid[r][c]
                grid[r][c]=0
                return (r+1,c)
            elif grid[r+1][c]==0:
                grid[r+1][c]=grid[r][c]
                grid[r][c]=0
                return (r+1,c)
        elif d == 3 and c!=3:
            if grid[r][c+1]==grid[r][c]:
                grid[r][c+1]+=grid[r][c]
                grid[r][c]=0
                return (r,c+1)
            elif grid[r][c+1]==0:
                grid[r][c+1]=grid[r][c]
                grid[r][c]=0
                return (r,c+1)
        elif d == 4 and c!=0:
            if grid[r][c-1]==grid[r][c]:
                grid[r][c-1]+=grid[r][c]
                grid[r][c]=0
                return (r,c-1)
            elif grid[r][c-1]==0:
                grid[r][c-1]=grid[r][c]
                grid[r][c]=0
                return (r,c-1)
    return (r,c) 

# used to help animate the movement from one tile to another, if functions are implemented correctly increasing
# this will increase the speed at which the tiles move and decreasing it will also cause the tiles to move slower
transition_value = 20

#Problem 7
#def animate_movement(game_board,key,h,v,d):
#   t=transition_value
#    if d == 1:
#       h=h*0
#        if v<t:
#            gui.move_tile(game_board,key,h,-v)
#            return True
#        else:
#            v-=t
#            gui.move_tile(game_board,key,h,-t)
#            return animate_movement(game_board,key,h,v,d)
#    elif d == 2:
#        h=h*0
#        if v<t:
#            gui.move_tile(game_board,key,h,+v)
#            return True
#       else:
#            v-=t
#           gui.move_tile(game_board,key,h,+t)
#            return animate_movement(game_board,key,h,v,d)
#    elif d == 3:
#        v=v*0
#        if h<t:
#            gui.move_tile(game_board,key,+h,v)
#            return True
#        else:
#            h-=t
#            gui.move_tile(game_board,key,+t,v)
#            return animate_movement(game_board,key,h,v,d)
#    elif d == 4:
#       v=v*0
#        if h<t:
#            gui.move_tile(game_board,key,-h,v)
#            return True
#        else:
#            h-=t
#            gui.move_tile(game_board,key,-t,v)
#            return animate_movement(game_board,key,h,v,d)
#    return False

#Problem 19 - Animates the movement of the tiles
def animate_movement(game_board,key,h,v,d):
    t=transition_value
    if d == 1:
        h=h*0
        if v<t:
            gui.move_tile(game_board,key,h,-v)
            if merge(game_board,key) == True:
               return False
            return True
        else:
            v-=t
            gui.move_tile(game_board,key,h,-t)
            return animate_movement(game_board,key,h,v,d)
    elif d == 2:
        h=h*0
        if v<t:
            gui.move_tile(game_board,key,h,+v)
            if merge(game_board,key) == True:
               return False
            return True
        else:
            v-=t
            gui.move_tile(game_board,key,h,+t)
            return animate_movement(game_board,key,h,v,d)
    elif d == 3:
        v=v*0
        if h<t:
            gui.move_tile(game_board,key,+h,v)
            if merge(game_board,key) == True:
               return False
            return True
        else:
            h-=t
            gui.move_tile(game_board,key,+t,v)
            return animate_movement(game_board,key,h,v,d)
    elif d == 4:
        v=v*0
        if h<t:
            gui.move_tile(game_board,key,-h,v)
            if merge(game_board,key) == True:
               return False
            return True
        else:
            h-=t
            gui.move_tile(game_board,key,-t,v)
            return animate_movement(game_board,key,h,v,d)
    return False

#Problem 8 - Moves a specific Tile on the board
def move(game_board,key,d):
    if (gui.move_number(game_board,key,d,update_grid,animate_movement))== True:
        return move(game_board,key,d)

#Problem 9 - Moves all the Tile, on the board, Down 
def move_all_down(game_board):
    d=DOWN
    for c in range(4):
        r=-1
        for s in (grid[::-1]):
            if s[c] != 0:
                move(game_board,find_identifier(game_board,r+4,c),d)
            r+=-1

#Problem 10 - Moves all the Tile, on the board, Up
def move_all_up(game_board):
    d=UP 
    for c in range(4):
        for r in grid:
            if r[c] != 0:
                move(game_board,find_identifier(game_board,grid.index(r),c),d)

#Problem 11 - Moves all the Tile, on the board, Right
def move_all_right(game_board):
    d=RIGHT 
    for r in range(4):
        c=-1
        for s in (grid[r])[::-1]:
            if s != 0:
                move(game_board,find_identifier(game_board,r,c+4),d)
            c+=-1

#Problem 12 - Moves all the Tile, on the board, Left
def move_all_left(game_board):
    d=LEFT 
    for r in range(4):
        for c in range(4):
            if grid[r][c] != 0:
                move(game_board,find_identifier(game_board,r,c),d)

# Dictionary that might be useful
helper = {"count": 0, "Right": RIGHT, "Up": UP, "Left": LEFT, "Down": DOWN}

#Problem 13 - Moves all Tile, on the board, in a specific direction based on the Arrow Key pressed
def move_all(game_board,event):
    if event == "Down":
        return move_all_down(game_board)
    elif event == "Up":
        return move_all_up(game_board)
    elif event == "Right":
        return move_all_right(game_board)
    elif event == "Left":
        return move_all_left(game_board)

#Problem 14 - Moves all Tiles on the board and should add a random number if they very moved
#def keyboard_callback(event, winframe, game_board):
#    old = deepcopy(grid)
#    move_all(game_board,event)
#    if old != grid:
#        add_random_number(game_board)

#Problem 21 - Moves all Tiles on the board and should add a random number if they very moved
def keyboard_callback(event, winframe, game_board):
    old = deepcopy(grid)
    unbind(winframe)
    move_all(game_board,event)
    if is_game_over(game_board) == False:
        bind(winframe,game_board)
    if old != grid:
        add_random_number(game_board)
        
#Problem 18 - Checks to see if a Tile was mergerd and updates and board if it was
def merge(game_board,key):
    r,c = gui.find_position(game_board,key)
    for tkey in board.numbers:
        if tkey != key:
            tr,tc = gui.find_position(game_board,tkey)
            if r == tr and c == tc:
                board.numbers.pop(key)
                gui.remove_number(game_board,tkey)
                gui.remove_number(game_board,key)
                val=gui.find_number(grid[r][c])
                board.score += val.value
                gui.update_score(game_board)
                gui.put(game_board,tkey,val,r,c)
                return True
    return False

# Used to store the available keyboard controls
controls = ["<Right>", "<Left>", "<Up>", "<Down>"]

#Problem 15 - Binds the strings in the 'controls' list with the keyboard_callback function
def bind(winframe,game_board):
    map(lambda x: winframe.bind(x,lambda event: keyboard_callback(event.keysym,winframe,game_board)),controls)
    

#Problem 16 - Unbinds the strings in the 'controls' list from the keyboard_callback function
def unbind(winframe):
    map(lambda x:winframe.unbind(x),controls)

#Problem 20 - Is the game over or not
def is_game_over(game_board):
    size = len(grid) -1
    truth=True
    for r in range(4):
        for c in range(4):
            val = grid[r][c]
            if val == 0 or (r > 0 and grid[r-1][c] == val) or (c > 0 and grid[r][c-1] == val) or (r < size and grid[r+1][c] == val) or (c < size and grid[r][c+1] == val):
                return False
    if max(max(grid)) >= 2048:
        gui.game_over(game_board,True)
    else: 
        gui.game_over(game_board,False)
    return True
    
if __name__ == '__main__':
    """Your Program will start here"""

    frame, board = gui.setup()
    #Problem 17
    r,c = add_random_number(board)
    r,c = add_random_number(board)
    key = find_identifier(board,r,c)

    bind(frame,board)
    
    gui.start(frame)
