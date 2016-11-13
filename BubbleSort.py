"""
Illustrating bubble sort
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(1)
"""

"""initialising array for bubble sort"""
arr = [21, 45, 100, 84, 2, 40, 17, 67, 59, 84]

"""
function for bubble sort
Args:
    inputArray: array which is to be sorted
Returns:
    sorted array
"""
def bubbleSort(inputArray):
    for i in range(0, len(inputArray)):
        for j in range(0, len(inputArray) - 1):
            if inputArray[j] > inputArray[j + 1]:
                inputArray[j], inputArray[j + 1] = inputArray[j + 1], inputArray[j]

    return arr

print bubbleSort(arr)