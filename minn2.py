li = [5,2,4,6,1,3,700,600,900,4567]

for i in range(0,len(li)):
    out = li[i]
    for j in range(0,len(li)):
        if out <= li[j]:
            min = out
        else:
            min = li[j]
        out = min
print min
    