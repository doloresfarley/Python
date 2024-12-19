v = [1,[3,2,4],[4,2,1]]
w=v[:]
for i,n in enumerate(v):
    if i == 0:
        v[i] =10
    else:
        n.sort()

print(v)
print(w)