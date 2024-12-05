from collections import Counter

def topKFrequent(nums, k):
    # Step 1: Count frequencies
    freq_map = Counter(nums)
    
    # Step 2: Initialize buckets
    max_freq = len(nums)
    buckets = [[] for _ in range(max_freq + 1)]

    
    for num, freq in freq_map.items():
        buckets[freq].append(num)
        
    print(buckets)
    
    # Step 3: Extract the top k frequent elements
    result = []
    for freq in range(max_freq, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result


nums1 = [1, 2, 2,2, 3, 3, 3,6]
k1 = 2
print(topKFrequent(nums1, k1))  # Output: [2, 3]

# Example 2
# nums2 = [7, 7]
# k2 = 1
# print(topKFrequent(nums2, k2))  # Output: [7]
