'''
List of arrival and departure time is given, 
Find the minimum number of platforms are required for the railway as no train waits

'''

def calculate_platform(arrival, departure):
    
    platforms = 0
    max_platform = 0
    i, j = 0, 0
    departure = sorted(departure)
    
    print (arrival)
    print (departure)
    while(1):
        
        if (i == len(arrival) - 1 or j == len(arrival) - 1):
            break
        
        if arrival[i] < departure[j]:
            platforms = platforms + 1
            
            if platforms > max_platform:
                max_platform = platforms
            i = i + 1    
        else:
            platforms = platforms - 1
            j = j + 1

        
    print (max_platform)    
        
arrival = [100, 140, 150, 200, 215, 400, 401] 
departure = [110, 300, 220, 230, 315, 600, 500] 

calculate_platform(arrival, departure)
