#quicksort

def partition (alist,p,r):
    pivot = alist[r-1]
    i = p-1
    for j in range(p,r):
        if alist[j] <= pivot:
            i=i+1
            (alist[i],alist[j]) = (alist[j],alist[i])
    (alist[i+1],alist[r-1]) = (alist[r-1],alist[i+1])
    return i+1

def quickSort(alist,p,r):
    if p<r:
        pivot = partition(alist,p,r)
        print(pivot)
        quickSort(alist,p,pivot-1)
        quickSort(alist,pivot,r)
        return (alist)


alist = [2,8,7,1,3,5,6,4]
print ("Original list ", alist)
p = alist[0]
print(p)
r = alist[-1]
print(r)
sorted = quickSort(alist,p,r)
print ("Sorted array ", sorted)
