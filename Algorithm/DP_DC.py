# 정의
#동적 계획법 (DP)
# 큰 문제를 작은 부분 문제를 해결하여 최종적으로 전체 문제를 해결하는 알고리즘이다.
# 가장 최하위의 해답을 저장한 후 이를 이용하여 큰 문제를 풀어 나간다 (중복 문제 다시 계산 X) 이를 Memoization이라 한다.

def fibonacci(n):
    storage = [0 for i in range(n + 1)]
    storage[0] = 0
    storage[1] = 1

    for i in range(2, n + 1):
        storage[i] = storage[i - 1] + storage[i - 2]
    return storage[n]


# 분할 정복
# 문제를 나눌 수 없을 때까지 나누어서 각각을 풀면서 나중에 다시 합쳐 문제의 답을 얻는다.
# 큰 문제를 풀기위해 큰 문제에서 작은 문제로 내려가면서 답을 구하는 방식이다. 주로 재귀 함수를 이용한다.
#작은 문제들은 서로 중복되지 않는다.
# ex) 병합 정렬, 퀵 정렬 등

# 재귀함수 풀이
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # 같은 문제를 여러번 풀게 되는 단점이 있음


# 공통점과 차이점
# 공통점
# 문제를 쪼개어 작은 문제를 풀어 큰 문제를 해결한다.
# 차이점
# 동적 계획법
# 부분 문제가 중복되어 Memoization 기법을 사용한다.
# 분할 정복
# 부분 문제는 중복되지 않는다.