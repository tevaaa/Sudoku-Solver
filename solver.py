board = [
    [2,0,0,6,0,1,0,0,5],
    [1,0,9,0,7,0,8,0,4],
    [0,0,0,8,0,9,0,0,0],
    [0,2,6,0,0,0,7,3,0],
    [7,0,0,0,0,0,0,0,6],
    [0,5,8,0,0,0,9,1,0],
    [0,0,0,2,0,8,0,0,0],
    [8,0,2,0,6,0,1,0,9],
    [6,0,0,3,0,5,0,0,7]
]


def print_board(bd):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - - - - - - -")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end = " ")

            if j == 8:
                print(bd[i][j])
            else:
                print(str(bd[i][j]) + " ", end = " ")
    


def find_empty(bd):
    for i in range(9):

        for j in range(9):
            if bd[i][j] == 0:
                return (i, j) # i-> row, j-> column


def valid(bd, n, pos):
    # Check if row is valid
    for i in range(9):
        if n == bd[pos[0]][i] and pos[1] != i:
            return False
    
    #Check if column is valid
    for j in range(9):
        if n == bd[j][pos[1]] and pos[0] != i:
            return False
    
    #Check box
    box_x = pos[0] // 3
    box_y = pos[1] // 3
    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 +3):
            if n == bd[i][j] and (i,j) != pos:
                return False
    return True


def solve(bd):
    find = find_empty(bd)
    if not find:
        return True
    else:
        row, col = find
        for i in range(1,10):
            if valid(bd, i,(row, col)):
                bd[row][col] = i

                if solve(bd):
                    return True
                else:
                    bd[row][col] = 0
    return False


print_board(board)
print("")
print("Solving...")
solve(board)
print("")
print_board(board)