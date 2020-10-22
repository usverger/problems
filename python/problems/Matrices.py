from typing import List
from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for i in range(len(board)):
            d = {}
            for j in range(len(board)):
                if board[i][j] in d: return False
                if board[i][j] != ".": d[board[i][j]] = board[i][j]
        
        # check columns
        for j in range(len(board)):
            d = {}
            for i in range(len(board)):
                if board[i][j] in d: return False
                if board[i][j] != ".": d[board[i][j]] = board[i][j]
                    
        # check squares
        for i in range(len(board)):
            d = {}
            lefti = (i // 3)*3
            leftj = (i % 3)*3
            for x in range(lefti, lefti + 3):
                for y in range(leftj, leftj + 3):
                    if board[x][y] in d:
                        return False
                    if board[x][y] != ".": d[board[x][y]] = board[x][y]
        return True

    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:            
        n = len(matrix)
        for i in range(n // 2): # iterate over the square radiuses
            for j in range(i, n - i - 1): # rotate each element of one side except the last one
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        return matrix

    def pascalTriangle_WithPaddedArrays(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        result = [[1]]
        
        for _ in range(numRows - 1):
            m = map(lambda x, y: x + y, result[-1] + [0], [0] + result[-1])
            result.append(list(m))
        return result

    def pascalTriangle(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        
        result = [[1], [1,1]]
        for r in range(3, numRows + 1):
            l = [0] * r
            l[0] = 1
            l[r - 1] = 1
            for i in range(1, r - 1):
                l[i] = result[r - 2][i - 1] + result[r - 2][i]
            result.append(l)
        return result

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0: return []
        N = len(matrix[0])
        if N == 0: return []

        result = []

        maxradius = -(-min(M, N) // 2) # divided by 2 rounded up
        for r in range(maxradius):
        #r = 1
            result.append(matrix[r][r])
            for j in range(r + 1, N - r):
                result.append(matrix[r][j])
            for i in range(r + 1, M - r):
                result.append(matrix[i][N - r - 1])
            if r < M - r - 1 and r < N - r - 1:
                for j in range(N - r - 2, r - 1, -1):
                    result.append(matrix[M - r - 1][j])
                for i in range(M - r - 2, r, -1):
                    result.append(matrix[i][r])            
        
        return result


    def findDiagonalOrder_WithMap(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0: return []
        N = len(matrix[0])
        if N == 0: return []
        
        # build a dictionary of diagonals, for each diagonal d its i+j equals d
        d = defaultdict(list)
        for i in range(M):
            for j in range(N):
                d[i+j].append(matrix[i][j])
        
        result = []
        for i in d:
            if i % 2 == 0: 
                result.extend(reversed(d[i]))
            else:
                result.extend(d[i])
        return result


    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0: return []
        N = len(matrix[0])
        if N == 0: return []
        
        result = []
        
        for d in range(0, M + N - 1): # diagonals where i + j = d
            if d % 2 == 0: # go to top-right
                r = d if d < M else M - 1
                c = 0 if d < M else d - M + 1
                while c < N and r > -1:
                    result.append(matrix[r][c])
                    c += 1
                    r -= 1
                    
            else: # go bottom-left
                r = 0 if d < N else d - N + 1
                c = d if d < N else N - 1
                while r < M and c > -1:
                    result.append(matrix[r][c])
                    r += 1
                    c -= 1
                    
        return result

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # the easiest solution is to calculate manhattan distances, then sort by it and then output
        # ideally we should put them to a storage that is already sorted
        # a simple array actually works because distance is naturally the index of array

        # initialize the array        
        result = [[] for i in range(R + C - 1)]
        
        # enumerate all cells, the order does not matter
        for i in range(R):
            for j in range(C):
                result[abs(i - r0) + abs(j - c0)].append([i, j])
                
        # output in the same order
        flattened = []
        for e in result:
            for e2 in e:
                flattened.append(e2)
            
        return flattened