'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, Time complexity O(n) and Space complexity O(1)

'''

def duplicate_remove(input_arr, low, high):
    
    k = 0
    for i in range (0, high):
        
        if input_arr[i] != input_arr[i+1]:
            input_arr[k] = input_arr[i]
            k += 1
        
    input_arr[k] = input_arr[i+1]
    print (input_arr)
    
input_arr = [1, 1, 4, 5, 5, 6, 8, 9, 10, 12 , 12 , 33 , 34,34] 



duplicate_remove(input_arr, 0, len(input_arr) - 1)
