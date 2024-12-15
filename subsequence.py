def print_all_subsequence(n,seq,lst):
    if n < 0:
        print(seq)
        return
    # pick   
    seq.append(lst[n])
    print_all_subsequence(n-1,seq,lst)
    
    # not pick
    seq.pop()
    print_all_subsequence(n-1,seq,lst)
    

print_all_subsequence(2,[],[3,1,2])