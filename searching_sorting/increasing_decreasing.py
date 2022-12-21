

'''

Question : One array of integers is given as an input ,
which is initially increasing and then decreasing or it can be only increasing or decreasing , 
you need to find the maximum value in the array in O(Log n) Time complexity and O(1) 
Space Complexity Asked in : AmazonMicrosoftUber


Problem faced:
1. Again with index like equal and greater than condition


'''
#input_arr = [3, 5, 9 , 66, 99, 65 , 33, 22 , 11 , 6, 1]

input_arr = [4, 98, 99, 65 , 33, 22 , 11 , 6, 1]
def find_max_number(input_arr, low, high):
    
    
    mid = low + int((high - low) / 2 )
    print ("mid " + str(mid) + "low " + str(low) + "high " + str(high))
    
    #if (mid == low or mid == high):
    #   return input_arr[mid]
        
    if (low + 1 == high):
        print ("here")
        if (input_arr[low] > input_arr[high]):
            print (input_arr[low])
        else:
            print (input_arr[high])
            
    if (input_arr[mid] > input_arr[mid+1] and input_arr[mid] > input_arr[mid-1]):
        print (input_arr[mid])
        
    if (input_arr[mid] > input_arr[mid+1] and input_arr[mid] < input_arr[mid-1]):
        find_max_number(input_arr, low, mid-1)
    else:
        find_max_number(input_arr, mid+1, high)
        

res = find_max_number(input_arr, 0, len(input_arr) - 1)

print (res)
