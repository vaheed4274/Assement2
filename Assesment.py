import sys
import re
import io

f = io.open(sys.argv[1],mode="r",encoding="utf-8")
contents = f.read()

# 1. Print all currencies in text, Accepted- $, ₹, £ 
pattern = '([\$|₹|£][\s]*[0-9]*.[0-9]*)'
print(re.findall(pattern,contents))

# 2. Print all date times in the text- dd/mm/yyyy, dd/mm/yy, mm/dd/yyyy, mm/dd/yy
pattern = '[0-9]*-[0-9]*-[0-9]*'
print(re.findall(pattern,contents))

#3. Print all cardinilities and orders- 4th, fifth, sixth, 1st, 2nd, nineteenth, fifth
pattern = '[0-9]+[nsrt][dth]'
print(re.findall(pattern,contents))

# 4. Print all 4 letter words that begin with vowels
pattern = '([\s]+[aeiouAEIOU][a-z]{3}[\s]+)'
print(re.findall(pattern,contents))
