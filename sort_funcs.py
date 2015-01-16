__author__ = 'Prashant Bhuyan'

#
#
#1. fill in this function
#   it takes a list for input and return a sorted version
#   do this with a loop, don't use the built in list functions
def sortwithloops(input):

    for i in range(1, len(input)):
        li = input[i]
        j = i
        while j > 0 and input[j-1] > li:
            input[j] = input[j-1]
            j = j-1
        input[j] = li


    return input #return a value

#2. fill in this function
#   it takes a list for input and return a sorted version
#   do this with the built in list functions, don't us a loop
def sortwithoutloops(input):

    li = []
    for i in input:
        li.append(i)

    li.sort()


    return li  #return a value

#3. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with a loop, don't use the built in list functions
def searchwithloops(input, value):

    listSize = len(input)
    valueFound = False
    valueLocation = 0
    currentLocation = 0
    while((currentLocation < listSize) and (not valueFound) and (input[currentLocation]<=value)):
        if(input[currentLocation] == value):
            valueFound = True
            valueLocation = currentLocation
        currentLocation = currentLocation+1




    return valueFound

#4. fill in this function
#   it takes a list for input and a value to search for
#	it returns true if the value is in the list, otherwise false
#   do this with the built in list functions, don't use a loop
def searchwithoutloops(input, value):

    val = input.__contains__(value)

    return val


if __name__ == "__main__":
    L = [5,3,6,3,13,5,6]

    #print sortwithloops(L) # [3, 3, 5, 5, 6, 6, 13]
    #print sortwithoutloops(L) # [3, 3, 5, 5, 6, 6, 13]
    #print searchwithloops(L, 5) #true
    #print searchwithloops(L, 11) #false
    #print searchwithoutloops(L, 5) #true
    #print searchwithoutloops(L, 11) #false
