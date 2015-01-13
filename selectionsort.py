def selection(a):
    for i in range(0,len(a)-1):
        indmin = i# assume the minimum is the first element
        for j in range(i+1,len(a)):
            if a[j]<=a[indmin]:
                indmin = j# find the minimum element
        if indmin != i:
            a[i],a[indmin] = a[indmin],a[i]# swap
    print a

alist = [6,5,4,3,2,1]
selection(alist)