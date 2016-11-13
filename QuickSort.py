"""
Illustrating quick sort
TIME COMPLEXITY worst case: O(n^2)
TIME COMPLEXITY average case: O(log n)
SPACE COMPLEXITY: O(1)
"""

"""initialising array for quick sort"""
arr = [21, 45, 100, 84, 2, 40, 17, 67, 59, 84]

"""
partitions the array taking by placing pivot in correct postion
Args:
    arr: array which is to  be sorted
    low: lower index for the array to be considered
    high: higher index for the array to be considered

Returns:
    pivotindex
    array by placing pivot at correct postion
"""
def partition(arr ,low, high):
    i = low - 1
    pivot = arr[high]

    for index in range(low, high):

        if arr[index] <= pivot:
            i += 1
            arr[i], arr[index] = arr[index], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1, arr


"""
recursively calls the quicksort for further pivoting the array
Args:
    arr: array which is to  be sorted
    low: lower index for the array to be considered
    high: higher index for the array to be considered

Returns:
    array after sorting
"""
def quickSort(arr, low, high):
    if low < high:

        partitionIndex, arr = partition(arr, low, high)

        quickSort(arr, low, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, high)

    return arr

low = 0
high = len(arr) - 1
print quickSort(arr, low, high)