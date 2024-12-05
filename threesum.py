
def twoSum(nums, target, start):
    seen = set()
    res = []
    for j in range(start, len(nums)):
        complement = target - nums[j]
        if complement in seen:
            # Add the pair and skip duplicates
            if not res or res[-1] != [nums[j], complement]:
                res.append([nums[j], complement])
        seen.add(nums[j])
    return res

def threeSum(nums):
    nums.sort() 
    res = []
    
    for i in range(len(nums)):
        # Skip duplicate numbers to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        target = -nums[i]
        two_sum_results = twoSum(nums, target, i + 1)  
        for pair in two_sum_results:
            res.append([nums[i]] + pair)  
            
    return res