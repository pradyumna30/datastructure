'''
You have an array of non-negative integers,you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index in O(n) Time complexity and O(1) Space Complexity Asked in : AdobeIntuit

'''

def jump_game(input_arr, low, high):
    
    a = input_arr[0]
    b = input_arr[0]
    jump = 1
    i = low
    print ("Jumps " + str(jump))
    for j in range(1, high+1):
        
        print ("J " + str(j))
        if (j == high):
            break
            
        a = a - 1
        b = b - 1
        
        if input_arr[j] > b:
            b = input_arr[j]
            
        if (a == 0):
            jump = jump + 1
            a = b
            
    print ("Jumps " + str(jump))
    
    
input_arr = [2,3,1,1,4] 

jump_game(input_arr, 0, len(input_arr) - 1)
