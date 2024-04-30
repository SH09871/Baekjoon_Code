n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

#행렬 B 생성
b = []
for i in range(n):
    b.append(list(map(int, input().split())))

#행렬 A+B 생성
c = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] + b[i][j]

#행렬 A+B 출력
for i in range(n):
    for j in range(m):
        print(c[i][j], end = ' ')