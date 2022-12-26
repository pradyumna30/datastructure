'''
Write an algorithm to find out next greater number to given number with the same set of digits

'''

def swap(input_arr, a, b):
    temp = input_arr[b]
    input_arr[b] = input_arr[a]
    input_arr[a] = temp
    
def next_largest(input_arr, low, high):
    
    h = high
    l = low
    
    lowest = input_arr[h]
    second_lowest = lowest
    h = h - 1
    
    while (h >= l):
        
        if (input_arr[h] < lowest):
            second_lowest = input_arr[h]
            swap(input_arr, h, high)
            #print (input_arr)
            break
    
        h = h - 1       
    
    #print (h)
    input_arr[h+1:] = sorted(input_arr[h+1:])        
            
    
input_arr = [2, 1 , 8 , 7, 6, 5] 
#input_arr = [5, 3, 4, 9, 7, 6]
print ("Input " + str(input_arr))
next_largest(input_arr, 0, len(input_arr) - 1)   

print(input_arr)
