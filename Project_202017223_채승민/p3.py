from collections import deque

input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]

    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    # queue를 활용하여 BFS를 구현해 현재 위치에서 가장 가까운 벌집을 찾는 함수를 만든다 
    def bfs(bear_x, bear_y, bear_size):
        #queue에 곰의 현재 위치와 거리를 저장한다.
        queue = deque([(bear_x, bear_y, 0)])  # (x, y, 거리)
        visited = set()
        visited.add((bear_x, bear_y))
        destination = []
        #현재 위치에서 앞뒤양옆 이웃한 칸에 이동 가능한 칸과 먹을 수 있는 벌집을 탐색한다
        #곰의 크기보다 작거나 같은 칸은 방문할 수 있고 그 중 곰의 크기보다 작은 칸은 먹을 수 있도록 한다.
        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_x = x + dx
                neighbor_y = y + dy
                if 0 <=  neighbor_x < N and 0 <= neighbor_y < N and (neighbor_x, neighbor_y) not in visited:
                    if forest[neighbor_x][neighbor_y] <= bear_size:  # 이동 가능
                        visited.add((neighbor_x, neighbor_y))
                        if 0 < forest[neighbor_x][neighbor_y] < bear_size:  # 먹을 수 있는 벌집
                            destination.append((dist+1,neighbor_x, neighbor_y))
                        #방문했다면 해당 위치를 저장하고 거리는 1을 늘려 queue에 저장한다.
                        queue.append((neighbor_x, neighbor_y,dist+1))

        # 가장 가까운 벌집을 구하기 위해 거리, x 좌표, y 좌표 순으로 정렬한다.
        if destination:
            destination.sort()
            return destination[0]
        else:
            return None

    while True:
        eat = bfs(bear_x, bear_y, bear_size)
        #반환된 값이 없다면 반복문을 빠져나간다.
        if eat is None:
            break
        #함수에서 반환된 값을 각각 dist, eat_x, eat_y에 저장하고 이동한 거리만큼 시간을 증가시킨다.
        dist, eat_x, eat_y = eat
        bear_x, bear_y = eat_x, eat_y
        time += dist

        # 벌집을 먹고 먹은 칸은 빈칸으로 만든다.
        forest[bear_x][bear_y] = 0
        honeycomb_count += 1

        # 먹은 벌집의 개수와 곰의 크기가 같다면 벌집의 개수를 초기화하고 곰의 크기를 1 늘린다.
        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0

    return time

# 입력 예시
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]

result = problem3(input)

assert result == 14
print("정답입니다.")
