# DFS

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


# 얘는 사전식으로 찾는다
def recursive_dfs(v, discovered=[]):
    discovered.append(v)

    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    
    return discovered


print(f"recuresive dfs: {recursive_dfs(1)}")


# 얘는 역순이다. 그거를 헷갈리지 않도록! 돌려보면 어? 한다.
def iterative_dfs(start_v):
    discovered = []

    stack = [start_v]
    while stack:
        v = stack.pop()

        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered


# print(f"iterative dfs: {iterative_dfs(1)}")


# BFS
#  큐로 구현한다. 재귀가 없다!

def iterative_bfs(start_v):
    from collections import deque

    discovered = [start_v]
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered


print(f"iterative bfs: {iterative_bfs(1)}")
