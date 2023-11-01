d=0
l=0
u=0
r=0
s=input("Enter a string: ")
r = len(s.split())
print(f"The number of words in the string {s} are {r}")
for i in s:
    if i.isnumeric():
        d+=1
print(f"There are {d} numbers in the string {s}")
for j in s:
    if j.isupper():
        u+=1
    elif j.islower():
        l+=1
print(f"There are {l} lower case letters in the string {s}")
print(f"There  are {u} upper case letter in the string {s}")

