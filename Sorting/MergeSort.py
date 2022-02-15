def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])

        