def btod(n):
    r = 0
    dec = 0
    p = 0
    while(n != 0):
        r = n % 10
        dec = dec + (r * (2 ** p))
        n = n // 10
        p +=1
    return dec
def octohex(n):
    return hex(int(n, 8))

n1 = int(input("Enter a binary number: "))
print(f"The decimal number of {n1} is {btod(n1)}")

n2 = input("Enter a octal number: ")
print(f"The hexadecimal number of {n2} is {octohex(n2)}")
