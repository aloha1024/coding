#coding: utf-8
import os
import subprocess
import string

s = string.printable   #可打印的字符串
s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

pname = "juckcode.exe"
p = subprocess.Popen(pname,stdin=subprocess.PIPE,stdout=subprocess.PIPE)


#for ch in s :
#	file = open('Flag','a+')
#	file.write(ch)
#	file.close()
	
#绑定程序
result = p.communicate("")
print result[0]
	
	
