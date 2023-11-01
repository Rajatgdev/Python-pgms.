import re


def is_ph_no(ph):
    if len(ph)!=12:
        return False
    for i in range(len(ph)):
        if i==3 or i==7:
            if ph[i]!='-':
                return False
        else:
            if not ph[i].isdigit():
                return False
    return True
def chk_ph(ph):
    ph_no_pattern=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if ph_no_pattern.match(ph):
        return True
    else:
        return False

n='415-555-4646'
if is_ph_no(n) and chk_ph(n):
    print("It is a phone number.")
else:
    print("It is not a phone number.")