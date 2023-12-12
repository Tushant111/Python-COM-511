def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found

# Get user input for the list
user_list_input = input("Enter a sorted list of numbers (comma-separated): ")
data = [int(item.strip()) for item in user_list_input.split(',')]

# Get user input for the target value
target_value = int(input("Enter the target value to search: "))

# Linear search
linear_result = linear_search(data, target_value)
if linear_result != -1:
    print(f"Linear Search: Element {target_value} found at index {linear_result}")
else:
    print(f"Linear Search: Element {target_value} not found in the list")

# Binary search
binary_result = binary_search(data, target_value)
if binary_result != -1:
    print(f"Binary Search: Element {target_value} found at index {binary_result}")
else:
    print(f"Binary Search: Element {target_value} not found in the list")
