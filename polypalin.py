class palin_str():
    def __init__(self):
        self.is_palin = False

    def chk_palin(self,str):
        if str == str[::-1]:
            self.is_palin=True
        else:
            self.is_palin=False
        return self.is_palin

class palin_num():
    def __init__(self):
        self.is_palin=False

    def chk_palin(self,num):
        r=0
        rev=0
        n1=num
        while(num != 0):
            r = num % 10
            rev = (rev *10)+r
            num = num // 10
        if rev == n1:
            self.is_palin = True
        else:
            self.is_palin = False

        return self.is_palin
str = input("Enter a string : ")
obj_str = palin_str()
if obj_str.chk_palin(str):
    print("Palindraome")
else:
    print("Not a palindrome ")

num = int(input("Enter a number: "))
obj_num = palin_num()
if obj_num.chk_palin(num):
    print("Palindrome")
else:
    print("Not a Palindrome ")