#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
\w \d \s . \.
[aAbB]
[a-z] [A-Z] [0-9] [A-Za-z]
a* a+ a? a{2,4}
"""

import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("yes!")
else:
    print("no")
pattern = re.compile(r'[\w\.]+@[a-z]+\.[a-z]+')
text = 'john.smith@mailbox.com is the e-mail of '\
'John. He often writes to his boss at '\
'boss@company.com. But the messages get forwarded '\
'to his secretary at info@company.com.'
x = re.finditer(pattern, text)
print(x)
for match in x:
    print(match)
    print(match.group())
    print(match.start())
    print(match.end())

substring = re.findall(pattern, text)
print(substring)
split_list = re.split(pattern, text)
print(split_list)












