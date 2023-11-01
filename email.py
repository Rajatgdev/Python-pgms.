import re
phone_regex = re.compile(r'^\s*\d{10}$')
email_regex = re.compile(r'^[A-Z a-z 0-9 .-]+@[A-Z a-z 0-9 .-]+\.[A-Z a-z]{2,}$')
with open('test','r') as f:
    for line in f:
        matches = phone_regex.findall(line)
        for match in matches:
            print(match)
        matches1 = email_regex.findall(line)
        for match in matches1:
            print(match)