# Greedy
# 현재 상황에서 당장 좋은 것만 고르는 방법
# 정당성 분석이 중요, 단순히 좋아 보이는 것만 선택해도 최적의 해를 구할 수 있는지 검토해야함

# 예시
# 1. 거스름돈 문제
# 최적의 해를 구하기 위해서는 가장 큰 화폐의 단위부터 거슬러 주면됨.
# 그런데 거스름돈 문제에서 큰 거스름돈이 작은 거스름돈의 배수가 아닐 경우
# (800원을 거슬러 줘야하는데 500, 400, 100원이 있는 경우)는 그리디 알고리즘이 최적해를 보장하지 못한다.

def money(n, lst=[500, 100, 50, 10]):
    cnt = 0
    for i in lst:
        cnt += n // i
        n %= i
    return cnt


money(1260)

# 2. 1이 될때까지
# N에 대하여 빼기 1 또는 나누기 K를 적용하여 가장 빨리 1로 만들수 있는 횟수를 구하는 문제
# 2이상의 수로 나눈는 작업이 1을 빼는 작업보다 숫자를 빨리 줄일 수 있기 때문에 나누기를 많이 하도록 유도 => 최적의 해만 선택하려로 하므로 그리디
# 그리디 알고리즘을 사용하도록 유도하는 문제라면 N은 항상 1에 도달하게 된다


def minus_division(n, k):
    result = 0
    while True:
        # N이 K로 나누어 떨이지는 수가 될때까지만 1씩 빼기
        target = (n//k) * k  # K로 나누어지는 가장 큰 수(target) 찾아서
        result += (n-target)  # 그 수를 N에서 빼면 1씩 빼는 횟수
        n = target

        if n < k:  # N이 K보다 작으면 (더 이상 나눌 수 없음) 반복문 탈출
            break

        # K로 나누므로 횟수 +1
        result += 1
        n //= k

    # 마지막으로 남은 수에서 1빼기
    result += (n - 1)
    print(result)
    return result


minus_division(100, 9)

# 3. 곱하기 혹은 더하기
# 0 ~ 9로만 이루어진 문자열이 주어지고, 왼쪽부터 오른쪽으로 하니씩 모든 숫자를 확인하여 숫자 사이에
# 곱하기/더하기 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 문제
# 단 모든 연산은 왼쪽에서부터 순서대로 이루어짐


def multiply_plus(data):
    # 첫 번째 문자를 숫자로 변경하여 대입
    result = int(data[0])
    for i in range(1, len(data)):
        # 두 수 중에서 하나라도 0 또는 1인 경우 더하기 수행
        num = int(data[i])
        if num < 1 or result <= 1:
            result += num
        else:
            result *= num
    print(result)
    return result


multiply_plus("1234567890")
