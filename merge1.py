lefthalf = [30,55,999999]
righthalf = [20,60,999999]
alist = [55,20,30,60]

i = 0
j = 0
k = 0
print len(alist)

for k in range(0,len(alist)):
    if lefthalf[i]<=righthalf[j]:
        alist[k] = lefthalf[i]
        i = i+1
    else:
        alist[k] = righthalf[j]
        j = j+1
print alist