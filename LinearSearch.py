
"""Initialising array for linear search"""
arr = [21, 45, 100, 2, 40, 39, 67, 59, 84]

"""Iterating through the array to find the item else return -1"""
def linearSearch(item):
    for i in range(0, len(arr)):
        if arr[i] == item:
            return i
    return -1

print linearSearch(59)

