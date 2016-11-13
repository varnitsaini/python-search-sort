"""
Illustrating selection sort
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(1)
"""

"""initialising array for selection sort"""
arr = [21, 45, 100, 84, 2, 40, 17, 67, 59, 84]


"""
function for selection sort
Args:
    inputArray: array which is to be sorted
Returns:
    sorted array
"""
def  selectionSort( inputArr ):
    for index in range(0, len(inputArr) - 1):
        minValue = inputArr[index]
        minValueIndex = index
        for i in range(index, len(inputArr)):
            if inputArr[i] < minValue:
                minValue = inputArr[i]
                minValueIndex = i

        inputArr[index], inputArr[minValueIndex] = inputArr[minValueIndex], inputArr[index]

    return inputArr

print selectionSort(arr)