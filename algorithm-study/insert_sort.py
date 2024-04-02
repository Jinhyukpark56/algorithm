def insert_sort(array=[5,4,3,2,1]):
    n= len(array) # 배열길이
    
    for i in range(1,n):
        # 1(2번째 원소)부터 n-1(마지막원소)까지 # 1번 위치의 값을 key로 저장
        newValue = array[i] # 3
        # 리스트의 i번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        j = i
        while j > 0 and array[j-1] > newValue:
            array[j] = array[j-1] # 3 4 5
            j = j -1
            array[j] = newValue # 찾은 삽입 위치에 key를 저장 1 2 3 4 5
            
array = [5, 4, 3, 2, 1]
insert_sort(array)
print(array)