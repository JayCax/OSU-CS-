def selection_sort(input_list):
    for i in range(len(input_list)-1):
        index_smallest = i
        
        for j in range(i+1, len(input_list)):
            if input_list[j] < input_list[index_smallest]:
                index_smallest = j
                
        temp = input_list[i]
        input_list[i] = input_list[index_smallest]  
        input_list[index_smallest] = temp
        
    return input_list

def binary_search(input_list, search_value):
    high = len(input_list) - 1 
    low = 0
    
    while high>= low:
        mid = (high+low) // 2
        
        if input_list[mid] > search_value:
            high = mid - 1
        elif input_list[mid] < search_value:
            low = mid + 1 
        else:
            return mid
    return -1

with open(input(r"Please enter the file you want to read in: ")) as file: #using with statement as context manager, no need to close.
                                                                        #Reading in raw string from input, no need to put "//" in input path
    content_array = file.read().splitlines() # read in array from file and split out the newline character


content_integers = [] #establish empty list 

for i in content_array:
    content_integers.append(int(i)) #append integers from file to empty list 
    

    
sorted_integer_list = selection_sort(content_integers) #call selection_sort function

print("The sorted integer list is: ", sorted_integer_list)

print()

search_value = int(input("Please enter the value you wish to search for: "))

list_search = binary_search(sorted_integer_list, search_value) #call binary_search function

if list_search == -1:
    print(search_value, "was not found in the list") #if function returns not found (-1)
else:
    print(search_value, "was found at position", list_search, "of the list") #if found, print value and corresponding index
