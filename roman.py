roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def romtodec(n):
    total = 0
    for i in range(len(n)):
        if roman[n[i-1]] < roman[n[i]] and i > 0:
            total = total + roman[n[i]] - 2* roman[n[i-1]]
        else:
            total = total+roman[n[i]]
    return total

n = input("Enter the roman number: ")
print(romtodec(n))
