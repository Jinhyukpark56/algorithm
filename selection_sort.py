def selection_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        max_index = largest(arr, i+1)
        arr[i], arr[max_index] = arr[max_index], arr[i]

def largest(arr, n):
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

# 테스트
arr = [84, 35, 18, 20, 13,1 ]
selection_sort(arr)
print("정렬된 배열:", arr)