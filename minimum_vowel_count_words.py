lst = list(input().split())
vo = ['a','e','i','o','u']
lst1 = {} 
c1 =0
for i in lst:
    c =0
    for j in i:
        if j in vo:
            c += 1
    lst1[i] = c
for i in lst1:
    if lst1[i] == min(lst1.values()) :
        c1 += 1
print(c1)
