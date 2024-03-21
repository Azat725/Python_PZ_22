def quick_sort(array: list) -> int:
    if len(array) <= 1:
        return array
    
    else:
        pivot = array[0]
        low = [x for x in array[1:] if x <= pivot]
        heigh = [x for x in array[1:] if x > pivot]
        
        return quick_sort(low) + [pivot] + quick_sort(heigh)
    
arr = [3, 6, 8, 10, 1, 2]
print(quick_sort(arr))