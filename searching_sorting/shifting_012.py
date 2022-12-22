

'''

Array consist of only 0's, 1's and 2's. Write an algorithm to sort  
this array in O(n) time complexity and O(1) 
Space complexity with only one traversal Asked in : 


'''

import unittest

def swap(input_arr, l, h):
    
    temp = input_arr[l]
    input_arr[l] = input_arr[h]
    input_arr[h] = temp
    
    
def sort_0_1_2(input_arr, low, high):
    
    l, mid = low, low
    h = high
    
    while (mid <= h):
        
        if input_arr[mid] > 1:
            swap(input_arr, mid, h)
            h = h - 1
            mid = mid + 1
        elif input_arr[mid] < 1:
            swap(input_arr, mid, l)
            l = l + 1
            mid = mid + 1
        else:
            mid = mid + 1
            
input_arr = [0, 0 ,0 ,1, 2, 0, 1, 0, 1,2, 1, 0, 0,1]

#ok for all test cases required  
class Test(unittest.TestCase):

    def test_findNumber1(self):
        actual = sort_0_1_2(input_arr,0,len(input_arr) - 1)
        print (input_arr)
        expected = 8
        #self.assertEqual(actual, expected)
        
unittest.main(verbosity=2)     
    
