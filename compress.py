def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    string  = ''
    for i in chars:
        if i not in string:
            string += i

    ans = []
    
    for i in string:
        count = str(chars.count(i))
        ans.append(i)
        ans.append(count)
    # print(ans)
    return len(ans)


chars = ["a","a","b","b","c","c","c"]

a = compress(chars)
print(a)