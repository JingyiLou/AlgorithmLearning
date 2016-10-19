OrigString = raw_input("please enter a series of random number:")

NumList = OrigString.split()
for j in range(1,len(NumList)):
    key = NumList[j]
    i = j-1
    while i>=0 and NumList[i]>key:
        NumList[i+1] = NumList[i]
        i = i-1
    NumList[i+1] = key

print NumList
