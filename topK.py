
def topK(num,k):
    num_map = {} 
    for i in num:
        if i not in num_map:
            num_map[i] = 1    
        else:
            num_map[i] += 1
            
    max_freq = max(num_map.values())
    
    bucket = [[] for _ in range(max_freq+1)]
    
    for key,val in num_map.items():
        bucket[val].append(key)
        
    result = []
    count = 0
    for i in range(len(bucket)-1,-1,-1):
        for j in bucket[i]:
            result.append(j)
            count += 1
            if count >= k:
                return result
            
    
                
# nums1 = [1, 2, 2,2, 3, 3, 3,6,5,5,5,5,5,5,5]
nums1=[1,1,1,2,2,3,3,3]
a = topK(nums1,2)

print(a)