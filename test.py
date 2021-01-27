#14500 테르토미노
# 교훈.. 단순하게 처리하려는 것 보다 단순 노가다가 좋을 떄가 있다
import copy
def process(shape):
    max_val = 0
    for i in range(N):
        for j in range(M):
            try: 
                tmp = data[i][j]
                for n, m in shape:
                    x, y = i + n, j + m
                    tmp += data[x][y]
                max_val = max(max_val, tmp)
            except IndexError:
                continue
    return max_val

def rotate(lst, n, m):
    new_lst = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            new_lst[j][m - i - 1] = lst[i][j]
    return new_lst

def mirror1(lst):
    new_lst = copy.deepcopy(lst)
    for i in range(N):
        for j in range(M):
            new_lst[i][M-j-1] = lst[i][j]
    return new_lst

def mirror2(lst):
    new_lst = copy.deepcopy(lst)
    for i in range(N):
        for j in range(M):
            new_lst[N-i-1][j] = lst[i][j]
    return new_lst

a = [(0, 1), (0, 2), (0, 3)]
b = [(0, 1), (1, 0), (1, 1)]
c = [(1, 0), (2, 0), (2, 1)]
d = [(1, 0), (1, 1), (2, 1)]
e = [(0, 1), (0, 2), (1, 1)]

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for el in [a, b, c, d, e]:
    for _ in range(4):
        ans = max(ans, process(el))
        data = mirror1(data)
        ans = max(ans, process(el))
        data = mirror1(data)
        data = mirror2(data)
        ans = max(ans, process(el))
        data = mirror2(data)
        N, M = M, N
        data = rotate(data, N, M)
print(ans)
