import os 
import sys

directory = input(r"Please enter the directory you want to read in: ")
if not os.path.isdir(directory):
    print("Unable to find directory: "+ directory)
    sys.exit()
else:
    print("\nReading directory: " + directory + "\n")

    
filesToNumTimes = {}
filetypeAtts = {}

for root, directories, files in os.walk(directory):
    for file in files:
        myfilepath = os.path.join(root, file)
        currfileSize = os.path.getsize(myfilepath)
        filetype = os.path.splitext(file)[1]
        
        if filetype in filesToNumTimes:
            filesToNumTimes[filetype] += 1
        else:
            filesToNumTimes[filetype] = 1  #when new file type is seen, add file type as key, initialized with value of 1
            
        if filetype in filetypeAtts:
            atts = filetypeAtts[filetype]
            atts[0] = (atts[0] + currfileSize)
            if atts[1] > currfileSize:
                atts[1] = currfileSize
            if atts[2] < currfileSize:
                atts[2] = currfileSize
            filetypeAtts[filetype] = atts  
        else:
            filetypeAtts[filetype] = [currfileSize, currfileSize,
                                      currfileSize] # add new filetype/key with a list of values of [total, min, max] sizes


            
if filesToNumTimes:
    print("The file extensions (key) in this directory and their respective count (value) are:\n")
    print(filesToNumTimes,"\n")
    print("{:<10}{:>42}".format("EXTENSION" , "COUNT\n"))
    for k,v in sorted(filesToNumTimes.items()):     #printing out filestoNumTimes as a sorted dictionary in alphabetical order with format specifiers
        print("{:<10}{:>40}".format(k,v))
    print()    
    print()
        
    print("The file extentions (key) and their total, minimum and maximum sizes in a respective list (value) are:\n")
    print(filetypeAtts,"\n")
    print("{:<10}{:>43}".format("EXTENSION" , "[TOTAL, MIN, MAX]\n"))
    for k,v in sorted(filetypeAtts.items()):     #printing out filetypeAtts as a sorted dictionary in alphabetical order with format specifiers
        print("{:<10}{!s:>42}".format(k,v))	 #formating the list of total, min, max with !s string conversion
    print()
    print()
        
    print("\n\t\t\t\t--------------------Summary------------------\n\n")
    
    print("There are a total of " + str(sum(filesToNumTimes.values())) + " files in this folder.\n")


    for filetype, typeAtts in sorted(filetypeAtts.items()):  
        avg= (filetypeAtts[filetype][0]) / filesToNumTimes[filetype]
        print("There are " + str(filesToNumTimes[filetype]) + " of File type " + filetype)	#printing out the average, min, max of respective file type
        print("Average size is " + str(avg) + " bytes - minimum is " + str(typeAtts[1]) +" bytes - maximum is " + str(typeAtts[2])+" bytes.\n")
       
else:
    
    print("There are no files in this directory.")

    
