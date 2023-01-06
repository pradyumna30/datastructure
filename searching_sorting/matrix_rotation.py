'''
You are given a square matrix, You need to rotate the matrix 
in a clockwise direction by 90 degrees in Time Complexity O(m*n) and 
No Extra Space i.e O(1) Asked in : Facebook, Google, Amazon, Microsoft

'''

mat = [ 
        [1,  2, 3,  4], 
        [5,  6, 7, 8], 
        [9, 10, 11, 12], 
        [13, 14, 15,16]
      ]
      
# (x, y) -> (y, N-x)
# 1 -> 4 
# (y, N-x) -> (N-x, N-y)
# (N-x, N-y) -> (N-y, x)
# (N-y, x) -> (x, y)

def rotate_matrix_90(N, mat):
    
    print (mat)
    p = int(N/2)
    for i in range(0, p+1):
        
        for j in range(i, N-i):
                
                temp = mat[N-j][i]
                mat[N-j][i] = mat[N-i][N-j]
                mat[N-i][N-j] = mat[j][N-i]
                
                mat[j][N-i] = mat[i][j]
                
                mat[i][j] = temp
                
                
    print (mat)            
                
rotate_matrix_90(3, mat)                
