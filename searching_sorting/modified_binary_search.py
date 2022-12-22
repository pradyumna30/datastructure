

'''

We rotate an ascending order sorted array at some point unknown to user. So for instance, 
3 4 5 6 7 might become 5 6 7 3 4. Modify binary search 
algorithm to find an element in the rotated array in O(log n) time and O(1) Space complexity


'''


import unittest

def findNumber(input_arr, low, high, si): 
    
    
    mid = low + int((high - low) / 2)
    
    if (low == high ):
        return -1
        
    print ("low " + str(low) + " high " + str(high) + " mid " + str(mid))
    print ("low " + str(input_arr[low]) + " high " + str(input_arr[high]) + " mid " + str(input_arr[mid]))
    
    if(low + 1 == high):
        print ("low + 1 = high")
        if input_arr[low] == si:
            return low 
            
        elif input_arr[high] == si:
            return high
        else:
            return -1
           
            
    if input_arr[mid] == si:
        return mid
        
    # input_arr =  [30, 35, 40, 45, 50, 55, 60, 10, 14, 20, 25]
    if (input_arr[mid] > input_arr[low]):
        if (input_arr[low] <= si < input_arr[mid]):
            return findNumber(input_arr, low, mid-1, si)
        else:
            return findNumber(input_arr, mid+1, high, si)
            
    if(input_arr[mid] < input_arr[high]):
        if (input_arr[high] >= si > input_arr[mid]):
            return findNumber(input_arr, mid+1, high, si)
        else:
            return findNumber(input_arr, low, mid-1, si)
   
   
#ok for all test cases required  
class Test(unittest.TestCase):

    def test_findNumber1(self):
        actual = findNumber([3, 4, 5, 6, 7, 8, 9, 10, 1, 2],0,9,1)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber2(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3],0,8,3)
        expected = 8
        self.assertEqual(actual, expected)

    def test_findNumber3(self):
        actual = findNumber([5, 6, 7, 8, 9, 10, 1, 2, 3],0,8,28)
        expected = -1
        self.assertEqual(actual, expected)
    
    def test_findNumber4(self):
        actual = findNumber([30, 40, 50, 10, 20],0,4,10)
        expected = 3
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)     
    
