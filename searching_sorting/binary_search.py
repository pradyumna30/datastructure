a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
low = 1
high = len(a)
print (high)

def binary_search(key, low, high, a):
     
    if (low > high):
        print("element not found")
        return
    
    mid = low + int((high - low) / 2)
    
    if (a[mid] == key):
        print ("Element found")
    elif (a[mid] > key):
        high = mid -1
        binary_search(key, low, high, a)
    elif (a[mid] < key):
        low = mid + 1
        binary_search(key, mid, high, a)
        
binary_search(-8, 0, 9, a) 
