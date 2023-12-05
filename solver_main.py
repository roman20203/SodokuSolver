Sodoku =[ 
    [0,0,6,0,0,0,5,0,8], 
    [1,0,2,3,8,0,0,0,4], 
    [0,0,0,2,0,0,1,9,0], 
    [0,0,0,0,6,3,0,4,5], 
    [0,6,3,4,0,5,8,7,0], 
    [5,4,0,9,2,0,0,0,0], 
    [0,8,7,0,0,4,0,0,0], 
    [2,0,0,0,9,8,4,0,7], 
    [4,0,9,0,0,0,3,0,0]
]



def print_board(board):
    for i in range(len(board)): 
        if i%3 == 0 and i !=0:
            print("-------------------------")
        
        for j in range(len(board[0])): 
            if j%3 == 0 and j!=0: 
                print("|"," ", end= "")
            if j == 8: 
                print(board[i][j])
            else: 
                print(board[i][j],"", end ="")


def Solver(board): 
    find = find_empty(board)
    if not find: 
        return True #no more empty spots and we have solved the puzzle 
    else:
        #if find found something it will return a row and col 
        row,col = find

        for i in range(1,10): 
            if valid(board,i,(row,col)): 
                #plugs in valid number into empty found position
                board[row][col] = i

                if Solver(board): 
                    #Will keep on running until Solver returns False 
                    #Solver only return false once a position has no valid numbers
                    return True
                else: 
                    board[row][col] = 0
        return False



    #Returns False once the solver has tried numbers 1-9,
    #which means an issue has occured 
    #Now line 89 will not run as Solver is now False, and 
    #the Else will run, reseting the last position and ba
    #ck tracking either resetting positions or finding new values to plug in 



def check_row(board, num, pos): 
    #Checks specified row for specified num 
    exists_row = False

    for i in range(len(board[0])): 
        if board[pos[0]][i] == num and i != pos[1]: 
            exists_row = True
    
    return exists_row
    

def check_column(board, num, pos): 
    #Checks column for num 
    exists_col = False

    for i in range(len(board)): 
        if board[i][pos[1]] == num and i != pos[0]: 
            exists_col = True

    return exists_col

def check_box(board,num, pos): 
    #finds what box it is in
    boxX = pos[1]//3
    boxY = pos[0]//3

    for i in range(boxY * 3, boxY*3 + 3): 
        for j in  range(boxX *3, boxX*3 +3): 
            if board[i][j] == num and (i,j) != pos :
                return True

def valid(board,num,pos): 
    return not check_column(board, num, pos,) and not check_row(board, num, pos,) and not check_box(board, num, pos)

def find_empty(board): 
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if board[i][j] == 0: 
                return (i,j) #row , col
    
    return False
            

    
    
print_board(Sodoku)
Solver(Sodoku) 
print("\n\nSolved Puzzle!:")
print_board(Sodoku)
