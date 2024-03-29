# N-Queens

'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 
Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiagonal = set()  # (r+c)
        negDiagonal = set()  # (r-c)

        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            # Iterate through each column
            for c in range(n):
                # Check if placing a queen at position (r, c) violates any constraints
                if c in col or (r+c) in posDiagonal or (r-c) in negDiagonal:
                    continue

                # Update occupied columns and diagonals
                col.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # Backtrack: remove the queen and reset states of occupied columns and diagonals
                col.remove(c)
                posDiagonal.remove(r + c)
                negDiagonal.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return result
