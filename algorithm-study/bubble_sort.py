def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n-1,0,-1): # 6 to 1 (마지막 바로전 자료)
        # 마지막 i 원소는 정렬이 이루어진 상태가  유지됨
        for j in range(0, i):
            # 0 to n-i-1 (j는 0-5, 0-4, 0-3, 0-2, 0-1, 0 까지 진행)
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] =arr[j+1], arr[j] # 4 3 2 1 5 6 7
                
# 테스트
arr = [7, 6, 5, 4, 3, 2, 1]

bubbleSort(arr)

print("정렬된 배열은 : ")
for i in range(len(arr)):
    print("%d" %arr[i])

