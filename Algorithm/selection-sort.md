## **1. 선택 정렬(selection sort) 이란?**

- 다음과 같은 순서를 반복하며 정렬하는 알고리즘
  1. 주어진 데이터 중, `최소값`을 찾음
  2. 해당 최소값을 데이터 `맨 앞에 위치한 값`과 교체함
  3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함
     - [selection Sort](ttps://visualgo.net/en/sorting)


## **2. 알고리즘 설명**

- 데이터가 두 개 일때
    - 예 : data_list = `[ 9, 1 ]`
        - `data_list[0] > data_list[1]` 이므로 `data_list[0]`의 값과 `data_list[1]` 값을 교환
- 데이터가 세 개 일 때
    - 예 : data_list = `[ 9, 1, 7 ]`
        - 처음 한번 실행하면 `[ 1, 9, 7 ]`
        - 두 번째 실행하면 `[ 1, 7, 9 ]`
- 데이터가 네 개 일때
    - 예 : data_list = `[ 9, 3, 2, 1 ]`
        - 처음 한번 실행하면 `[ 1, 3, 2, 9 ]`
        - 두 번째 실행하면 `[ 1, 2, 3, 9 ]`
        - 세 번째 실행하면 변화 없음

## **3. 알고리즘 구현**

1. `for stand in range(len(data_list) - 1)` 로 반복
2. `lowest = stand` 로 놓고,
3. `for num in range(stand, len(data_list)) stand `이후부터 반복
    - 내부 반복문 안에서 `data_list[lowest] > data_list[num]` 이면,
        - `lowest = num`
4. `data_list[num], data_list[lowest] = data_list[lowest], data_list[num]`

## **4. Code 구현**

- selection_sort함수 : 선택정렬 하는 함수
```python
def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data
```

- selection_sort를 사용하는 코드
```python
import random

data_list = random.sample(range(100), 10)
selection_sort(data_list)
```

## **5. 알고리즘 분석**
- 반복문 2개
    - $O(n^2)$
- 실제 분석
    - $n*n(n-1)/2$