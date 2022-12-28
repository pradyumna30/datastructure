'''
you are given a matrix of m x n elements (m rows, n columns), 
Print all elements of the matrix in spiral 
order in O(m*n) Time Complexity and O(1) Space Complexity Asked in : MicrosoftOLAPayTmOracle

'''

matrix = [[1, 2, 3, 4], 
	      [5,6,7,8], 
	      [9, 10, 11, 12],
	      [13, 14, 15, 16],
	      [11, 12, 13, 14]] 

def print_spiral_matrix(matrix, m, n):
    
    l, k = 0, 0
    
    while (l < m and k < n):
        for i in range(l, m):
            print(matrix[l][i])
        
        for j in range(k, n):
            print(matrix[j][m])
        
        for g in range(m, k, -1):
            print (matrix[n][g])
        
        for h in range(n, l, -1):
            print( matrix[h][k])
        
        l = l + 1
        k = k + 1
        m = m - 1
        n = n - 1
        
print_spiral_matrix(matrix, 3, 4)
