"""
Illustrating bubble sort
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(1)
"""

"""initialising array for insertion sort"""
arr = [21, 45, 100, 84, 2, 40, 17, 67, 59, 84]

"""
function for insertion sort
Args:
    inputArray: array which is to be sorted
Returns:
    sorted array
"""
def insertionSort(inputArr):
    for i in range(0, len(inputArr)):
        currentVal = inputArr[i]
        pointer = i

        while pointer > 0 and currentVal < inputArr[pointer - 1]:
            inputArr[pointer] = inputArr[pointer - 1]
            pointer -= 1

        inputArr[pointer] = currentVal

    return inputArr


print insertionSort(arr)