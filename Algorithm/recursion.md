# Recursion

## 재귀 용법
> 고급 정렬 알고리즘에서 재귀 용법을 사용

### 재귀 용법(recursive call), 재귀 호출
- 함수 안에서 동일한 함수를 호출하는 형태

### 예제
- 팩토리얼 => Recursive Call

### 예제 - 분석하기
- 간단한 경우
  - 2! = 1 * 2
  - 3! = 3 * 2 * 1
  - 4! = 4 * 3 * 2 * 1 = 4 * 3!
- 규칙 : n! = n * (n-1)!
  - 함수를 하나 만든다
  - 함수(n)은 n > 1 이면 return n * 함수(n)
  - 함수(n)은 n = 1 이면 return n
- 검증(코드로 검증하지 않고, 직접 간단한 경우부터 대입해서 검증해야함)
  - 먼저 2!
    - 함수(2) 이면 2 > 1 이므로 2 * 함수(1)
    - 함수(1) 은 1 이므로, return 2 * 1 = 2
  - 3! 검증
    - 함수(3)이면 3 > 1 이므로 3 * 함수(2)
    - 함수(2)는 결국 1번에 의해 2! 이므로, return 2 * 1 = 2
    - 3 * 함수(2) = 3 * 2 = 3 * 2 * 1 = 6
  - 4!
    - 함수(4) 이면, 4 > 1 이므로 4 * 함수(3)
    - 함수(3)은 결국 2번에 의해 3 * 2 * 1 = 6
    - 4 * 함수(3) = 4 * 6 = 24

```python
def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num

for num in range(10):
    print(factorial(num))
```

### 예제 - 시간 복잡도와 공간 복잡도
- factorial(n)은 factorial() 함수를 호출해서, 곱셈을 함
  - 일종의 n - 1번 반복문을 호출할 것과 동일
  - factorial() 함수를 호출할 때마다, 지역변수 n이 생성
- 시간 복잡도/공간 복잡도는 O(n-1)이므로, 둘다 O(n)

### 재귀 호출의 일반적인 형태
```python
def function(입력):
    if 입력 > 일정값: #입력이 일정 값 이상이면
        return function(입력 - 1)
    else:
        return 일정값 #재귀 호출 종료
```

```python
def function(입력):
    if 입력 <= 일정값:
        return 결과값
    function(입력보다 작은 값)
    return 결과값
```

### 재귀 호출은 스택의 전형적인 예이다
- 함수는 내부적으로 스택처럼 관리한다


