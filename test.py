#3190

# D => idx 증가 L => idx 감소
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
data = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    data[r-1][c-1] = 1
L = int(input())
L_dic = {}
for _ in range(L):
    x, C = input().split()
    L_dic[int(x)] = C

    
visited = [[-1] * N for _ in range(N)]
sec = 0
visited[0][0] = 0
head = [0, 0]
tail = [0, 0]
vec = 0
while True:
    sec += 1
    head = [head[0] + dx[vec], head[1] + dy[vec]]
    if  head[0] < 0 or head[0] > N-1 or head[1] < 0 or head[1] > N-1 or visited[head[0]][head[1]] >= visited[tail[0]][tail[1]] :
        break
    visited[head[0]][head[1]] = sec
    if data[head[0]][head[1]] == 1:
        data[head[0]][head[1]] = 0
    else:
        for i in range(4):
            x, y = tail[0] + dx[i], tail[1] + dy[i]
            if 0 <= x <= N-1 and 0 <= y <= N-1 and visited[x][y] == visited[tail[0]][tail[1]] + 1:
                tail = [x, y]
                break
    if L_dic.get(sec):
        if L_dic[sec] == "D":
            vec = (vec + 1) % 4
        else:
            vec = (vec - 1) % 4
print(sec)