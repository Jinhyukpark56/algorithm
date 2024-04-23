#선택 정렬 알고리즘

#최솟값 기준

def selection_sort(arr):
    n = len(arr)
    for i  in range(n) : 
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 최댓값 기준

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1,0,-1) :
        max_idx = i
        for j in range(i):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

# ----------------------------------------------------------

# 삽입 정렬

def insert_sort(arr):
    for i in range(i, len(arr)):
        key = arr[i]
        j = i+1
    while j >= 0 and key < arr[j]:
        arr [j+1] = arr [j]
        j -= i
    arr[j+1] = key

# ----------------------------------------------------------

#버블 정렬

def bubble_sort(arr):
    n = len(arr)
    for i in range(i):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]

# ----------------------------------------------------------

# 퀵 정렬

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1 :] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
    
# ----------------------------------------------------------

# 병합 정렬

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid] 
        right_half = arr[:mid] 
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else :
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half) :
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half) :
            arr[k] = left_half[j]
            i += 1
            k += 1
        
# ----------------------------------------------------------

# 힙 정렬

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
