#setcover working without cost
#Works with s0 as a dummy subset
def calculate_cost(cost,sset):
    total = 0
    for i in sset:
        #print(cost[i])
        total = total + cost[i]
    return total

universe = [1,2,3,4,5,6]
subsets = {'s0':[],'s1':[1,3,5,6],'s2':[3,2,6,4,5],'s3':[1,4,2]}
cost = {'s1':5,'s2':10,'s3':3}

set_cover = []
covered = []
cost_all = []
s = len(set(universe) - set(covered))
rem = set(universe)-set(covered)
key_subsets = list(subsets.keys())
value_subsets = list(subsets.values())
print(value_subsets)
l=0
print("---------------------------------------------------")
while set(covered)!=universe:
    n = len(value_subsets[l])
    print(n)
    for i in range(1,len(value_subsets)-1):
        print(i, value_subsets[i])
        if (rem or set(value_subsets[i]) == True):
            print("rem in value_subsets")
            if len(value_subsets[i])>=n: #select maximum elements in subsets
                n = len(value_subsets[i])
                #print("largest subset picked ", n, subsets_key[i])
                l = i
    position = l
    sel_subset = key_subsets[position]
    set_cover.append(sel_subset)
    covered = covered+value_subsets[l]
    del value_subsets[position]
    del key_subsets[position]
    rem = set(universe) - set(covered)
    print(rem)
    if rem == set():
        print("-----------------------")
        print("Covered set ",set_cover)
        total_cost = calculate_cost(cost,set_cover)
        print("Total Cost ", total_cost)
        print("Covered elements", set(covered))
        break
