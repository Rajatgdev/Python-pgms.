l = int(input("Enter the lower bound: "))
u = int(input("Enter the upper bound: "))
p = []
for i in range(l,u):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count+=1
    if count == 2:
            p.append(i)
print(p)