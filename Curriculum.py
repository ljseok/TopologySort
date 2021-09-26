from collections import deque
import copy

v = int(input()) # 노드의 개수 입력받기
indegree = [0] * (v + 1) # 진입차수는 0으로 초기화
graph = [[] for i in range(v + 1)] # 노드에 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
time = [0] * (v + 1) # 강의 시간을 0으로 초기화

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 가지고 있다
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort(): # 위상 정렬 함수 정의
    result = copy.deepcopy(time) # 결과값 리스트
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0: # 진입차수가 0인 노드를 큐에 삽입
            q.append(i)

    while q: # 큐가 빌 때까지 반복한다
        # 큐에서 원소 꺼내기
        now = q.popleft()

        for i in graph[now]: # 해당 원소와 연결된 노드들의
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1 #진입차수에서 1 빼기

            if indegree[i] == 0: # 진입차수가 0이 되는노드를
                q.append(i) # 큐에 삽입

    for i in range(1, v + 1):
        print(result[i])

topology_sort()