def find_magic_index(arr):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            return mid  # Magic index found

        elif arr[mid] < mid:
            start = mid + 1  # Search in the right half
        else:
            end = mid - 1  # Search in the left half

    return -1  # No magic index found

# Example usage:
arr = [-1, 0, 1, 3, 5, 7, 9]
result = find_magic_index(arr)
print("Magic index:", result if result != -1 else "No magic index found")
