############## Insertion sort #####################

def swap(lst,a,b):
    lst[a],lst[b] = lst[b],lst[a]
    
def push_down(lst,i):
    j = i
    while j > 0:
        if lst[j-1] > lst[j]:
            swap(lst,j,j-1)
        j -= 1
                      
def ins_sort(lst):
    n = len(lst)
    i = 0
    while i < n:
        push_down(lst,i)
        i += 1
        
    print(lst)
        
# a = [2,1,4,3,6,0]
# b = ins_sort(a)


###############    selection sort    ##############


def find_min(lst,start):
    min_ind = start
    for i in range(start,len(lst)):
        if lst[i] < lst[min_ind]:
            min_ind = i
    # print(min_ind)
            
    return min_ind
    
    
def sel_sort(lst):
    n = len(lst)
    i = 0
    
    while i < n :
        a = find_min(lst,i)
        swap(lst,i,a)
        i += 1
        
    print(lst)
        
    
# a = [2,1,4,3,6,0]
# b = sel_sort(a)


##################### quick sort #############################

def partition(lst,h,k):
	
	i = h
	j = k
	pivot = lst[h]

	while i < j :
		if lst[i+1] <  pivot :
			lst[i],lst[i+1] = lst[i+1],lst[i]
			i += 1

		else:
			lst[i+1],lst[j] = lst[j],lst[i+1]
			j -= 1

	return i

def quick_sort(lst,h,k):

	if h > k :
		return

	else:
		p = partition(lst,h,k)
		quick_sort(lst,h,p-1)
		quick_sort(lst,p+1,k)


        