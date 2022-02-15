######################################################################
# Merge Sort 
# Note: Lists as well as Dicts and Sets are PASSED BY REFERENCE in python
######################################################################

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[mid:]
        right = lst[:mid]
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        
import timeit

lst = [5,4,2,1,5,7,5,3,4,1,6,8,5]

start = timeit.timeit('output = 10*3')

merge_sort(lst)

end = timeit.timeit('output = 10*3')

print(lst)
print(f"was done in {str(end - start)[:6]}ms")

