import re

text = "i have 5000 dollars"

x = re.search(r'\d',text)
print(x)
print(x.span())
print(x.group())

y = re.split(r'\s',text)
print(y)

z = re.sub(r'\s', '-',text)
print(z)

twit = "aku sedang belajar coding :)"
a = re.sub(r':\)', 'senang', twit)
print(a)