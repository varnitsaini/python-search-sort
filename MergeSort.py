"""
Illustrating merge sort
TIME COMPLEXITY: O(n log(n))
SPACE COMPLEXITY: O(log n)
"""

"""initialising array for selection sort"""
arr = [21, 45, 100, 2, 40, 39, 84, 67, 59, 84]

"""function to merge two arrays"""
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    a = arr[:(len(arr))/2]
    b = arr[(len(arr))/2:]

    a = mergeSort(a)
    b = mergeSort(b)
    return merge(a, b)

"""function to sort two arrays"""
def merge(arr1, arr2):
    print arr1, arr2

    arr = []
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            arr.append(arr2[0])
            arr2.remove(arr2[0])
        else:
            arr.append(arr1[0])
            arr1.remove(arr1[0])

    while arr1:
        arr.append(arr1[0])
        arr1.remove(arr1[0])

    while arr2:
        arr.append(arr2[0])
        arr2.remove(arr2[0])

    return arr

print mergeSort(arr)