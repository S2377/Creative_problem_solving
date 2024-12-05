def find_subsets_iterative(nums):
    subsets = [[]]  # Start with an empty subset

    for num in nums:
        # For each element, add it to all existing subsets
        new_subsets = [subset + [num] for subset in subsets]
        subsets.extend(new_subsets)

    return subsets

# Example usage:
nums = [1, 2, 3]
print("All subsets:", find_subsets_iterative(nums))
