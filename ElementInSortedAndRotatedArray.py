

"""
Search function for finding index of element in rotated array
"""
def search(arr, low, high, key):

    """

    :param arr: input array of integers
    :param low: lower index of the array above which the key is to searched for
    :param high: higher index of the array above which the key is to searched for
    :param key: key to be searched for in the array
    :return: returns the index value of the array
    """

    if low > high:
        return -1

    """
    mid element of the arary
    """
    mid = (low + high) / 2

    """
    check if the mid element is equal to the key and return the key
    """
    if arr[mid] == key:
        return mid

    """
    check if first half is sorted
    """
    if arr[low] <= arr[mid]:

        """
        if the key lies in the first half then recursively find the element in that half
        """
        if key >= arr[low] and key <= arr[mid]:
            return search(arr, low, mid - 1, key)

        """
        if the key is not in first half then find in second half
        """
        return search(arr, mid + 1, high, key)

    """
    if first half is not sorted then second half must be sorted and
    check if the key exist in second half
    """
    if key >= arr[mid] and key <= arr[high]:
        return search(arr, mid + 1, high, key)

    """
    if the key doesnt lie in second half then the key must lie in first half so
    search the key in first half of the array
    """
    return search(arr, low, mid - 1, key)


arr = [15, 16, 19, 20, 1, 3, 4, 5, 7]

print search(arr, 0, len(arr) - 1, 16)
