def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

arr = [45, 7, 8, 9, 1, 5, 7 ,8 ,9, 2 ,11]
sorted_arr = quick_sort(arr)
print("Arreglo ordenado:")
print(sorted_arr)
