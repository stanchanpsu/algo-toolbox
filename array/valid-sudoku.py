'''
https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''

class Solution:
    valid = set(['1','2','3','4','5','6','7','8','9'])
    
    def isValidList(self, array):
        for l in array:
            left = copy.copy(Solution.valid)
            for cell in l:
                if cell == '.':
                    continue
                if cell in left:
                    left.remove(cell)
                else:
                    return False
        return True
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = [[] for i in range(9)]
        blocks = [[] for i in range(9)]
            
        
        # Check rows
        for row in board:
            left = copy.copy(Solution.valid)
            for index, cell in enumerate(row):
                if cell == '.':
                    continue
                elif cell in left:
                    left.remove(cell)
                else:
                    return False

                # In same loop make columns
                columns[index].append(cell)
                
        # Check columns
        if not self.isValidList(columns):
            return False
        
        # Build blocks
        for i in range(9):
            for j in range(9):
                extra = 0
                row = int(i/3)
                col = int(j/3)
                if col == 1:
                    extra = 2
                elif col == 2:
                    extra = 4
                block = row + col + extra
                blocks[block].append(board[i][j])
                
        # Check blocks
        # return blocks
        return self.isValidList(blocks)
            
            