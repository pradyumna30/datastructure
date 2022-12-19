'''
The problem faced during implementation
1. Problem with indexes to start with
2. Not copying the array to original array hence the problem came.


'''
# merge sorted
input_arr = [1, 4, 6, 34, 5, 67, 7, 99, -1]

result_arr = [0, 0 , 0 , 0 , 0, 0, 0, 0, 0]

#print (len(input_arr))
def merge(input_arr, result_arr, low, high, mid):
    
    i, p = low, low
    k, j = high, mid  + 1 
    
    while (i <= mid and j <= k):
        
        if input_arr[i] <= input_arr[j]:
            result_arr[p] = input_arr[i]
            p = p + 1
            i = i + 1
        elif input_arr[i] > input_arr[j]:
            result_arr[p] = input_arr[j]
            p = p + 1
            j = j + 1
        
    while (i <= mid):
        result_arr[p] = input_arr[i]
        p = p + 1
        i = i + 1
    
    while (j <= high):
        result_arr[p] = input_arr[j]
        p = p + 1
        j = j + 1
    
    print ("low " + str(low) + "high " + str(high) + "mid " + str(mid))
    #g = g + 1
    print ("recursion" + str(result_arr))
    for s in range(low, high+1):
        input_arr[s] = result_arr[s]
    
    
def divide(input_arr, result_arr, low, high):
  
    #print (input_arr[int((low + high)/2)])
    
    if (low == high):
        return
   
    mid = int((low + high)/2)
    
    divide(input_arr, result_arr, low, mid)
    divide(input_arr, result_arr, mid + 1, high)
    merge(input_arr, result_arr, low, high, mid)
    
divide(input_arr, result_arr, 0, len(input_arr) -1)

print (input_arr)
print (result_arr)

