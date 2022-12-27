'''
We have an array, we have to find an element before which all elements are less than it, 
and after which all are greater than it. Finally, return the index of the element, 
if there is no such element, then return -1: Time complexity O(n) and Space Complexity O(n)

'''

def find_left_right_sequence(input_arr, low, high):
    
    left = [-1] * len(input_arr) 
    right = [-1] * len(input_arr)
    
    highest_left = input_arr[0]
    lowest_righ = input_arr[high]
    right[high - 1] = input_arr[high]
    
    for i in range(low+1, high + 1):
        if input_arr[i] > highest_left:
            left[i] = highest_left
            highest_left = input_arr[i]
        
            
    
    for i in range(high-2, low-1, -1):
        print (i)
        if input_arr[i] < lowest_righ:
            lowest_righ = input_arr[i]
        right[i] = lowest_righ    
    
    
    print ("Input " + str(left))
    print ("Input " + str(right))
    
    
            
    
input_arr = [2, 1 , 8 , 7, 6, 5] 
#input_arr = [5, 3, 4, 9, 7, 6]
input_arr = [6, 2, 5, 4, 7, 9, 11, 8, 10]

# left    = [,  6, 6, 6, 6, 7, 9, 11, 11]
# right.  = [2, 4, 4, 7, 8, 8, 8, 10]

print ("Input " + str(input_arr))
find_left_right_sequence(input_arr, 0, len(input_arr) - 1)   

print(input_arr)

