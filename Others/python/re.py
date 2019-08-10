#python 正则表达式 实例代码

import re
pattern = re.compile('hello')
match = pattern.match('hello world!')
match = pattern.match('hello world')
print match.group

############################

word = re. findall('hello','hello world!')
print word

 
