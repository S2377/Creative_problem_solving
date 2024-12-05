           
# def dutch_flag(lst):
#     start = 0
#     middle = 0
#     end = len(lst) - 1

#     while middle <= end:
#         if lst[middle] == 0:
#             lst[start], lst[middle] = lst[middle], lst[start]
#             start += 1
#             middle += 1
#         elif lst[middle] == 1:
#             middle += 1
#         else:
#             lst[middle], lst[end] = lst[end], lst[middle]
#             end -= 1

#     return lst


   
def dutch_flag(lst,pivot):
    low = 0
    i = 0
    high = len(lst) - 1
    while i <= high:
        if lst[i] > pivot:
            lst[i], lst[high] = lst[high], lst[i]
            high -= 1
           
        elif lst[i]< pivot:
            lst[i], lst[low] = lst[low], lst[i]
            low += 1
            i += 1
            
        else:
            i += 1
            
    return lst

a = dutch_flag([2, 1, 1, 0, 2, 1,0],1)
a = dutch_flag([3, 5, 6, 9, 2, 5,7,4],5)
print(a)




# def isDuplicate(s):
#     a = set()
    
#     for i in s:
#         if i not in a:
#             a.add(i)
            
#         else:
#             return True
        
#     return False


# print(isDuplicate('shivams'))



# def removeDuplicateLetters( s):
#         """
#         :type s: str
#         :rtype: str
#         """

#         a = set()
#         for i in s:
#             if i not in a:
#                 a.add(i)

#             else:
#                 continue
            
#         sorted_list = sorted(list(a))
#         print(sorted_list)

#         ans =''
#         for i in sorted_list:
#             ans =   ans + i
            
#         print(ans)

#         return ans
    
# removeDuplicateLetters("bcabc")
# from collections import deque, defaultdict
# graph = defaultdict(list)

# lst = [[0,1],[0,2],[2,6]]
# for u,v in lst:
#     graph[u].append(v)
#     graph[v].append(u)
    
# print(graph)

