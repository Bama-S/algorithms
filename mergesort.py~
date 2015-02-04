def mergesort(alist):
    if len(alist)>1:
        #splitting the list
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        print "left half", lefthalf, ":", 
        print "right half", righthalf
        mergesort(lefthalf)#recurrence
        mergesort(righthalf) #recurrence
        i =0
        j =0
        lefthalf.append(999999)
        righthalf.append(999999)
        #merge lefthalf and righthalf
        for k in range(0,len(alist)):
            if lefthalf[i]<=righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
        print "sorted list for",lefthalf,righthalf,":",alist
        


alist = [5,2,4,7,1,3,2,6]
mergesort(alist)
