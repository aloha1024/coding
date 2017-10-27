#encoding=utf-8
import urllib2
import urllib
import cookielib


url_basic='192.168.19.47'
port='80'
dect='wp-login.php'#添加可攻击页面
payload=''
url='http://'+url_basic+':'+port+'/'+dect+payload
req=urllib2.Request(url)
res=urllib2.urlopen(req)
res_data=res.read() 
flag=res_data.split("\n")[0][0:22] #讲读取的html按行变成列表，把要读取的行数写入，此处为0，然后读取0-22个字符
print flag

f=open('./flag_store.txt','a')
f.write(flag+' ') #写入文件，然后直接放到提交flag脚本的列表中
f.close()




















