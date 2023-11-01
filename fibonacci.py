def f(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else: return f(n-1)+f(n-2)

n = int(input("Enter a number: "))
if n == 0 :
    print("The number can't be zero. ")
else:
    for i in range(1,n+1):
        print(f(i))