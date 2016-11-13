

"""
Initialising sorted array for binary search.
Pre requisite for binay search is that input array should be in sorted order
COMPLEXITY : O(log(n))
"""
arr = [2, 21, 39, 40, 45, 59, 67, 84, 100]


"""
function for binary search
Args:
    inputArr: input array in which item is to be searched for
    value: the value which is to be searched for in the array
"""
def binarySearch(inputArr, value):
    min = 0
    max = len(inputArr) - 1
    while(min <= max):
        mid = (max + min) / 2
        if inputArr[mid] > value :
            max = mid - 1
        elif inputArr[mid] < value :
            min = mid + 1
        else:
            return mid

    return -1

print binarySearch(arr, 102)