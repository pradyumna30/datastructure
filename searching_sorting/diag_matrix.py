'''
Given a matrix of M x N elements (M rows, N columns), 
Print all elements of the matrix in diagonal order in Time Complexity O(m*n) and Space Complexity O(1)

'''

matrix = [
            [1,  2,  3,  4], 
	        [5,  6,  7,  8], 
	        [9, 10, 11, 12],
	        [13, 14, 15, 16],
	        [11, 12, 13, 14]
	     ] 

def print_diagonal_matrix(matrix, m, n):
    
    i, j = 0, 0
    p, k = 0, 0
    while i <= m:
        p = i
        k = j
        while (p >= 0 and k <= n):
            print (matrix[p][k])
            p = p - 1
            k = k + 1
        i = i + 1
    
    i = m
    j = 1
    
    while ( j <= n ):
        p = i 
        k = j
        
        while (p >= 0 and k <= n):
            print (matrix[p][k])
            
            p = p - 1
            k = k + 1
            
        j = j + 1    
    
    
print_diagonal_matrix(matrix, 4, 3)
