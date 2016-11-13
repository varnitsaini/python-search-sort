
"""
Initialising sorted array for binary search.
Pre requisite for binay search is that input array should be in sorted order
COMPLEXITY : O(log(n))
"""
arr = [2, 21, 39, 40, 45, 59, 67, 84, 100]

"""
function for binary search
Args:
    inputArray: input array in which item is to be searched for
    value: the value which is to be searched for in the array
    min: minimum index to start search from
    max: maximum index to start search from
"""
def binarySearch(inputArray, value, min, max):
    mid = (min + max) / 2
    if min <= max :
        if inputArray[mid] < value:
            return binarySearch(inputArray, value, mid + 1, max)
        elif inputArray[mid] > value:
            return binarySearch(inputArray, value, min, mid - 1)
        else:
            return mid
    return -1


min = 0
max = len(arr) - 1
print binarySearch(arr, 101, min, max)