import re

def chk_usn(n):
    usn_pattern=re.compile(r'\d{1}[A-Z a-z]{2}\d{2}[A-z a-z]{2}\d{3}')
    if usn_pattern.match(n):
        return True
    else:
        return False
print("enter n ")
n=int(input())
i=0
lst=[]
print(f"enter {n} strings")
while(i<n):
    item=input()
    lst=lst+[item]
    i=i+1
print("USNs are: ")
for i in lst :
    if chk_usn(i):
        print(i)
