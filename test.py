#14503
# 북, 동, 남, 서
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def check(n, m):
    return 0 <= n <= N-1 and 0 <= m <= M-1

N, M = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0
while True:
    if visited[r][c] == 0:
        visited[r][c] = 1
        ans += 1
    isfind = False
    for _ in range(4):
        #n , m은 탐색할 좌표 
        n, m = r + dx[d], c + dy[d]
        if  check(n,m) and data[n][m] != 1 and visited[n][m] == 0:
            d = (d - 1) % 4
            r, c = n, m
            isfind = True
            break
        else:
            d = (d - 1) % 4
    if not isfind:
        # 후진 좌표
        n = r + dx[d-1]
        m = c + dy[d-1]
        if not check(n,m) or data[n][m] == 1 :
            break
        else:
            r, c = n, m
print(ans)