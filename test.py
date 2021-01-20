#17406
import copy, sys

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def rotate(lst, K):
    r, c, s = K
    new_lst = copy.deepcopy(lst)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for j in range(4):
            for k in range(i*2):
                rrr, ccc = rr + dx[j], cc + dy[j]
                print(rrr, ccc, rr, cc)
                print(lst)
                print(r, c, i)
                new_lst[rrr][ccc] = lst[rr][cc]
                rr, cc = rrr, ccc
    return new_lst

def DFS(data, count):
    ret = sys.maxsize
    if count == K:
        ret = min(ret, min([sum(el) for el in data]))
        return ret
    for i in range(K):
        if visited[i] == 0:
            visited[i] = 1
            new_lst = rotate(data, k_lst[i])
            ret = min(ret, DFS(new_lst, count+1))
            visited[i] = 0
    return ret
            
N, M, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
k_lst = [list(map(int, input().split())) for _ in range(K)]
visited = [0 for _ in range(K)]
print(DFS(data, 0))