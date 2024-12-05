def sub_sort(arr):
    left = 0
    right = len(arr)-1
    
    while left < right and arr[left] <= arr[left+1]:
        left += 1
        
    while right > 0 and arr[right -1] <= arr[right]:
        right -= 1
        
    print(left,right)
    
    mid_arr = arr[left:right+1]
    
    print(mid_arr)
    
    min_num,max_num  =  min(mid_arr),max(mid_arr)
    
    ans = []
    
    i = 0
    
    while i <= left:
        if arr[i] > min_num:
            left = i
            ans.append(left)
            i +=1
            break
        else:
            i += 1
            
    j = len(arr) -1
    
    while  j >= right :
        if arr[j] < max_num:
            right = j
            ans.append(right)
            j -= 1
            break
        
        else:
            j -= 1
        
    return ans
              
    
a = sub_sort([1,2,4,7,10,11,7,12,6,7,16,18,19])

print(a)
    
    