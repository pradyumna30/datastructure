'''
An array is given as Input where ith element is the price of a given stock on day 
You were permitted to complete unlimited transaction. 
Derive an algorithm to find the maximum profit in O(n) 
Time complexity and O(n) Space Complexity Asked in: Amazon, Microsoft, Flipkart, DE-Shaw

'''

input_price = [1, 10, 8, 20, 25, 90, 10, 45, 10, 12]

def get_max_profit(input_price):
    
    buy_sell = []
    local_min = input_price[0]
    local_max = -1
    
    i = 0 
    k = len(input_price) - 1
    
    while ( i < k ):
        print (i)
        
        if input_price[i+1] < local_min:
            local_min = input_price[i+1]
            i = i + 1
            continue
        else:
            if local_min != -1:
                buy_sell.append(local_min)
                local_min = -1
            
        if input_price[i+1] < input_price[i]:
            local_max = input_price[i]
            buy_sell.append(local_max)
            local_min = input_price[i + 1]
            
        i = i + 1    
    buy_sell.append(input_price[k])
    
    print (buy_sell)    
        
    
    
get_max_profit(input_price) 
