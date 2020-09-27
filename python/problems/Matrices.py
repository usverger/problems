from typing import List
from collections import defaultdict

class Solution:

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