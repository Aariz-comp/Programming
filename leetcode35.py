def binary_search(arr, target):
    left=0
    right=len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
print(f"Target found at index: {result}")
