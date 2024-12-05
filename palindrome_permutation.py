def palindrome_permutation(string):
    if len(string) == 0 or len(string) == 1:
        return True

    char_dict = {}
    
    # Build a frequency dictionary
    for i in string:
        if i not in char_dict:
            char_dict[i] = 1       
        else:
            char_dict[i] += 1
            
    count = 0
    
    # Check for at most one character with an odd count
    for i in char_dict.values():
        if i % 2 != 0:
            count += 1
            if count > 1:
                return False
    
    return True

# Test examples
print(palindrome_permutation("civic"))
print(palindrome_permutation("ivicc")) 
print(palindrome_permutation("hello")) 
print(palindrome_permutation("aabbh"))  
