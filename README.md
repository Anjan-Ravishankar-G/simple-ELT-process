# simple-ELT-process
NULL INNOVATION TECHNICAL TEST

to create 3 different components
Extract(read)
Transform
Load(write)

part 1: we will convert the extracted data to capital letters and load it into a new file 
part 2: we will convert the extracted data to find unique words and find the count of words and write in to a new file.

APPROACH
Will be explaining the idea flow to approach the problem 
 EXTRACT-
 1. we will be getting user input for the file directory(will be considering TXT file for example)
 2. open the file , read it and assign it to a variable and close the file
 (we will be doing both the parts in a single file , so we will use if statement so it corresponds to the specific part)
 
 TRANSFORM-
 part1:
 1.we will be passing the extracted data from extract to transform func .
 2.we will use .upper() method and assign it to a variable(this is all about part 1)
 
 part2:
 1.we will be passing the extracted data from extract to transform func .
 2.we will convert all the data to lower case using .lower(), and we will remove all the punctuations using for-loop to runthrough every char and use if-statement and     replace-method to remove punctuation's from the string
 3.then we will convert it ino array of words using .split() ,then using Counter from collections we will convert it to counter,so we get the count for every words and append require values in a list
 
 LOAD-
 part1:
 1.req user input for the file directory with file name <will be considering txt file for example> use write func to write it into the user providef file and close the   file.
 part2:
 1.req user input for the file directory with file name <will be considering txt file for example> 
 2.use write func to write line by line using for loop so that we get ouit put in our desired format and close the file. 
 
