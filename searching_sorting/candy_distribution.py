'''
There are N children standing in a line with some rating value. 
You want to distribute a minimum number of candies to these children such that:

Each child must have at least one candy.
The children with higher ratings will have more candies than their neighbors.
You need to write a program to calculate the minimum candies you must give.

'''


def candy_distribution(rating):
    
    left = [1] * len(rating)
    right = [1] * len(rating)
    
    i = 1
    candy = 0
    for j in range(i, len(rating)):
        if rating[j] > rating[j-1]:
            left[j] = left[j-1] + 1
            
    for j in range(len(rating) -2, 0, -1):
        if rating[j] > rating[j+1]:
            right[j] = right[j+1] + 1
            
    for i in range(0, len(rating)):
        candy = candy + max(left[i], right[i])
    
    print (candy)    
    print (left)
    print (right)
    
candy_distribution([1, 5, 2, 1])    
