#solves forward substitution
import numpy as np

l = np.array([[1,0,0],[2,1,0],[3,2,1]])
n = 3

y=np.zeros(n)
y = y.astype(np.float)
print(y)
d = np.array([1,1,3])
d = d.astype(np.float)
print(d)
i = 3
y[0]=d[0]

print(y)
for i in range(1,i):
    print ("y", y)
    y[i]=d[i]
    for j in range(i):
        print("i j" , i,j)
        print("lij value ", l[i][j])
        print("y value ", y[j])
        y[i] = y[i] - (l[i][j]*y[j])
    y[i] = y[i]/l[i][i]
    print("yi value ", y[i])
print(y)
