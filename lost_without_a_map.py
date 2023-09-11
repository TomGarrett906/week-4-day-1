'''8KYU - LOST WITHOUT A MAP

Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''


#O(N)- has to iterate through a list
a = [1, 2, 3] #O(N) - mutiple iterations

def maps(a): #O(1) - a is a constant her just calls once
    result = [] #O(1) setting varible passes through once
    for num in a: #O(N) for loop interates each time for the list
        num *= 2  #O(n) does this  calculation more than once
        result.append(num)  #O(N) has to append more than once
    return result   #O(1) just the result, a constant