
def longest_unique_substr(s):
    n = len(s)
    a = set()
    left = 0
    max_len = 0
    
    for right in range(n):
        if s[right] not in a:
            a.add(s[right])
            max_len = max(max_len,right-left+1)
            
        else:
            while s[right] in a:
                a.remove(s[left])
                left += 1   
            a.add(s[right])
                 
    print(max_len)  
longest_unique_substr('shivrvam')


