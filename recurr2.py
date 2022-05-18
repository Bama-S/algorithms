def recur(a):
    global i
    n = len(a)
    if a[i] == 0: ## refer the marker here
        print "stop" 
    else:
        a[i] = a[i] + 1
        print a[i]
        i += 1
        recur(a)


a = [1,2,3,4,5,6,0] # 0 is the end marker
global i 
i = 0
recur(a)
