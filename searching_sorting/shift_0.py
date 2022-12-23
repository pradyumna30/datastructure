'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the 
relative order of the non-zero elements in O(n) 
Time complexity and O(1) Space complexity with single traversal allowed

'''

def swap(input_arr, a, b):
    
    temp = input_arr[a]
    input_arr[a] = input_arr[b]
    input_arr[b] = temp
    
def sort_0(input_arr, low, high):
    
    h = high
    l = low
    zero = high
    flag = False
    non_zero = high
    
    while (h >= l):
        
        if (input_arr[zero] == 0 and flag == False):
            flag = True
            #zero = h
        elif flag == False:
            zero = zero - 1 
        if (input_arr[h] != 0):
            non_zero = h
            
        h = h - 1
        
        if (flag == True and non_zero < zero):
           
            swap(input_arr, non_zero, zero)
            flag = False
            non_zero = zero
            zero = zero - 1
            

#input_arr = [1 , 3, 0, 1, 0, 45, 1, 33, 55, 66 ,77, 0, 1, 0, 0, 33, 0 ,0 ,0 ,0 ,0 ,0 ,0 ]
input_arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
print (input_arr)
sort_0(input_arr, 0, len(input_arr) - 1)   

print (input_arr)
