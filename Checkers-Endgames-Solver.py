import argparse
import copy
import sys
import time
import math

cache = {} # you can use this to implement state caching!

class State:
    # This class is used to represent a state.
    # board : a list of lists that represents the 8*8 board
    def __init__(self, board):

        self.board = board
        self.new_row = -999
        self.new_col = -999
        self.update_to_king = 0   # 0 - No; 1 - Yes
        self.is_red_next_turn = False

    def display(self):
        for i in self.board:
            for j in i:
                print(j, end="")
            print("")
        print("")
        
        


def check_red_jumps(state: State):
    """
    Returns a list of possible jumps for the red moves.
    Returns an empty list if no jumps are available for the red moves.
    """
    
    jump_lst = []
    
    for i in range(0, 8):
        for j in range(0, 8):
            
            if state.board[i][j] == 'r':
                # Note that 'r' can only move forward and can thus only jump forward right or forward left
                
                # Checking if it can jump forward right
                if i >= 2 and j <= 5:
                    # check for jumps, because a jump forward right is now possible
                    
                    if state.board[i - 1][j + 1] in ['b', 'B'] and state.board[i - 2][j + 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j + 1] = '.'
                        temp.board[i - 2][j + 2] = 'r'
                        temp.update_to_king = 0
                        temp.new_row = i - 2
                        temp.new_col = j + 2
                        temp.is_red_next_turn = False  # because red just made a turn here; now next is blue's turn
                        if i - 2 == 0:
                            temp.board[i - 2][j + 2] = 'R'
                            temp.update_to_king = 1
                        jump_lst.append(temp)
                
                # Checking if it can jump forward left
                if i >= 2 and j >= 2:
                    # check for jumps, because a jump forward left is now possible
                    
                    if state.board[i - 1][j - 1] in ['b', 'B'] and state.board[i - 2][j - 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j - 1] = '.'
                        temp.board[i - 2][j - 2] = 'r'
                        temp.update_to_king = 0
                        temp.new_row = i - 2
                        temp.new_col = j - 2
                        temp.is_red_next_turn = False
                        if i - 2 == 0:
                            temp.board[i - 2][j - 2] = 'R'
                            temp.update_to_king = 1
                        jump_lst.append(temp)
            
            
            if state.board[i][j] == 'R':
                # Note that R can jump forward (right,left) as well as jump backward (right,left)
                
                # Checking if it can jump forward right
                if i >= 2 and j <= 5:
                    # check for jumps, because a jump forward right is now possible
                    
                    if state.board[i - 1][j + 1] in ['b', 'B'] and state.board[i - 2][j + 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j + 1] = '.'
                        temp.board[i - 2][j + 2] = 'R'
                        temp.new_row = i - 2
                        temp.new_col = j + 2
                        temp.update_to_king = 0
                        temp.is_red_next_turn = False
                        jump_lst.append(temp)
                
                # Checking if it can jump forward left
                if i >= 2 and j >= 2:
                    # check for jumps, because a jump forward left is now possible
                    
                    if state.board[i - 1][j - 1] in ['b', 'B'] and state.board[i - 2][j - 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j - 1] = '.'
                        temp.board[i - 2][j - 2] = 'R'
                        temp.new_row = i - 2
                        temp.new_col = j - 2
                        temp.update_to_king = 0
                        temp.is_red_next_turn = False
                        jump_lst.append(temp)
                        
                # Checking if it can jump backward right
                if i <= 5 and j <= 5:
                    # check for jumps, because a jump backward right is now possible
                    
                    if state.board[i + 1][j + 1] in ['b', 'B'] and state.board[i + 2][j + 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j + 1] = '.'
                        temp.board[i + 2][j + 2] = 'R'
                        temp.new_row = i + 2
                        temp.new_col = j + 2
                        temp.update_to_king = 0
                        temp.is_red_next_turn = False
                        jump_lst.append(temp)
                                            
                # Checking if it can jump backward left
                if i <= 5 and j >= 2:
                    # check for jumps, because a jump bcakward left is now possible

                    if state.board[i + 1][j - 1] in ['b', 'B'] and state.board[i + 2][j - 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j - 1] = '.'
                        temp.board[i + 2][j - 2] = 'R'
                        temp.new_row = i + 2
                        temp.new_col = j - 2
                        temp.update_to_king = 0
                        temp.is_red_next_turn = False
                        jump_lst.append(temp)
                        
    return jump_lst


def check_red_simple_moves(state: State):
    """
    Returns a list of possible simple moves for red moves.
    Returns an empty list if no simple moves are available for red.
    """
    
    jump_lst = []
    
    for i in range(0, 8):
        for j in range(0, 8):
            
            if state.board[i][j] == 'r':
                # Note that 'r' can only move forward and can thus only simple move forward right or simple move forward left
                
                # Checking if it can simple move forward right
                if i >= 1 and j <= 6:
                    # check for simple moves, because a simple move forward right is now possible
                    
                    if state.board[i - 1][j + 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j + 1] = 'r'
                        temp.update_to_king = 0
                        temp.new_row = i - 1
                        temp.new_col = j + 1
                        temp.is_red_next_turn = False  # because red just made a turn here; now next is blue's turn
                        if i - 1 == 0:
                            temp.board[i - 1][j + 1] = 'R'
                            temp.update_to_king = 1
                        jump_lst.append(temp)
                
                # Checking if it can simple move forward left
                if i >= 1 and j >= 1:
                    # check for simple moves, because a simple move forward left is now possible
                    
                    if state.board[i - 1][j - 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j - 1] = 'r'
                        temp.update_to_king = 0
                        temp.new_row = i - 1
                        temp.new_col = j - 1
                        temp.is_red_next_turn = False
                        if i - 1 == 0:
                            temp.board[i - 1][j - 1] = 'R'
                            temp.update_to_king = 1
                        jump_lst.append(temp)
            
            
            if state.board[i][j] == 'R':
                # Note that R can simple move forward (right,left) as well as simple move backward (right,left)
                
                # Checking if it can simple move forward right
                if i >= 1 and j <= 6:
                    # check for simple moves, because a simple move forward right is now possible
                    
                    if state.board[i - 1][j + 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j + 1] = 'R'
                        temp.new_row = i - 1
                        temp.new_col = j + 1
                        temp.update_to_king = 0
                        temp.is_red_next_turn = False
                        jump_lst.append(temp)
                
                # Checking if it can simple move forward left
                if i >= 1 and j >= 1:
                    # check for simple moves, because a simple move forward left is now possible
                    
                    if state.board[i - 1][j - 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j - 1] = 'R'
                        temp.new_row = i - 1
                        temp.new_col = j - 1
                        temp.update_to_king = 0
                        temp.is_red_next_turn = False
                        jump_lst.append(temp)
                        
                # Checking if it can simple move backward right
                if i <= 6 and j <= 6:
                    # check for simple moves, because a simple move backward right is now possible
                    
                    if state.board[i + 1][j + 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j + 1] = 'R'
                        temp.new_row = i + 1
                        temp.new_col = j + 1
                        temp.update_to_king = 0
                        temp.is_red_next_turn = False
                        jump_lst.append(temp)
                                            
                # Checking if it can simple move backward left
                if i <= 6 and j >= 1:
                    # check for simple move, because a simple move bcakward left is now possible

                    if state.board[i + 1][j - 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j - 1] = 'R'
                        temp.new_row = i + 1
                        temp.new_col = j - 1
                        temp.update_to_king = 0
                        temp.is_red_next_turn = False
                        jump_lst.append(temp)
                        
    return jump_lst




def check_specific_red_jump(state: State, i, j):
    """
    Returns a list of possible jumps for the red moves.
    Returns an empty list if no jumps are available for the red moves.
    """
    
    jump_lst = []
            
    if state.board[i][j] == 'r':
        # Note that 'r' can only move forward and can thus only jump forward right or forward left
        
        # Checking if it can jump forward right
        if i >= 2 and j <= 5:
            # check for jumps, because a jump forward right is now possible
            
            if state.board[i - 1][j + 1] in ['b', 'B'] and state.board[i - 2][j + 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i - 1][j + 1] = '.'
                temp.board[i - 2][j + 2] = 'r'
                temp.update_to_king = 0
                temp.new_row = i - 2
                temp.new_col = j + 2
                temp.is_red_next_turn = False  # because red just made a turn here; now next is blue's turn
                if i - 2 == 0:
                    temp.board[i - 2][j + 2] = 'R'
                    temp.update_to_king = 1
                jump_lst.append(temp)
        
        # Checking if it can jump forward left
        if i >= 2 and j >= 2:
            # check for jumps, because a jump forward left is now possible
            
            if state.board[i - 1][j - 1] in ['b', 'B'] and state.board[i - 2][j - 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i - 1][j - 1] = '.'
                temp.board[i - 2][j - 2] = 'r'
                temp.update_to_king = 0
                temp.new_row = i - 2
                temp.new_col = j - 2
                temp.is_red_next_turn = False
                if i - 2 == 0:
                    temp.board[i - 2][j - 2] = 'R'
                    temp.update_to_king = 1
                jump_lst.append(temp)
    
    
    if state.board[i][j] == 'R':
        # Note that R can jump forward (right,left) as well as jump backward (right,left)
        
        # Checking if it can jump forward right
        if i >= 2 and j <= 5:
            # check for jumps, because a jump forward right is now possible
            
            if state.board[i - 1][j + 1] in ['b', 'B'] and state.board[i - 2][j + 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i - 1][j + 1] = '.'
                temp.board[i - 2][j + 2] = 'R'
                temp.new_row = i - 2
                temp.new_col = j + 2
                temp.update_to_king = 0
                temp.is_red_next_turn = False
                jump_lst.append(temp)
        
        # Checking if it can jump forward left
        if i >= 2 and j >= 2:
            # check for jumps, because a jump forward left is now possible
            
            if state.board[i - 1][j - 1] in ['b', 'B'] and state.board[i - 2][j - 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i - 1][j - 1] = '.'
                temp.board[i - 2][j - 2] = 'R'
                temp.new_row = i - 2
                temp.new_col = j - 2
                temp.update_to_king = 0
                temp.is_red_next_turn = False
                jump_lst.append(temp)
                
        # Checking if it can jump backward right
        if i <= 5 and j <= 5:
            # check for jumps, because a jump backward right is now possible
            
            if state.board[i + 1][j + 1] in ['b', 'B'] and state.board[i + 2][j + 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i + 1][j + 1] = '.'
                temp.board[i + 2][j + 2] = 'R'
                temp.new_row = i + 2
                temp.new_col = j + 2
                temp.update_to_king = 0
                temp.is_red_next_turn = False
                jump_lst.append(temp)
                                    
        # Checking if it can jump backward left
        if i <= 5 and j >= 2:
            # check for jumps, because a jump bcakward left is now possible

            if state.board[i + 1][j - 1] in ['b', 'B'] and state.board[i + 2][j - 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i + 1][j - 1] = '.'
                temp.board[i + 2][j - 2] = 'R'
                temp.new_row = i + 2
                temp.new_col = j - 2
                temp.update_to_king = 0
                temp.is_red_next_turn = False
                jump_lst.append(temp)
                        
    return jump_lst
    


def recursive_red_jump(state: State):
    """
    Recursively finding the final red jump
    """
    
    if state.update_to_king == 1:
        return [state]
    lst = check_specific_red_jump(state, state.new_row, state.new_col)
    if lst == []:
        return [state]
    else:
        r_lst = []
        for x in lst:
            r_lst = r_lst + recursive_red_jump(x)
        return r_lst
            
    

def generate_successors_red(state: State):
    """
    Generates successors for the red move
    """
    # You will return only jump moves or only single simple moves
    
    successors = []
    
    # Checking if a jump is possible
    jump_lst = check_red_jumps(state)
    
    if jump_lst != []:          # if jump_lst is not empty, you return the jumps                              
        
        for jump in jump_lst:
            successors = successors + recursive_red_jump(jump)
            
        return successors
    
    else:    # if jump_lst is empty, you return the single simple moves i.e. no jumps are possible in this case
        
        successors = successors + check_red_simple_moves(state)
        
        return successors






def check_black_jumps(state: State):
    """
    Returns a list of possible jumps for the black moves.
    Returns an empty list if no jumps are available for the black moves.
    """
    
    jump_lst = []
    
    for i in range(0, 8):
        for j in range(0, 8):
                                
            if state.board[i][j] == 'b':
                # Note that 'b' can only move backward and can thus only jump backward right or backward left
                
                # Checking if it can jump backward right
                if i <= 5 and j <= 5:
                    # check for jumps, because a jump backward right is now possible
                    
                    if state.board[i + 1][j + 1] in ['r', 'R'] and state.board[i + 2][j + 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j + 1] = '.'
                        temp.board[i + 2][j + 2] = 'b'
                        temp.update_to_king = 0
                        temp.new_row = i + 2
                        temp.new_col = j + 2
                        temp.is_red_next_turn = True  # because black just moved, thus the next turn is of red
                        if i + 2 == 7:
                            temp.board[i + 2][j + 2] = 'B'
                            temp.update_to_king = 1
                        jump_lst.append(temp)
                                            
                # Checking if it can jump backward left
                if i <= 5 and j >= 2:
                    # check for jumps, because a jump bcakward left is now possible

                    if state.board[i + 1][j - 1] in ['r', 'R'] and state.board[i + 2][j - 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j - 1] = '.'
                        temp.board[i + 2][j - 2] = 'b'
                        temp.update_to_king = 0
                        temp.new_row = i + 2
                        temp.new_col = j - 2
                        temp.is_red_next_turn = True
                        if i + 2 == 7:
                            temp.board[i + 2][j - 2] = 'B'
                            temp.update_to_king = 1
                        jump_lst.append(temp)
                   
                        
            if state.board[i][j] == 'B':
                # Note that B can jump forward (right,left) as well as jump backward (right,left)
                
                # Checking if it can jump forward right
                if i >= 2 and j <= 5:
                    # check for jumps, because a jump forward right is now possible
                    
                    if state.board[i - 1][j + 1] in ['r', 'R'] and state.board[i - 2][j + 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j + 1] = '.'
                        temp.board[i - 2][j + 2] = 'B'
                        temp.new_row = i - 2
                        temp.new_col = j + 2
                        temp.update_to_king = 0
                        temp.is_red_next_turn = True
                        jump_lst.append(temp)
                
                # Checking if it can jump forward left
                if i >= 2 and j >= 2:
                    # check for jumps, because a jump forward left is now possible
                    
                    if state.board[i - 1][j - 1] in ['r', 'R'] and state.board[i - 2][j - 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j - 1] = '.'
                        temp.board[i - 2][j - 2] = 'B'
                        temp.new_row = i - 2
                        temp.new_col = j - 2
                        temp.update_to_king = 0
                        temp.is_red_next_turn = True
                        jump_lst.append(temp)
                        
                # Checking if it can jump backward right
                if i <= 5 and j <= 5:
                    # check for jumps, because a jump backward right is now possible
                    
                    if state.board[i + 1][j + 1] in ['r', 'R'] and state.board[i + 2][j + 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j + 1] = '.'
                        temp.board[i + 2][j + 2] = 'B'
                        temp.new_row = i + 2
                        temp.new_col = j + 2
                        temp.update_to_king = 0
                        temp.is_red_next_turn = True
                        jump_lst.append(temp)
                                            
                # Checking if it can jump backward left
                if i <= 5 and j >= 2:
                    # check for jumps, because a jump bcakward left is now possible

                    if state.board[i + 1][j - 1] in ['r', 'R'] and state.board[i + 2][j - 2] == '.':
                        # jump
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j - 1] = '.'
                        temp.board[i + 2][j - 2] = 'B'
                        temp.new_row = i + 2
                        temp.new_col = j - 2
                        temp.update_to_king = 0
                        temp.is_red_next_turn = True
                        jump_lst.append(temp)
                        
    return jump_lst


def check_black_simple_moves(state: State):
    """
    Returns a list of possible simple moves for the black moves.
    Returns an empty list if no simple moves are available for the black moves.
    """
    
    jump_lst = []
    
    for i in range(0, 8):
        for j in range(0, 8):
                                
            if state.board[i][j] == 'b':
                # Note that 'b' can only move backward and can thus only simple move backward right or backward left
                
                # Checking if it can simple move backward right
                if i <= 6 and j <= 6:
                    # check for simple moves, because a simple move backward right is now possible
                    
                    if state.board[i + 1][j + 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j + 1] = 'b'
                        temp.update_to_king = 0
                        temp.new_row = i + 1
                        temp.new_col = j + 1
                        temp.is_red_next_turn = True  # because black just moved, thus the next turn is of red
                        if i + 1 == 7:
                            temp.board[i + 1][j + 1] = 'B'
                            temp.update_to_king = 1
                        jump_lst.append(temp)
                                           
                # Checking if it can simple move backward left
                if i <= 6 and j >= 1:
                    # check for simple moves, because a simple bcakward left is now possible

                    if state.board[i + 1][j - 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j - 1] = 'b'
                        temp.update_to_king = 0
                        temp.new_row = i + 1
                        temp.new_col = j - 1
                        temp.is_red_next_turn = True
                        if i + 1 == 7:
                            temp.board[i + 1][j - 1] = 'B'
                            temp.update_to_king = 1
                        jump_lst.append(temp)
                   
                        
            if state.board[i][j] == 'B':
                # Note that B can simple move forward (right,left) as well as simple move backward (right,left)
                
                # Checking if it can simple move forward right
                if i >= 1 and j <= 6:
                    # check for simple moves, because a simple move forward right is now possible
                    
                    if state.board[i - 1][j + 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j + 1] = 'B'
                        temp.new_row = i - 1
                        temp.new_col = j + 1
                        temp.update_to_king = 0
                        temp.is_red_next_turn = True
                        jump_lst.append(temp)
                
                # Checking if it can simple move forward left
                if i >= 1 and j >= 1:
                    # check for simple moves, because a simple move forward left is now possible
                    
                    if state.board[i - 1][j - 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i - 1][j - 1] = 'B'
                        temp.new_row = i - 1
                        temp.new_col = j - 1
                        temp.update_to_king = 0
                        temp.is_red_next_turn = True
                        jump_lst.append(temp)
                        
                # Checking if it can simple move backward right
                if i <= 6 and j <= 6:
                    # check for simple moves, because a simple move backward right is now possible
                    
                    if state.board[i + 1][j + 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j + 1] = 'B'
                        temp.new_row = i + 1
                        temp.new_col = j + 1
                        temp.update_to_king = 0
                        temp.is_red_next_turn = True
                        jump_lst.append(temp)
                                            
                # Checking if it can simple move backward left
                if i <= 6 and j >= 1:
                    # check for simple moves, because a simple move bcakward left is now possible

                    if state.board[i + 1][j - 1] == '.':
                        # simple move
                        
                        temp = copy.deepcopy(state)
                        temp.board[i][j] = '.'
                        temp.board[i + 1][j - 1] = 'B'
                        temp.new_row = i + 1
                        temp.new_col = j - 1
                        temp.update_to_king = 0
                        temp.is_red_next_turn = True
                        jump_lst.append(temp)
                        
    return jump_lst



def check_specific_black_jump(state: State, i, j):
    """
    Returns a list of possible jumps for the black moves.
    Returns an empty list if no jumps are available for the black moves.
    """
    
    jump_lst = []
                                
    if state.board[i][j] == 'b':
        # Note that 'b' can only move backward and can thus only jump backward right or backward left
        
        # Checking if it can jump backward right
        if i <= 5 and j <= 5:
            # check for jumps, because a jump backward right is now possible
            
            if state.board[i + 1][j + 1] in ['r', 'R'] and state.board[i + 2][j + 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i + 1][j + 1] = '.'
                temp.board[i + 2][j + 2] = 'b'
                temp.update_to_king = 0
                temp.new_row = i + 2
                temp.new_col = j + 2
                temp.is_red_next_turn = True  # because black just moved, thus the next turn is of red
                if i + 2 == 7:
                    temp.board[i + 2][j + 2] = 'B'
                    temp.update_to_king = 1
                jump_lst.append(temp)
                                    
        # Checking if it can jump backward left
        if i <= 5 and j >= 2:
            # check for jumps, because a jump bcakward left is now possible

            if state.board[i + 1][j - 1] in ['r', 'R'] and state.board[i + 2][j - 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i + 1][j - 1] = '.'
                temp.board[i + 2][j - 2] = 'b'
                temp.update_to_king = 0
                temp.new_row = i + 2
                temp.new_col = j - 2
                temp.is_red_next_turn = True
                if i + 2 == 7:
                    temp.board[i + 2][j - 2] = 'B'
                    temp.update_to_king = 1
                jump_lst.append(temp)
            
                
    if state.board[i][j] == 'B':
        # Note that B can jump forward (right,left) as well as jump backward (right,left)
        
        # Checking if it can jump forward right
        if i >= 2 and j <= 5:
            # check for jumps, because a jump forward right is now possible
            
            if state.board[i - 1][j + 1] in ['r', 'R'] and state.board[i - 2][j + 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i - 1][j + 1] = '.'
                temp.board[i - 2][j + 2] = 'B'
                temp.new_row = i - 2
                temp.new_col = j + 2
                temp.update_to_king = 0
                temp.is_red_next_turn = True
                jump_lst.append(temp)
        
        # Checking if it can jump forward left
        if i >= 2 and j >= 2:
            # check for jumps, because a jump forward left is now possible
            
            if state.board[i - 1][j - 1] in ['r', 'R'] and state.board[i - 2][j - 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i - 1][j - 1] = '.'
                temp.board[i - 2][j - 2] = 'B'
                temp.new_row = i - 2
                temp.new_col = j - 2
                temp.update_to_king = 0
                temp.is_red_next_turn = True
                jump_lst.append(temp)
                
        # Checking if it can jump backward right
        if i <= 5 and j <= 5:
            # check for jumps, because a jump backward right is now possible
            
            if state.board[i + 1][j + 1] in ['r', 'R'] and state.board[i + 2][j + 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i + 1][j + 1] = '.'
                temp.board[i + 2][j + 2] = 'B'
                temp.new_row = i + 2
                temp.new_col = j + 2
                temp.update_to_king = 0
                temp.is_red_next_turn = True
                jump_lst.append(temp)
                                    
        # Checking if it can jump backward left
        if i <= 5 and j >= 2:
            # check for jumps, because a jump bcakward left is now possible

            if state.board[i + 1][j - 1] in ['r', 'R'] and state.board[i + 2][j - 2] == '.':
                # jump
                
                temp = copy.deepcopy(state)
                temp.board[i][j] = '.'
                temp.board[i + 1][j - 1] = '.'
                temp.board[i + 2][j - 2] = 'B'
                temp.new_row = i + 2
                temp.new_col = j - 2
                temp.update_to_king = 0
                temp.is_red_next_turn = True
                jump_lst.append(temp)
                        
    return jump_lst


def recursive_black_jump(state: State):
    """
    Recursively finding the final black jump
    """
    
    if state.update_to_king == 1:
        return [state]
    lst = check_specific_black_jump(state, state.new_row, state.new_col)
    if lst == []:
        return [state]
    else:
        r_lst = []
        for x in lst:
            r_lst = r_lst + recursive_black_jump(x)
        return r_lst




def generate_successors_black(state: State):
    """
    Generates successors for the black move
    """
    # You will return only jump moves or only single simple moves
    
    successors = []
    
    # Checking if a jump is possible
    jump_lst = check_black_jumps(state)
    
    if jump_lst != []:          # if jump_lst is not empty, you return the jumps                              
        
        for jump in jump_lst:
            successors = successors + recursive_black_jump(jump)
            
        return successors
    
    else:    # if jump_lst is empty, you return the single simple moves i.e. no jumps are possible in this case
        
        successors = successors + check_black_simple_moves(state)
        
        return successors



























def check_terminal_black(state: State):  # Return 0 to indicate a terminal state; Return 1 to indicate a non-terminal state
    """
    Check if it is a terminal state for a black move
    """
    # It is a terminal state for a black move if, all the black pieces are gone (i.e. no black pieces left to move)
    # or the state is such that black does not have any legal moves left
    
    
    # let's check if all the black pieces are gone or not
    
    counter = 0
    
    for i in range(0, 8):
        for j in range(0, 8):
            
            if state.board[i][j] in ['b', 'B']:
                counter = counter + 1
                
    if counter == 0:
        return 0      # this is a terminal state
    
    # let's check if there are any legal moves for black pieces or not
    
    lst = generate_successors_black(state)
    
    if lst == []:
        return 0     # this is a terminal state
    
    return 1         # if the program has reached till here, then this is not a terminal state for black


def check_terminal_red(state: State):  # Return 0 to indicate a terminal state; Return 1 to indicate a non-terminal state
    """
    Check if it is a terminal state for a red move
    """
    # It is a terminal state for a red move if, all the red pieces are gone (i.e. no red pieces left to move)
    # or the state is such that red does not have any legal moves left
    
    
    # let's check if all the red pieces are gone or not
    
    counter = 0
    
    for i in range(0, 8):
        for j in range(0, 8):
            
            if state.board[i][j] in ['r', 'R']:
                counter = counter + 1
                
    if counter == 0:
        return 0      # this is a terminal state
    
    # let's check if there are any legal moves for red pieces or not
    
    lst = generate_successors_red(state)
    
    if lst == []:
        return 0     # this is a terminal state
    
    return 1         # if the program has reached till here, then this is not a terminal state for red




def eval2(state: State):
    """
    The evaluation function in terms of red (positive) and black (negative).
    """
    total = 0
    
    for i in range(0, 8):
        for j in range(0, 8):
            
            if state.board[i][j] == 'r':
                total = total + 5 + (7-i)
            if state.board[i][j] == 'R':
                total = total + 5 + 8 + 2
            if state.board[i][j] == 'b':
                total = total - 5 - i
            if state.board[i][j] == 'B':
                total = total - (5 + 8 + 2)
                
    return total
    

def eval(state: State):
    """
    The evaluation function in terms of red (positive) and black (negative).
    """
    total = 0
    
    for i in range(0, 8):
        for j in range(0, 8):
            
            if state.board[i][j] == 'r':
                total = total + 1
            if state.board[i][j] == 'R':
                total = total + 2
            if state.board[i][j] == 'b':
                total = total - 1
            if state.board[i][j] == 'B':
                total = total - 2
                
    return total





def max_to_min(state_lst):
    """
    Order states from max heuristic value to min heuristic value based on evaluation function.
    """
    new_lst = []
    
    for x in state_lst:
        new_lst.append( [eval(x), x] )

    # bubble sort
    for i in range(0, len(new_lst)-1):  
        for j in range(len(new_lst)-1):  
            if( new_lst[j][0] < new_lst[j+1][0]):  
                temp = new_lst[j]  
                new_lst[j] = new_lst[j+1]  
                new_lst[j+1] = temp  


    return [x[1] for x in new_lst]



def min_to_max(state_lst):
    """
    Order states from min heuristic value to max heuristic value based on evaluation function.
    """
    new_lst = []
    
    for x in state_lst:
        new_lst.append( [eval(x), x] )

    # bubble sort
    for i in range(0, len(new_lst)-1):  
        for j in range(len(new_lst)-1):  
            if( new_lst[j][0] > new_lst[j+1][0]):  
                temp = new_lst[j]  
                new_lst[j] = new_lst[j+1]  
                new_lst[j+1] = temp  


    return [x[1] for x in new_lst]



































def max_value(state: State, alpha, beta, depth): # -> [utility_value, state] returns a utility value as well as an action (the next action)
    """
    Function for max (red)
    """
    if check_terminal_red(state) == 0: # it is a terminal state for red
        return [-math.inf, state]
    if depth >= 7:                     # reached the depth limit - Updated depth limit to 7
        return [eval2(state), state]

    v = -math.inf
    
    final_action = 0
    
    for action in max_to_min(generate_successors_red(state)):
        
        temp = min_value(action, alpha, beta, depth + 1)
        
        v = max(v, temp[0])
        
        if v >= beta:
            return [v, action]
        
        alpha = max(alpha, v)
        
        final_action = action
    
    return [v, final_action]




def min_value(state: State, alpha, beta, depth): # -> [utility_value, state] returns a utility value as well as an action (the next action)
    """
    Function for min (black)
    """
    if check_terminal_black(state) == 0:
        return [math.inf, state]
    if depth >= 7:             # Updated depth limit to 7
        return [eval2(state), state]
    
    v = math.inf
    
    final_action = 0
    
    for action in min_to_max(generate_successors_black(state)):
        
        temp = max_value(action, alpha, beta, depth + 1)
        
        v = min(v, temp[0])
        
        if v <= alpha:
            return [v, action]
        
        beta = min(beta, v)
        
        final_action = action
    
    return [v, final_action]
    













def runner(state: State): # returns the desired path
    """
    Run Alpha-Beta Pruning with evaluation function
    """
    temp = [0, state]
    
    path = []
    path.append(state) # appended the initial state
    
    while True: 
        # assumed that red makes the first move
        if check_terminal_red(temp[1]) == 0:
            return path
        
        t = max_value(temp[1], -math.inf, math.inf, 0)
        
        path.append(t[1])
        
        if check_terminal_black(t[1]) == 0:
            return path
        
        temp = min_value(t[1], -math.inf, math.inf, 0)
        
        path.append(temp[1])
        # also assumed that red always wins









  

def get_opp_char(player: chr):
    if player in ['b', 'B']:
        return ['r', 'R']
    else:
        return ['b', 'B']
    
    

def get_next_turn(curr_turn: chr):
    if curr_turn == 'r':
        return 'b'
    else:
        return 'r'
    
    

def read_from_file(filename):

    f = open(filename)
    lines = f.readlines()
    board = [[str(x) for x in l.rstrip()] for l in lines]
    f.close()

    return board




if __name__ == '__main__':
    
    start_time = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputfile",
        type=str,
        required=True,
        help="The input file that contains the puzzles."
    )
    parser.add_argument(
        "--outputfile",
        type=str,
        required=True,
        help="The output file that contains the solution."
    )
    args = parser.parse_args()
    
    initial_board = read_from_file(args.inputfile)
    
    state = State(initial_board)
    state.is_red_next_turn = True
    
    t = runner(state)
    
    f = open(args.outputfile, 'w')
    
    for x in t:
        for i in range(0, 8):
            for j in range(0, 8):
                f.write(str(x.board[i][j]))
            f.write("\n")
        f.write("\n")
        
    f.close()
    
    # print("--- %s seconds ---" % (time.time() - start_time))
    # latest - Modified using 2 evaluation functions
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # turn = 'r'
    # ctr = 0

    # sys.stdout = open(args.outputfile, 'w')

    # sys.stdout = sys.__stdout__

