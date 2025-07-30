from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        usedColumn = [[0] * 9 for _ in range(9)]
        usedRow = [[0] * 9 for _ in range(9)]
        usedGrid = [[[0] * 9 for _a in range(3)] for _b in range(3)]
        space = 0
        
        for row in range(9):
            for column in range(9):
                if board[row][column].isdigit():
                    number = int(board[row][column]) - 1
                    usedColumn[column][number] = 1
                    usedRow[row][number] = 1
                    usedGrid[row//3][column//3][number] = 1
                else:
                    space += 1

        def dfs(space):
            if space == 0:
                return True
            for row in range(9):
                for column in range(9):
                    if board[row][column] == '.':
                        for no in range(1,10):
                            if usedColumn[column][no-1] == 0 and usedRow[row][no-1] == 0 and usedGrid[row//3][column//3][no-1] == 0:
                                board[row][column] = str(no)
                                usedColumn[column][no-1] = usedRow[row][no-1] = usedGrid[row//3][column//3][no-1] = 1
                                flag = dfs(space-1)
                                if flag:
                                    return True
                                board[row][column] = '.'
                                usedColumn[column][no-1] = usedRow[row][no-1] = usedGrid[row//3][column//3][no-1] = 0
                        # The most important part of this solution
                        # Cause it reduce the complexity greatly
                        # By cut the wrong way in early time before many depths.

                        # Cause backTrack is meant to be wrong choice at now
                        # If all the choices has been to be proved wrong
                        # This way to fill numbers must be wrong.

                        # Cause we can't find a suitable number to fill the blank
                        # This is far from a may-be right choice.
                        return False
                                

        dfs(space)


# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         def dfs(pos: int):
#             nonlocal valid
#             if pos == len(spaces):
#                 valid = True
#                 return
            
#             i, j = spaces[pos]
#             for digit in range(9):
#                 if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
#                     line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
#                     board[i][j] = str(digit + 1)
#                     dfs(pos + 1)
#                     line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
#                 if valid:
#                     return
            
#         line = [[False] * 9 for _ in range(9)]
#         column = [[False] * 9 for _ in range(9)]
#         block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
#         valid = False
#         spaces = list()

#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == ".":
#                     spaces.append((i, j))
#                 else:
#                     digit = int(board[i][j]) - 1
#                     line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

#         dfs(0)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return
            
        line = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)

        dfs(0)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def flip(i: int, j: int, digit: int):
            line[i] ^= (1 << digit)
            column[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            # python's unique problem caused by python's interpretation of negative number
            # python中关于负数（二进制)无法合理地正常显示
            # 只能展示为  -（绝对值的原码）的形式
            # 所以此处与0x1ff位与是为了恢复正确的形式
            mask = ~(line[i] | column[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digitMask = mask & (-mask)
                digit = bin(digitMask).count("0") - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return
            
        line = [0] * 9
        column = [0] * 9
        block = [[0] * 3 for _ in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)

        dfs(0)


sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol.solveSudoku(board)
def beautify(lst):
    for no, item in enumerate(lst):
        if isinstance(item, list):
            if no % 3 == 0 and no != 0:
                print('-' * 21)
            beautify(item)
        else:
            if no % 3 == 0 and no != 0:
                print('|', end=' ')
            print(item, end=' ')
    print()
beautify(board)



        
