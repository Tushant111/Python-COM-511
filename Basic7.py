#sorting using bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [45, 22, 11, 78, 34, 21, 1]

bubble_sort(array1)
bubble_sort(array2)

print("Sorted Array 1:", array1)
print("Sorted Array 2:", array2)
