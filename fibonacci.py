def fib (n):
    global t
    print "list has been called with n =", n
    if n <=1:
        print "returning back the value ", n
        return 1
    else:
        #print "1st element", n[0]
        res = fib (n-1)
        print "Intermediate result", res
        return res

t = 1
print fib(4)
