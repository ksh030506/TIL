# BFS
# 탐색 방법으로서 너비 우선 탐색의 약자이다.
# 횡으로 움직이면서 지점을 탐색하는 것이다.
# 시작 지점으로 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 지점을 나중에 방문하는 개념이다.
# 주로 최단 경로를 찾고 싶을 때 BFS를 사용한다. 대표적으로 다익스트라 알고리즘에서 사용된다.

# 구현
# 큐를 이용해 구현한다. 먼저 들어온 순서대로 뽑아낼 수 있기 때문이다.
# 1. 지점들(vertex)를 순서대로 큐에 넣고 하나 뽑고(pop)
# 2. 그 뽑은 지점의 하위 경로를 다시 큐에 넣고
# 3. 그 다음 지점을 큐에서 뽑고
# 4. 그 지점의 하위 경로를 다시 큐에 넣고.. 하는 식으로 진행된다.
# 이렇게 구현하면 먼저 넣은 지점들부터 탐색하고 그 후 그 지점들의 하위 지점들을 탐색하는 식으로 진행된다.

# 코드
# 인접간선 설명
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'G', 'H'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E'],
    'G': ['C'],
    'H': ['C'],
}


def iterative_bfs(start_vertex):
    visited = [start_vertex]
    queue = [start_vertex]
    while queue:
        vertex = queue.pop(0)
        for item in graph[vertex]:
            if item not in visited:
                print(visited)
                visited.append(item)
                queue.append(item)
    return visited


iterative_bfs('A')
