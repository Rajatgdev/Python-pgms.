n = int(input("Enter a number: "))
r = 0
rev = 0
n1 = n
while(n != 0):
    r = n % 10
    rev =(rev * 10)+r
    n = n // 10
if rev == n1:
    print("Palindrome")
else:
    print("Not a Palindrome")

num = str(n1)
l = num.split()
for i in num :
    if i not in l:
        l.append(i)
        print(f"The number {i} is repeated {num.count(i)} times")