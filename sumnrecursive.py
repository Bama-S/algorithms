def recursive (n):
    global t
    print "list has been called with n =", n
    if len(n) ==1:
        print "returning back the value ", n[0]
        return n[0]
    else:
        print "1st element", n[0]
        res = n[0]+ recursive(n[1:])
        print "Intermediate result", res
        return res

t = 1
recursive([1,2,3,4,5])
