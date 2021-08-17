from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

# 자주 사용되는 표준 라이브러리
# 1. itertiools - 반복되는 형태의 데이터를 처리하는 기능을 제공, 순열과 조합 라이브러리를 제공
# 2. heapq - 힙 기능을 제공하는 라이브러리, 우선 순위 큐 기능을 구현
# 3. bisect - 이진 탐색 기능을 제공하는 라이브러리
# 4. collections - 덱, 카운터 등의 유용한 자료구조를 포함
# 5. math - 수학적인 기능을 제공

# . itertitools

# - permutations : r개의 데이터를 뽑아 나열하는 모든 경우(순열)
data = [1, 2, 3]
result = list(permutations(data))
print('1', result)

# - combinations : r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)
result1 = list(combinations(data, 2))
print('2', result1)

# - product : r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다. 다만 원소를 중복하여 뽑는다.
result = list(product(data, repeat=2))
print('3', result)

# combinations_with_replacement : r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다. 다만 원소를 중복하여 뽑는다.
result = list(combinations_with_replacement(data, 2))
print('4', result)
