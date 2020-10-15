def rainfall_statistics(*rainfall_months): #using the star to pass in the multiple values of a list (it takes in 12 arguments for the months of the year)
    total_rainfall = 0
    highest = rainfall_months[0] #set highest to element zero of rainfall_months
    lowest = rainfall_months[0] #set lowest to element zero of rainfall_months
    
    for rainfall in rainfall_months:
        total_rainfall += float(rainfall) #sum of values of the list
        
      
        
        
        average_rainfall = float(total_rainfall /  len(rainfall_months))
    
       
        
        if rainfall < lowest:
            lowest = float(rainfall) #change lowest
            
    
        
    
        if rainfall > highest:
            highest = float(rainfall) #change highest
            
        lowest_month = rainfall_months.index(lowest) #get index of month with lowest rainfall
        highest_month = rainfall_months.index(highest) #get index of month with highest rainfall
        
    return(total_rainfall, average_rainfall, lowest, lowest_month, highest, highest_month)

months = ['JAN', 'FEB', 'MAR','APR','MAY','JUNE','JUL','AUG','SEP','OCT','NOV','DEC']

monthly_rainfall = [] #empty list that will hold respective rainfall values for each corresponding month

for i in range(len(months)):
    monthly_rainfall.append(float(input("Please enter rainfall in centimeters for " + months[i] +": "))) #append rainfall for corresponding month in empty list
    i+1
    

    
total_rainfall, average_rainfall, lowest, lowest_month, highest, highest_month =  rainfall_statistics(*monthly_rainfall) #call function on the list and unpack return tuple into appropriate variables

print("The total rainfall is ", total_rainfall," cm")
print("The average rainfall is ", average_rainfall, " cm")
print("The lowest rainfall is ", lowest," cm on ",months[lowest_month]) 
print("The highest rainfall is ", highest, " cm on ", months[highest_month])
