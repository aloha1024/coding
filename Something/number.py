#统计一段话中每个字符出现的次数
import pprint
str = 'please in put your str'

count = {}
for i in str:
    count[i] = count.setdefault(i,0)
    count[i] += 1

pprint.pprint(count)