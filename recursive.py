def recursive (n):
    global t
    if n ==1:
        return n
    else:
        t += 1        
        return  recursive(n-1),t

t = 1
print recursive(10)
