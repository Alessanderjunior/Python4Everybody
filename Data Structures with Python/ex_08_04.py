# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in 
# the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst2 = list()
#lst = lst.rstrip()
for lst in fh:
    lst = lst.rstrip().split()
    #print(lst)
    for element in lst:
        if element in lst2: continue
        else:
            lst2.append(element) 
            lst2 = sorted(lst2)
#conc = lst2[1]+lst2[2]+lst2[2]

#conc.sort()
      
print(lst2)            
      