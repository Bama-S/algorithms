a = [[1,3],[5,7]]
b = [[0,2],[4,6]]

c = [[0,0],[0,0]]

n = len(a) # Find the number of rows
for i in range (0,n):
    for j in range(0,n):
        c[i][j] = 0
        for k in range(0,n):
            c[i][j] = c[i][j] + a[i][k]*b[k][j]
print c
    
