import re

str=input()
date_ex= re.compile(r'(\d{1,2})-(\d{1,2})-(\d{4})')
date_list=date_ex.sub('\\3-\\2-\\1',str)
print(date_list)