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
			swap(lst,i,i+1)
			i += 1

		else: 
			swap(lst,i+1,j)
			j -= 1

	return i



def quick_sort(lst,h,k):

	if h > k :
		return

	else:
		p = partition(lst,h,k)
		quick_sort(lst,h,p-1)
		quick_sort(lst,p+1,k)
    
a = [2,1,4,3,6,0]
b = quick_sort(a,0,len(a)-1)
print(a)


############## Bubble sort #####################

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)
    return arr

# data = [64, 34, 25, 12, 22, 11, 90]
# print("Unsorted Array:", data)
# sorted_data = bubble_sort(data)
# print("Sorted Array:", sorted_data)




################  Merge sort ##############################

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element was left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# data = [38, 27, 43, 3, 9, 82, 10]
# print("Unsorted Array:", data)
# merge_sort(data)
# print("Sorted Array:", data)


    