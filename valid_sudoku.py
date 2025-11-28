'''
Problem name: Valid Sudoku

Link: https://leetcode.com/problems/valid-sudoku/description/

Description: 
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

My thought process:
So I basically bruteforced it and the thought behind it was to check each thing individually such as 
the row, column, and sub boxes and if there are duplicates then I just return false otherwise return
true at the end. So I basically did the row and col check in one go where I just put a hashmap and
check if there are duplicates and return false if there is, otherwise just move on. I simply reversed
the indexes for the column and did the same process and pattern. For the sub boxes, I simply checked
the middle by iterating through 3 on row and col indexes and starting by [1][1] which is the first
center. Then I pre defined the row and col indexes for the surroundings of the middles so I could
check each tiles and put them in a hashmap by looping through it and adding it to the indexes. I
then checked if there are duplicates in the hashmap and returned False if there is otherwise just 
return True at the end.

Time & space complexity:
O(n^2) time
O(n) space
'''


class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            row_dic = {}
            col_dic = {}

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_dic:
                        return False
                    else:
                        row_dic[board[i][j]] = i, j
                
                if board[j][i] != ".":
                    if board[j][i] in col_dic:
                        return False
                    else:
                        col_dic[board[j][i]] = i, j
                
        for i in range(1, 9, 3):
            row = [-1, -1, -1, 0, 0, 1, 1, 1]
            col = [-1, 0, 1, -1, 1, -1, 0, 1]
            for j in range(1, 9, 3):
                dic = {}
                if board[i][j] != ".":
                    dic[board[i][j]] = i, j
                for k in range(len(row)):
                    new_row = i + row[k]
                    new_col = j + col[k]
                    if board[new_row][new_col] != ".":
                        if board[new_row][new_col] in dic:
                            return False
                        dic[board[new_row][new_col]] = new_row, new_col
                print(dic)
        return True
                

g = Solution()

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]

print(g.isValidSudoku(board))
