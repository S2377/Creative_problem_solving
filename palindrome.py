def isPalindrome(s):
    s = s.split()
    
    # print(s)

    s_compressed = ''

    for i in s:
        s_compressed += i 
      
    a_filter = ''  
    for i in s_compressed:
        if i.isalnum():
            a_filter += i
    
    b = a_filter.lower()       
    print(a_filter)   
    s_reversed = ''
    for i in range(len(b)-1,-1,-1):
        s_reversed += b[i]
    

    if b == s_reversed :
        return True

    else:
        return False
    
a = isPalindrome("Was it a car or a cat I saw?")

print(a)
