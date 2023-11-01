import difflib
from difflib import SequenceMatcher

def similarity(p1,p2):
    s = SequenceMatcher(a=p1.lower(), b=p2.lower())
    return s.ratio()

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("The similarity of the two strings are: ", similarity(s1,s2))
