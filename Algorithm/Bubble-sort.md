# 버블 정렬

## **정렬(sorting) 이란?**

- 정렬 : 어떤 데이터들이 주어졌을때 이를 정해진 순서대로 나열하는 것
- 정렬은 프로그램 작성시 빈번하게 필요로 함
- 다양한 알고리즘이 고안되었으며, 알고리즘 학습이 필수!😄

> 다양한 알고리즘 이해를 통해 동일한 문제에 대해 다양한 알고리즘이 고안될 수 있음을 이해하고, 각 알고리즘간 성능 비교를 통해, 알고리즘 성능 분석에 대해서도 이해할 수 있음 ❤️


## **버블 정렬(bubble sort) 이란?**

- 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면 자리를 바꾸는 알고리즘
  - [Bubble Sort](https://visualgo.net/en/sorting)

![https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

## **버블 정렬 알고리즘 설명**

* 데이터가 4개 일 때 (데이터 개수에 따라 복잡도가 떨어지는 것은 아니므로, 네 개로 바로 로직을 이해할 수 있다.)
  * 예 : data_list = [ 1, 9, 3, 2 ]
    * 1차 로직
      * 1 과 9 비교, 자리바꿈 없음 [ 1, 9, 3, 2 ]
      * 9 와 3 비교, 자리바꿈 [ 1, 3, 9, 2 ]
      * 9 와 2 비교, 자리바꿈 [ 1, 3, 2, 9 ]
    * 2차 로직
      * 1 과 3 비교, 자리바꿈 없음 [ 1, 3, 2, 9 ]
      * 3 과 2 비교, 자리바꿈 [ 1, 2, 3, 9 ]
      * 3 과 9 비교, 자리바꿈 없음  [ 1, 2, 3, 9 ]
    * 3차 로직
      * 1 과 2 비교, 자리바꿈 없음 [ 1, 2, 3, 9 ]
      * 2 과 3 비교, 자리바꿈 없음 [ 1, 2, 3, 9 ]
      * 3 과 9 비교, 자리바꿈 없음 [ 1, 3, 3, 9 ]


## **알고리즘 구현 with ```Python```**


* 특이점 찾아보기
  * n개의 리스트가 있는 경우 최대 n-1번의 로직을 적용한다.
  * 로직을 1번 적용할 때마다 가장 큰 숫자가 뒤에서부터 1개씩 결정된다.
  * 로직이 경우에 따라 일찍 끝날 수도 있다. 따라서 로직을 적용할 때 한 번도 데이터가 교환된 적이 없다면 이미 정렬된 상태이므로 더 이상 로직을 반복 적용할 필요가 없다.

  **알고리즘 순서**
  1. for num in range(len(data_list)) 반복
  2. swap = 0 (교환이 되었는지를 확인하는 변수를 두자)
  3. 반복문 안에서, for index in range(len(data_list) - num - 1) n - 1번 반복해야 하므로
  4. 반복문안의 반복문 안에서, if data_list[index] > data_list[index + 1] 이면
  5. data_list[index], data_list[index + 1] = data_list[index + 1], data_list[index]
  6. swap += 1
  7. 반복문 안에서, if swap == 0 이면, break 끝

## **코드**

```python
def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
  
        if swap == False:
            break
    return data
```





python
def bubblesort(data):
for index in range(len(data) - 1):
swap = False
for index2 in range(len(data) - index - 1):
if data[index2] > data[index2 + 1]:
data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
swap = True

if swap == False:
break
return data
